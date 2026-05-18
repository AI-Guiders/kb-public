# White-label org KB

How **any** GitHub organization deploys **`{ORG_SLUG}/kb`** (private) + **`{ORG_SLUG}/kb-public`** (public) with agent-notes-mcp multi-root.

**Canonical playbook:** [playbook-org-kb-white-label-v1.md](../knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md)  
**Bootstrap templates:** `template-org-kb-bootstrap-*` in [newcomer templates](../knowledge/templates/newcomer/README.md)

## Naming

| Placeholder | Example |
|-------------|---------|
| `{ORG_SLUG}` | `acme-corp` |
| `{REPO_GROUP}` | `acme-corp/kb` |
| `{REPO_PUBLIC}` | `acme-corp/kb-public` |

MCP ids **`group`** and **`public`** stay fixed; only clone paths differ per machine.

## What you need

| Piece | Notes |
|-------|--------|
| **agent-notes-mcp** | MIT; publish or install locally |
| **Source canon** (maintainer) | Full tree with `scripts/`, `public-kb.ignore`, `group-kb.ignore` |
| **GitHub org** | Teams: `kb-maintainers`, optional canon-maintainers |

## Phase A — repositories

1. Create `{REPO_PUBLIC}` (public) and `{REPO_GROUP}` (private).
2. LICENSE **CC BY-SA 4.0** on KB text.
3. Commit CONTRIBUTING / CODEOWNERS / README from bootstrap templates (replace placeholders).

## Phase B — maintainer source canon

Configure `public-kb.ignore` and `group-kb.ignore`. Sanitize `work/projects/` (no drive letters, no `personal/`).

## Phase C — first public build

```powershell
.\scripts\build-public-kb.ps1
.\scripts\push-public-kb.ps1   # remotes in knowledge/public-kb.push (local only)
```

Enable **GitHub Pages** on `{REPO_PUBLIC}` from `/docs` (this site) — see repo `mkdocs.yml`.

## Phase D — seed group KB

```powershell
.\scripts\seed-org-kb.ps1
```

Push `dist/group-kb/` to `{REPO_GROUP}`. Keep `knowledge/group/smoke-test-v1.md` for MCP smoke tests.

## Phase E — team members

Point them to [Clean setup](clean-setup.md) phase 4 (read-only group). They do **not** need the maintainer source canon.

## Roles

| Role | Responsibility |
|------|----------------|
| **org-maintainer** | PR review in group KB |
| **canon-maintainer** | build/public push, seed, import to source canon |
| **Member** | personal git; read group/public via MCP |

## DoD

- [ ] Public site builds (MkDocs).
- [ ] Group smoke reads via `knowledge_root_id=group`.
- [ ] Members: personal primary, group/public read-only.
