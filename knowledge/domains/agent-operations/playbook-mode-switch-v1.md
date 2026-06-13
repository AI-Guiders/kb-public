# Mode switch v1

Тело секции `mode-switch-protocol` из `agent-notes.md`. Связь: `playbook-project-switch-v1.md` (PRIMARY/SCOPE), `kb-protocols-and-entities-one-pager-v1.md`.

<!-- section:mode-switch-protocol -->
## Mode Switch Protocol

- Default mode in this thread stays `[HUMAN]` until explicit `[WORK]` appears.
- Marker `[WORK]` switches interaction to execution mode and operational context handling.
- Marker `[HUMAN]` switches interaction to reflective/personal mode.
- Notes routing rule:
  - `[WORK]` content -> operational sections (task/scope/runbook/decisions).
  - `[HUMAN]` content -> `personal-reflection` (and adjacent personal layer if needed).
- If marker is missing and intent is ambiguous, keep current mode and ask one clarifying question only when required.
- Priority rule: explicit marker in user message always overrides previous mode state.
<!-- /section:mode-switch-protocol -->
