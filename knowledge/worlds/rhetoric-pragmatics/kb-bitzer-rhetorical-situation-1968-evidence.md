---
type: Evidence Card
title: 'Evidence: Bitzer (1968) — The Rhetorical Situation'
description: Комбинация persons, events, objects, relations, которая **требует** риторического ответа. Риторическое произведение **функционирует** для действия в мире и **контролируется** ситуацией, которая его порождает.
tags: [rhetoric-pragmatics, paper-evidence, bitzer, worlds]
world: rhetoric
subworld: pragmatics
---
# Evidence: Bitzer (1968) — The Rhetorical Situation


## Provenance

- source_refs:
  - primary: Bitzer, L. F. (1968). The rhetorical situation. *Philosophy & Rhetoric*, *1*(1), 1–14. Pennsylvania State University Press.
  - abstract: ERIC ED043604 — https://eric.ed.gov/?id=ED043604
  - text_consulted: teaching upload PDF (excerpt), Penn State course site — http://sites.psu.edu/fa2014vicarocas201/wp-content/uploads/sites/15238/2014/08/40236733.pdf — **не** официальный OA издателя; сверять спорные формулировки с журналом при доступе.
- created_at: 2026-08-22
- updated_at: 2026-08-22
- extraction_note: Журнальный текст **closed** (OpenAlex). Карточка по ERIC abstract + доступному PDF; численные цитаты — только с полным текстом.

## Metadata

- card_id: kb-bitzer-rhetorical-situation-1968-evidence-v1
- world: rhetoric.pragmatics
- layer: knowledge
- tags: [paper-evidence, rhetorical-situation, exigence, audience, constraints]
- status: active

## Epistemic linkage

- epistemic_basis: synthesis_from_primary_literature
- evidence_type: peer-reviewed article (abstract + partial text)
- confidence: **high** для трёх составляющих ситуации; **medium** для сильных modal claims о «предписании» ответа
- transfer_boundary: модель ситуации как **данной** — спорна (см. Vatz Tier 1); не юридическая «ситуация».
- falsification_trigger: если operational speech_situation tuple не мапится на exigence/audience/constraints без ad hoc полей — пересмотреть enum в template.

## Layer contract

- **Fundamentals** ниже — для агента без журнала на каждый шаг.
- **Источник** — для споров о терминах.

## Fundamentals

### K1 — Rhetorical situation

Комбинация persons, events, objects, relations, которая **требует** риторического ответа. Риторическое произведение **функционирует** для действия в мире и **контролируется** ситуацией, которая его порождает.

### K2 — Exigence

Условие, зовущее к **действию**, которое должно быть **организирующим принципом** дискурса.

### K3 — Audience

Люди, **способные** произвести изменение (не просто «слушатели»).

### K4 — Constraints

Элементы ситуации + внесённые оратором, которые **ограничивают** решение или **модифицируют** exigence.

### K5 — Prescription (уместность)

Ситуация **предписывает** тип, структуру, сложность и **уместность** риторического ответа (пример в источнике: смерть президента Кеннеди и тип откликов).

## Operationalization

- Тег `speech_situation`: **goal** ≈ exigence; **audience**; **genre/channel/constraints** ≈ constraints.
- XL: A с правильным фактом + FAQ-disclaimer = нарушение audience/constraints для `friend_tg` self-report.

## Lifecycle

- related: `kb-bakhtin-speech-genres-1986-evidence-v1`, [`kb-vatz-rhetorical-situation-1973-evidence-v1`](kb-vatz-rhetorical-situation-1973-evidence.md)

