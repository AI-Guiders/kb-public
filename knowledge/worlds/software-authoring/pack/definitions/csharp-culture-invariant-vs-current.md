---
type: Definition Card
title: 'Culture: Invariant vs Current'
description: Протоколы, сырой парсинг, машиночитаемые логи → `InvariantCulture`. Текст UI → `CurrentCulture`.
tags: [llm-native-card, definition, software-authoring, csharp, trap]
world: software
subworld: authoring
---

# Culture: Invariant vs Current

- id: csharp-culture-invariant-vs-current
- kind: definition
- informal: Протоколы, сырой парсинг, машиночитаемые логи → `InvariantCulture`. Текст UI → `CurrentCulture`.
- formal.rule: machine_data_invariant_ui_current
- applies_when: Parse/ToString of numbers/dates for wire/files; log payloads; sorting keys shared across locales
- does_not_apply: user-facing copy; locale-aware display already routed through UI layer
- inference_hooks: applicability-then-infer
- llm_cue: Is this for a machine or a human reader?
- related: csharp-async-no-sync-over-async
- sources: worlds/software-authoring/code-writing-principles.md

