# JavaScript — operational playbook v1

**Purpose:** перевод **fundamentals** (модель языка ECMAScript в KB) в **действия, контракты и проверки** в репозитории и CI.  
**Мир:** `software.javascript`.  
**Связь:** карта fundamentals + operational kb — [`index-knowledge-javascript-cluster-v1.md`](index-knowledge-javascript-cluster-v1.md).

---

## 1. Порядок слоёв: fundamentals → operational

1. **`status-javascript-v1.md`** — снимок домена и триггеры.
2. **Этот playbook** — когда и что проверять в работе (прочитать до углубления в kb).
3. **Fundamentals (теория / спецификация):** один или цепочка карточек из §2 — **не грузить все сразу** без full pass.
4. **Operational (экосистема):** [`kb-javascript-operational-ecosystem-v1.md`](kb-javascript-operational-ecosystem-v1.md) — после fundamentals или сразу при чисто инфраструктурном вопросе (lockfile, audit, CSP).

---

## 2. Слой fundamentals (карточки)

Читать **последовательно** только при явном «полном фундаментальном проходе»; иначе — **одна** карточка по таблице в index.

| Шаг | Файл | Кратко |
|-----|------|--------|
| A1 | `kb-javascript-ecmascript-and-modules-v1.md` | редакции ECMA-262, ESM/CJS, транспиляция vs полифилл, **движки и хосты** |
| A2 | `kb-javascript-types-coercion-and-scope-v1.md` | типы времени выполнения, принуждения, TDZ, замыкания, `this` |
| A3 | `kb-javascript-objects-prototypes-and-classes-v1.md` | прототипы, классы, `#`, итерируемость |
| A4 | `kb-javascript-async-and-event-loop-v1.md` | Promises, async/await, микро/макрозадачи, AbortSignal |

**Остановка:** после шага, закрывшего вопрос.

---

## 3. Слой operational (карточка)

| Файл | Когда |
|------|--------|
| `kb-javascript-operational-ecosystem-v1.md` | npm/semver/lockfile, ESLint/Prettier, бандлеры, тест‑раннеры, XSS/CSP/eval, audit в CI |

---

## 4. Мост «fundamentals → действие в проекте»

| Идея (fundamentals) | Практический шаг |
|----------------------|------------------|
| ESM vs CJS, `import.meta` | Зафиксировать `package.json` `"type"`, соглашение по `.mjs`/`.cjs`, проверить граф на CI |
| Транспиляция vs полифилл | Записать матрицу сред и `targets`; не смешивать «только синтаксис» с рантайм‑полифиллами без учёта |
| TDZ / порядок модулей | Минимальный reproduce циклического графа; не «лечить» порядком импортов без модели |
| `this` и стрелки | Один задокументированный стиль для колбэков на границах публичного API |
| Микрозадачи / async | Один тест порядка Promise vs `setTimeout` в **целевой** среде CI |
| Фабрики vs `new` | Явная команда договорённость в style guide для объектных API |

---

## 5. Full pass (fundamentals → operational)

**Фаза A (fundamentals):** A1 → A2 → A3 → A4 (как в §2).  
**Фаза B (operational):** `kb-javascript-operational-ecosystem-v1.md`.

Не выполнять обе фазы в одной загрузке контекста без необходимости.

---

## 6. Evidence‑based рабочий формат

- **Fact:** версия движка (`node -p process.versions`), матрица браузера из конфигурации или Baseline.
- **Hypothesis:** ожидаемый эффект изменения (сборка, порядок задач, разрешение модулей).
- **Check:** минимальный reproduce в целевом рантайме.
- **Decision criterion:** тест + зелёный CI на целевой ветке зависимостей.
- **Confidence mark:** явно.

---

## 7. Контракты (сжато)

- **Runtime:** не смешивать ментальную модель «браузерный global» и ESM‑модуля Node без явной политики.
- **Dependencies:** приложения — lockfile под VCS; audit как сигнал, не как единственная защита.
- **Security:** минимизировать `eval`/`Function` от пользовательских строк; CSP — осознанно, вместе с экранированием HTML.

---

## 8. Смежные домены

- **TypeScript** (`software.typescript`) — отдельный онбординг; не подменяет fundamentals JS.
- **RegExp во flavor JS:** `worlds/pattern-regex/regex-playbook.md` → `worlds/pattern-regex/kb-regex-flavors-practice-v1.md` § JavaScript.

---

## 9. Revisit triggers

- Смена major платформы (ESM‑only, смена разрешения модулей в Node).
- Массовые deprecations после обновления движка или ESLint major.

---

## Layer (memory-architecture)

- **L1:** `status-javascript-v1.md` → **этот** playbook.
- **L1 deep fundamentals:** карточки §2 по одной.
- **L1 operational:** `kb-javascript-operational-ecosystem-v1.md`.

---

*Версия: v1 · operational split fundamentals → operational · 2026-05-10*
