# JavaScript — operational: экосистема, сборка, тесты, угрозы

**Назначение:** **операционный слой** мира **`software.javascript`** после fundamentals: npm/lockfile, semver, статический анализ, бандлеры, тест‑раннеры, базовая модель угроз (XSS, CSP, динамический код). Не заменяет спецификацию языка — см. карточки `kb-javascript-*` в фазе fundamentals в `index-knowledge-javascript-cluster-v1.md`.

**Порядок загрузки:** `status-javascript-v1.md` → `playbook-javascript-operational-v1.md` → этот файл (после прохождения fundamentals по вопросу или в фазе B full pass).

---

## Provenance

- source_refs: `npm:docs`; `nodejs.org` / `bun.sh` / `deno.land`; `cheatsheetseries.owasp.org` (XSS — ориентир); `kb:internal` synthesis 2026-05-10; supersedes раздел tooling из `kb-javascript-runtime-tooling-and-security-baseline-v1.md`
- created_at: 2026-05-10
- updated_at: 2026-05-10

## Metadata

- card_id: kb-javascript-operational-ecosystem-v1
- world: software.javascript
- layer: operational (kb)
- tags: node, npm, tooling, security, csp, ci
- status: active

## Epistemic Linkage

- epistemic_basis: inference + fact
- confidence: high для lockfile+semver; medium для матрицы конкретного бандлера

## Core Unit

- **context:** проект выходит за пределы «одного скрипта в HTML».
- **signal:** «сломалось после minor», audit CI, CSP ломает инлайн, флейки тестов из-за таймеров.
- **action:** зафиксировать lockfile, политику audit, минимальный security baseline.
- **outcome:** воспроизводимые сборки и снижение типовых supply-chain/XSS ошибок конфигурации.

### 1. npm, lockfile, semver

- **Fact:** диапазон версий в `package.json` **не** фиксирует дерево; lockfile фиксирует разрешённое дерево при том же менеджере и дисциплине вроде `npm ci`.
- **Heuristic:** **приложения** коммитят lockfile; библиотеки — по политике пакета (часто только `package.json`).
- **Uncertainty:** при конфликте `peerDependencies` смотреть отчёт установщика конкретной версии.
- **Confidence:** high

### 2. ESLint / Prettier и дисциплина стиля

- **Fact:** линтер ловит класс ошибок и опасные паттерны, но **не** заменяет тесты на семантику языка.
- **Heuristic:** правила async/import‑организации включать после согласования — массовые автофиксы несут риск семантических регрессий.
- **Confidence:** high

### 3. Транспиляция и бандлеры

- **Fact:** esbuild/swc/Rollup/webpack/Vite решают граф модулей и совместимость целей; артефакты могут различаться картами кода и транзитивными лицензиями инструментов.
- **Heuristic:** supply chain и лицензии — отдельная политика организации; KB фиксирует класс риска.
- **Confidence:** medium

### 4. Тестирование: Vitest / Jest / `node:test`

- **Fact:** раннер задаёт окружение модулей и моки времени/сети; влияет на флейки порядка задач.
- **Heuristic:** изолировать глобальное состояние и таймеры; `useFakeTimers` — с пониманием взаимодействия с microtasks.
- **Confidence:** high

### 5. Базовые web‑угрозы (XSS, CSP)

- **Fact:** XSS часто связан со склейкой HTML без экранирования, а не «с JS как языком».
- **Heuristic:** CSP и отказ от `unsafe-inline` — осознанно; **CSP не заменяет** корректное экранирование в HTML‑контекстах на сервере/шаблоне.
- **Confidence:** high как ориентир

### 6. Динамический код: `eval`, `new Function`

- **Fact:** компиляция строк в код расширяет blast radius при вводе пользователя или компрометации конфигов.
- **Heuristic:** по умолчанию deny без threat model; REPL и исключения — изолировать.
- **Confidence:** high

## Operationalization (сводка слоя)

- **first_adoption_task:** включить `npm audit` / эквивалент в CI как **сигнал**, не как единственную гарантию.
- **validation_check:** `node -p process.versions` согласован между dev и CI.
- **success_criterion:** lockfile приложения под версионированием; нет «случайного» его отсутствия.

## Lifecycle

- supersedes: kb-javascript-runtime-tooling-and-security-baseline-v1 (содержимое tooling/security перенесено сюда; движки — в `kb-javascript-ecmascript-and-modules-v1.md` § реализации)
- superseded_by: —
- deprecation_reason: —
