# IT Knowledge Set v1 (Cloud, Platform, Economics, Diagnostics Rules)

Set: 24 cards.  
Focus: cloud/platform engineering + architecture economics + large-scale diagnostics.

---

## Card 01
- card_id: KC-2026-02-26-179
- world: it.phase-c.reliability
- epistemic_basis: `fact`
- confidence: `high`
- signal: reliability discussions stay abstract without explicit SLOs
- action: define SLI/SLO per critical user journey before alert tuning
- transfer_boundary: no error-budget policy without measurable SLI

## Card 02
- card_id: KC-2026-02-26-180
- world: it.phase-c.reliability
- epistemic_basis: `fact`
- confidence: `high`
- signal: alert fatigue from static threshold alerts
- action: prefer multi-window burn-rate alerting for SLO protection
- transfer_boundary: burn-rate profiles must be calibrated per service criticality

## Card 03
- card_id: KC-2026-02-26-181
- world: it.phase-c.reliability
- epistemic_basis: `inference`
- confidence: `medium`
- signal: teams spend error budget too early in release cycle
- action: gate risky releases by remaining budget trend
- transfer_boundary: requires agreed release governance model

## Card 04
- card_id: KC-2026-02-26-182
- world: it.phase-c.platform
- epistemic_basis: `fact`
- confidence: `high`
- signal: service restarts occur despite "healthy ping"
- action: separate liveness from readiness with dependency-aware probes
- transfer_boundary: binary health endpoint alone is insufficient

## Card 05
- card_id: KC-2026-02-26-183
- world: it.phase-c.platform
- epistemic_basis: `fact`
- confidence: `high`
- signal: cluster maintenance causes avoidable user impact
- action: enforce disruption budgets and rollout windows for critical workloads
- transfer_boundary: disruption policy must match business criticality tiers

## Card 06
- card_id: KC-2026-02-26-184
- world: it.phase-c.platform
- epistemic_basis: `inference`
- confidence: `medium`
- signal: environment instability traced to implicit resource assumptions
- action: pin CPU/memory limits and monitor throttling/oom signals
- transfer_boundary: limits require workload-specific load validation

## Card 07
- card_id: KC-2026-02-26-185
- world: it.phase-c.economics
- epistemic_basis: `fact`
- confidence: `high`
- signal: cloud spend lacks business-aligned interpretation
- action: introduce unit economics per business capability
- transfer_boundary: unit metric must be shared by product and platform teams

## Card 08
- card_id: KC-2026-02-26-186
- world: it.phase-c.economics
- epistemic_basis: `fact`
- confidence: `high`
- signal: cost optimization efforts are tactical and short-lived
- action: run FinOps inform-optimize-operate loop continuously
- transfer_boundary: optimization without ownership model is unstable

## Card 09
- card_id: KC-2026-02-26-187
- world: it.phase-c.economics
- epistemic_basis: `inference`
- confidence: `medium`
- signal: architecture choice made without run-cost projection
- action: require cost-risk-value comparison in ADRs
- transfer_boundary: projection confidence must be declared explicitly

## Card 10
- card_id: KC-2026-02-26-188
- world: it.phase-c.diagnostics
- epistemic_basis: `fact`
- confidence: `high`
- signal: telemetry cost grows faster than incident-resolution value
- action: enforce cardinality limits and attribute budgets
- transfer_boundary: no high-cardinality attributes in default metric dimensions

## Card 11
- card_id: KC-2026-02-26-189
- world: it.phase-c.diagnostics
- epistemic_basis: `fact`
- confidence: `high`
- signal: traces collected but not actionable in incidents
- action: align trace instrumentation to critical path and error classes
- transfer_boundary: tracing without incident use-cases is observability debt

## Card 12
- card_id: KC-2026-02-26-190
- world: it.phase-c.diagnostics
- epistemic_basis: `inference`
- confidence: `medium`
- signal: metrics and logs disagree during outages
- action: validate timestamp, sampling, and aggregation alignment
- transfer_boundary: no cross-signal conclusion before alignment check

