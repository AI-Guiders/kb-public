---
type: Note
title: 'WORK: Guiders F# — Math conformance + ADR-0003 gate'
description: '**Status:** debt_closure (P0 green · CommandPlane+cdp-mcp fixed · NuGet on hold)'
---
# WORK: Guiders F# — Math conformance + ADR-0003 gate

**Status:** debt_closure (P0 green · CommandPlane+cdp-mcp fixed · NuGet on hold)  
**Parent:** coordinator routing 2026-09-12  
**Fix workers:** [Ide.Session P0](05c4cf93-140c-4b1d-9adc-ea6216cc8271) ✅ · [Platform IR forks](892683ab-79e1-43dd-b3da-0a8f2f94c7a1) ✅

---

## Goal

Gate before NuGet wave and CDP/Forge/DashSpec migration:
1. `docs/math/ide-session` ↔ `Modeling.Ide.Session` conformance
2. GUIDERS-FSHARP-ADR-0003 Modeling/Execution matrix compliance
3. Publish allowlist + product migration waves only after P0 green

---

## Verdict (2026-09-12, gate closed)

**P0 green** — NuGet `Modeling.Ide.Session` + core GDL IR facades unblocked (P1 IO seam still documented).

| Area | F# exists | Compliant | Blocker |
|------|-----------|-----------|--------|
| Foundation §4.1 | 100% | ~90% | Paths naming drift |
| GDL §4.2–4.3 | 100% | **~91%** | wave 1 hybrid done; wave 2 (Combinations, etc.) remains |
| Ide.Session (0004) | 100% | **~92%** | P1: IO in orchestrator/ports |
| Golden GS1–GS6 | tests | **verified** | 34/34 |
| Platform P0 forks | — | **fixed** | — |
| cdp-mcp LRC cutover | — | **fixed** | — |

### Shipped commits

**Worker A:** `a4f13d4`, `a0bd0be` (Ide.Session P0)  
**Worker B:** `069525a`, `263ab2b` (fsharp) · `11c8383` (platform)  
**Coordinator:** `7e587ea` · `3159c4f`+`d5d85b4` · `0204235` · `f3ec1c4` · `9eed4e9` · `ce73242` · `cd8b6e6` · `beb9d3a` · `bc12839` · `9238084` · `6b71b01`+`3df7e5a` · `b22255a` · `baf1747`  
**F# wave 1:** `ae9813c` (Invocation tests) · `a5079db` (Gdl.Language TypeKey)

---

## P0 must-fix (math / Ide.Session) — Worker A ✅

1. ~~**I1/I4 invalidation**~~ → `a0bd0be`
2. ~~**GS CI green**~~ → `a4f13d4`
3. ~~**Capability surface**~~ → CodeTransform/CodeStyle added; LspBridge kept
4. ~~**Job lane minimum**~~ → `SnapshotJob.fs` stub
5. ~~**SessionPatch.scope**~~ → ProjectCrud / SolutionProjectCrud ladder

## P0 must-fix (ADR-0003 / platform) — Worker B ✅

1. ~~**V-P0-1** reverse ref~~ → `069525a` + `11c8383`
2. ~~**V-P0-2..5** forked shapes~~ → IR facades to Modeling.Gdl

### Debt closure queue (NuGet wave **on hold** until done)

1. ~~**CommandPlane.Catalog**~~ → `3159c4f` + `d5d85b4` (build green via `cdp_build`)
2. **Hybrid C# wave (11 pkgs)** — prepass `9eed4e9`; inventory [Hybrid inventory](e83682cc-9592-4f40-bad5-302b435b6aac):
   - ~~**#1** `IR.Binding`~~ → `0204235` ([IR.Binding cutover](5ec97413-8ba0-42d7-b2aa-466d5f290d23))
   - ~~**#2** `Notations` core~~ → `f3ec1c4` ([Notations core cutover](10e240cb-42c4-4d02-9199-81429d964098))
   - ~~**#3** `IR.Invocation`~~ → `ce73242`+`ae9813c` ([IR.Invocation cutover](333fbf80-b35c-4c69-8fe1-d3813282a70c))
   - ~~**#4** `IR.Language`~~ → `cd8b6e6`+`a5079db` ([IR.Language cutover](d2edeeac-9b66-451e-b87b-9fb12c709399))
   - ~~**#5** `IR.Presentation`~~ → `beb9d3a` ([IR.Presentation cutover](3c0ef83d-1c7d-4cc7-aa3c-83ef39d9119b))
   - ~~**#6** Authoring Catalog/Bundles/Conformance~~ → `9238084` ([Authoring Catalog cutover](12f0f071-20a8-4ec8-8dfd-4e673c08f6be)); walker/parser C# by design
   - ~~**#7** Navigation + Policy~~ → `bc12839` ([Navigation+Policy cutover](cf3a99c5-e758-4d29-884f-0f3f328a99ea))
   - **Wave 1 integration:** full slnx build **red** (26 err — MelodyStep/MelodyLineProfile, CatalogRouteEntry static param, CommandDocumentFormat GlobalUsings); UoW tests green
   - Wave 2: Combinations, Conformance.Navigation, Notations.Command/Keyboard leaves
