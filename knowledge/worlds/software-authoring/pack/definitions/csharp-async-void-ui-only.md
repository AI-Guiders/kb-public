**Tags:** #llm-native-card #definition #software-authoring #csharp #trap

# async void — UI events only

- id: csharp-async-void-ui-only
- kind: definition
- informal: `async void` — только обработчики событий UI. Иначе `Task` / `ValueTask`.
- formal.rule: async_void_only_for_event_handlers
- applies_when: WinForms/WPF/Avalonia event handlers that must match void signature
- does_not_apply: libraries; ASP.NET; any API you control the signature of
- inference_hooks: csharp-async-no-sync-over-async, applicability-then-infer
- llm_cue: Is this forced void by an event — or lazy fire-and-forget?
- related: csharp-async-no-sync-over-async, csharp-valuetask-semantics
- sources: worlds/software-authoring/code-writing-principles.md

