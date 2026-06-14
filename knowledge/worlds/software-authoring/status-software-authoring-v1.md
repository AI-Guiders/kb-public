# Status: software.authoring v1

**Домен:** принципы написания кода, декомпозиция, OOA&D (канон для агента и человека).

**Версия:** v1.0 · 2026-05-17

---

## Operating contract (текущий)

| Приоритет | Документ | Когда |
|-----------|----------|--------|
| 1 | `playbook-ooad-agent-operational-v1.md` | Новая фича, рефакторинг, рост `switch`/god-class |
| 2 | `kb-ooad-fundamentals-v1.md` | Фундамент, GRASP, источники (Larman, UML) |
| 3 | `playbook-domain-nouns-verbs-decomposition-v1.md` | Быстрый контракт: существительные → типы, глаголы → методы |
| 4 | `code-writing-principles-v1.md` | C# / .NET стиль после структуры |

---

## Maintenance Policy

- **Проверено:** при изменении инженерной практики в Cascade IDE или после сессии с явным уроком (как chat Skia 2026-05).
- **Связь с engineering-evidence:** Track C в `map-engineering-reading-v1.md`; evidence-строки — в `kb-engineering-evidence-v1.md` § Object-oriented analysis and design.

---

## Closure snapshot

- OOA&D фундамент и операционный проход — **в каноне** (v1.0).
- Nouns/verbs playbook — **дочерний** операционный слой.
- Отдельный `status-ooad-v1` не выделяем: домен **software.authoring** покрывает анализ→код.

<!-- section:operating-contract-matrix -->
## Transfer matrix (cross-domain software)

| Когда | Документ |
|-------|----------|
| Неявный симптом (визуал + структура, god-class, switch, Skia, новый экран) | `matrix-software-cross-domain-transfer-v1.md` **до** углубления в kb |
| Явный OOA&D / декомпозиция | сразу `playbook-ooad-agent-operational-v1.md` (матрица опциональна) |

Роутер supplement: `router-software-transfer-matrix` в `index-knowledge-router-supplement-v1.md`.
<!-- /section:operating-contract-matrix -->

<!-- section:language-worlds-v1 -->
## Языковые миры (иерархия)

Родитель **`software.authoring`** — только кросс-языковое (OOA&D, matrix, nouns/verbs).

Дочерние (примеры): `software.authoring.dotnet.csharp`, `software.authoring.php`, `software.authoring.javascript` — полная таблица и резолв по файлам: **`kb-software-authoring-language-worlds-v1.md`**.

Легаси-теги `software.php`, `software.javascript` в старых карточках = те же миры.
<!-- /section:language-worlds-v1 -->

