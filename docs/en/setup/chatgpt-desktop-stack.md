## Agent stack: Cursor and ChatGPT Desktop (Windows)

Guide for **local stdio MCP** on Windows. With **agent-notes-mcp 2.x** you need a **TOML** file and **`--config`** in the host settings; **`AGENT_NOTES_CANON_PATH`** is no longer used.

Full onboarding (personal + group): [Clean setup](../onboarding/clean-setup.md), playbook [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md), TOML template [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml).

### 1. Stack components

| Component | Role |
|-----------|------|
| **kb-public** | Public KB slice (GitHub clone) |
| **agent-notes-mcp** | Memory, hot-context, `knowledge/` ([releases](https://github.com/AI-Guiders/agent-notes-mcp/releases)) |
| **git-mcp** | Git status/diff/commit ([AI-Guiders/git-mcp](https://github.com/AI-Guiders/git-mcp)) |
| **webcam-capture-mcp** / **webcam-analysis-mcp** | Capture and analysis (optional; [open stack](https://ai-guiders.github.io/)) |
| **Git for Windows** | For git-mcp and clones |

MCP servers ship as self-contained **.NET 10 win-x64**; no SDK required on the user machine.

### 2. Requirements

- Windows 10/11 (x64).
- **Git for Windows** (`git` on PATH).
- **Cursor** and/or **ChatGPT Desktop** with **local** MCP support (stdio: `command` + `args`).
- Internet access for **GitHub** clones and releases.

!!! note "ChatGPT and remote MCP"
    Some ChatGPT setups only accept MCP over **HTTPS URL** (connectors), not a local `.exe`. The stdio stack below targets **Cursor** first; for URL-based ChatGPT see [OpenAI MCP docs](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt). A remote endpoint for agent-notes-mcp is upstream backlog.

### 3. Directory layout (example)

```text
D:\agent-stack\
  kb-public\              ← git clone
  agent-notes-mcp\        ← AgentNotesMcp.exe + agent-notes-mcp.toml
  tools\git-mcp\
```

```powershell
New-Item -ItemType Directory -Path D:\agent-stack\tools -Force
```

### 4. kb-public

```powershell
cd D:\agent-stack
git clone https://github.com/AI-Guiders/kb-public.git kb-public
```

Slice root: `D:\agent-stack\kb-public` (contains `knowledge/` and trimmed `agent-notes.md`).

### 5. agent-notes-mcp (binary)

1. [Releases](https://github.com/AI-Guiders/agent-notes-mcp/releases) → **win-x64** archive.
2. Extract to `D:\agent-stack\agent-notes-mcp\`.
3. Verify `D:\agent-stack\agent-notes-mcp\AgentNotesMcp.exe`.

From source: [AI-Guiders/agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp) — `dotnet publish`; `publish-and-deploy.ps1` copies a sample TOML next to the exe.

### 6. agent-notes-mcp config (TOML, required)

Keep the file **out of git** (e.g. `D:\agent-stack\agent-notes-mcp\agent-notes-mcp.toml`). Without **`--config`** the process exits with an error.

**kb-public only** (no personal canon yet):

```toml
version = 1

[knowledge]
primary = "public"

[knowledge.roots]
public = "D:/agent-stack/kb-public"

[workspace]
default_scope = "mixed"
```

**kb-public + personal canon** — after [clean setup](../onboarding/clean-setup.md): use [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml) (`primary = "personal"`, `personal` + `public` roots, optional `[[knowledge.read_only]]` for group).

| Section | Meaning |
|---------|---------|
| `[knowledge]` / `[knowledge.roots]` | Where `knowledge/` and `agent-notes.md` live (primary root) |
| `[workspace]` | `default_scope`, paths to `scope_map` / `scope_aliases` in **personal** canon |
| `[status]` | Optional localhost status — see ADRs in [agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp/tree/main/docs/adr) |

Use **forward slashes** in TOML paths (`D:/...`) where possible.

More: [ADR 014 (local TOML)](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/014-agent-notes-local-settings-toml-v1.md), [MCP-TOOLS](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/MCP-TOOLS.md).

### 7. Cursor (`mcp.json`)

File: **`%USERPROFILE%\.cursor\mcp.json`**. Example **agent-notes** entry:

```json
{
  "mcpServers": {
    "agent-notes": {
      "command": "D:\\agent-stack\\agent-notes-mcp\\AgentNotesMcp.exe",
      "args": ["--config", "D:/agent-stack/agent-notes-mcp/agent-notes-mcp.toml"],
      "env": {}
    }
  }
}
```

Alternative: env **`AGENT_NOTES_CONFIG`** pointing at the same TOML if the host does not pass `args`.

Restart **Cursor** after changes.

### 8. ChatGPT Desktop

If **local MCP servers** (stdio) are available in settings, use the **same** `command` and `args` as in §7, including **`--config`** with an absolute TOML path.

| Field | Value |
|-------|--------|
| Command | `D:\agent-stack\agent-notes-mcp\AgentNotesMcp.exe` |
| Args | `["--config", "D:/agent-stack/agent-notes-mcp/agent-notes-mcp.toml"]` |

Do not use empty `args: []` — that was pre–MCP 2.0.

### 9. Optional MCP servers

Each gets its own `command` in `mcp.json` (no `--config` unless that server requires it):

| Server | Example command |
|--------|-----------------|
| **git-mcp** | `D:\agent-stack\tools\git-mcp\GitMcp.exe` |
| **webcam-capture-mcp** | `...\WebcamCaptureMcp.exe` |
| **webcam-analysis-mcp** | `...\WebcamAnalysisMcp.exe` |

Releases: [AI-Guiders](https://github.com/AI-Guiders) repos linked from [ai-guiders.github.io](https://ai-guiders.github.io/).

### 10. Smoke test

With agent-notes connected:

1. **`memory_health`** with `workspace_path` set to any local project folder.
2. **`read_knowledge_file`** — `file_path`: `SHOWCASE.md` (root from TOML `public`).
3. **`route_context`** — query like “kb clean setup”; response should reference kb-public playbooks.

For **git-mcp**: `git_status` on a repo and compare with terminal `git status`.

### 11. Troubleshooting

| Symptom | Check |
|---------|--------|
| MCP exits immediately | `--config` file exists; valid TOML (`version = 1`) |
| No knowledge | `[knowledge.roots]` path is a clone containing **`knowledge/`** |
| Empty hot / scope | Full workspace map needs **personal** canon + `work/local/` ([clean setup](../onboarding/clean-setup.md)) |
| Docs mention `AGENT_NOTES_CANON_PATH` | Migrate to TOML + `--config` |
| Antivirus | Allow the folder with `.exe` |
