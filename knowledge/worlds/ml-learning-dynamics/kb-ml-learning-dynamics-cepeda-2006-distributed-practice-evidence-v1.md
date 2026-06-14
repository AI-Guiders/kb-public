# Evidence: Cepeda, Pashler, Vul, Wixted & Rohrer (2006) — Distributed practice (spacing) meta-analysis

## Provenance
- source_refs:
  - primary: Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, *132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354
  - pdf: https://www.yorku.ca/ncepeda/publications/CPVWR2006.pdf
  - text_consulted: **full** (web fetch 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Якорь для spacing effect; определяет ISI/retention-interval как совместные факторы.

## Metadata
- card_id: kb-ml-learning-dynamics-cepeda-2006-distributed-practice-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, cepeda-2006, spacing-effect, distributed-practice, meta-analysis, ISI, retention-interval, scheduling]
- status: active

## Epistemic Linkage
- epistemic_basis: meta-analysis (317 эксп., 184 статьи) — human verbal recall
- evidence_type: quantitative synthesis
- confidence: **high** для spacing>massing; **medium** для точной формы ISI×RI (литература неравномерна)
- read_depth: **full**
- transfer_boundary: human memory → CASA **allow-with-check** (мотивирует расписание rehearsal; не прямой перенос человеческих интервалов)
- falsification_trigger: на CASA spaced не превосходит massed rehearsal при равном бюджете; или оптимальный интервал не зависит от горизонта retention

## Core Unit
- context: как распределять повторения во времени для максимума retention.
- signal: spaced (разнесённые эпизоды) стабильно лучше massed при **равном времени изучения**.
- action: разносить повторения; выбирать ISI под горизонт retention.
- outcome: 271 сравнений massed/spaced — только 12 без/против эффекта; выигрыш есть от <1 мин до >30 дней retention.
- lesson: расписание повторений — отдельный рычаг; ISI и retention interval работают **совместно**.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Мета-анализ: 839 оценок distributed practice в 317 эксп./184 статьях (verbal recall). |
| **K2** | **Spacing > massing** при равном study-time: ~+9% при RI<1 мин; выигрыш сохраняется на всём диапазоне RI; только 12/271 — нет/отрицательный (робастно). |
| **K3** | Ключевое: ISI и retention interval действуют **совместно** — оптимальный ISI **растёт** с ростом горизонта retention. |
| **K4** | «Too long» существует: слишком большой ISI при коротком RI снижает retention (inverse-U по ISI). |
| **K5** | Метод-гигиена: важно фиксировать число relearning-trials, иначе ISI путается с объёмом практики (контроль бюджета!). |

### Ограничения
- Только verbal recall (не skill/др.); литература неравномерно покрывает длинные RI.
- Человеческие интервалы не мапятся напрямую в tick'и CASA.

## Operationalization (CASA hypothesis only)
- first_adoption_task: расписание replay (ADR-0009): не massed повтор, а растущий интервал под горизонт удержания (`min_recurrence` + staleness).
- validation_check: massed vs spaced rehearsal на retention@N при **равном** числе повторений (K5).
- success_criterion: spaced ≥ massed на длинном горизонте; оптимум сдвигается с горизонтом.
- rollback_or_mitigation: избегать слишком большого ISI при коротком горизонте (K4).

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (Psych. Bulletin 132(3):354–380)*
