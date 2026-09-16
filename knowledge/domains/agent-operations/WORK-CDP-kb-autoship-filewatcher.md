# WORK: KB AutoShip — FileWatcher in CdpService

**Status:** shipped (cdp-mcp `0b6619a`, CDP-ADR-0224)  
**ADR:** `cdp-mcp/docs/adr/CDP-ADR-0224-kb-autoship-filewatcher.md`  
**Spec:** [`note-cdp-autoship-coordinator-bridge.md`](note-cdp-autoship-coordinator-bridge.md) (corrected)

---

## Goal

Background service watches KB git working tree; after debounced quiet period, auto commit + push. Agent stops hand-committing agent-notes after every edit.

---

## Touch list (expected)

### cdp-mcp / CdpService

- `KbAutoShipService.cs` (HostedService) — FileSystemWatcher + debounce timer
- `KbAutoShipOptions` — debounce_ms (default 90000), roots[], enabled, branch
- Wire in `CdpServiceHost` / DI
- SA alert on rebase conflict (`IdeReviewChannel` or existing alert path)
- Settings: `[kb.autoship]` in agent-notes-mcp.toml or cdp service config

### guiders-core (optional v0)

- None required if watcher is filesystem-only (preferred v0)

### Tests

- `CdpMcp.Tests/KbAutoShipDebounceTests.cs` — burst writes → one ship
- Conflict path → alert emitted, no push

---

## Algorithm

```text
on FS change (filtered: .git/**, scratch noise optional):
  reset debounce timer (90s)

on debounce fire:
  git fetch origin
  if origin/main ahead of HEAD → SA alert + abort (no auto-rebase)
  git add -A (respect .gitignore)
  if clean → return
  commit "KB auto: <top paths>"
  git push origin main
  if rejected → SA alert
```

---

## Acceptance

1. Edit KB via `cdp_buffer` → no manual commit → pushed within ~90s after last write
2. Parallel burst edits → **one** commit
3. Simulated rebase conflict → alert, tree untouched
4. Product repo outside KB roots → watcher ignores

---

## Smoke

```text
cdp_buffer create path=.../knowledge/.../smoke-autoship.md
cdp_shell_run git -C D:/Experiments/agent-notes status
# wait 90s
cdp_shell_run git -C D:/Experiments/agent-notes log -1
```

---

## Seed

Implement WORK KB AutoShip FileWatcher per spec. Min diff. Tests + deploy smoke.

