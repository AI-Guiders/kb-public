# Hot section template: knowledge-roots-routing-v1

Copy the fenced block into personal `agent-notes.md` (below `<!-- public-cut -->` if used).

```markdown
<!-- section:knowledge-roots-routing-v1 -->
## Knowledge roots routing (chmod ugo)

| chmod | Role | MCP |
|-------|------|-----|
| **u** (user) | personal primary — hot, writes, scope-map | default (no `knowledge_root_id`) |
| **g** (group) | team KB `{ORG_SLUG}/kb` (private) | `read_knowledge_file(..., knowledge_root_id=group)` |
| **o** (other) | kb-public slice | `read_knowledge_file(..., knowledge_root_id=public)` when configured |

If TOML has `[[knowledge.read_only]]` with `id=group` (or `public`):

1. **TOML** `[[knowledge.read_only]]` — whole clone; read any path with `knowledge_root_id=group` (or `public`).
2. **Registry** `work/local/knowledge-roots-index-v1.md` — **route_context hints only** (exact file or `prefix/` with trailing `/`); not a full file catalog. Scope names: `work/org/scope-contour-map-v1.md`.
3. **Do not** copy full group playbooks into personal tree; import consciously.
4. **`route_context`** (Core 2.1.2+): on group/roots/registry queries or registry hit → this section + preview (`knowledge_roots_overlay_applied`). Writes primary only.

Clone paths: TOML `--config` only (not this file).
<!-- /section:knowledge-roots-routing-v1 -->
```