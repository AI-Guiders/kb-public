---
type: Definition Card
title: GoF — Factory Method
description: Суперкласс задаёт интерфейс создания; подклассы решают, какой продукт вернуть. Замена размазанных `new Concrete`.
tags: [llm-native-card, definition, software-authoring, gof]
world: software
subworld: authoring
---

# GoF — Factory Method

- id: gof-factory-method
- kind: definition
- informal: Суперкласс задаёт интерфейс создания; подклассы решают, какой продукт вернуть. Замена размазанных `new Concrete`.
- formal.intent: interface for creating an object, deferring type to subclasses
- applies_when: creation varies by subtype; Open/Closed on product families without editing call sites
- does_not_apply: one-off `new` with no variation; DI container already resolves; Abstract Factory needed (product *families*); pattern-first before types
- inference_hooks: solid-ocp, solid-srp, mc-pattern-first, gof-strategy
- llm_cue: Is creation the varying axis — or am I just avoiding `new` aesthetics?
- related: what-is-design-pattern, gof-strategy, solid-ocp, mc-pattern-first
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/design-patterns/factory-method

