---
type: Misconception Card
title: 'Misconception: mc-harness-human-first'
tags: [llm-native-card, misconception, epistemic-scene, harness, cdp]
language: ru
world: epistemic
subworld: scene
---

# Misconception: mc-harness-human-first

- id: mc-harness-human-first
- kind: misconception
- false_claim: Harness UX = human IDE UX; модель должна «научиться» кликать/грепать/спрашивать как джун в VS Code.
- why_wrong: В agent-IDE доля human-turns обычно ~≤5%. Если путь модели — обход препятствий (grep вместо get_definition, confirmation theater вместо policy), харнесс заточен не под пользователя. Human surface — тонкий проектор той же плоскости (CIDE later), не хозяин формы.
- correction_definition: harness-model-first
- applies_when: design or agent behavior prioritizes pixel rituals over LLM-native affordances
- does_not_apply: steward oversight, integrity gates, explicit human ask policy
- inference_hooks: harness-model-first, curiosity-kolb-loop
- delta_radius_hint: If model work needed human-shaped tools to succeed, ergonomics inverted.

