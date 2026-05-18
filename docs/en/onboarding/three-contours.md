# Three KB contours

Use **`{ORG_SLUG}`** as your GitHub organization slug (e.g. `acme-corp`). Example instance: `AI-Guiders` — not required for readers of kb-public.

**Canonical (long form):** [map-kb-three-contours-v1.md](../knowledge/domains/agent-operations/map-kb-three-contours-v1.md)

## Contours

| # | Contour | Where | MCP |
|---|---------|-------|-----|
| **1** | **Personal canon** | your `agent-notes` repo | `primary` / **u** |
| **2a** | **Group KB** | `{ORG_SLUG}/kb` (private) | `knowledge_root_id=group` / **g** |
| **2b** | **Public KB** | `{ORG_SLUG}/kb-public` | `knowledge_root_id=public` / **o** |
| **3** | **Workspace** | IDE roots, product repos | code; hot file is a **mirror** of (1) |

`knowledge/work/` and `knowledge/personal/` live **inside (1)** only — they are **not** in kb-public by design.

```text
[Workspace]  sync          [Personal agent-notes]
     │                            │ git
     └──────► agent-notes.md ◄────┘
                    │ export (sanitize)
                    ▼
             [{ORG_SLUG}/kb]
                    │ build-public-kb.ps1
                    ▼
             [{ORG_SLUG}/kb-public]
```

## Cheat sheet

| Content | Contour |
|---------|---------|
| Playbooks, router, META | **1** `knowledge/...` |
| Project cards, ops notes | **1** `work/projects/...` (not in kb-public) |
| Private drafts | **1** `personal/...` |
| Product code | **3** product repo |
| Public sanitized slice | **2b** build from **1** |

## Agent triggers

“Which repo?”, “where to write”, “three repositories”, “white-label”, “sync notes” → this page, then the focused playbook.
