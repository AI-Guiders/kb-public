# Contributing to {ORG_DISPLAY} KB (group)

Спасибо за вклад в **организационный** слой знаний `{REPO_GROUP}`. Это **не** личный канон участника и **не** замена `{REPO_PUBLIC}` для внешнего мира.

## Три контура (куда писать)

| Контур | Репозиторий | Ты пишешь сюда? |
|--------|-------------|-----------------|
| **Personal** | свой `agent-notes` (или fork) | `personal/`, `work/local/` с путями диска, hot ниже `public-cut` |
| **Group** | **`{REPO_GROUP}`** (этот репо) | `knowledge/worlds/`, playbooks, router, **`work/projects/`** (без путей диска) |
| **Public** | **`{REPO_PUBLIC}`** | сборка и push — **canon-maintainer**; скрипты в **`scripts/`** group-репо |

Подробнее: `knowledge/domains/agent-operations/map-kb-three-contours-v1.md`, `playbook-org-kb-white-label-v1.md` (в kb-public).

## Перед первым PR

1. **Карта workspace** — только в **личном** каноне: `knowledge/work/local/workspace-scope-map-v1.md` (не коммитить в group).
2. **MCP** — `agent-notes-mcp.toml` с `[[knowledge.read_only]]` id `group` → clone `{REPO_GROUP}`.
3. Проверка: `read_knowledge_file(..., knowledge_root_id=group)`; `write_knowledge_file` в group → отклонение.

## Что можно менять в group

- `knowledge/worlds/**`, `knowledge/domains/**`, router, META, ADR
- `knowledge/work/projects/**` — карточки без абсолютных путей
- `knowledge/group/**` — team-wide stubs (например smoke)

## Чего не должно быть в group

- `knowledge/personal/**`
- Реальные `work/local/*` с дисками (кроме шаблонов / `.gitignore`)
- Секреты, токены, `public-kb.push` с личными remotes

## Review

Минимум один **org-maintainer** (`@{ORG_SLUG}/kb-maintainers` или CODEOWNERS).

## Лицензия

Тексты KB — **CC BY-SA 4.0** (см. `LICENSE`).