3. **P1 Ide.Session IO** — [Ide.Session IO](9d88ad9f-55f8-45f2-aa99-1101f6b2572f) ✅
   - ~~**Slice A**~~ → `6b71b01`+`3df7e5a` ([loadContentsFromDisk move](d112d433-fbe8-404e-bbfc-b5476ba31e1c)); 34/34 GS
   - ~~**Slice B (doc)**~~ → [Ports IO seam exception](note-guiders-fsharp-ide-session-ports-io-seam.md)
4. **CDP habitat** — audit [CDP JSON/TOML](5fe55023-99ed-475a-9f44-07e5b655df2f)
   - **0219:** P0 store-registry (`4883d02`) · identity witdb (`b22255a`) · P3 RecallFallback (`7e8c5b2`); P1–P2 wake/identity remain
   - ~~**0222 Slice 1**~~ → `baf1747` ([CDP 0222 CdpConfigLoader](9d811c88-b1bd-4143-8dd3-ad685328d4b5)); tests 14/14
5. ~~guiders-fsharp WIP triage~~ — CRLF-only noise on 3 Ports files (restored)

## P1 (before product rewrite)

- Move `SessionOrchestrator.loadContentsFromDisk` + port disk IO → Execution.Ide.Session
- Policy lattice: `LifecyclePhase` incomparable RunTime/TestTime; ρ_eff / E_gov (open §9.5)
- Hybrid unsplit: 6× Authoring, 9× IR, Combinations, Conformance, Navigation

---

## NuGet allowlist (after P0)

| Package | Condition |
|---------|----------|
| `Modeling.Core`, `Modeling.Routing`, `Modeling.Paths` | Foundation P0 platform deps clean |
| `Modeling.Ide.Session` | P0 math + GS green |
| `Modeling.Ide.Session.Ports.*` | IO moved or documented seam exception → [slice B doc](note-guiders-fsharp-ide-session-ports-io-seam.md) |
| GDL/Notations packages | platform IR forks removed |

---

## Product migration waves (after gate)

1. **CDP** — session orchestration via `Modeling.Ide.Session` seam (partial Fcs/0216 exists)
2. **DashSpec** — 0048 Modeling parse / Execution compose
3. **Forge** — after CDP pattern proof

---

## CI grep candidates (from ADR audit)

See worker B report: Modeling→Execution refs, IO in core Modeling, hybrid csproj without UseGuidersModeling.

---

## Acceptance

