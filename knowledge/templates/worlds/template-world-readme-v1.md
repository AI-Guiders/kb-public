# Мир **`<world.id>`** (template)

**Идентификатор мира:** `<world.id>` (напр. `arts.music`, `software.authoring`)  
**Каталог:** `knowledge/worlds/<slug>/`

## Слои канона

| Слой | Файл | Роль |
|------|------|------|
| **Status** | `status-<domain>-v1.md` | Operating contract, maintenance, DoD |
| **Playbook** | `playbook-<topic>-v1.md` | Операционные правила |
| **Fundamentals** | `kb-<topic>-fundamentals-v1.md` | Определения, anti-patterns |
| **Matrix** (опц.) | `matrix-<topic>-transfer-v1.md` | Симптом → playbook/kb |

## Router

Строка в `index-knowledge-router-v1.md` (Domain Entry Map) + при необходимости `router-*` в supplement.

## Версия

v1.0 · YYYY-MM-DD