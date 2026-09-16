# Knowledge roots index (template — copy to personal `work/local/knowledge-roots-index.md`)
**Tags:** #template #templates


**Not** a catalog of every file in group/public. TOML `[[knowledge.read_only]]` already mounts the full clone — use `read_knowledge_file(..., knowledge_root_id=group)` for any path.

This file hints **`route_context`** which root to prefer when the query matches (ADR 017 / Core 2.1.2+).

Format: one line per entry — `relative/path/under/knowledge/ => root_id`

- **No trailing `/`** — single file only (e.g. `group/smoke-test.md => group`)
- **Trailing `/`** — prefix: all files under that directory (e.g. `work/projects/<group-scope-dir>/ => group`)
- `group` — team KB (`{ORG_SLUG}/kb`)
- `public` — kb-public slice
- `user` — primary personal (or omit after import)

Scope catalog names: **`work/org/scope-contour-map.md`** — do not duplicate every card here.

Lines starting with `#` are comments. No prose blocks in the committed real file.

# --- minimal example ---

group/smoke-test.md => group
work/org/ => group
work/projects/<group-scope-dir>/ => group

