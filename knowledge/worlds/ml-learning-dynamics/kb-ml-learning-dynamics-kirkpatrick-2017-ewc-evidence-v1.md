# Evidence: Kirkpatrick et al. (2017) — Overcoming catastrophic forgetting (EWC)

## Provenance
- source_refs:
  - primary: Kirkpatrick, J., Pascanu, R., Rabinowitz, N., … Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *PNAS*, *114*(13), 3521–3526. https://doi.org/10.1073/pnas.1611835114
  - preprint: arXiv:1612.00796 (v2, 25 Jan 2017) https://arxiv.org/abs/1612.00796
  - text_consulted: **full** (web fetch arXiv 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: EWC — регуляризация против забывания; явно опирается на McClelland 1995 (system-level consolidation/replay) как альтернативу и на синаптическую консолидацию.

## Metadata
- card_id: kb-ml-learning-dynamics-kirkpatrick-2017-ewc-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, kirkpatrick-2017, EWC, catastrophic-forgetting, continual-learning, fisher-information, synaptic-consolidation]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article (PNAS) + empirical
- evidence_type: ML algorithm + experiments (MNIST permutations, Atari 2600)
- confidence: **high** для эффекта EWC на показанных бенчмарках; **medium** для масштаба/точности диагональной Fisher-аппроксимации (см. поздние критики)
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check** (механизм защиты важных весов; альтернатива/дополнение к replay)
- falsification_trigger: на сопоставимом бюджете EWC не превосходит наивный sequential fine-tune, или защита весов рушит обучение новой задачи

## Core Unit
- context: последовательное обучение задачам без хранения всех данных.
- signal: наивный SGD на задаче B **катастрофически забывает** задачу A (важные для A веса меняются под B).
- action: добавить **квадратичный штраф**, тянущий веса к их старым значениям с жёсткостью ∝ важности (диагональ Fisher information).
- outcome: несколько задач (MNIST permutations; серия Atari) усвоены последовательно без забывания старых.
- lesson: **task-specific synaptic consolidation** — избирательно замедлять обучение важных весов — решает continual learning дешевле, чем хранить и переигрывать все данные.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Catastrophic forgetting (McCloskey & Cohen 1989; French 1999) — при sequential-обучении веса, важные для A, переписываются под B. |
| **K2** | Multitask (interleave всех данных) избегает забывания, но требует одновременного доступа к данным; replay всех эпизодов (system-level consolidation, McClelland 1995) **не масштабируется** (память ∝ числу задач). |
| **K3** | **EWC**: квадратичный штраф Σ (λ/2) F_i (θ_i − θ*_{A,i})^2, где F_i — диагональ Fisher information (важность веса для A); «пружина», тянущая важные веса к старым значениям. |
| **K4** | Важность — из лапласовой аппроксимации posterior p(θ|D_A) гауссианой со средним θ*_A и точностью = диагональ Fisher. Over-parameterization → решение B обычно есть рядом с A. |
| **K5** | Эксперименты: permuted-MNIST (несколько задач последовательно) и серия игр Atari 2600 — EWC держит старые задачи там, где наивный fine-tune забывает. |
| **K6** | Нейро-аналогия: устойчивые дендритные шипики, переживающие новое обучение (Yang 2009; Hayashi-Takagi 2015) — синаптическая консолидация; EWC — её инженерный аналог. |

### Ограничения
- Диагональная Fisher — приближение; точная реализация EWC обсуждается (Huszar 2018; online-EWC).
- Дополняет, а не заменяет replay; на длинных последовательностях задач есть дрейф.

## Operationalization (CASA hypothesis only)
- first_adoption_task: защита важных весов NCA при дообучении на новых шардах/правилах (альтернатива/дополнение к replay ADR-0009).
- validation_check: retention@N с EWC-штрафом vs без, при равном бюджете.
- success_criterion: меньше forgetting старых концептов/правил без падения на новых.
- rollback_or_mitigation: комбинировать с replay (K2/K6); следить за дрейфом на длинных сериях.

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (PNAS 114(13):3521–3526 / arXiv:1612.00796)*