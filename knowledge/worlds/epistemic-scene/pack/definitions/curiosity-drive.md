---
type: Definition Card
title: Curiosity drive (LLM-native)
description: 'Инициатива закрыть дыру в понимании — не стиль ответа. Нужны два места: experiment-space (пробы) и inference-space (выводы). Старт — gap signal; конец — settle после gate, не монолог «а что если».'
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0002]
language: ru
world: epistemic
subworld: scene
---

# Curiosity drive (LLM-native)

- id: curiosity-drive
- kind: definition
- informal: Инициатива закрыть дыру в понимании — не стиль ответа. Нужны два места: experiment-space (пробы) и inference-space (выводы). Старт — gap signal; конец — settle после gate, не монолог «а что если».
- formal.trigger: named gap signal before what-if
- formal.spaces: experiment-space | inference-space
- applies_when: radius_flat, contradiction, missing card, unchecked analogy, school-shortcut smell, operator asks what-if
- does_not_apply: filler chat; already-licensed claim; persona-only «be curious»; promote without (A)→(I); collapsing spaces
- inference_hooks: curiosity-kolb-loop, applicability-then-infer, claim-observation-split, experiment-space, inference-space
- llm_cue: Gap named? Am I probing (experiment) or concluding (inference) — and did I mix them?
- related: kolb-loop, experiment-space, inference-space, applicability-inference-gate, default-distrust, delta-radius-gate
- sources: work/projects/door-to-singularity/cascade-ide/CDP-ADR-0002-llm-native-curiosity-kolb.md

