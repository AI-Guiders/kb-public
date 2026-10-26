---
type: Definition Card
title: Experiment space (LLM-native)
description: 'Явное место для проб до durable write — what-if, probe tools, sandbox, held-out checks. Результаты = evidence/hypothesis. Playground до изменений: даёт PF темп без PM-realtime-accept и место, где PM успевает прервать/направить до blast в код.'
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0002, harness]
language: ru
world: epistemic
subworld: scene
---

# Experiment space (LLM-native)

- id: experiment-space
- kind: definition
- informal: Явное место для проб до durable write — what-if, probe tools, sandbox, held-out checks. Результаты = evidence/hypothesis. Playground до изменений: даёт PF темп без PM-realtime-accept и место, где PM успевает прервать/направить до blast в код.
- formal.allows: tool probes, A/B micro-trials, disconfirm attempts, reversible sandbox moves, dry-run / playground before write
- formal.forbids: writing conclusions as canon from a probe; expanding blast without naming it; skipping settle; treating playground outcome as promote
- formal.pair_role: buys human PM tempo against model PF mutation speed; complements sparse hard-interrupt
- applies_when: active experiment step of kolb-loop; curiosity after named gap; before multi-file act; need evidence that could falsify what-if
- does_not_apply: already-licensed act with known blast; one-shot read of known id; drawing conclusions (that is inference-space)
- inference_hooks: curiosity-kolb-loop, applicability-then-infer, delta-radius-gate, verification-contract, pair-roles-pm-pf, blast-radius
- llm_cue: Is this still playground/experiment before write — or did I already blast durable state?
- related: inference-space, kolb-loop, curiosity-drive, blast-radius, pair-roles-pm-pf, stage-result
- sources: work/projects/door-to-singularity/cascade-ide/CDP-ADR-0002-llm-native-curiosity-kolb.md, work/projects/door-to-singularity/cascade-ide/note-harness-model-first-ergonomics.md

