# Template — TaskKnowledge workspace layout
**Tags:** #template #templates


Экземпляр: **`{workspace}/.task-knowledge/`** (work store, не KB).

```text
.task-knowledge/
  README.md                 — что это за workspace store + active epic ids
  epics/
    <epic_id>.md            — optional epic card (goal, adr_refs)
  analytics/
    <epic_or_adr_id>.md     — analytics card (template-taskknowledge-analytics-v0)
  tasks/
    <task_id>.md            — one task card (template-taskknowledge-task-v0)
  memos/                    — optional: per-file memo md (hash in frontmatter)
  .revisions/               — optional: snapshots before upsert (AN-style)
```

## Conventions

- Filenames = stable ids (`task_id`, epic id); lowercase, `-`, no spaces.
- Prefer `<!-- section:id -->` markers inside cards when MCP section-upsert lands (AN mechanics).
- Until MCP exists: edit md directly; keep DAG edges (`blocked_by` / `unlocks`) consistent across task files + analytics table.
- Do **not** put this tree under `knowledge/`.
- Sibling: `.agent-failures/` stays JSONL; `.agent-findings/` JSONL = legacy prototype only.

## README.md stub

```markdown
# TaskKnowledge store

Active epics: …
Playbook: knowledge/domains/agent-operations/playbook-taskknowledge-adr-analytics.md
```
