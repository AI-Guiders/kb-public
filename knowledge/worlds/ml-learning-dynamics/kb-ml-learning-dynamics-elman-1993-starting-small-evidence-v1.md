# Evidence: Elman (1993) — Learning and development in NN: the importance of starting small

## Provenance
- source_refs:
  - primary: Elman, J. L. (1993). Learning and development in neural networks: the importance of starting small. *Cognition*, *48*(1), 71–99. https://doi.org/10.1016/0010-0277(93)90058-4
  - pdf: https://web.cs.swarthmore.edu/~meeden/cogs1/s07/elman_cognition1993.pdf
  - text_consulted: **full** (web fetch 2026-05-31; 29 pp.)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: SRN-моделирование. Связан с Rohde & Plaut (1999) — критика/частичный no-replication «starting small».

## Metadata
- card_id: kb-ml-learning-dynamics-elman-1993-starting-small-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, elman-1993, curriculum, starting-small, SRN, working-memory, staged-capacity]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article
- evidence_type: connectionist simulation
- confidence: **high** для эффекта в SRN на этой задаче; **medium** для генерализации (см. Rohde & Plaut 1999)
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check** (мотивация staged-capacity / куррикулум, не доказательство для конкретного субстрата)
- falsification_trigger: контролируемая replication показывает, что full-capacity сеть учит ту же задачу так же — как и заявили Rohde & Plaut (1999) для части условий

## Core Unit
- context: SRN учат обрабатывать сложные предложения (relative clauses, number agreement, verb argument structure).
- signal: full-capacity «взрослая» сеть **проваливает** обучение; успех только при старте с **ограниченной рабочей памятью** и постепенном «созревании».
- action: staged increase ёмкости/окна (или фильтрация входа по сложности) на ранней фазе.
- outcome: успешное усвоение грамматической структуры; «starting small» как enabling condition.
- lesson: ограничение ресурсов на старте — не баг, а фильтр, фокусирующий обучение на простой структуре до сложной.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | SRN на корпусе сложных предложений (вложенные клаузы, согласование числа, типы аргументов глагола): сеть с полной ёмкостью с самого начала — **не сходится** к решению. |
| **K2** | Успех — только при **staged regime**: старт с ограниченной working memory (короткое эффективное окно), затем постепенное «созревание» к взрослому состоянию. |
| **K3** | Эквивалентный эффект достигается фильтрацией **входа**: ранняя фаза видит более простые/короткие конструкции (ограничение памяти = неявный фильтр данных). |
| **K4** | Интерпретация: раннее ограничение **сужает пространство решений**, уводя от ложных локальных минимумов в сложных доменах (язык, «projection problem», Gold 1967). |
| **K5** | Парадокс «иногда нужно start big» (Harris 1991): для некоторых задач полный датасет с начала лучше; часть II статьи выводит общие принципы gradient-descent, объясняющие когда что. |
| **K6** | Развитийная мораль: длительная незрелость может быть **адаптивной** — «starting small» делает обучаемым то, что иначе неучимо. |

### Ограничения
- Эффект показан на конкретной SRN/задаче; Rohde & Plaut (1999) ставят под вопрос универсальность «starting small» для языка.
- Не утверждает оптимальности для произвольного субстрата.

## Operationalization (CASA hypothesis only)
- first_adoption_task: куррикулум фаз 0–2 в `infancy-corpus-phases` (B0→B2) как «starting small».
- validation_check: Exp-DP — staged vs full-capacity/full-data baseline на одинаковом held-out.
- success_criterion: staged быстрее сходится / лучше generalize при равном бюджете.
- rollback_or_mitigation: учесть «start big» класс задач (K5) — не делать staged догмой; мерить, а не предполагать.

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (Cognition 48:71–99)*