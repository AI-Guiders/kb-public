# Human perception domain — status v1
**Tags:** #cognition-human-perception #status #worlds


## Scope

Психофизиологически мотивированный слой между **когнитивными основами** и **операционными** правилами UX/IDE/агента: внимание, нагрузка, стресс, заметность — без претензии на клиническую полноту.

## Completion state

Status: **Done v1**

Artifacts:

- [`README.md`](README.md) — мир `cognition.human-perception`
- [`kb-human-perception-fundamentals.md`](kb-human-perception-fundamentals.md) — fundamentals
- [`kb-human-perception-scientific-evidence.md`](kb-human-perception-scientific-evidence.md) — первоисточники и DOI (слой evidence)
- [`kb-human-perception-miller-1956-evidence.md`](kb-human-perception-miller-1956-evidence.md), [`kb-human-perception-treisman-gelade-1980-evidence.md`](kb-human-perception-treisman-gelade-1980-evidence.md) — evidence-карточки по первоисточникам (тезисы, методы, границы)
- [`playbook-human-perception-operational.md`](playbook-human-perception-operational.md) — operational

## Guardrails

- Не подменять домен **Psychology** при клинических/терапевтических запросах.
- Продуктовые числа и размещение панелей — **ADR/репо продукта**; KB не дублирует.

## Router

- Domain Entry Map: `index-knowledge-router.md`
- Триггеры: `router-human-perception` в `index-knowledge-router-supplement.md`

*Версия: v1.4 · 2026-04-20 — семантические имена `kb-human-perception-*-evidence-v1`*

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

