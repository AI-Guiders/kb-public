**Tags:** #llm-native-card #definition #software-authoring #csharp #trap #async

# CancellationToken — propagate

- id: csharp-cancellationtoken-propagate
- kind: definition
- informal: Для отменяемых операций проталкивать `CancellationToken` по цепочке (публичные async API, I/O, long loops). Не глотать cancel без схемы; не invent'ить токен «внизу», если caller уже дал.
- formal.rule: cancellable_work_accepts_and_forwards_token
- applies_when: async I/O; request-scoped work; timeouts; cooperative cancel between layers
- does_not_apply: pure sync CPU with no cancel path; fire-and-forget where cancel is undefined by design
- inference_hooks: csharp-async-no-sync-over-async, applicability-then-infer
- llm_cue: Does every awaitable hop see the caller's CancellationToken?
- related: csharp-async-no-sync-over-async, csharp-async-void-ui-only, csharp-valuetask-semantics
- sources: worlds/software-authoring/code-writing-principles.md

