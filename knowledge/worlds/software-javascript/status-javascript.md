# Status: JavaScript (ECMAScript) v1
**Tags:** #software-javascript #status #worlds


**Канон перечня артефактов домена:** § Closure snapshot ниже. В `index-knowledge-router.md` в таблице доменов — короткая строка; полная карта **fundamentals → operational** — `index-knowledge-javascript-cluster.md`.

## Closure snapshot

- **Fundamentals (`software.javascript`, язык):**
  - `kb-javascript-ecmascript-and-modules.md`
  - `kb-javascript-types-coercion-and-scope.md`
  - `kb-javascript-objects-prototypes-and-classes.md`
  - `kb-javascript-async-and-event-loop.md`
- **Operational (экосистема, сборка, угрозы):**
  - `kb-javascript-operational-ecosystem.md`
- **Операционный playbook (мост + контракты):** `playbook-javascript-operational.md`
- **Карта кластера:** `index-knowledge-javascript-cluster.md`
- **Router supplement:** `router-javascript` в `index-knowledge-router-supplement.md`

## Operational invariant

- **Версии движка и возможности языка не смешиваются без явной цели.** Указывать **целевой runtime** (Baseline браузеры или версии Chromium/Firefox/Safari, либо `node`/`deno`/`bun`). Не использовать «современный JS» без матрицы поддержки или политики транспиляции.

## Связанные домены

- **`software.typescript`** — статический слой типов поверх этого ядра; отдельный проход.
- **RegExp (диалект JS):** `worlds/pattern-regex/kb-regex-flavors-practice.md` § JavaScript.

## Maintenance Policy

- **Проверено:** 2026-08-15 (operational playbook + ecosystem dig vs Baseline 2026 / ES2026)
- Event-driven refresh via **Next review triggers** below.
- Order: `status-*` → operational playbook → fundamentals → evidence (`playbook-kb-operational-freshness.md`).
## Next review triggers
- Крупные изменения ECMA-262, влияющие на операционную матрицу (модули, async).

- Изменение политики Baseline / interop в целевых браузерах — пересмотреть шаг транспиляции.

## Retrieval hint (memory-architecture)

1. Этот `status-*`
2. `playbook-javascript-operational.md`
3. **Fundamentals** — один `kb-javascript-*` из списка выше **или** фаза A по index
4. **Operational** — `kb-javascript-operational-ecosystem.md` при вопросах npm/CI/security tooling

## Full pass hint

- «Полный проход» → `index-knowledge-javascript-cluster.md` (фаза A → фаза B) + `playbook-javascript-operational.md` § 5.

