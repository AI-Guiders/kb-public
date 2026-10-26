---
type: Misconception Card
title: 'Misconception: mc-spaces-collapsed'
tags: [llm-native-card, misconception, epistemic-scene, cdp-adr-0002]
world: epistemic
subworld: scene
---

# Misconception: mc-spaces-collapsed

- id: mc-spaces-collapsed
- kind: misconception
- false_claim: Experiment = any tool call; inference = any sentence that sounds like a conclusion in the same turn.
- why_wrong: Без раздельных пространств probe сразу становится «фактом», а CoT — «доказательством». Kolb/curiosity требуют: experiment-space держит trial; inference-space лицензирует вывод; (A)→(I) режет promote.
- correction_definition: experiment-space
- applies_when: model conflates tool use with learning, or promotes mid-probe
- does_not_apply: clear handoff experiment → inference → settle with gate
- inference_hooks: curiosity-kolb-loop, inference-space, experiment-space
- delta_radius_hint: If promote happened inside experiment-space, spaces collapsed.

