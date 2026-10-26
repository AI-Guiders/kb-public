---
type: Definition Card
title: Smell — Feature Envy
description: Метод чаще использует данные другого объекта, чем свои. «Что меняется вместе — держать вместе».
tags: [llm-native-card, definition, software-authoring, refactoring-guru, smell]
language: ru
world: software
subworld: authoring
---

# Smell — Feature Envy

- id: smell-feature-envy
- kind: definition
- informal: Метод чаще использует данные другого объекта, чем свои. «Что меняется вместе — держать вместе».
- formal.signal: foreign fields/properties dominate body; candidate Move Method
- applies_when: method mostly operates on another type's state
- does_not_apply: intentional separation (Strategy/Visitor); pure functions over DTOs at boundaries
- inference_hooks: grasp-information-expert, mutation-blast-bound
- llm_cue: Whose data is this behavior about — move there or Extract+Move part?
- related: smell-long-method, grasp-information-expert, gof-strategy
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/smells/feature-envy
- formal.roslyn_hint: Move Method / Extract Method then move

