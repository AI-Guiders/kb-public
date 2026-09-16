# {ORG_DISPLAY} — group KB (`{REPO_GROUP}`)
**Tags:** #template #templates


Приватный **командный** контур знаний (chmod **g**, MCP `knowledge_root_id=group`).

| Контур | Репозиторий | Доступ |
|--------|-------------|--------|
| **Public** | `{REPO_PUBLIC}` | read-only, онбординг |
| **Group** | **этот репо** | PR + org-maintainer |
| **Personal** | у каждого участника | не здесь |

## Онбординг

- Участник команды: [`playbook-knowledge-stack-clean-setup.md`](knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup.md) + read-only clone этого репо в MCP.
- Основатель / maintainer org: [`playbook-org-kb-white-label.md`](knowledge/domains/agent-operations/playbook-org-kb-white-label.md).

## Smoke

`knowledge/group/smoke-test.md` — проверка MCP read (`knowledge_root_id=group`).

## Лицензия

Тексты — **CC BY-SA 4.0** (`LICENSE`). Код MCP — отдельно (**MIT** в репозитории agent-notes-mcp).

