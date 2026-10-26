---
type: Definition Card
title: Dispose / await using
description: '`IDisposable` / `IAsyncDisposable` освобождать через `using` / `await using`. Не глотать исключения так, что объект остаётся битым без схемы.'
tags: [llm-native-card, definition, software-authoring, csharp, trap]
language: ru
world: software
subworld: authoring
---

# Dispose / await using

- id: csharp-dispose-using
- kind: definition
- informal: `IDisposable` / `IAsyncDisposable` освобождать через `using` / `await using`. Не глотать исключения так, что объект остаётся битым без схемы.
- formal.rule: deterministic_cleanup_via_using
- applies_when: owning streams, clients, scopes, locks that implement dispose
- does_not_apply: objects owned by DI/container lifetime; fire-and-forget without ownership
- inference_hooks: applicability-then-infer
- llm_cue: Who owns this resource — and is cleanup on every path?
- related: httpclient-reuse, csharp-async-no-sync-over-async
- sources: worlds/software-authoring/code-writing-principles.md

