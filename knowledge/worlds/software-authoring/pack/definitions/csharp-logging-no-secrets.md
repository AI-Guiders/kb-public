**Tags:** #llm-native-card #definition #software-authoring #csharp #trap

# Logging — no secrets / PII

- id: csharp-logging-no-secrets
- kind: definition
- informal: Структурированные логи и уровни — да. Секреты и лишний PII в логах — нет.
- formal.rule: structured_logs_without_secrets_or_excess_pii
- applies_when: writing Log*/ILogger; exception messages that might echo input
- does_not_apply: local scratch debug never shipped (still prefer scrubbing habit)
- inference_hooks: default-distrust, applicability-then-infer
- llm_cue: Would I paste this log line into a ticket for a stranger?
- related: csharp-culture-invariant-vs-current
- sources: worlds/software-authoring/code-writing-principles.md

