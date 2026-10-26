---
type: Definition Card
title: Kolb loop (LLM-native)
description: 'Опыт → рефлексия → абстракция → эксперимент. В CDP не только шаги, а два пространства: experiment-space (можно пробовать) и inference-space (можно выводить). Между ними — handoff; promote только через (A)→(I).'
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0002, methodology]
world: epistemic
subworld: scene
---

# Kolb loop (LLM-native)

- id: kolb-loop
- kind: definition
- informal: Опыт → рефлексия → абстракция → эксперимент. В CDP не только шаги, а два пространства: experiment-space (можно пробовать) и inference-space (можно выводить). Между ними — handoff; promote только через (A)→(I).
- formal.phases: gap | reflect | abstract_what_if | experiment | infer | gate_AI | settle
- formal.spaces: experiment-space (probes stay hypothesis) | inference-space (licensed conclusions)
- applies_when: learning or investigation where understanding must change (not only execute a known recipe)
- does_not_apply: pure mechanical edit with known blast; one-shot lookup with known id; CASA field ticks; collapsed spaces (mc-spaces-collapsed)
- inference_hooks: curiosity-kolb-loop, applicability-then-infer, claim-observation-split, verification-contract, experiment-space, inference-space
- llm_cue: Which space am I in — experiment or inference — and did I skip the handoff?
- related: curiosity-drive, experiment-space, inference-space, applicability-inference-gate, stage-result
- sources: work/projects/door-to-singularity/cascade-ide/CDP-ADR-0002-llm-native-curiosity-kolb.md, CASA kolb_cycle prior art

