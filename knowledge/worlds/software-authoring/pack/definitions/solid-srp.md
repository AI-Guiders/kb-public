**Tags:** #llm-native-card #definition #software-authoring

# SOLID — Single Responsibility

- id: solid-srp
- kind: definition
- informal: У модуля одна причина меняться.
- formal.rule: one_axis_of_change_per_type
- misconception: SRP ≠ «один метод на класс»
- applies_when: after responsibilities exist (OOA/OOD/GRASP); reviewing change axes of a type
- does_not_apply: before types/responsibilities named; method-count hygiene; UI file open/save affordances
- inference_hooks: applicability-then-infer, mc-srp-one-method, solid-after-grasp
- llm_cue: What reasons-to-change does this type have? More than one axis?
- related: grasp-high-cohesion, solid-after-grasp, applicability-inference-gate
- sources: worlds/software-authoring/code-writing-principles.md, worlds/software-authoring/kb-ooad-fundamentals.md#5

