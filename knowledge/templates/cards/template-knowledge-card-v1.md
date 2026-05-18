# Knowledge Card Template v1

Универсальный каркас KB-единицы. Для evidence-карт (`kb-*-evidence-v1`) предпочтительнее [`template-kb-evidence-v1.md`](template-kb-evidence-v1.md) (Layer contract + Fundamentals).

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