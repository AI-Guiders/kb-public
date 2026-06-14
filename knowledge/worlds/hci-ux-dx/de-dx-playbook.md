# DE/DX Playbook v1

## Purpose
Practical standards for developer effectiveness and sustainable delivery speed.

## Core Outcomes
- Faster safe delivery with lower cognitive load.
- Predictable onboarding and fewer environment-specific failures.
- Higher signal in tooling, tests, and feedback loops.

## Evidence-Based Working Format
- Fact: document current observable state (metrics, incidents, queue age, failure class).
- Hypothesis: state expected causal change from an intervention.
- Check: define the smallest test and observation window.
- Decision criterion: predefine keep/rollback/escalate threshold.
- Confidence mark: explicitly tag confidence and uncertainty before rollout.

## Operating Principles
- Make the easy path the correct path.
- Minimize friction before adding process.
- Prefer automation over recurring manual rituals.
- Preserve focus: lower context switching and queue growth.

## Environment and Tooling Baseline
- One-command local start for the main product path.
- Explicit dependency and version policy.
- Stable debug profile with reproducible breakpoints.
- Project templates and scripts for repeated workflows.

## Delivery and Flow Rules
- Small batches, clear scope, reversible changes.
- WIP limits for active tasks.
- Fast feedback from lint/build/test before merge.
- Visible bottlenecks and queue size monitoring.

## Code Review Quality
- Review for risk and behavior, not style-only nits.
- Require rationale for architecture-impacting changes.
- Prefer actionable comments with concrete alternatives.
- Track recurring review findings into checklist updates.

## Reliability and Dev Loop
- Keep a minimal smoke suite for critical user paths.
- Define rollback path for risky releases.
- Capture incident lessons as reusable rules.
- Protect p95/p99 user-facing performance during iteration.

## Metrics
- Lead time for changes.
- Change failure rate.
- Mean time to restore.
- PR cycle time and review latency.
- Onboarding time to first successful contribution.

## Literature synthesis (IDE / UI — классика, не метрики команды)

- **Опыт разработчика и интегрированная среда** (Osmani, Goldberg/Smalltalk-80, diSessa/Boxer): `kb-ide-dx-literature-evidence-v1.md` — принципы инструмента и IDE; **дополняет** этот playbook, но **не заменяет** разделы про поток поставки и DORA-ориентир выше.
- **UI/UX интерфейса** (Norman, Nielsen, Shneiderman, Krug): `kb-ui-ux-literature-evidence-v1.md` — эвристики и язык ревью; пересечение с доменом **HCI** (`status-hci-v1.md`).

## Revisit Triggers
- Rising cycle time or merge delay.
- Frequent environment-specific failures.
- Repeat incident classes with no checklist improvement.
- Team feedback that tooling is harder than product work.

