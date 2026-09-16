**Tags:** #llm-native-card #definition #software-authoring #csharp #trap #di

# DI — no scoped from singleton

- id: csharp-di-no-scoped-from-singleton
- kind: definition
- informal: Singleton не должен захватывать Scoped (и часто Transient в долгий кэш). Captive dependency = тихие баги жизненного цикла.
- formal.rule: shorter_lifetime_must_not_be_captured_by_longer
- applies_when: registering/resolving in MS.DI; ctor-injecting DbContext/request services into singletons
- does_not_apply: pure singletons of immutable/stateless services; manual scopes via IServiceScopeFactory when intentional
- inference_hooks: applicability-then-infer, gof-singleton
- llm_cue: Is a shorter-lived service stuck inside a longer-lived one?
- related: gof-singleton, httpclient-reuse, csharp-dispose-using
- sources: worlds/software-authoring/code-writing-principles.md

