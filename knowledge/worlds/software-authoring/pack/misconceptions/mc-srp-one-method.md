---
type: Misconception Card
title: 'Misconception: mc-srp-one-method'
tags: [llm-native-card, misconception, software-authoring]
world: software
subworld: authoring
---

# Misconception: mc-srp-one-method

- id: mc-srp-one-method
- kind: misconception
- false_claim: SRP значит «один метод на класс».
- why_wrong: Классическая карикатура SRP. Настоящий SRP — одна ось / причина изменения, не счётчик методов.
- correction_definition: solid-srp
- applies_when: someone equates SRP with method count or «small class»
- does_not_apply: cohesion / single axis-of-change review (use solid-srp)
- inference_hooks: applicability-then-infer, solid-after-grasp
- delta_radius_hint: Count reasons-to-change, not method count.

