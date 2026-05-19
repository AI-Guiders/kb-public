# Map: three KB contours

**Version:** v1.0 · **2026-05-19**

Remove friction around “which repo” and “where to write”. One page for **agents** and **humans** (approve).

**Canonical:** [map-kb-three-contours-v1.md](../knowledge/domains/agent-operations/map-kb-three-contours-v1.md) · **Your org:** [White-label org KB](../onboarding/white-label.md)

*Example instance: `AI-Guiders` — not required for readers.*

See also: [Protocols and entities](../onboarding/protocols.md) · [Memory and KB](../guide/memory-and-kb.md) · [PUBLISHING.md](../knowledge/PUBLISHING.md)

---

## Contours (do not mix up)

| # | Contour | Where | MCP / chmod | Who writes |
|---|---------|-------|-------------|------------|
| **1** | **Canon** (personal) | maintainer repo (`agent-notes` / fork) | `primary` / **u** | canon owner |
| **2a** | **Group KB** | **`{ORG_SLUG}/kb`** (private) | `knowledge_root_id=group` / **g** | PR + org-maintainer |
| **2b** | **Public KB** | **`{ORG_SLUG}/kb-public`** | read-only / **o** | canon-maintainer → `build-public-kb.ps1` |
| **3** | **Workspace** | IDE root, product repos | code, hot mirror | code in product repos; knowledge in **1** |

**Not a fourth contour:** `knowledge/work/` and `knowledge/personal/` live **inside canon (1)**; they are **excluded** from kb-public by design.

```text
[Workspace]  copy/sync     [Canon — personal]
     │                           │ git
     └──────► agent-notes.md ◄───┘
                    │ export (sanitize)
                    ▼
             [{ORG_SLUG}/kb — group KB]
                    │ build-public-kb.ps1
                    ▼
                [{ORG_SLUG}/kb-public]
```

---

## Where to put what (cheat sheet)

| Content | Contour | Action |
|---------|---------|--------|
| Playbooks, router, META, worlds | **1** | `knowledge/...` in canon |
| L0, hot sections | **1** | `agent-notes.md` (above `<!-- public-cut -->` may go public) |
| Project card, operational | **1**, work layer | full canon only (not kb-public) |
| “Only me” draft | **1**, personal | not published |
| C#, tests, UI | **3** | product repo |
| Edit from Cursor chat | **1** | update canon; workspace hot is mirror |
| Public sanitized slice | **2b** | build from **1** → push kb-public |

---

## Sync: workspace hot ↔ canon

- **Source of truth** — contour **1** (canon git).
- Hot in workspace (`.cascade-ide/agent-notes.md`, etc.) is MCP working surface; after substantive edits → **canon** and commit.
- Agent must not treat workspace file as canon when `AGENT_NOTES_CANON_PATH` points at a canon clone.

---

## MCP: multiple roots

| Parameter | Meaning |
|-----------|---------|
| `knowledge_root_id=group` | read from **`{ORG_SLUG}/kb`** (read-only in MCP) |
| `primary` | write only to personal/main canon |
| `route_context` | overlay from hot + optional group KB preview ([ADR 015](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/015-multi-root-knowledge-roots-v1.md)) |

More: [ADR 012](../knowledge/adr/012-multi-canon-workspace-resolution-v1.md) · [Protocols](../onboarding/protocols.md)

---

## Roles

| Action | Agent | Human |
|--------|-------|-------|
| “Which contour to edit” | ✅ per this map | approve if unsure |
| Commit to canon | prepare | approve, commit |
| `build-public-kb`, push | preview, diff | **canon-maintainer** |
| Weaken Integrity | ❌ | ❌ |

---

## Agent triggers

“which repo”, “where to write”, “three repositories”, “kb-public vs agent-notes”, “group KB”, “sync notes” → **this map first**, then a narrow playbook.
