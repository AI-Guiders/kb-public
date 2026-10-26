---
type: Status
title: Rhetoric & pragmatics — status v1
description: Риторическая ситуация, речевые жанры, register/pragmatics — **fundamentals + evidence** для агента и XL. Не заменяет `domains/agent-operations` (операционные playbooks) и не `culture.dialogue-insights` (инсайты из живого диалога).
tags: [rhetoric-pragmatics, status, worlds]
language: ru
world: rhetoric
subworld: pragmatics
---
# Rhetoric & pragmatics — status v1


## Scope

Риторическая ситуация, речевые жанры, register/pragmatics — **fundamentals + evidence** для агента и XL. Не заменяет `domains/agent-operations` (операционные playbooks) и не `culture.dialogue-insights` (инсайты из живого диалога).

## Completion state

Status: **Draft v0** (fundamental pass in progress)

Artifacts:

- Hub [`README.md`](README.md)
- [`playbook-rhetoric-pragmatics.md`](playbook-rhetoric-pragmatics.md)
- [`kb-rhetoric-pragmatics-fundamentals.md`](kb-rhetoric-pragmatics-fundamentals.md) — spine (synthesis)
- Evidence: Bitzer 1968, Bakhtin speech genres 1986
- [`map-rhetoric-pragmatics-fundamental-pass.md`](map-rhetoric-pragmatics-fundamental-pass.md) — очередь первоисточников

**Not done v1:**

- Grice / politeness / Searle speech acts (evidence cards)
- Операторский «Камасутра для оратора» — `source_refs` после уточнения издания
- Полный `kb-rhetoric-pragmatics-scientific-evidence-v1` после ≥5 evidence-карт

## Retrieval

Order: `status → playbook → fundamentals → targeted evidence card`.  
Не грузить весь мир на вопрос «как написать самоотчёт» — сначала `speech_situation` на целевой карточке / wetware case report.

## Guardrails

- Не подменять **Psychology** / **Medicine** при клинических запросах.
- Evidence-карточки — извлечение; при споре о формулировках — первоисточник.

## Maintenance Policy

Event-driven. Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).

**Next review triggers:**

- Новая evidence-карта по fundamental pass
- Смена operational speech_situation template
- Operator flags bleed в agent-operations playbooks

