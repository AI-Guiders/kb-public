---
type: Transfer Matrix
title: 'Matrix: rhetoric.pragmatics bridges v1'
description: '**Transfer allow:** speech_situation tuple → XL metadata; Bitzer/Bakhtin K-тезисы → fundamentals spine.'
tags: [rhetoric-pragmatics, matrix, worlds]
language: ru
world: rhetoric
subworld: pragmatics
---
# Matrix: rhetoric.pragmatics bridges v1


| Сосед | Связь | Не смешивать |
|-------|--------|--------------|
| **`domains/agent-operations`** | `speech_situation` теги, playbooks, XL | теория живёт в worlds; operational — в domains |
| **`culture.dialogue-insights`** | инсайты из живого human–agent диалога | не канон риторики |
| **`hci-ux-dx`** | UI tone, error copy, microcopy | продуктовые числа — ADR продукта |
| **`cognition-human-perception`** | когнитивная нагрузка, attention | не register theory |
| **`cognition-neurolinguistics`** | язык в мозге, bilingual | не speech genre catalog |
| **`evidence-humanities-shelf`** | логика, utility, argumentation | **не** складировать риторику в shelf — этот мир |
| **`explainable-learning`** | register axes в \(S\), scenarios | dataset ≠ fundamentals |
| **`personal/`** | самоотчёты как gold `genre=case_report` | не kb-public без чеклиста |

**Transfer allow:** speech_situation tuple → XL metadata; Bitzer/Bakhtin K-тезисы → fundamentals spine.  
**Transfer deny:** риторические тезисы → клинические рекомендации; жанр самоотчёта → legal disclaimer.

## Channel transfer (KB contour → human)

Механика: **`speech_situation (primary)`** = где живёт артефакт; **`when citing to human`** = перенос в канал человека. Шаблон матриц: [`../../templates/matrices/template-transfer-matrix.md`](../../templates/matrices/template-transfer-matrix.md). Перед cross-world: [`../knowledge-engineering/matrix-do-not-transfer.md`](../knowledge-engineering/matrix-do-not-transfer.md).

| Источник / контур | Переносимое | Целевой канал | Boundary check |
|-------------------|-------------|---------------|----------------|
| `personal/` case_report · `kb_canon` | феноменологический текст | `tg` · `friend_tg` | артефакт: `*.send.md` sibling; не KB meta |
| `domains/` playbook · `kb_canon` | operational protocol | `cockpit_dialog` · `operator_pair` / `public_reader` | см. `when citing to human` на карточке |
| `personal/` самоотчёт | — | `kb-public` / group KB | **deny** без [`checklist-sanitize-paths-for-org.md`](../../work/org/checklist-sanitize-paths-for-org.md) |

