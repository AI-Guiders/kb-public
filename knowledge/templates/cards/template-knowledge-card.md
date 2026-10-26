---
type: Template
title: Knowledge Card Template v1
description: Универсальный каркас KB-единицы. Для evidence-карт (`kb-*-evidence-v1`) предпочтительнее [`template-kb-evidence.md`](template-kb-evidence.md) (Layer contract + Fundamentals).
tags: [template, templates]
language: ru
---

﻿# Knowledge Card Template v1

Универсальный каркас KB-единицы. Для evidence-карт (`kb-*-evidence-v1`) предпочтительнее [`template-kb-evidence.md`](template-kb-evidence.md) (Layer contract + Fundamentals).

## Provenance (происхождение)
- source_refs: (источники: `revision:... line:N`; `transcript:... line:M`; или документ/URL)
- created_at: (дата первой фиксации)
- updated_at: (дата последнего обновления)
- author: (опционально; для совместного накопления — кто внёс/извлёк)

## Metadata
- card_id:
- world:
- layer: (`world` | `router` | `meta`)
- tags:
- status: (`active` | `deprecated` | `draft`)

## Speech Situation (опционально)

Для operational карточек с явным жанром/адресатом — см. [`template-speech-situation-metadata.md`](template-speech-situation-metadata.md).

- speech_situation_primary: (audience · goal · genre · channel · stakes · distance)
- speech_situation_when_citing_to_human: (если агент переносит в другой канал)
- speech_situation_forbidden_moves: (опционально)

## Epistemic Linkage
- epistemic_basis: (`fact` | `inference` | `hypothesis`)
- evidence_type:
- confidence: (`low` | `medium` | `high`)
- uncertainty:
- falsification_trigger:
- transfer_boundary:

## Core Unit
- context:
- signal:
- action:
- outcome:
- lesson:

## Operationalization
- first_adoption_task:
- validation_check:
- success_criterion:
- rollback_or_mitigation:

## Lifecycle
- supersedes:
- superseded_by:
- deprecation_reason:

