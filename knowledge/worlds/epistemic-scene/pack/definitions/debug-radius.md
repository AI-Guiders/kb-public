---
type: Definition Card
title: Debug Radius
description: Насколько далеко мы от причины бага; размер оставшегося H.
tags: [llm-native-card, definition, epistemic-scene, agent-operations]
language: ru
world: epistemic
subworld: scene
---

# Debug Radius

- id: debug-radius
- kind: definition
- modes: bug
- informal: Насколько далеко мы от причины бага; размер оставшегося H.
- formal.measure: size of remaining hypothesis set H
- formal.unit: hypothesis_count | entropy_proxy | typed_open_ids
- gate_step: delta_radius < 0
- gate_done: radius == 0
- llm_cue: Does this conclusion shrink debug-radius? If not — do not promote.
- related: hypothesis-space-h, delta-radius-gate, stage-result, verification-contract
- sources: work/projects/door-to-singularity/cascade-ide/note-cdp-design-doc.md

