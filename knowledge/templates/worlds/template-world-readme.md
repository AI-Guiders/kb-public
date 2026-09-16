**Tags:** #template #templates

﻿# Мир **`<world.id>`** (template)

**Идентификатор мира:** `<world.id>` (напр. `arts.music`, `software.authoring`)  
**Каталог:** `knowledge/worlds/<slug>/`

## Слои канона

| Слой | Файл | Роль |
|------|------|------|
| **Status** | `status-<domain>.md` | Operating contract, maintenance, DoD |
| **Playbook** | `playbook-<topic>.md` | Операционные правила |
| **Fundamentals** | `kb-<topic>-fundamentals.md` | Определения, anti-patterns |
| **Matrix** (опц.) | `matrix-<topic>-transfer.md` | Симптом → playbook/kb |

## Router

Строка в `index-knowledge-router.md` (Domain Entry Map) + при необходимости `router-*` в supplement. **Без** путей к `work/` в публичной строке.

## Публикация (kb-public)

Экземпляр **любого** мира попадёт в kb-public. Перед коммитом: [`playbook-kb-world-public-authoring.md`](../worlds/knowledge-engineering/playbook-kb-world-public-authoring.md) (общий чеклист для всех `worlds/<slug>/`). Clone/scope/диск — не в этом README.

