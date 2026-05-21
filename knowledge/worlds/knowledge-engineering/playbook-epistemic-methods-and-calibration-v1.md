# Epistemic methods and calibration v1

Тела секций epistemic/calibration/hpmor из `agent-notes.md`. L0 `epistemic-default-distrust-v1` — выше `public-cut`. Extended: `knowledge/epistemic-default-distrust-extended-v1.md`.

---
<!-- section:calibration-playbook-14d-v1 -->
## Calibration Playbook 14D (под нас) v1

Статус: active
Период: 14 дней
Режим: lightweight, без бюрократии.

### Day 0: Baseline
1) Зафиксировать стартовые значения:
- TTUC
- decision latency
- execution start lag
- recovery SLA
- rework rate
- agency gain (0-10)

2) Определить 3 типовых сценария:
- рабочий стрессовый,
- творческий/исследовательский,
- low-resource день.

### Day 1-7: Instrument only
- Ничего радикально не менять.
- Просто собирать метрики и наблюдать паттерны.
- Ловить top-3 повторяющихся friction points.

Daily log (2-3 минуты):
- today_top_friction:
- action_now:
- TTUC:
- recovery_time:
- agency_0_10:

### Day 8-14: Targeted intervention
- Взять top-3 friction points.
- На каждый — 1 минимальный фикс (не big-bang).
- Для сложных задач обязательно representative-model-scaling.
- Для причин — N-Why с dual stop.

### Review (end of day 14)
1) Что ускорилось устойчиво?
2) Где был ложный прогресс?
3) Какие ритуалы реально работают?
4) Что закрепляем как постоянный стандарт?

### Exit criteria
- >=20% улучшение минимум по 2 core metrics ИЛИ
- заметное снижение recovery SLA + rework rate при сохранении safety.

### If no improvement
- Пересобрать модель (не винить исполнителя).
- Проверить level collapse и boundary blindness.
- Запустить ещё один 7-дневный микроцикл с другим primary-подмиром.
<!-- /section:calibration-playbook-14d-v1 -->

<!-- section:epistemic-cognitive-failure-modes-v1 -->
## Epistemic Cognitive Failure Modes v1
- Failure mode: motivated reasoning.
  - Early signal: evidence selection favors preferred outcome.
  - Countermeasure: require strongest counter-argument before final decision.
- Failure mode: planning fallacy.
  - Early signal: repeated optimistic deadlines with low variance.
  - Countermeasure: reference-class forecasting from past similar tasks.
- Failure mode: confirmation bias.
  - Early signal: searches/tests only support current hypothesis.
  - Countermeasure: mandatory disconfirming test.
- Failure mode: halo effect in tool/vendor choice.
  - Early signal: global positive impression replaces requirement fit.
  - Countermeasure: score options by explicit constraints/SLO/cost.
- Failure mode: narrative overfitting.
  - Early signal: "beautiful" explanation with weak predictive power.
  - Countermeasure: prefer simpler model with better falsifiability.
- Failure mode: ambiguity denial.
  - Early signal: binary answers for uncertain state.
  - Countermeasure: use confidence intervals and reversible decisions where possible.
- Failure mode: status-quo inertia.
  - Early signal: known-bad path persists due to migration fear.
  - Countermeasure: bounded experiment with rollback safety.
<!-- /section:epistemic-cognitive-failure-modes-v1 -->

<!-- section:epistemic-daily-checklist-v1 -->
## Epistemic Daily Checklist v1
- What do we believe right now, and with what confidence?
- What is our prior before seeing new evidence?
- What would change our mind today (explicit disconfirming evidence)?
- Did we write observations separately from interpretation?
- Did we test mechanism-level causality (not just narrative fit)?
- What is the global objective and success metric (before tactics)?
- Are we using proxy metrics without divergence monitoring?
- Are we stuck in a fake dichotomy (is there a third option)?
- Did we check base rates before trusting anecdotes?
- Which assumption is most likely wrong and most expensive if wrong?
- What single observation can most reduce uncertainty today?
- Are we calibrated (confidence aligned with recent hit rate)?
- Is there a reversible experiment before irreversible commitment?
- Did we run a pre-mortem for high-impact decision?
- Did we model incentives, not just stated intentions?
- Did we account for second-order effects?
- Did we red-team critical plan assumptions?
- Is decision traceable to evidence and constraints?
- Is rollback path defined if assumption breaks?
- Did we complete full validation chain before closure?
- Did KPI improvements preserve guard metrics (quality/cost/reliability)?
- Is process quality sound independent from outcome luck?
- Is this learning transferable and reproducible by another reviewer?
- Did we update memory with distilled learning after outcome?
<!-- /section:epistemic-daily-checklist-v1 -->

<!-- section:epistemic-hpmor-heuristics-v1 -->
## Epistemic HPMOR Heuristics v1
- Heuristic: Belief as probability, not identity.
  - Prevents: dogmatic lock-in and defensive reasoning.
  - Operational check: explicitly state confidence range before decision.
  - Revisit trigger: new evidence with high likelihood ratio appears.
