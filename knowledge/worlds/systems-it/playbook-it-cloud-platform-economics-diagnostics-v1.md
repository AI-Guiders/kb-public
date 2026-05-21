# IT Cloud, Platform, Economics, and Diagnostics Playbook v1

## Purpose

Close the pending IT roadmap segment focused on:
- cloud/platform engineering,
- architecture economics,
- large-scale diagnostics and reliability operations.

## Scope

- SLO/error-budget operating model.
- Platform reliability patterns (health, disruption budgets, rollout safety).
- Observability cost-quality tradeoffs (especially cardinality discipline).
- Cloud financial governance (FinOps + unit economics).
- Controlled resilience validation (chaos discipline with bounded blast radius).

## Core Contracts

- **Reliability as budgeted policy**: every critical service has SLO + error budget + burn-rate alerting profile.
- **Economics as architecture input**: every major design option includes unit-cost and operational-cost projection.
- **Diagnostics at scale**: instrumentation is designed with cardinality limits and triage paths, not only with "more telemetry".
- **Failure testing discipline**: resilience claims require staged experiments with explicit steady-state hypothesis.

## Architecture Economics Lens

- Evaluate decisions on three axes:
  - business value throughput,
  - reliability risk reduction,
  - cost of ownership (run + change + incident cost).
- Use `good-enough reliability` target, not maximum possible reliability by default.
- Track high-interest technical debt in high-change/high-incident zones first.

## Cloud/Platform Operating Pattern

- Define platform SLOs and service SLOs separately.
- Use error-budget policy to govern release velocity under stress.
- Standardize readiness/liveness semantics and disruption controls.
- Keep platform contracts explicit (resource limits, restart behavior, rollback paths).

## Large-Scale Diagnostics Pattern

- Use "signal budget":
  - logs for narratives and edge incidents,
  - metrics for trend and burn-rate detection,
  - traces for path causality and latency decomposition.
- Control metric cardinality at source and collection boundaries.
- Keep incident triage runbooks map-based (`symptom -> first probes -> escalation`).

## DoD v1

This playbook slice is "done v1" when:
- playbook exists with reliability/economics/diagnostics contracts;
- at least one curated knowledge set captures reusable rules;
- reading digest includes source-backed entries;
- canonical index points to all slice artifacts.
