---
type: Definition Card
title: Applicability → inference gate
description: Перед promote major claim — сначала лицензия области (A), потом согласованность/следствие (I); иначе reject или honest unknown.
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0001]
language: ru
world: epistemic
subworld: scene
---

# Applicability → inference gate

- id: applicability-inference-gate
- kind: definition
- informal: Перед promote major claim — сначала лицензия области (A), потом согласованность/следствие (I); иначе reject или honest unknown.
- formal.order: applicability then inference then promote|reject|unknown
- applies_when: major claim, mutation intent, rule/principle citation, cross-domain analogy
- does_not_apply: pure formatting nits; already-gated tool results with typed evidence; operator-explicit override
- inference_hooks: applicability-then-infer, claim-observation-split, default-distrust, delta-radius-gate
- gate_step: (A) stated or unknown; (I) no unchecked contradiction with active claims
- llm_cue: Did I name applies_when / does_not_apply before inferring? If unknown — do not promote.
- related: claim-observation-split, default-distrust, verification-contract, delta-radius-gate, blast-radius
- sources: work/projects/door-to-singularity/cascade-ide/CDP-ADR-0001-llm-native-applicability-inference.md

