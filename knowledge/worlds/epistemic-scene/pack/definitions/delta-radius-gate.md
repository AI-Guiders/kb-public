---
type: Definition Card
title: Δradius effectiveness gate
description: Шаг полезен только если радиус уменьшился.
tags: [llm-native-card, definition, epistemic-scene, agent-operations]
world: epistemic
subworld: scene
---

# Δradius effectiveness gate

- id: delta-radius-gate
- kind: definition
- informal: Шаг полезен только если радиус уменьшился.
- formal.gate_step: delta_radius < 0
- formal.wasted: delta_radius ≈ 0 at full turn cost
- formal.done_bug: radius == 0
- applies_when: any Bug/Feature step where progress is claimed; before promote of diagnosis or fix
- does_not_apply: pure status chatter with no claim that radius moved; exploratory notes marked unknown
- inference_hooks: applicability-then-infer, debug-radius, hypothesis-space-h
- llm_cue: Before promote: Δradius < 0?
- related: debug-radius, hypothesis-space-h, applicability-inference-gate
- sources: work/projects/door-to-singularity/cascade-ide/note-cdp-design-doc.md

