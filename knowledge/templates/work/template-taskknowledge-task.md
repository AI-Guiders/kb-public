---
type: Template
title: Template — TaskKnowledge Task Card
description: '**Контур:** TaskKnowledge work store (не KB).'
tags: [template, templates]
---
# Template — TaskKnowledge Task Card


**Контур:** TaskKnowledge work store (не KB).  
**Когда:** узел DAG после analytics; исполнение только по этой карточке.  
**Где живёт экземпляр:** `{workspace}/.agent-findings/tasks.jsonl` (поля ниже → store); markdown-копия опциональна для review.

---

## Identity

- task_id: (stable token, e.g. `cide-anui-bridge-harvest`)
- title:
- part: (часть системы; один фокус)
- epic_id: (optional)
- status: (`pending` | `ready` | `in_progress` | `done` | `blocked`)

---

## Substance

- as_is: (локальный AS IS этой части — что уже правда)
- to_be: (локальный TO BE **этого шага**, не копия ADR)
- why: (brief + какой EnvInvariant/ADR якорь)
- criterion: (наблюдаемый признак done: тест / export shape / memo check / файл существует — **не** «как в ADR»)

---

## Graph & bounds

- blocked_by: []
- unlocks: []
- member_paths: []  (границы diff)
- sources: []  (якоря: ADR path, memo id, file — не dump)

---

## Verify (закрытие)

- criterion_met: (`yes` | `no` | `n/a`)
- evidence: (как проверили: test name, path, tool result)
- next_ready: (какой task_id стал ready после done)

---

## Field purposes (зачем каждое поле)

| Поле | Зачем |
|------|--------|
| `task_id` / title | стабильный узел маршрута; не путать с chat topic |
| `part` | один смысл на карточку; меньше scope creep |
| `as_is` | не гадать заново после compact |
| `to_be` | цель шага; ADR остаётся EnvInvariant |
| `why` | откуда шаг (brief / analytics / ADR id) |
| `criterion` | verify без «прочитай ADR ещё раз» |
| `blocked_by` / `unlocks` | DAG; `route_next` = ready без unmet blockers |
| `member_paths` | минимальный diff; что не трогать |
| `sources` | source-on-demand; не RAG-dump |
| `status` + evidence | закрытие узла и разблокировка графа |

---

## Mapping → Findings store (today)

| Card field | `TaskRecord` / store today |
|------------|----------------------------|
| task_id, title, as_is, to_be, why | есть |
| blocked_by, unlocks, member_paths, status | есть |
| part, criterion, sources | **gap** — пока в why/to_be текстом или ждать schema bump |
| Verify evidence | пока вне store (chat / test log) |

Не блокировать работу: criterion можно временно писать первой строкой `to_be` или в `why` как `criterion: …` до расширения схемы.
---

## Storage (2026-07-17)

Экземпляр живёт как **markdown** under `{workspace}/.task-knowledge/tasks/<task_id>.md` (см. layout template). Findings JSONL — не целевой формат.

| Card field | md card |
|------------|--------|
| all Substance/Graph/Verify fields | first-class in template |
| section upsert | when MCP lands (AN markers) |

