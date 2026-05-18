# KB evidence card template (kb-`<slug>`-evidence-v1)

**Имя файла:** `kb-<topic>-evidence-v1.md` (в `knowledge/` или `worlds/<world>/`).

**Связь:** тот же каркас, что [`template-knowledge-card-v1.md`](template-knowledge-card-v1.md); этот файл — **evidence-профиль** с Layer contract и опциональным слоем Fundamentals (пример: `worlds/evidence-humanities-shelf/kb-covey-7-habits-evidence-v1.md`).

---

## Provenance (происхождение)
- source_refs: (книга, URL, `revision:…`, `transcript:…`)
- created_at:
- updated_at:
- author: (опционально)
- extraction_note: (опционально: издание, язык, ограничения цитирования)

## Metadata
- card_id: kb-<topic>-evidence-v1
- world: (напр. `culture.global`, `software.engineering-evidence`)
- layer: (`world` | `router` | `meta`)
- tags: []
- status: (`active` | `deprecated` | `draft`)

## Epistemic Linkage
- epistemic_basis: (`fact` | `inference` | `hypothesis`)
- evidence_type: (book | paper | spec | experience | …)
- confidence: (`low` | `medium` | `high`)
- uncertainty:
- falsification_trigger:
- transfer_boundary:

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — самодостаточный опорный слой; агент не обязан открывать первоисточник на каждый шаг.
- **Core Unit + Operationalization** — сжатый триггер и применение.
- **Источник** — для сверки формулировок и изданий, не обязательный шаг в operational-контуре.

## Core Unit
- context:
- signal:
- action:
- outcome:
- lesson:

## Fundamentals (опционально, для evidence-карт)

Развёрнутые определения, таблицы, якоря «где в источнике» — достаточно для рассуждения без книги/PDF на каждый запрос.

### …

## Operationalization
- first_adoption_task:
- validation_check:
- success_criterion:
- rollback_or_mitigation:

## Lifecycle
- supersedes:
- superseded_by:
- deprecation_reason: