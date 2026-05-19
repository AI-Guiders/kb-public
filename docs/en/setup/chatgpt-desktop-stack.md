## ChatGPT Desktop stack (Windows)

### 1. Stack components

- **ChatGPT Desktop** — official desktop app.
- **kb-public** — local clone of the public knowledge slice.
- **agent-notes-mcp** — MCP for long-term notes and canon access.
- **webcam-mcp** — MCP for camera/screen/audio capture and analysis.
- **git-mcp** — MCP for git status/diff/log/commit/push.
- **Git for Windows** — system git (for git-mcp and repos).

MCP servers ship as self-contained .NET 10 win-x64; end users do not need the .NET SDK.

### 2. Requirements

- Windows 10/11 (x64).
- Access to your Git host (GitHub, GitLab, etc.).
- Account on that host.
- **Git for Windows** installed (`git` on PATH).

### 3. Install ChatGPT Desktop

1. Download the latest ChatGPT Desktop from OpenAI.
2. Install with defaults.
3. Sign in; confirm the app starts cleanly.

### 4. Directory layout

Suggested layout:

- `D:\ChatGPT\tools\agent-notes-mcp\`
- `D:\ChatGPT\tools\webcam-mcp\`
- `D:\ChatGPT\tools\git-mcp\`
- `D:\ChatGPT\kb-public\`

Create base folders:

```powershell
mkdir D:\ChatGPT
mkdir D:\ChatGPT\tools
```

### 5. Install kb-public

```powershell
cd D:\ChatGPT
git clone https://github.com/AI-Guiders/kb-public.git kb-public
```

Canon path: `D:\ChatGPT\kb-public`.

Recommended environment variable:

- `AGENT_NOTES_CANON_PATH = D:\ChatGPT\kb-public`

Restart ChatGPT Desktop after changing environment variables.

### 6. Install agent-notes-mcp

1. Open your Git host → project `agent-notes-mcp` → **Releases**.
2. Download the **win-x64** archive.
3. Extract to `D:\ChatGPT\tools\agent-notes-mcp\`.
4. Confirm `D:\ChatGPT\tools\agent-notes-mcp\AgentNotesMcp.exe` exists.

(Optional junction)

```powershell
New-Item -ItemType Junction -Path "D:\agent-notes-mcp" -Target "D:\ChatGPT\tools\agent-notes-mcp"
```

### 7. Install webcam-mcp

1. Releases → **win-x64** archive.
2. Extract to `D:\ChatGPT\tools\webcam-mcp\`.
3. Confirm `WebcamMcp.exe`.

### 8. Install git-mcp

1. Confirm `git --version` in PowerShell.
2. Releases → **win-x64** archive.
3. Extract to `D:\ChatGPT\tools\git-mcp\`.
4. Confirm `GitMcp.exe`.

### 9. Connect to ChatGPT Desktop

ChatGPT Desktop MCP UI changes over time; here we only fix commands/paths.

Per server:

- **agent-notes-mcp** — `D:\ChatGPT\tools\agent-notes-mcp\AgentNotesMcp.exe`, args `[]`
- **webcam-mcp** — `D:\ChatGPT\tools\webcam-mcp\WebcamMcp.exe`, args `[]`
- **git-mcp** — `D:\ChatGPT\tools\git-mcp\GitMcp.exe`, args `[]`

Then either add local MCP servers in ChatGPT Desktop settings, or use an external profile (e.g. mcp.run) if supported.

See current ChatGPT Desktop MCP docs and your org runbooks.

### 10. Smoke test

After connecting MCP:

- **agent-notes-mcp** — ask for `memory_health` for the current workspace.
- **webcam-mcp** — `capture_webcam_frame` and check a frame appears in workspace.
- **git-mcp** — `git_status` for a local repo and compare with console git.

If issues: check `.exe` paths, antivirus blocks, `AGENT_NOTES_CANON_PATH`, git on PATH.
