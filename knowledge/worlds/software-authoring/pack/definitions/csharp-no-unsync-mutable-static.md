---
type: Definition Card
title: Shared mutable static
description: Общая изменяемая статика без синхронизации — гонки. Нужны `Concurrent*`, `lock`, `SemaphoreSlim` по смыслу — или убрать shared mutable.
tags: [llm-native-card, definition, software-authoring, csharp, trap]
language: ru
world: software
subworld: authoring
---

# Shared mutable static

- id: csharp-no-unsync-mutable-static
- kind: definition
- informal: Общая изменяемая статика без синхронизации — гонки. Нужны `Concurrent*`, `lock`, `SemaphoreSlim` по смыслу — или убрать shared mutable.
- formal.rule: no_unsynchronized_shared_mutable_static
- applies_when: static fields mutated from requests/threads; caches; lazy init races
- does_not_apply: immutable static readonly; thread-static intentional; single-threaded console toys
- inference_hooks: applicability-then-infer
- llm_cue: Can two threads touch this static state?
- related: csharp-async-no-sync-over-async, gof-singleton
- sources: worlds/software-authoring/code-writing-principles.md

