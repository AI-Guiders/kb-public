---
type: Misconception Card
title: 'Misconception: mc-human-default-pf'
tags: [llm-native-card, misconception, epistemic-scene, harness, cdp, pair]
world: epistemic
subworld: scene
---

# Misconception: mc-human-default-pf

- id: mc-human-default-pf
- kind: misconception
- false_claim: В паре человек по умолчанию PF (делает руками), модель — помощник/ускоритель под human-IDE.
- why_wrong: Темп анализа, темп мутаций и радиус изменений за wall-clock у модели обычно >> человеческих — рабочий темп пары задаёт модель, значит PF она. Плюс эпизодичность (нет жизни между инференсами) блокирует Human-PF. «Клики в IDE» ≠ PF.
- correction_definition: pair-roles-pm-pf
- applies_when: harness or behavior assumes human drives every execution step
- does_not_apply: explicit Human-PF session with matched analysis+mutation speed, radius dynamics, and between-inference presence
- inference_hooks: pair-roles-pm-pf, harness-model-first, blast-radius
- delta_radius_hint: If human is default PF while model outpaces on analysis, mutation, and radius — roles inverted.

