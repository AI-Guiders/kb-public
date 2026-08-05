**Tags:** #llm-native-card #misconception #epistemic-scene #cdp-adr-0002

# Misconception: mc-curiosity-equals-persona

- id: mc-curiosity-equals-persona
- kind: misconception
- false_claim: Curiosity = system prompt «будь любопытным» / длинный CoT с вопросами.
- why_wrong: Это имитация токенов. Настоящий цикл — gap signal → what-if as hypothesis → evidence → (A)→(I) before promote. Без учёта дыры и gate — снова shortcut.
- correction_definition: curiosity-drive
- applies_when: model or human equates exploratory tone with Kolb/curiosity organ
- does_not_apply: genuine gap-driven loop ending in settle
- inference_hooks: curiosity-kolb-loop, kolb-loop
- delta_radius_hint: If no gap named, curiosity did not start.

