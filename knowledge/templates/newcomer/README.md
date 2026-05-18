# `templates/newcomer/` — онбординг (kb-public → personal · group · white-label)

Публикуется в **kb-public**. Без привязки к конкретной GitHub-org: подставляй **`{ORG_SLUG}`** (slug организации).

| Трек | Playbook |
|------|----------|
| Участник: ANM + kb-public → personal | [`playbook-knowledge-stack-clean-setup-v1.md`](../../domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md) |
| Основатель org: свой `{ORG_SLUG}/kb` + kb-public | [`playbook-org-kb-white-label-v1.md`](../../domains/agent-operations/playbook-org-kb-white-label-v1.md) |
| Карта контуров | [`map-kb-three-contours-v1.md`](../../domains/agent-operations/map-kb-three-contours-v1.md) |

## Personal + MCP (участник)

| Шаблон | Куда после копирования |
|--------|-------------------------|
| `template-clean-setup-workspace-scope-map-v1.md` | personal `work/local/workspace-scope-map-v1.md` |
| `template-clean-setup-knowledge-roots-index-v1.md` | personal `work/local/knowledge-roots-index-v1.md` |
| `template-clean-setup-hot-knowledge-roots-routing-v1.md` | блок в `agent-notes.md` |
| `template-clean-setup-hot-clean-setup-routing-v1.md` | блок в `agent-notes.md` |
| `template-clean-setup-agent-notes-mcp-toml-v1.toml` | диск + `mcp.json` (не в git канона) |

## Bootstrap group repo (`{ORG_SLUG}/kb`) — maintainer

Подставить `{ORG_SLUG}`, `{ORG_DISPLAY}`, `{REPO_GROUP}`, `{REPO_PUBLIC}` в тексте; сохранить как `CONTRIBUTING.md`, `CODEOWNERS`, `README.md` в корне group-репо.

| Шаблон | Файл в group-репо |
|--------|-------------------|
| `template-org-kb-bootstrap-contributing-v1.md` | `CONTRIBUTING.md` |
| `template-org-kb-bootstrap-codeowners-v1.md` | `CODEOWNERS` |
| `template-org-kb-bootstrap-readme-group-v1.md` | `README.md` |

Верхний индекс: [`../README.md`](../README.md).