- [x] P0 math fixes + Ide.Session.Tests 34/34
- [x] P0 platform fork removal (V-P0-1..5)
- [x] FSharp.Core aligned 10.1.400 (`7e587ea`)
- [x] CommandPlane.Catalog cutover + cdp-mcp LRC (`3159c4f`, `d5d85b4`)
- [x] Hybrid UoW #1 IR.Binding (`0204235`)
- [x] Ide.Session IO slice A (`6b71b01`, `3df7e5a`)
- [x] Hybrid UoW #2 Notations core (`f3ec1c4`)
- [x] Hybrid UoW #3 IR.Invocation (`ce73242`, `ae9813c`)
- [x] Hybrid UoW #4 IR.Language (`cd8b6e6`, `a5079db`)
- [x] Hybrid UoW #5 IR.Presentation (`beb9d3a`)
- [x] Hybrid UoW #6 Authoring Catalog (`9238084`)
- [x] Hybrid wave 1 (#1–#7) — integration (`eb2e4ce` GlobalUsings + `4e55ec6` MelodyStep)
- [x] Ide.Session Ports seam doc (slice B) — [note-guiders-fsharp-ide-session-ports-io-seam.md](note-guiders-fsharp-ide-session-ports-io-seam.md)
- [ ] Operator steer → NuGet wave
- [x] CDP 0222 Slice 1 (`baf1747` — CdpConfigLoader)
- [x] CDP 0219 P3 RecallFallback peer stash → witdb (`7e8c5b2`)
- [x] CDP 0219 P0 store-registry catalog (`4883d02`)
- [x] Hybrid wave 2 W1 — Notations.Command + Slash (`71e5123`)
- [x] Hybrid wave 2 W2 — Conformance.Navigation wire models (`cffb423`)
- [x] Hybrid wave 2 W3 — Combinations core (`20b8227`)
- [x] Hybrid wave 2 W4 — Conformance.Policies (`7982f04`)
- [ ] Hybrid wave 2 merge — slnx + downstream consumers (Command.Console/All, Overlay/Workspace)
- [x] Hybrid wave 2 prep — NavigationProfileWire SSOT (`9c34c84`, guiders-fsharp)

---

## Fix sprint workers (2026-09-12)

| Worker | Scope | Status |
|--------|-------|--------|
| [Ide.Session P0](05c4cf93-140c-4b1d-9adc-ea6216cc8271) | invalidation, GS CI, capability, job lane | **done** `a4f13d4`+`a0bd0be` |
| [Platform IR forks](892683ab-79e1-43dd-b3da-0a8f2f94c7a1) | adapter ref invert, IR DTO forks | **done** `11c8383`+`069525a` |
| [Notations core cutover](10e240cb-42c4-4d02-9199-81429d964098) | hybrid UoW #2 | **done** `f3ec1c4` |
| [IR.Invocation cutover](333fbf80-b35c-4c69-8fe1-d3813282a70c) | hybrid UoW #3 | **done** `ce73242`+`ae9813c` |
| [IR.Language cutover](d2edeeac-9b66-451e-b87b-9fb12c709399) | hybrid UoW #4 | **done** `cd8b6e6`+`a5079db` |
| [IR.Presentation cutover](3c0ef83d-1c7d-4cc7-aa3c-83ef39d9119b) | hybrid UoW #5 | **done** `beb9d3a` |
| [Authoring Catalog cutover](12f0f071-20a8-4ec8-8dfd-4e673c08f6be) | hybrid UoW #6 | **done** `9238084` |
| [Navigation+Policy cutover](cf3a99c5-e758-4d29-884f-0f3f328a99ea) | hybrid UoW #7 | **done** `bc12839` |
| [Ide.Session IO A](d112d433-fbe8-404e-bbfc-b5476ba31e1c) | loadContentsFromDisk → Execution | **done** `6b71b01`+`3df7e5a` |
| [Ide.Session IO B](note-guiders-fsharp-ide-session-ports-io-seam.md) | Ports.* seam exception doc | **done** (slice B doc) |
| [CDP 0222 CdpConfigLoader](9d811c88-b1bd-4143-8dd3-ad685328d4b5) | TOML unification | **done** `baf1747` |
| [Platform integration ship](fce0e162-5c25-4b39-815e-8372b4b912fb) | GlobalUsings IR + MelodyStep | **done** `eb2e4ce`+`4e55ec6` |
| [CDP RecallFallback witdb](03d221ba-0605-47c8-b01b-34e23e7ff54d) | peer tenant stash SSOT | **done** `7e8c5b2` |
| [CDP 0219 store-registry P0](8782c5ba-3c97-46b3-9fa1-1591cf9d0583) | catalog + GS-HS1 partial tests | **done** `4883d02` |
| [Hybrid Conformance.Navigation](fd22c29c-d44a-4e62-b34a-4b9f1440eaed) | wave 2 W2 wire models + JsonElement bridge | **done** `cffb423` |
| [Hybrid Notations.Command](2b33a0a2-5329-471d-b466-98e302e5df74) | wave 2 W1 Command + Slash cutover | **done** `71e5123` |
| [Hybrid Combinations core](fc04e621-bcef-4f42-82e8-d154dd0c6bbd) | wave 2 W3 enum/DU bridge | **done** `20b8227` |
| [Hybrid Conformance.Policies](655132c4-7f60-4453-8b06-331837fc029a) | wave 2 W4 wire models | **done** `7982f04` |
| [DashSpec card.view M-slice](014e20b1-bae2-408c-b9dc-b3d74c9c6b71) | delete ViewCommandPaths, wire id parity | **done** `3142f39` |
| [Deploy GDL wave 1](1dc6d04e-46ac-4abc-a709-9b33392fe22d) | CdpDeployCatalogResolver + delete parser | **done** `f61f279` |
| [Hybrid wave 2 map](6d38e15e-5be0-41d2-9a87-1c9c96a2ca44) | NavigationProfileWire prep | **done** `9c34c84` |

**Coordinator rule:** audit/fix workers = background + CDP-first; не блокировать чат синхронным explore.

### CDP open (workers)

1. **Prefer** `cdp_open path=D:/Experiments/AIGuiders.All.slnx` — federation root (F# + platform + refs).
2. Per-repo fallback: `AIGuiders.Platform.Modeling.slnx` (A) · `AIGuiders.Platform.slnx` (B).
3. **Parallel hazard:** `cdp_open` без `add_root=true` перетягивает primary session у соседа (tenant slices есть, но subagent часто делит bridge/default). Mitigation: coordinator держит All.slnx; workers — absolute `cdp_buffer` paths; или stagger / worktree.
4. `cdp_buffer` relative path → ProjectRoot **после** open.

## Smoke

```text
cdp_test project=AIGuiders.Platform.Modeling.Ide.Session.Tests
cdp_shell_run rg "Map\.empty" --glob "**/MaterializedState*.fs" guiders-fsharp/
```

