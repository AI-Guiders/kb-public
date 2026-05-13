# Status: JavaScript (ECMAScript) v1

**Канон перечня артефактов домена:** § Closure snapshot ниже. В `index-knowledge-router-v1.md` в таблице доменов — короткая строка; полная карта **fundamentals → operational** — `index-knowledge-javascript-cluster-v1.md`.

## Closure snapshot

- **Fundamentals (`software.javascript`, язык):**
  - `kb-javascript-ecmascript-and-modules-v1.md`
  - `kb-javascript-types-coercion-and-scope-v1.md`
  - `kb-javascript-objects-prototypes-and-classes-v1.md`
  - `kb-javascript-async-and-event-loop-v1.md`
- **Operational (экосистема, сборка, угрозы):**
  - `kb-javascript-operational-ecosystem-v1.md`
- **Операционный playbook (мост + контракты):** `playbook-javascript-operational-v1.md`
- **Карта кластера:** `index-knowledge-javascript-cluster-v1.md`
- **Router supplement:** `router-javascript` в `index-knowledge-router-supplement-v1.md`

## Operational invariant

- **Версии движка и возможности языка не смешиваются без явной цели.** Указывать **целевой runtime** (Baseline браузеры или версии Chromium/Firefox/Safari, либо `node`/`deno`/`bun`). Не использовать «современный JS» без матрицы поддержки или политики транспиляции.

## Связанные домены

- **`software.typescript`** — статический слой типов поверх этого ядра; отдельный проход.
- **RegExp (диалект JS):** `worlds/pattern-regex/kb-regex-flavors-practice-v1.md` § JavaScript.

## Next review triggers

- Крупные изменения ECMA-262, влияющие на операционную матрицу (модули, async).

- Изменение политики Baseline / interop в целевых браузерах — пересмотреть шаг транспиляции.

## Retrieval hint (memory-architecture)

1. Этот `status-*`
2. `playbook-javascript-operational-v1.md`
3. **Fundamentals** — один `kb-javascript-*` из списка выше **или** фаза A по index
4. **Operational** — `kb-javascript-operational-ecosystem-v1.md` при вопросах npm/CI/security tooling

## Full pass hint

- «Полный проход» → `index-knowledge-javascript-cluster-v1.md` (фаза A → фаза B) + `playbook-javascript-operational-v1.md` § 5.
