# Три контура KB

Используй **`{ORG_SLUG}`** — slug вашей GitHub-организации. Пример: `AI-Guiders` — не обязателен.

**Полный текст:** [map-kb-three-contours-v1.md](../knowledge/domains/agent-operations/map-kb-three-contours-v1.md)

## Контуры

| # | Контур | Где | MCP |
|---|--------|-----|-----|
| **1** | **Личный канон** | ваш `agent-notes` | primary / **u** |
| **2a** | **Group KB** | `{ORG_SLUG}/kb` private | `knowledge_root_id=group` / **g** |
| **2b** | **Public KB** | `{ORG_SLUG}/kb-public` | `public` / **o** |
| **3** | **Workspace** | корни IDE, код продуктов | hot — зеркало **(1)** |

`work/` и `personal/` — только в **(1)**, в kb-public **нет**.

## Шпаргалка

| Содержание | Контур |
|------------|--------|
| Playbooks, роутер | **1** |
| Карточки проектов | **1** `work/projects/` |
| Черновики | **1** `personal/` |
| Код | **3** |
| Публичный срез | **2b** |

## Свой org

[White-label](white-label.md) · [Чистая установка](clean-setup.md)
