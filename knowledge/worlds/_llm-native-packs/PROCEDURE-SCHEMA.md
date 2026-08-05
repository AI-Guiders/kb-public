# Procedure schema — when-cards (host-rule analogue)

**Tags:** #llm-ready #packs #cdp #schema #procedure  
**Status:** live · [CDP-ADR-0003](../../work/projects/door-to-singularity/cascade-ide/CDP-ADR-0003-llm-native-procedures.md)  
**Date:** 2026-07-21

Тонкий ритуал: **когда** + **короткие шаги**. Не Guided Graph (`processes.toml`) и не длинный playbook.

## File

`pack/procedures.toml`:

```toml
[[procedure]]
id = "example-when-card"
name = "Short ritual name"
apply_when = "human-readable trigger"
signals = ["signal_a", "signal_b"]
phases = ["verify", "handoff"]          # optional
steps = [
  "step one",
  "step two",
]
gate = ["optional check"]               # optional
definition_anchors = ["card-id", "mc-id"]
related_process = "optional-process-id" # optional
tool_anchors = ["get_definition:card-id"]
llm_cue = "One question before acting?"
host_projectors = [".cursor/rules/example.mdc"]  # optional; not SSOT
```

## vs process vs definition

| Kind | Use when |
|------|----------|
| **definition** | словарь / лицензия / cue |
| **process** | полный граф (steps+gate+anchors), multi-stage investigation |
| **procedure** | host-rule analogue: trigger → 3–7 steps |

## Tools

- `get_procedure(procedure_id, pack_id?)`  
- `list_pack` → `procedure_ids`  
- `cdp_session` may embed a matched procedure (dogfood)

## Cursor `.mdc` map

| `.mdc` | procedure |
|--------|-----------|
| description | `name` / `llm_cue` |
| alwaysApply / globs | `apply_when` + `signals` + `phases` |
| body | `steps` (+ gate) |

