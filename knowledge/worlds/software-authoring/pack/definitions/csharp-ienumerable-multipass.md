---
type: Definition Card
title: IEnumerable — materialize when multipass
description: Повторный enumerate может быть дорогим или с побочными эффектами. Несколько проходов — осознанно материализовать (`ToList` и т.п.).
tags: [llm-native-card, definition, software-authoring, csharp, trap]
language: ru
world: software
subworld: authoring
---

# IEnumerable — materialize when multipass

- id: csharp-ienumerable-multipass
- kind: definition
- informal: Повторный enumerate может быть дорогим или с побочными эффектами. Несколько проходов — осознанно материализовать (`ToList` и т.п.).
- formal.rule: multipass_requires_materialization_or_replay_safe_source
- applies_when: counting then iterating; multiple consumers of same query; LINQ over I/O or deferred side effects
- does_not_apply: single forward pass; already a list/array; streaming where multipass is forbidden by design
- inference_hooks: applicability-then-infer
- llm_cue: Will this sequence be walked more than once?
- related: csharp-async-no-sync-over-async, kiss
- sources: worlds/software-authoring/code-writing-principles.md

