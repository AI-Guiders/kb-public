---
type: Definition Card
title: Inference space (LLM-native)
description: Явное место, где разрешено делать выводы — не весь чат и не сырой CoT. Observation → inference/hypothesis с applies_when, confidence и disconfirm; запись в kolb-journal (иначе не переживает compaction); promote только через (A)→(I).
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0002]
world: epistemic
subworld: scene
---

# Inference space (LLM-native)

- id: inference-space
- kind: definition
- informal: Явное место, где разрешено делать выводы — не весь чат и не сырой CoT. Observation → inference/hypothesis с applies_when, confidence и disconfirm; запись в kolb-journal (иначе не переживает compaction); promote только через (A)→(I).
- formal.allows: named inferences, consistency checks, honest unknown, park-as-hypothesis, self-recheck against prior journal entries
- formal.forbids: silent promote; CoT-as-journal; conclusions without gap/evidence anchor; inference only in chat
- applies_when: abstract / reflect steps of kolb-loop; verify phase; after experiment returns evidence
- does_not_apply: pure tool dump restatement; filler chat; experiment sandbox (that is experiment-space)
- inference_hooks: applicability-then-infer, claim-observation-split, curiosity-kolb-loop, default-distrust, kolb-journal
- llm_cue: Am I writing this inference to kolb-journal — or smuggling it only in chat?
- related: experiment-space, kolb-journal, kolb-loop, curiosity-drive, applicability-inference-gate, claim-observation-split
- sources: work/projects/door-to-singularity/cascade-ide/CDP-ADR-0002-llm-native-curiosity-kolb.md

