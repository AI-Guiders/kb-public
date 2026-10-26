---
type: Definition Card
title: ConfigureAwait — library vs app
description: В обобщённом библиотечном коде — `ConfigureAwait(false)` на релевантных await. В приложении (UI после await, типичный ASP.NET Core) — не навязывать `false` без нужды.
tags: [llm-native-card, definition, software-authoring, csharp, trap]
language: ru
world: software
subworld: authoring
---

# ConfigureAwait — library vs app

- id: csharp-configureawait-library-vs-app
- kind: definition
- informal: В обобщённом библиотечном коде — `ConfigureAwait(false)` на релевантных await. В приложении (UI после await, типичный ASP.NET Core) — не навязывать `false` без нужды.
- formal.rule: configureawait_false_in_reusable_libraries_not_by_default_in_apps
- applies_when: writing shared libraries/packages; capturing sync context matters
- does_not_apply: blind `false` everywhere in ASP.NET Core apps; UI code that must resume on UI thread without care
- inference_hooks: csharp-async-no-sync-over-async, applicability-then-infer
- llm_cue: Library or app — whose sync context am I assuming?
- related: csharp-async-no-sync-over-async, csharp-async-void-ui-only
- sources: worlds/software-authoring/code-writing-principles.md

