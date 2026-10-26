---
type: Definition Card
title: GoF — Observer
description: Издатель уведомляет подписчиков о событиях; набор слушателей неизвестен или меняется в рантайме.
tags: [llm-native-card, definition, software-authoring, gof]
world: software
subworld: authoring
---

# GoF — Observer

- id: gof-observer
- kind: definition
- informal: Издатель уведомляет подписчиков о событиях; набор слушателей неизвестен или меняется в рантайме.
- formal.intent: define a one-to-many dependency so dependents are notified of state changes
- applies_when: dynamic subscribers; decouple subject from concrete listeners; UI/events/domain events fit
- does_not_apply: Mediator (many-to-many via hub); sync return values needed from listeners; hidden global event bus as Singleton theater
- inference_hooks: solid-ocp, mc-pattern-first, gof-singleton
- llm_cue: One-way notify to many — or components need structured dialogue (→ Mediator)?
- related: what-is-design-pattern, gof-strategy, gof-singleton, solid-ocp
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/design-patterns/observer

