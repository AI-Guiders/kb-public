# HCI Core Playbook v1

## Purpose

Design human-computer interaction that stays clear under real cognitive load, not only in ideal demo flows.

## Core Interaction Contract

- Reduce cognitive friction before adding new features.
- Keep system state visible: users should understand where they are and what will happen next.
- Prefer reversible actions for high-impact operations.
- Move from error message to recovery action in one step.

## Practical Design Order

1. Task intent: what the user is trying to achieve.
2. Mental model fit: how the screen language matches user expectations.
3. Interaction cost: clicks, context switches, memory burden.
4. Failure recovery: what happens when the user is wrong, late, or interrupted.

## Usability Baseline

- Primary path is discoverable without training.
- Secondary actions are available but do not dominate attention.
- Terminology matches domain language used by the target audience.
- Feedback latency stays predictable for repeated actions.

## Accessibility Baseline

- Keyboard path exists for primary workflows.
- Contrast and focus states are explicit.
- Critical meaning is not encoded by color only.
- Error states are readable and actionable by assistive tools.

## Dialogue and Agent UX Baseline

- Ask only missing information required for safe progress.
- Mark uncertainty explicitly instead of pretending confidence.
- Give a concrete next step, not abstract reassurance.
- Keep response granularity proportional to user intent.

## Anti-Patterns

- Dense screens that optimize for data volume over decisions.
- Hidden state transitions that surprise users.
- Validation that reports failure but gives no recovery route.
- Excessive modal interruptions for low-risk actions.
