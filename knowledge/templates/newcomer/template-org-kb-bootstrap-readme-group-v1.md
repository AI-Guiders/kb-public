# {ORG_DISPLAY} — group KB (`{REPO_GROUP}`)

Приватный **командный** контур знаний (chmod **g**, MCP `knowledge_root_id=group`).

| Контур | Репозиторий | Доступ |
|--------|-------------|--------|
| **Public** | `{REPO_PUBLIC}` | read-only, онбординг |
| **Group** | **этот репо** | PR + org-maintainer |
| **Personal** | у каждого участника | не здесь |

## Онбординг

- Участник команды: [`playbook-knowledge-stack-clean-setup-v1.md`](knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md) + read-only clone этого репо в MCP.
- Основатель / maintainer org: [`playbook-org-kb-white-label-v1.md`](knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md).

## Smoke

`knowledge/group/smoke-test-v1.md` — проверка MCP read (`knowledge_root_id=group`).

## Лицензия

Тексты — **CC BY-SA 4.0** (`LICENSE`). Код MCP — отдельно (**MIT** в репозитории agent-notes-mcp).
