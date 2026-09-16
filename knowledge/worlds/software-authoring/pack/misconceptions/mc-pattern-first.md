**Tags:** #llm-native-card #misconception #software-authoring #gof

# Misconception: mc-pattern-first

- id: mc-pattern-first
- kind: misconception
- false_claim: Сначала выбрать GoF/паттерн, потом подогнать типы под него.
- why_wrong: Паттерн без кандидатов в типы и без именованной боли = theater; размывает границы и раздувает blast.
- correction_definition: what-is-design-pattern
- applies_when: urge to say Factory/Singleton/Strategy in the first design sentence
- does_not_apply: after recurring pain + responsibilities already named
- inference_hooks: noun-verb-analysis, solid-after-grasp, applicability-then-infer
- llm_cue: Did I name the pain and types first — or the pattern name first?
- related: mc-solid-before-types, what-is-design-pattern, gof-singleton, gof-factory-method
- sources: worlds/software-authoring/kb-ooad-fundamentals.md, personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/design-patterns/what-is-pattern
- delta_radius_hint: Reject pattern-first; restore noun-verb → types → pattern if pain repeats.

