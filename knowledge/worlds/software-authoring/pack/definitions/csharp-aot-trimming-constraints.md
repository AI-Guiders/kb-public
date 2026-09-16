**Tags:** #llm-native-card #definition #software-authoring #csharp #trap

# Native AOT / trimming constraints

- id: csharp-aot-trimming-constraints
- kind: definition
- informal: Native AOT / trimming режут рефлексию и динамику. Таргет AOT → отдельные ограничения, не «как обычный JIT».
- formal.rule: aot_trimming_needs_explicit_compatibility
- applies_when: PublishAOT / trimming enabled; reflection-heavy libs; dynamic code gen
- does_not_apply: ordinary framework-dependent deploy without trimming
- inference_hooks: tfm, applicability-then-infer
- llm_cue: Will this survive trim/AOT — or am I relying on JIT reflection?
- related: tfm, dotnet-cli-as-ssot
- sources: worlds/software-authoring/code-writing-principles.md

