## Cursor: local MCP stack (Windows)

!!! warning "ChatGPT Desktop is not stdio"
    **ChatGPT Desktop does not** attach local MCP via `command` + `args` and a `.exe` the way Cursor does. ChatGPT connectors use a **public HTTPS URL** (Settings → Connectors → Create); see [Connect from ChatGPT](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt).  
    **agent-notes-mcp** today is **stdio only** (`AgentNotesMcp.exe` + `--config`). Copying the Cursor snippet into ChatGPT **will not work**. A remote HTTP/SSE endpoint is [upstream backlog](https://github.com/AI-Guiders/agent-notes-mcp) (§1).

The page URL still says `chatgpt-desktop-stack` (legacy wiki title). Content below is the **Cursor** install path.

Full onboarding: [Clean setup](../onboarding/clean-setup.md), [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md), [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml).

### 1. ChatGPT Desktop — what works today

| Host | MCP transport | agent-notes-mcp |
|------|----------------|-----------------|
| **Cursor**, VS Code + MCP | Local **stdio** (`mcp.json`) | ✅ §5–7 |
| **Cascade IDE** | In-proc MCP | ✅ [cascade-ide docs](https://ai-guiders.github.io/cascade-ide/) |
| **ChatGPT Desktop** | **HTTPS** connector → `https://…/mcp` | ❌ no shipped public endpoint; binary is stdio-only |

If you need ChatGPT specifically:

1. You need an MCP server reachable over **HTTPS** (or a tunnel to one) — not raw `AgentNotesMcp.exe`.
2. In ChatGPT: **Settings → Connectors → Create** — **Connector URL**, not an exe path.
3. For kb-public content in ChatGPT, use this [site](https://ai-guiders.github.io/kb-public/en/) or run the same canon in **Cursor** on disk.

Remote agent-notes-mcp for ChatGPT is backlog; watch [agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp).

### 2. Stack (Cursor)

| Component | Role |
|-----------|------|
| **kb-public** | Public KB slice |
| **agent-notes-mcp** | Memory, hot-context, `knowledge/` |
| **git-mcp** | Git operations |
| **webcam-*** | Optional capture/analysis |
| **Git for Windows** | For git-mcp and clones |

Self-contained **.NET 10 win-x64**; no SDK on the user machine.

### 3. Requirements

- Windows 10/11 (x64).
- **Cursor** (or another host with **stdio MCP**).
- **Git for Windows**.
- GitHub access for clones and releases.

### 4. Layout (example)

```powershell
New-Item -ItemType Directory -Path D:\agent-stack\tools -Force
cd D:\agent-stack
git clone https://github.com/AI-Guiders/kb-public.git kb-public
```

### 5. agent-notes-mcp (binary)

[Releases](https://github.com/AI-Guiders/agent-notes-mcp/releases) → **win-x64** → `D:\agent-stack\agent-notes-mcp\AgentNotesMcp.exe`.

### 6. Config (TOML, required)

Example `D:\agent-stack\agent-notes-mcp\agent-notes-mcp.toml`. **`AGENT_NOTES_CANON_PATH`** is not used in MCP 2.x.

**kb-public only:**

```toml
version = 1

[knowledge]
primary = "public"

[knowledge.roots]
public = "D:/agent-stack/kb-public"

[workspace]
default_scope = "mixed"
```

With personal canon: [template](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml), [clean setup](../onboarding/clean-setup.md).

More: [ADR 014](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/014-agent-notes-local-settings-toml-v1.md).

### 7. Cursor — `mcp.json`

**`%USERPROFILE%\.cursor\mcp.json`:**

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

Or **`AGENT_NOTES_CONFIG`** env var. Restart Cursor after edits.

### 8. Smoke test (Cursor)

`memory_health`, `read_knowledge_file` (`SHOWCASE.md`), `route_context` — with a real `workspace_path`.

### 9. Troubleshooting

| Symptom | Check |
|---------|--------|
| MCP exits immediately | `--config` file and TOML |
| Tried exe in ChatGPT | ChatGPT needs HTTPS MCP, not stdio |
| Old `AGENT_NOTES_CANON_PATH` docs | Use TOML + `--config` |
