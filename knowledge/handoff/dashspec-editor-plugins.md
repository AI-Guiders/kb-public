# DashSpec editor plugins (handoff)

## Status: LSP v0.2.3 (2026-07-10)

### Done
- **Core:** TextPositions, DashSpecDiagnosticService, DashSpecWorkspaceIndex, SourceOffset on parse errors
- **IncludePathCompletion** — `!include "…"` suggests subdirs (`layouts/`), files in subdirs, glob presets (`diagrams/*.dashdiagram`)
- **LSP:** src/DashSpec.LanguageServer — OmniSharp 0.19.9, stdio (diagnostics, completion, go-to-definition)
- **Editor parse:** DashSpecParseOptions.Editor — MergeReferencedTabModules=false, ExtensionBlockKeywords views
- **VS Code:** editor/vscode-dashspec v0.2.3 — vscode-languageclient, bundled server/
- **VSIX:** editor/vscode-dashspec/dashspec-0.2.3.vsix
- **Script:** scripts/package-vscode-extension.ps1 (publish server + npm + vsce)
- **Tests:** IncludePathCompletionTests, DashSpecDiagnosticServiceTests (soak shell no false positive)

### Include completion
- Trigger: inside `!include "` (opening quote required); trigger chars `"`, `/`
- `!include "` + Ctrl+Space → root files, `layouts/`, `diagrams/`, glob presets
- `!include "layouts/` + Ctrl+Space → `soak-toolbar.dashlayout`, etc.

### OmniSharp note
TextDocumentSyncKind → OmniSharp.Extensions.LanguageServer.Protocol.Server.Capabilities (NOT Protocol.Models, NOT Microsoft.VisualStudio.*).

### Dev workflow
```powershell
cd dash-spec
./scripts/package-vscode-extension.ps1
# Install: Command Palette → Extensions: Install from VSIX → dashspec-0.2.3.vsix
# F5 dev, open LUS docs/dashspec
```

Settings: dashspec.languageServerEnabled (default true). CLI validate optional via dashspec.hostDll.