## Card 13
- card_id: KC-2026-02-26-191
- world: it.phase-c.sre-operations
- epistemic_basis: `fact`
- confidence: `high`
- signal: operational load grows linearly with system growth
- action: classify and automate toil aggressively
- transfer_boundary: do not normalize repetitive manual ops as permanent work

## Card 14
- card_id: KC-2026-02-26-192
- world: it.phase-c.sre-operations
- epistemic_basis: `fact`
- confidence: `high`
- signal: incident recurrence despite heroic response
- action: enforce postmortem-to-backlog conversion with ownership
- transfer_boundary: postmortem without tracked remediation is incomplete

## Card 15
- card_id: KC-2026-02-26-193
- world: it.phase-c.sre-operations
- epistemic_basis: `inference`
- confidence: `medium`
- signal: high-change systems have rising recovery time
- action: prioritize rollback and blast-radius controls over feature throughput
- transfer_boundary: depends on mature release automation

## Card 16
- card_id: KC-2026-02-26-194
- world: it.phase-c.resilience-testing
- epistemic_basis: `fact`
- confidence: `high`
- signal: resilience claims are not tested under realistic failures
- action: run chaos experiments from steady-state hypothesis with bounded blast radius
- transfer_boundary: no production experiment without rollback trigger

## Card 17
- card_id: KC-2026-02-26-195
- world: it.phase-c.resilience-testing
- epistemic_basis: `inference`
- confidence: `medium`
- signal: staging-only resilience tests miss production-specific failure modes
- action: include controlled production experiments for top-risk dependencies
- transfer_boundary: requires explicit safety governance and communication protocol

## Card 18
- card_id: KC-2026-02-26-196
- world: it.phase-c.architecture-economics
- epistemic_basis: `fact`
- confidence: `high`
- signal: teams target maximal reliability by default
- action: define "good-enough reliability" by business impact and budget
- transfer_boundary: cannot lower reliability below agreed risk appetite

## Card 19
- card_id: KC-2026-02-26-197
- world: it.phase-c.architecture-economics
- epistemic_basis: `inference`
- confidence: `medium`
- signal: architecture complexity grows faster than marginal value
- action: challenge additions with YAGNI + debt-interest perspective
- transfer_boundary: simplification must preserve required compliance/safety controls

## Card 20
- card_id: KC-2026-02-26-198
- world: it.phase-c.architecture-economics
- epistemic_basis: `fact`
- confidence: `high`
- signal: technical debt tracking is generic and not decision-useful
- action: annotate debt by interest signal (change rate, incident amplification, delay cost)
- transfer_boundary: debt register without prioritization model is noise

## Card 21
- card_id: KC-2026-02-26-199
- world: it.phase-c.governance
- epistemic_basis: `fact`
- confidence: `high`
- signal: cross-team conflicts on reliability vs speed are ad-hoc
- action: codify error-budget release policy and exception workflow
- transfer_boundary: exception process must be time-bounded and auditable

## Card 22
- card_id: KC-2026-02-26-200
- world: it.phase-c.governance
- epistemic_basis: `fact`
- confidence: `high`
- signal: architecture economics is absent from review rituals
- action: add value-risk-cost triad to ADR template
- transfer_boundary: triad must include uncertainty/confidence marker

## Card 23
- card_id: KC-2026-02-26-201
- world: it.phase-c.governance
- epistemic_basis: `inference`
- confidence: `medium`
- signal: teams interpret platform SLO and app SLO interchangeably
- action: separate platform and application objective layers explicitly
- transfer_boundary: shared language contract required across teams

## Card 24
- card_id: KC-2026-02-26-202
- world: it.phase-c.domain-closure
- epistemic_basis: `fact`
- confidence: `high`
- signal: phase marked complete without artifact-level closure
- action: require playbook + cards + digest entries + status artifact + index sync
- transfer_boundary: no "phase done" declaration before all closure artifacts exist

---

## Source Footing

- DORA 2024 delivery/reliability framework and metric evolution.
- FinOps framework and unit-economics guidance.
- Google SRE workbook guidance (toil, SLO alerting).
- Kubernetes reliability components and disruption control references.
- AWS Well-Architected cost optimization principles.
- OpenTelemetry metrics SDK and cardinality-governance guidance.
