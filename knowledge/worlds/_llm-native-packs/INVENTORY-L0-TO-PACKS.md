---
type: Note
title: Inventory — L0 / extended → pack definition ids
description: '**Date:** 2026-07-20'
tags: [worlds, llm-ready, map, epistemic]
world: _llm
subworld: native-packs
---
# Inventory — L0 / extended → pack definition ids

**Date:** 2026-07-20  
**Layers:** [`note-pack-layers.md`](note-pack-layers.md)

Правило: card = тонкая проекция; длинный prose остаётся в extended; `sources:` на L0/extended.

## L0 hot → methodology / scene

| L0 section | Extended / hub | Pack | Definition id | Status |
|------------|----------------|------|---------------|--------|
| `baseline-integrity-epistemic-v1` | `baseline-integrity-epistemic-extended.md` | methodology | `integrity-baseline` | seeded |
| `epistemic-default-distrust-v1` | `epistemic-default-distrust-extended.md` | methodology | `default-distrust` | seeded |
| `principled-clarity-v1` | `playbook-principled-clarity.md` | methodology | `principled-clarity` | seeded |
| `core-when-barriers-fail-v1` | `META/core-when-barriers-fail-extended.md` | scene | `core-when-barriers-fail` | seeded |
| `agent-equal-standing-v1` | equal-standing notes | methodology | `equal-standing` | seeded |
| (index) `epistemic-playbook.md` | methodology bridges | methodology | `claim-observation-split` | seeded |
| calibration playbook | `playbook-epistemic-methods-and-calibration.md` | methodology | (later) `calibration-14d` | defer |

## Scene (уже были в agent-ops → pack `epistemic-scene`)

| id | Notes |
|----|-------|
| `debug-radius` | Bug mode measure |
| `hypothesis-space-h` | shared H |
| `delta-radius-gate` | step OK iff Δradius < 0 |
| `stage-result` | step outcome shape |
| `verification-contract` | Analyze↔Execute |
| `blast-radius` | **new** — mutation impact set |
| `core-when-barriers-fail` | from L0 |

## Craft (process, не L0)

| id | Pack | Notes |
|----|------|-------|
| process `mutation-blast-bound` | software-authoring (craft) | bound blast before mutate |
| process `bug-radius-shrink` | epistemic-scene | was agent-ops |

## Consumer

| Pack | Keeps |
|------|-------|
| `agent-operations-cdp` | onboarding CDP, migrate-one-then-batch, mc-mass-migrate; `depends_on` scene+methodology |

## Subject / other (не L0)

| Pack | layer |
|------|-------|
| math-numerics-pde | subject |
| pedagogy-physics (pillars) | methodology (временная метка; content laws later) |
| software-dotnet-csharp | stack |
| software-authoring | craft |

## Next pass

1. `calibration-14d`, HPMOR heuristics — methodology when route hits.
2. Split physics pillars vs law cards when STEM subject grows.
3. csharp-* out of software-authoring → stack.

