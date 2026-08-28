**Tags:** #llm-native-card #definition #software-authoring #refactoring-guru #smell

# Smell — Long Method

- id: smell-long-method
- kind: definition
- informal: Метод разросся; читать и менять тяжело. Запах → рефакторинг, не «ещё одна строка».
- formal.signal: method hard to name in one verb; many nested branches/loops; grows by accretion
- applies_when: reviewing readability; before adding more behavior to an already long method
- does_not_apply: generated code; intentionally linear scripts with clear steps; micro-methods that destroy locality without gain
- inference_hooks: mutation-blast-bound, applicability-then-infer
- llm_cue: Can I Extract Method with a name that states purpose — or am I chopping noise?
- related: smell-feature-envy, kiss, dry
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/smells/long-method
- formal.roslyn_hint: prefer roslyn Extract Method / introduce local over hand-edit sprawl

