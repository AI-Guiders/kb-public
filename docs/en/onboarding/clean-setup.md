# Clean setup (kb-public → personal)

For **participants** who consume a public slice and maintain a **personal** canon. To **create** `{ORG_SLUG}/kb` for your company, see [White-label org KB](white-label.md).

**Canonical playbook:** [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md)  
**Templates:** [templates/newcomer/](../knowledge/templates/newcomer/README.md)

## chmod ugo

| chmod | Layer | MCP |
|-------|-------|-----|
| **u** | personal (primary) | default |
| **g** | `{ORG_SLUG}/kb` | `knowledge_root_id=group` |
| **o** | kb-public | `knowledge_root_id=public` |

## Phase 0 — machine

.NET SDK, Git, Cursor; avoid spaces in paths when possible.

## Phase 1 — agent-notes-mcp

1. Build **agent-notes-mcp** from upstream (MIT).
2. Copy [`template-clean-setup-agent-notes-mcp-toml-v1.toml`](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml) — set **your** paths.
3. Cursor `mcp.json`: `"args": ["--config", "<path-to-toml>"]`.

Until personal exists: `primary = "public"` pointing at **your** kb-public clone.

## Phase 2 — personal canon

1. Create or fork a personal `agent-notes` repository.
2. TOML: `primary = "personal"`, roots for personal + public.
3. Apply templates from `templates/newcomer/`.
4. Restart MCP.

## Phase 3 — `work/local/` (personal only)

| File | Template |
|------|----------|
| `work/local/workspace-scope-map-v1.md` | `template-clean-setup-workspace-scope-map-v1.md` |
| `work/local/knowledge-roots-index-v1.md` | `template-clean-setup-knowledge-roots-index-v1.md` |
| hot sections in `agent-notes.md` | `template-clean-setup-hot-*.md` |

These paths are **not** in the kb-public zip — templates live under `knowledge/templates/newcomer/` in the repo.

## Phase 4 — group (optional)

If your team already runs `{ORG_SLUG}/kb`:

1. Clone group repo; add `[[knowledge.read_only]]` id `group` in TOML.
2. Fill `knowledge-roots-index-v1.md`.
3. Verify: `read_knowledge_file(..., knowledge_root_id=group)`; writes to group are rejected.

## Phase 5 — done

`memory_health`, `route_context`, personal primary, optional group/public read-only.
