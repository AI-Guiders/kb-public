# Protocols & KB entities (one-pager)

Chat markers and Scope vs Primary — quick reference for agents and humans.

**Full one-pager:** [kb-protocols-and-entities-one-pager-v1.md](../knowledge/kb-protocols-and-entities-one-pager-v1.md)

## In 60 seconds

| Question | Answer |
|----------|--------|
| What to type in chat? | `[HUMAN]`, `[WORK]`, `[PRIMARY:…]`, `[SCOPE:…]` |
| What wins? | Marker in **this** message → install default → path heuristic (does not override recent marker) |
| Scope vs Primary? | **SCOPE** = workspace slice; **PRIMARY** = product in focus |

## Mode: `[HUMAN]` / `[WORK]`

| Marker | When | Agent |
|--------|------|--------|
| `[HUMAN]` | reflection, meaning, “let’s talk” | no runbooks unless asked |
| `[WORK]` | task, code, KB, “do it” | tools, checklists |

One thread — one stable mode until switched.

## Focus: `[PRIMARY:…]` / `[SCOPE:…]`

| Marker | Sets |
|--------|------|
| `[PRIMARY:id]` | main product / `project-id` for this thread |
| `[SCOPE:slice]` | which workspace L1 hot-context slice |

Do not confuse `[PRIMARY:EDWH]` (product) with `[SCOPE:HRV]` (harvester slice).

## MCP (not chat markers)

| Tool / param | Use |
|--------------|-----|
| `read_hot_context` | session start, scope change |
| `route_context` | what to load by topic |
| `read_knowledge_file` | one playbook/kb file |
| `knowledge_root_id=group` | read `{ORG_SLUG}/kb` (read-only) |
| `knowledge_root_id=public` | read kb-public |
| **writes** | **primary only** (personal) |

## Layers

| Layer | Role |
|-------|------|
| **kb-public** | public playbooks + this site |
| **group KB** | team private canon |
| **personal** | your canon + `work/local/` |

See [Three contours](three-contours.md).
