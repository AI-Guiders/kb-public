# Evidence: Robins (1995) — Catastrophic forgetting, rehearsal and pseudorehearsal

## Provenance
- source_refs:
  - primary: Robins, A. (1995). Catastrophic forgetting, rehearsal and pseudorehearsal. *Connection Science*, *7*(2), 123–146. https://doi.org/10.1080/09540099550039318
  - secondary: Semantic Scholar (CorpusID:22882861); tandfonline abstract; обзор Robins (1998) «Solutions to the catastrophic forgetting problem» (CogSci)
  - text_consulted: **abstract + secondary** (полный PDF за paywall tandfonline на 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Оригинал термина **pseudorehearsal**; прямой предшественник generative replay.

## Metadata
- card_id: kb-ml-learning-dynamics-robins-1995-pseudorehearsal-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, robins-1995, pseudorehearsal, rehearsal, sweep-rehearsal, catastrophic-forgetting, generative-replay]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article (читан по abstract+secondary)
- evidence_type: connectionist simulation
- confidence: **medium** (основные тезисы из abstract/обзоров надёжны; числа экспериментов не сверены по первоисточнику)
- read_depth: **abstract+secondary** (не full — честно помечено; добрать full PDF при доступе)
- transfer_boundary: ML → CASA **allow-with-check**
- falsification_trigger: pseudo-элементы не сохраняют старое лучше, чем отсутствие rehearsal, на сопоставимой задаче

## Core Unit
- context: catastrophic forgetting есть, но старые данные **недоступны** для переобучения.
- signal: rehearsal (переобучать часть старых) работает, но требует доступа к ним.
- action: **pseudorehearsal** — сгенерировать случайные входы, взять **собственные выходы сети** как псевдо-метки и rehearse их вместе с новым.
- outcome: защита старого **без доступа к исходным данным**; «sweep rehearsal» особенно эффективен.
- lesson: можно «переигрывать» поведение сети, а не данные — основа generative replay.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Воспроизведены эксперименты Ratcliff (1990), вкл. recency-rehearsal; развиты более эффективные режимы. |
| **K2** | **Rehearsal** (переобучение подмножества старых элементов вместе с новыми) сильно снижает forgetting; **sweep rehearsal** — лучший. |
| **K3** | Ограничение rehearsal: старые данные могут быть недоступны. |
| **K4** | **Pseudorehearsal**: случайные «pseudo-inputs» + выходы текущей сети → pseudo-items, которые rehearse'ат вместе с новыми; сохраняют функцию без доступа к исходной популяции. |
| **K5** | Интерпретация через function-approximation: rehearsal фиксирует точки функции, удерживая аппроксимацию при дообучении. |

### Ограничения
- read_depth не full: числа/детали sweep vs recency не сверены по PDF.
- Качество pseudo-items зависит от распределения pseudo-inputs.

## Operationalization (CASA hypothesis only)
- first_adoption_task: альтернатива «хранить все эпизоды» (ADR-0009): генерировать pseudo-эпизоды из NCA для rehearsal при ограниченной памяти.
- validation_check: pseudorehearsal vs полный replay vs без rehearsal на retention@N.
- success_criterion: pseudorehearsal близок к полному replay при меньшей памяти.
- rollback_or_mitigation: контролировать распределение pseudo-inputs (K-огр.).

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — abstract+secondary (Connection Science 7(2):123–146)*
