---
type: Definition Card
title: GoF — Singleton
description: Один экземпляр класса + глобальная точка доступа. Часто нарушает SRP и усложняет тесты/многопоточность.
tags: [llm-native-card, definition, software-authoring, gof]
language: ru
world: software
subworld: authoring
---

# GoF — Singleton

- id: gof-singleton
- kind: definition
- informal: Один экземпляр класса + глобальная точка доступа. Часто нарушает SRP и усложняет тесты/многопоточность.
- formal.intent: ensure a class has only one instance and provide a global access point
- applies_when: genuine process-wide unique resource with explicit lifecycle (rare); coordinated access is the pain
- does_not_apply: service locator habit; hiding DI; «удобный static»; most app services (prefer DI/scoped); test-heavy code without seams
- inference_hooks: solid-srp, solid-dip, mc-pattern-first, applicability-then-infer
- llm_cue: Do I need uniqueness — or just global convenience?
- related: what-is-design-pattern, mc-pattern-first, solid-dip, httpclient-reuse
- sources: personal/ah-history/ah-hot-full-07-2026-02-24-dev-books-and-courses-notes.md, https://refactoring.guru/design-patterns/singleton

