---
type: Note
title: Card schema — applicability + inference fields
description: '**Status:** live · [CDP-ADR-0001](../../work/projects/door-to-singularity/cascade-ide/CDP-ADR-0001-llm-native-applicability-inference.md)'
tags: [llm-ready, packs, cdp, schema]
language: ru
world: _llm
subworld: native-packs
---
# Card schema — applicability + inference fields

**Status:** live · [CDP-ADR-0001](../../work/projects/door-to-singularity/cascade-ide/CDP-ADR-0001-llm-native-applicability-inference.md)  
**Date:** 2026-07-21

Рекомендуемые поля на **markdown cards**. Существующие cards без них валидны; новые — заполнять. Не дублировать длинный prose — короткие лицензии.

## Definition cards (`definitions/<id>.md`)

| Field | Role |
|-------|------|
| `applies_when` | Когда лицензия есть (область / предусловия). |
| `does_not_apply` | Когда shortcut врёт / область другая. |
| `inference_hooks` | ids process или related cards для шага (I) после (A). |
| `llm_cue` | (уже есть) вопрос перед promote. |
| `related` | (уже есть) рёбра словарей / соседние cards. |

## Misconception cards (`misconceptions/<id>.md`)

| Field | Role |
|-------|------|
| `false_claim` | (уже есть) |
| `why_wrong` | (уже есть) — часто = `does_not_apply` школьного правила |
| `correction_definition` | (уже есть) |
| `applies_when` | optional: когда false_claim *выглядит* правдоподобно |
| `does_not_apply` | optional: где карикатура ломается |
| `inference_hooks` | optional: process id после correction |

## Process (`processes.toml`)

Канон двухтакта: **`applicability-then-infer`** в pack `epistemic-scene`.

## Procedure (`procedures.toml`)

When-cards (host-rule analogue): [PROCEDURE-SCHEMA.md](./PROCEDURE-SCHEMA.md) · [CDP-ADR-0003](../../work/projects/door-to-singularity/cascade-ide/CDP-ADR-0003-llm-native-procedures.md). Pilot: `kolb-journal-park`.

## CASA → LLM map (ideas only)

| CASA | LLM-native |
|------|------------|
| isa / affords / arg validate | `applies_when` / `does_not_apply` + domain pack |
| check_consistency / rules / chain | process (I) + `llm_cue` + later Verify oracle |
| proof / ·дано | claim-observation-split + anchors |
| curiosity / Kolb | deferred CDP-ADR-0002 |

