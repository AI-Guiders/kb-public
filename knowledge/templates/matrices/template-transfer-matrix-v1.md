# Transfer matrix template (matrix-`<slug>`-v1)

**Имя файла:** `matrix-<domain-or-topic>-<purpose>-v1.md` (обычно в `worlds/<world>/`).

**Примеры в каноне:**
- `worlds/knowledge-engineering/matrix-culture-routing-v1.md`
- `worlds/knowledge-engineering/matrix-do-not-transfer-v1.md`
- `worlds/software-authoring/matrix-software-cross-domain-transfer-v1.md`

**Не путать с:** Domain Entry Map в `index-knowledge-router-v1.md` — матрица компактнее, для **переноса / маршрутизации** между playbook и kb.

---

## Purpose

(1–3 предложения: какую ошибку маршрутизации снимает матрица.)

## Transfer contract (обязательно для cross-world)

- Переносить **принципы и порядок чтения**, не копировать детали без проверки.
- Перед cross-world: [`worlds/knowledge-engineering/matrix-do-not-transfer-v1.md`](../../worlds/knowledge-engineering/matrix-do-not-transfer-v1.md).
- Культура/формулировки: при необходимости [`matrix-culture-routing-v1.md`](../../worlds/knowledge-engineering/matrix-culture-routing-v1.md).
- Порядок загрузки: `status-*` → **эта матрица** (строка) → целевой `playbook-*` → `kb-*`.

## Core flow (опционально, для procedural routing)

1. …
2. …
3. fallback: …

## Fast symptom router (таблица для агента)

| Симптом / триггер | Сначала | Потом | Не делать |
|-------------------|---------|-------|-----------|
| … | `playbook-…` | `kb-…` | … |

## Matrix (детально)

| Источник / условие | Переносимое | Целевой артефакт | Boundary check |
|--------------------|-------------|------------------|----------------|
| … | … | … | … |

## Decision table (опционально)

| Condition | Action |
|-----------|--------|
| … | … |

## Anti-patterns

- …

## Evidence contract (опционально)

- когда нужен `source_refs` / уровень уверенности;
- когда оставаться в fallback.

## Связь с роутером

После стабилизации — строка в `index-knowledge-router-v1.md` (Domain Entry Map) и при необходимости `router-*` в supplement.
