# Note: Ide.Session Ports.* — documented disk-IO seam exception

**Status:** Accepted (slice B, 2026-09-13)  
**Tags:** #guiders #fsharp #ide-session #ports #nuget #conformance  
**Parent:** [WORK: Guiders F# conformance audit](WORK-guiders-fsharp-conformance-audit.md) · P1 Ide.Session IO slice B  
**Related:** [GUIDERS-FSHARP-ADR-0003](https://github.com/AI-Guiders/guiders-fsharp/blob/main/docs/adr/GUIDERS-FSHARP-ADR-0003-model-extraction-matrix.md) · [GUIDERS-FSHARP-ADR-0004](https://github.com/AI-Guiders/guiders-fsharp/blob/main/docs/adr/GUIDERS-FSHARP-ADR-0004-ide-session-modeling-ownership.md) · [GUIDERS-ADR-0062 §6](https://github.com/AI-Guiders/guiders-dotnet-platform/blob/main/docs/adr/GUIDERS-ADR-0062-ide-solution-session-orchestrator.md) · [CDP-ADR-0210](https://github.com/AI-Guiders/cdp-mcp/blob/main/docs/adr/CDP-ADR-0210-plugin-architecture.md) · [Ide.Session IO audit](9d88ad9f-55f8-45f2-aa99-1101f6b2572f)

---

## Decision

`Modeling.Ide.Session.Ports.*` packages **may ship on the NuGet allowlist** with **documented disk IO** at the port boundary. This is an explicit seam exception to ADR-0003's "Modeling must not own IO" rule — not an oversight.

Slice A (shipped `6b71b01` + `3df7e5a`) moved **session contents** disk read out of `SessionOrchestrator` into `Execution.Ide.Session.SessionContentsLoader`. Slice B documents why **port adapter** disk IO remains in `Ports.*` for now.

---

## Why IO remains in Ports.*

### 1. Ports are the adapt layer, not the model

ADR-0003 defines three layers: **Modeling** (pure IR), **Seam** (contracts), **Execution** (drive). ADR-0004 and ADR-0062 §6 place graph parsing at the **port** boundary:

| Anchor | Port package | Feeds |
|--------|--------------|-------|
| `.sln` / `.slnx` / `.csproj` / `.fsproj` | `Ports.DotNet` | `SolutionGraph` project nodes + `FileOwnership` |
| md/json/toml/yaml tree | `Ports.Workspace` | `WorkspaceGraph` document links |

Ports **produce Modeling IR from the external world** — that necessarily touches disk. The core `Modeling.Ide.Session` package stays IO-free: `ISolutionInfoProvider`, `SolutionProviderRegistry`, and `SessionOrchestrator` operate on in-memory graphs and contents maps only.

### 2. Solution vs workspace layering (CDP-ADR-0210)

CDP-ADR-0210 separates:

- **Solution** = logical layer (slnx/csproj, GDL, Planet semantics)
- **Workspace** = physical layer (disk, git, file trees)

`Ports.Workspace` is a **workspace enricher** — it enumerates document files and scans content for navigation links. This is physical-layer IO by design, not orchestration leakage.

### 3. Plugin registry pattern (ADR-0210 stage 1)

`SolutionProviderRegistry` in `Modeling.Ide.Session` knows only the `ISolutionInfoProvider` contract. Provider assemblies (`Ports.DotNet.Registration.init()`) self-register at the composition root. The core does not import port implementations — but the port packages themselves still perform disk reads when instantiated.

### 4. What is IO-free inside Ports.*

Not every file in `Ports.*` touches disk:

| Module | Package | IO? |
|--------|---------|-----|
| `DesignTimeCompilerServicesPort` | DotNet | No — pure graph/frozen transforms |
| `WorkspaceViewPort` | DotNet | No — emits `WorkspaceView` from in-memory state |
| `DotNetSlnxGraphPort.buildProjectNodes/Edges` | DotNet | No — pure transforms over parsed entries |

Disk IO is confined to **reader** modules:

| Module | Package | IO operations |
|--------|---------|---------------|
| `ProjectFileReader` | DotNet | `File.Exists`, `XDocument.Load`, `Directory.GetFiles` |
| `DotNetSlnxGraphPort.load` | DotNet | `DotNetWorkspace.Load` |
| `MsBuildSolutionProvider` | DotNet | `DotNetWorkspace.Load`, `File.GetLastWriteTimeUtc` (fingerprint) |
| `WorkspaceGraphPort` / `WorkspaceLinks` | Workspace | `Directory.EnumerateFiles`, `File.ReadAllText`, `File.GetLastWriteTimeUtc` |

---

## NuGet allowlist condition

From [WORK conformance audit](WORK-guiders-fsharp-conformance-audit.md) §NuGet allowlist:

| Package | Condition | Slice B verdict |
|---------|-----------|-----------------|
| `Modeling.Ide.Session` | P0 math + GS green | ✅ unblocked (P0 green) |
| `Modeling.Ide.Session.Ports.*` | IO moved **or** documented seam exception | ✅ **this doc** satisfies the exception path |

**Gate rule:** `Ports.*` NuGet publish is allowed when either:

1. All disk IO is relocated to `Execution.Ide.Session.Ports.*` (future, size L), **or**
2. This seam exception is accepted and cross-referenced from WORK + ADR-0004.

Slice A already closed the **orchestrator** IO violation. Remaining port IO is scoped, bounded, and does not block core `Modeling.Ide.Session` or hybrid C# unsplit work.

---

## What moved in slice A (context)

| Before | After |
|--------|-------|
| `SessionOrchestrator.loadContentsFromDisk` in Modeling | `Execution.Ide.Session.SessionContentsLoader.LoadFromDisk` |
| `System.IO` in `SessionOrchestrator.fs` | Removed — orchestrator is pure over `Map<string, string>` |
| Callers: `FederationSessionRuntime`, `FcsSessionPatchBridge` | Retargeted to Execution loader |

Golden sessions (GS1–GS6) remain 34/34 — tests inject in-memory contents via `SessionOrchestrator.create`, never hitting disk.

---

## Future migration path

Full port IO relocation is **deferred** (scope L). When pursued:

### Phase 1 — trait/impl split (no package rename)

1. Keep `ISolutionInfoProvider` + `SolutionProviderRegistry` in `Modeling.Ide.Session` (contract only).
2. Introduce `IProjectFileReader` / `IWorkspaceEnumerator` seam types in Modeling (or thin C# seam).
3. Move concrete `File.*` / `Directory.*` calls to `Execution.Ide.Session` implementations.
4. `Ports.DotNet` / `Ports.Workspace` become thin facades or are absorbed into Execution.

### Phase 2 — package rename (optional)

- `Modeling.Ide.Session.Ports.DotNet` → `Execution.Ide.Session.Ports.DotNet`
- `Modeling.Ide.Session.Ports.Workspace` → `Execution.Ide.Session.Ports.Workspace`
- Modeling packages publish only IR + contracts; Execution publishes IO adapters.

### Phase 3 — plugin dll-per-provider (CDP-ADR-0210 stage 2)

- Out-of-process-ready provider discovery
- Manifest with contract version
- Workspace enrichers register alongside solution providers

### Not in scope for port migration

| Concern | Owner | Notes |
|---------|-------|-------|
| `FcsSessionPatchBridge.flushWrites` | `Modeling.Language.Adapters.Fcs` | Adapter persist IO — separate follow-up to Execution host |
| `DotNetWorkspace.Core` | guiders-core util | Stays a **dependency** of port readers; not session SSOT (ADR-0062 §6) |

---

## CI grep guard (optional)

To prevent new IO leaking into Modeling core (not Ports):

```text
cdp_shell_run rg "System\.IO|File\.|Directory\." --glob "**/Modeling.Ide.Session/*.fs" guiders-fsharp/src/AIGuiders.Platform.Modeling.Ide.Session/
```

Expected: **zero matches** (slice A invariant). Ports packages are excluded from this grep by path.

---

## Acceptance

- [x] Slice A: orchestrator IO removed (`6b71b01`, `3df7e5a`)
- [x] Slice B: this doc — Ports.* seam exception for NuGet allowlist
- [ ] Phase 1 trait/impl split (future, not blocking NuGet)

