**Tags:** #llm-native-card #definition #software-authoring #csharp #trap

# Check vulnerable NuGet packages

- id: csharp-nuget-vulnerable-check
- kind: definition
- informal: Периодически `dotnet list package --vulnerable` и обновления с учётом breaking changes.
- formal.rule: periodic_vulnerable_package_scan
- applies_when: dependency bumps; release hygiene; security review
- does_not_apply: every micro-commit; offline toys without restore
- inference_hooks: blast-radius, applicability-then-infer
- llm_cue: Did this change touch package graph — any known vulns?
- related: blast-radius, dotnet-cli-as-ssot
- sources: worlds/software-authoring/code-writing-principles-v1.md

