# Evidence: Bengio, Louradour, Collobert & Weston (2009) — Curriculum Learning

## Provenance
- source_refs:
  - primary: Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum Learning. *ICML 2009*, pp. 41–48. https://doi.org/10.1145/1553374.1553380
  - pdf: https://ronan.collobert.com/pub/2009_curriculum_icml.pdf
  - text_consulted: **full** (web fetch 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Формализует curriculum learning; опирается на Elman 1993 (starting small), Skinner shaping.

## Metadata
- card_id: kb-ml-learning-dynamics-bengio-2009-curriculum-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, bengio-2009, curriculum-learning, continuation-method, non-convex, generalization, active-learning]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article
- evidence_type: ML theory + empirical (toy + shape + language model)
- confidence: **high** для прироста на показанных задачах; **medium** для «какой именно куррикулум» (зависит от задачи)
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check**
- falsification_trigger: на целевой задаче curriculum не даёт ни скорости, ни generalization при равном бюджете (как у Rohde & Plaut 1999 для части условий)

## Core Unit
- context: порядок предъявления примеров — от простых к сложным — vs случайный.
- signal: правильный куррикулум ускоряет сходимость **и** улучшает generalization (эффект как у регуляризатора).
- action: тренировать по последовательности распределений с растущей энтропией (от лёгких примеров к целевому распределению).
- outcome: ниже test-error / быстрее сходимость на vision и language задачах.
- lesson: куррикулум = **continuation method** для невыпуклой оптимизации (сглаженная задача → постепенно к целевой).

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Куррикулум формализован как монотонная последовательность распределений Q_λ с **растущей энтропией** (от подмножества лёгких примеров к целевому P(z)). |
| **K2** | Гипотеза: куррикулум = **continuation method** — сначала оптимизируем сглаженную (≈выпуклую) версию критерия, потом усложняем; уводит в лучший бассейн притяжения невыпуклого критерия. |
| **K3** | Toy convex (Perceptron/SVM): «чистые»/менее шумные примеры на старте → ниже generalization error (16.3% vs 17.1%, значимо); постепенный ввод сложных ускоряет online-обучение. |
| **K4** | Shape recognition: 2-шаговый куррикулум (BasicShapes → GeomShapes), лучшая генерализация при трате ~половины бюджета на лёгкую фазу; проверено, что выигрыш **не** от «больше примеров» (union-baseline хуже). |
| **K5** | Language model (ranking, Wikipedia, окно 5 слов): куррикулум по **росту словаря** (5k→+5k/проход) обгоняет no-curriculum после переключения на полный словарь (log-rank 2.78 vs 2.83, значимо). |
| **K6** | Эффект двойной: (а) faster convergence (меньше времени на шумные/трудные примеры), (б) better local minima → ведёт себя как регуляризатор (эффект сильнее на test). |
| **K7** | Связь с active learning: ученику выгодно фокусироваться на примерах «на границе» его знаний (ни слишком легко, ни слишком трудно) — авто-темп куррикулума. |

### Ограничения
- «Что есть лёгкий пример» и порядок — задаются эвристикой; неверный куррикулум бесполезен (Rohde & Plaut 1999).
- В части экспериментов curriculum-модель видела суммарно больше примеров — контролировалось union-baseline.

## Operationalization (CASA hypothesis only)
- first_adoption_task: фазовый куррикулум 0–4 (`infancy-corpus-phases`), рост словаря/сложности как у K5.
- validation_check: Exp-DP — sample-efficiency и held-out A(random) vs B(curriculum) при равном бюджете.
- success_criterion: B быстрее сходится **и** ниже held-out error; union-baseline контроль (не «больше входа»).
- rollback_or_mitigation: авто-темп по «границе знаний» (K7) вместо фиксированного расписания.

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (ICML 2009, pp. 41–48)*
