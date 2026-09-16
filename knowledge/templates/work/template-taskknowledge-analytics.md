# Template — TaskKnowledge Analytics Card
**Tags:** #template #templates


**Контур:** TaskKnowledge (не KB-карточка).  
**Когда:** после EnvInvariant/ADR, **до** реализации.  
**Куда класть заполненный экземпляр:** per-workspace work store (сегодня findings tasks + optional scratch `…/scratch/analytics-<adr-or-epic>-YYYY-MM-DD.md`); **не** в канон `knowledge/` как «ещё один ADR».

EnvInvariant / ADR ref: (path or id)
Epic id: (optional)
Status: (`draft` | `ready_for_dag` | `superseded`)

---

## Purpose

Разложить Decision/Consequences ADR на **Parts → Facts/Gaps → Tasks + criteria**, чтобы агент получил маршрут, а не стену текста.

---

## EnvInvariant (якорь, не dump)

- adr_or_note:
- one_line_decision: (1–2 предложения; не копировать весь ADR)
- must_not_break: (инварианты, которые шаги не имеют права нарушить)

---

## Parts (что трогаем)

| part_id | часть системы | зачем в эпике |
|---------|---------------|---------------|
| | | |

---

## Facts (локальный AS IS)

Уже установленная правда. Источник — path / memo / тест.

| fact_id | утверждение | source |
|---------|-------------|--------|
| | | |

---

## Gaps (чего нет относительно эпика)

| gap_id | чего нет | related part | closes_via_task |
|--------|----------|--------------|-----------------|
| | | | |

---

## Task DAG (черновик узлов)

Каждый узел потом = Task card (см. `template-taskknowledge-task.md`). Здесь — граф.

| task_id | title | part | blocked_by | unlocks | criterion (черновик) |
|---------|-------|------|------------|---------|----------------------|
| | | | | | |

---

## Ready now

- next_task_id: (первый `ready` / нет blockers)
- why_this_first:

---

## Out of scope (этот эпик)

- …

---

## Field purposes (зачем поля карточки)

| Блок | Зачем агенту |
|------|----------------|
| EnvInvariant якорь | не тащить ADR целиком; сверять шаги с инвариантом |
| Parts | не размывать diff «по всему репо» |
| Facts | не rediscover то, что уже установлено |
| Gaps | явная цель шагов, не «сделай как в ADR» |
| Task DAG + criterion | исполняемая спецификация + verify |
| Ready now | ответ «что делать дальше» без RAG |

