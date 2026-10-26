---
type: Definition Card
title: No sync-over-async
description: Не блокировать async через .Result/.Wait/GetResult без веской причины.
tags: [llm-native-card, definition, software-authoring]
language: ru
world: software
subworld: authoring
---

# No sync-over-async

- id: csharp-async-no-sync-over-async
- kind: definition
- informal: Не блокировать async через .Result/.Wait/GetResult без веской причины.
- formal.rule: avoid_blocking_on_async_in_library_and_request_path
- llm_cue: Am I blocking a thread on a Task?
- related: csharp-async-void-ui-only, csharp-configureawait-library-vs-app, csharp-valuetask-semantics, csharp-cancellationtoken-propagate
- sources: worlds/software-authoring/code-writing-principles.md

