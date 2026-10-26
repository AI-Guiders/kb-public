---
type: Definition Card
title: GoF — Strategy
description: Семейство взаимозаменяемых алгоритмов в отдельных классах; контекст делегирует, клиент подставляет стратегию.
tags: [llm-native-card, definition, software-authoring, gof]
world: software
subworld: authoring
---

# GoF — Strategy

- id: gof-strategy
- kind: definition
- informal: Семейство взаимозаменяемых алгоритмов в отдельных классах; контекст делегирует, клиент подставляет стратегию.
- formal.intent: define a family of algorithms, encapsulate each, make them interchangeable
- applies_when: same context, multiple algorithms; need runtime swap or Open/Closed on behavior without fat conditionals
- does_not_apply: one algorithm forever; State (behavior tied to object lifecycle/transitions); Template Method better as inheritance skeleton; premature extract before pain
- inference_hooks: solid-ocp, composition-over-inheritance, mc-pattern-first, gof-observer
- llm_cue: Am I swapping algorithms — or modeling object state transitions (→ State)?
- related: what-is-design-pattern, composition-over-inheritance, solid-ocp, gof-factory-method
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/design-patterns/strategy

