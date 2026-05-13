# Кластер JavaScript (**world (KE):** `software.javascript`) — навигация v1

**Назначение:** точка входа с явным разложением **fundamentals → operational**. Контракт memory-architecture: **status → playbook → kb**; playbook — [`playbook-javascript-operational-v1.md`](playbook-javascript-operational-v1.md) (операционный слой и мост от теории к действиям).

**Статус домена:** `status-javascript-v1.md`.

---

## Слой fundamentals (спецификация и модель выполнения)

Карточки **только про язык ECMAScript** (и движки на уровне «что это за реализации», без npm/CI). Читать **по одной**, кроме явного full pass.

**Порядок full pass (фаза A):**

1. `kb-javascript-ecmascript-and-modules-v1.md` — редакции, модули ESM/CJS, транспиляция vs полифилл, **реализации и хосты**
2. `kb-javascript-types-coercion-and-scope-v1.md` — значения, принуждения, TDZ, замыкания, `this`
3. `kb-javascript-objects-prototypes-and-classes-v1.md` — прототипы, классы, `#`, итерируемость
4. `kb-javascript-async-and-event-loop-v1.md` — Promises, async/await, микро/макрозадачи

**После fundamentals при работе только с DOM/Web API** — MDN/спеки платформы; этот кластер держит **язык**, не каждый браузерный интерфейс.

---

## Слой operational (репозиторий, CI, угрозы)

**Фаза B** после A **или** сразу при чисто инфраструктурном вопросе:

- `kb-javascript-operational-ecosystem-v1.md` — npm/lockfile/semver, ESLint/Prettier, бандлеры, тест‑раннеры, XSS/CSP/eval, audit

Детальные контракты и таблица «идея fundamentals → шаг в проекте» — в **`playbook-javascript-operational-v1.md`**.

---

## Таблица: вопрос → куда смотреть

| Тип вопроса | Первичный kb |
|-------------|----------------|
| ES20xx, TC39, ESM/CJS/`import.meta`, транспилятор, цели сборки | `kb-javascript-ecmascript-and-modules-v1.md` |
| Движки V8/JSC/SM, зачем различать браузеры и версии для одной семантики | `kb-javascript-ecmascript-and-modules-v1.md` § 7 |
| `==`/`===`, UTF‑16, TDZ, `function`/`=>`, `this` | `kb-javascript-types-coercion-and-scope-v1.md` |
| Прототипы, `class`, `#`, итераторы | `kb-javascript-objects-prototypes-and-classes-v1.md` |
| Promises, порядок микро/макрозадач, AbortSignal | `kb-javascript-async-and-event-loop-v1.md` |
| Lockfile, audit, ESLint, бандлеры, тест‑раннеры, CSP/XSS | `kb-javascript-operational-ecosystem-v1.md` |

---

## Правила нагрузки контекста

- Не смешивать **фундаментальный** спор о семантике с **npm**‑темой в одной загрузке без нужды.
- При споре о поведении языка — **ECMA-262** + версия движка.

---

## Registry note

- **world:** software.javascript  
- **layer:** router (индекс кластера)  
- **status:** active  
- **updated_at:** 2026-05-10
