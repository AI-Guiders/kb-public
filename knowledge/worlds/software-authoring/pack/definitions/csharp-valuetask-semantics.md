---
type: Definition Card
title: ValueTask semantics
description: '`ValueTask` — только понимая семантику (в т.ч. повторный await одного экземпляра). Сомнение → `Task`.'
tags: [llm-native-card, definition, software-authoring, csharp, trap]
world: software
subworld: authoring
---

# ValueTask semantics

- id: csharp-valuetask-semantics
- kind: definition
- informal: `ValueTask` — только понимая семантику (в т.ч. повторный await одного экземпляра). Сомнение → `Task`.
- formal.rule: valuetask_only_with_known_consumption_rules
- applies_when: hot path allocation sensitivity; implementing IValueTaskSource patterns
- does_not_apply: ordinary app/service async APIs; unknown consumption (multiple await/then)
- inference_hooks: csharp-async-no-sync-over-async, applicability-then-infer
- llm_cue: Do I know every consumer awaits this ValueTask exactly once?
- related: csharp-async-no-sync-over-async
- sources: worlds/software-authoring/code-writing-principles.md

