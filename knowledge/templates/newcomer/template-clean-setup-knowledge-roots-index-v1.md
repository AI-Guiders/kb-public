# Knowledge roots index (template — copy to personal `work/local/knowledge-roots-index-v1.md`)

Machine-local registry: **which file under `knowledge/` lives in which root** (chmod ugo).
**Not** clone paths — those go in TOML `--config` (`[[knowledge.read_only]]`).

Format: one line per entry — `relative/path/under/knowledge/ => root_id`
- `group` — team KB (`AI-Guiders/kb`), read via `knowledge_root_id=group`
- `public` — kb-public slice, read via `knowledge_root_id=public`
- `user` — primary personal canon (or omit line after import into personal)

Lines starting with `#` are comments. No prose blocks in the committed real file.

# --- examples (fictional paths) ---

index-knowledge-router-v1.md => group
playbook-multi-project-context-v1.md => group

kb-music-theory-fundamentals-v1.md => user