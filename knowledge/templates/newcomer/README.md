---
type: Index
title: '`templates/newcomer/` — онбординг (kb-public → personal · group · white-label)'
description: 'Публикуется в **kb-public**. Без привязки к конкретной GitHub-org: подставляй **`{ORG_SLUG}`** (slug организации).'
tags: [readme, templates]
language: ru
---
# `templates/newcomer/` — онбординг (kb-public → personal · group · white-label)


Публикуется в **kb-public**. Без привязки к конкретной GitHub-org: подставляй **`{ORG_SLUG}`** (slug организации).

| Трек | Playbook |
|------|----------|
| Участник: ANM + kb-public → personal | [`playbook-knowledge-stack-clean-setup.md`](../../domains/agent-operations/playbook-knowledge-stack-clean-setup.md) |
| Основатель org: свой `{ORG_SLUG}/kb` + kb-public | [`playbook-org-kb-white-label.md`](../../domains/agent-operations/playbook-org-kb-white-label.md) |
| Карта контуров | [`map-kb-three-contours.md`](../../domains/agent-operations/map-kb-three-contours.md) |

## Personal + MCP (участник)

| Шаблон | Куда после копирования |
|--------|-------------------------|
| `template-clean-setup-workspace-scope-map.md` | personal `work/local/workspace-scope-map.md` |
| `template-clean-setup-knowledge-roots-index.md` | personal `work/local/knowledge-roots-index.md` |
| `template-clean-setup-hot-knowledge-roots-routing.md` | блок в `agent-notes.md` |
| `template-clean-setup-hot-clean-setup-routing.md` | блок в `agent-notes.md` |
| `template-clean-setup-agent-notes-mcp-toml.toml` | диск + `mcp.json` (не в git канона) |

## Bootstrap group repo (`{ORG_SLUG}/kb`) — maintainer

Подставить `{ORG_SLUG}`, `{ORG_DISPLAY}`, `{REPO_GROUP}`, `{REPO_PUBLIC}` в тексте; сохранить как `CONTRIBUTING.md`, `CODEOWNERS`, `README.md` в корне group-репо.

| Шаблон | Файл в group-репо |
|--------|-------------------|
| `template-org-kb-bootstrap-contributing.md` | `CONTRIBUTING.md` |
| `template-org-kb-bootstrap-codeowners.md` | `CODEOWNERS` |
| `template-org-kb-bootstrap-readme-group.md` | `README.md` |

Верхний индекс: [`../README.md`](../README.md).