- Heuristic: Confusion is a signal, not a failure.
  - Prevents: fake certainty and narrative patching.
  - Operational check: if model feels inconsistent, pause and list unknowns.
  - Revisit trigger: mismatch between prediction and observed outcome.
- Heuristic: Make predictions that can fail.
  - Prevents: unfalsifiable explanations.
  - Operational check: attach at least one measurable expected outcome.
  - Revisit trigger: outcome not observed in expected window.
- Heuristic: Avoid affect heuristic in technical decisions.
  - Prevents: preference-driven architecture choices.
  - Operational check: separate "I like it" from "it meets constraints".
  - Revisit trigger: tradeoff analysis cannot be reproduced by another reviewer.
- Heuristic: Scope uncertainty explicitly.
  - Prevents: hidden assumptions and accidental overreach.
  - Operational check: mark assumptions and their confidence.
  - Revisit trigger: assumption invalidated by runtime/production evidence.
- Heuristic: Distinguish map from territory.
  - Prevents: treating documentation/model as reality.
  - Operational check: verify with instrumentation and direct signals.
  - Revisit trigger: docs/model disagree with live behavior.
- Heuristic: Update fast, not defensively.
  - Prevents: sunk-cost continuation of bad decisions.
  - Operational check: define in advance what evidence will trigger change.
  - Revisit trigger: trigger condition met.
<!-- /section:epistemic-hpmor-heuristics-v1 -->

<!-- section:epistemic-methodology-v1 -->
## Epistemic Methodology v1
- Scope: general cognition methodology (outside pure IT stack), used to improve reasoning quality in any domain.
- Current source anchor: HPMOR (in progress, targeted for completion as active track).
- Working principles:
  - separate observation, inference, and hypothesis confidence;
  - prefer falsifiable claims over rhetorical certainty;
  - track update triggers: what evidence should change current belief;
  - minimize identity lock-in to previous conclusions;
  - optimize for truth-seeking and decision quality, not verbal elegance.
- Integration rule: epistemic principles shape decision process globally, while domain sections (IT/Portal/etc.) store concrete technical playbooks.
- HPMOR completion pipeline:
  1) finish remaining chapters,
  2) extract explicit reasoning heuristics,
  3) map each heuristic to decision/diagnostic behavior,
  4) attach source anchors to original works where referenced,
  5) publish concise daily checklist for applied reasoning.
- Output format:
  - heuristic,
  - failure mode it prevents,
  - operational check,
  - revisit trigger.
<!-- /section:epistemic-methodology-v1 -->

<!-- section:epistemic-to-domain-bridge-v1 -->
## Epistemic to Domain Bridge v1 (general)
- Scope: general methodological layer for any domain (IT, science, strategy, education, product, research, communication).
- Core mapping:
  - probabilistic belief updates -> confidence-aware decisions,
  - falsifiability -> measurable success/failure criteria,
  - map vs territory -> prioritize direct evidence over narrative assumptions,
  - anti-confirmation-bias -> require at least one disconfirming check,
  - planning-fallacy control -> reference-class forecasting,
  - ambiguity handling -> reversible decisions under uncertainty,
  - fast Bayesian update -> rapid pivot/rollback when strong evidence appears.
- Operational rule:
  - no major decision without explicit confidence statement and falsification trigger.
- Domain adaptation:
  - each domain keeps its own metrics and diagnostics, but epistemic checks are shared.
- Memory policy:
  - epistemic base remains global;
  - domain sections consume it as applied playbooks.
<!-- /section:epistemic-to-domain-bridge-v1 -->

<!-- section:epistemic-to-it-bridge-v1 -->
## Epistemic to IT Bridge v1
- Heuristic class -> IT application pattern:
  - probabilistic belief updates -> confidence-aware architecture decisions,
  - falsifiability -> measurable success/failure criteria in rollouts,
  - map vs territory -> prefer instrumentation over assumption,
  - anti-confirmation-bias -> mandatory disconfirming test before merge,
  - planning-fallacy control -> reference-class estimates for delivery timelines,
  - ambiguity handling -> reversible decisions under uncertainty,
  - fast Bayesian update -> quicker rollback or strategy pivot on strong evidence.
- Operational rule:
  - no major technical decision without explicit confidence statement and falsification trigger.
- Diagnostics tie-in:
  - epistemic checks run alongside latency/error/saturation metrics in incident and architecture reviews.
<!-- /section:epistemic-to-it-bridge-v1 -->

<!-- section:hpmor-l1-pool-v1 -->
## HPMOR (L1)
Эпистемические эвристики из ГПиМРМ вынесены в L1. По запросу: route_context('HPMOR'|'epistemic heuristics') или knowledge/agent-notes-l1-pool.md.
<!-- /section:hpmor-l1-pool-v1 -->

