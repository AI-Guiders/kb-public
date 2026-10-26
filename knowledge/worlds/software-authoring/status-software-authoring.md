---
type: Status
title: 'Status: software.authoring v1'
description: '**Домен:** принципы написания кода, декомпозиция, OOA&D (канон для агента и человека).'
tags: [software-authoring, status, worlds]
world: software
subworld: authoring
sections: [operating-contract-matrix, language-worlds-v1]
---

﻿# Status: software.authoring v1

**Домен:** принципы написания кода, декомпозиция, OOA&D (канон для агента и человека).


---

## Operating contract (текущий)

| Приоритет | Документ | Когда |
|-----------|----------|--------|
| 1 | `playbook-ooad-agent-operational.md` | Новая фича, рефакторинг, рост `switch`/god-class |
| 2 | `kb-ooad-fundamentals.md` | Фундамент, GRASP, источники (Larman, UML) |
| 3 | `playbook-domain-nouns-verbs-decomposition.md` | Быстрый контракт: существительные → типы, глаголы → методы |
| 4 | `code-writing-principles.md` | C# / .NET стиль после структуры |

---

## Maintenance Policy

- **Проверено:** при изменении инженерной практики в Cascade IDE или после сессии с явным уроком (как chat Skia 2026-05).
- **Связь с engineering-evidence:** Track C в `map-engineering-reading.md`; evidence-строки — в `kb-engineering-evidence.md` § Object-oriented analysis and design.

---
- **Next review triggers:** new primary source / platform release / URL rot / repeated field mismatch / stale-claim flag

## Closure snapshot

- OOA&D фундамент и операционный проход — **в каноне** (v1.0).
- Nouns/verbs playbook — **дочерний** операционный слой.
- Отдельный `status-ooad-v1` не выделяем: домен **software.authoring** покрывает анализ→код.

<!-- section:operating-contract-matrix -->
## Transfer matrix (cross-domain software)

| Когда | Документ |
|-------|----------|
| Неявный симптом (визуал + структура, god-class, switch, Skia, новый экран) | `matrix-software-cross-domain-transfer.md` **до** углубления в kb |
| Явный OOA&D / декомпозиция | сразу `playbook-ooad-agent-operational.md` (матрица опциональна) |
| SoftFL / FileLines warn (CDP quality) | OOA&D + DRY + KISS; `partial` = узкий случай — playbook §Когда + cdp-mcp `.cdp/domain/quality.md` |

Роутер supplement: `router-software-transfer-matrix` в `index-knowledge-router-supplement.md`.
<!-- /section:operating-contract-matrix -->

<!-- section:language-worlds-v1 -->
## Языковые миры (иерархия)

Родитель **`software.authoring`** — только кросс-языковое (OOA&D, matrix, nouns/verbs).

Дочерние (примеры): `software.authoring.dotnet.csharp`, `software.authoring.php`, `software.authoring.javascript` — полная таблица и резолв по файлам: **`kb-software-authoring-language-worlds.md`**.

Легаси-теги `software.php`, `software.javascript` в старых карточках = те же миры.
<!-- /section:language-worlds-v1 -->

