# HCI Reading Map v1

## Purpose

Keep HCI decisions evidence-backed while staying operational for daily product work.

## Track A: Foundational Principles

- ISO 9241-110 dialog principles.
- ISO 9241-210 human-centered design process.
- Nielsen Norman Group core usability heuristics.
- **Классика UI/UX в одном файле KB:** `kb-ui-ux-literature-evidence-v1.md` (Norman, Nielsen 10 heuristics, Shneiderman eight rules, Krug) — литературный синтез для ревью и языка критериев.

Outcome: stable baseline for interaction quality and usability language.

## Track B: Applied UI Heuristics

- Information architecture and visual hierarchy guidance.
- Form and validation design best practices.
- Error prevention and progressive disclosure patterns.

Outcome: practical screen-level design decisions with lower user error rate.

## Track C: Accessibility and Inclusive Design

- WCAG 2.2 normative guidance.
- WAI-ARIA authoring practices.
- Platform accessibility basics for web and desktop workflows.

Outcome: primary user flows remain operable across different abilities and contexts.

## Track D: Cognitive Load and Decision Support

- Cognitive load management for dense operational interfaces.
- Recognition-over-recall strategies for complex domain tasks.
- Interruption-tolerant task design.

Outcome: reduced user fatigue and fewer high-cost misoperations.

## Track E: Conversational and Agent Interaction

- Clarifying-question discipline.
- Uncertainty communication and confidence labeling.
- Recovery-oriented response style for failures and ambiguity.

Outcome: assistant behavior that is helpful under pressure, not verbose noise.

## Ingestion Contract

- Add only sources that change design or review decisions in practice.
- For each source, record:
  - core fact,
  - transfer rule,
  - first applied task,
  - confidence after repeated use.
- Prefer short evidence loops over large unread backlogs.

## Validation Rule

HCI guidance is accepted as operational only if it improves one of:

- task completion reliability,
- time-to-correct-action,
- error recovery success,
- accessibility pass rate.

