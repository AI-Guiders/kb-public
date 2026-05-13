# ECMAScript: редакции, модули и граница совместимости

**Назначение:** опорный слой **спецификации ECMA-262** и **системы модулей** в реальных проектах: годовые редакции, политика «что допустимо в исходниках без транспиляции», ESM vs CommonJS. Мир **`software.javascript`**.

**Порядок загрузки:** `status-javascript-v1.md` → `playbook-javascript-operational-v1.md` → этот файл (или по карте `index-knowledge-javascript-cluster-v1.md`).

---

## Provenance

- source_refs: `spec:ECMA-262` (ежегодные редакции; текст на ecma-international.org); `doc:MDN` (обзорные страницы по модулям и `import`); `kb:internal` synthesis 2026-05-10
- created_at: 2026-05-10
- updated_at: 2026-05-10
- author: agent (ANKB ingestion)

## Metadata

- card_id: kb-javascript-ecmascript-and-modules-v1
- world: software.javascript
- layer: world (L1 kb)
- tags: ecmascript, modules, esm, cjs, interop, engines (fundamentals)
- status: active

## Epistemic Linkage

- epistemic_basis: fact + inference
- evidence_type: normative specification + de-facto platform behavior
- confidence: high для разделения ESM/CJS; medium для конкретных краёв interop между рантаймами
- transfer_boundary: не подменяет официальный **Import Maps** или bundler‑специфичные расширения — только языковой минимум и типовые ловушки

## Core Unit

- **context:** проект объявляет целевые среды (браузер, Node, edge) и иногда **транспилятор** с полем `targets` / browserslist.
- **signal:** путаница «ES6 / ES2015 / ES2023», broken `require`/`import`, «заработало в браузере, упало под Node».
- **action:** зафиксировать **минимальную поддерживаемую матрицу**; для исходников — политику: нативный синтаксис vs только после сборки.
- **outcome:** предсказуемый граф модулей и отсутствие «магического» смешения семантик без явного shim.
- **lesson:** язык задаёт **синтаксис и семантику ESM**; упаковщик может эмулировать разрешение путей, но не отменяет отличий `this` и hoisting между системами.

### 1. ECMAScript как линия времени

- **Fact:** стандарт развивается **ежегодными редакциями** (ES2015 как крупный рубеж для модулей, классов, стрелок, Promises и др.); коллоквиально «ES6» ≈ ES2015, но в инженерной переписке лучше **год**.
- **Heuristic:** называть фичу **по редакции**, в которой она стабилизирована в спецификации, и сверять с **matrix** браузера/Node (например через Baseline‑статусы или `compat`‑таблицы), а не по блогам.
- **First adoption task:** один источник правды на проект — `package.json` `engines`, browserslist или эквивалент.
- **Success criterion:** нет расхождения «учебник ES5» и «реальный код под ESM‑only».
- **Confidence:** high

### 2. ESM: статический импорт и живой биндинг

- **Fact:** `import` на верхнем уровне модуля создаёт **живые read-only биндинги** к экспортам при условии, что экспортирующий модуль использует `let`/`const`/`class` с экспортом (модель в спецификации описывается через Module Record и Environment Records).
- **Heuristic:** циклические графы допустимы, но порядок инициализации чувствителен к тому, **где читается** ещё не проинициализированный биндинг (TDZ на уровне модуля для `let`/`const`).
- **First adoption task:** явно документировать шаблон безопасного re-export (`export { x } from './m.js'`).
- **Confidence:** high

### 3. Dynamic `import()` и разделение кода

- **Fact:** `import(specifier)` возвращает Promise на namespace‑объект; доступность на верхнем уровне модулей и в async‑функциях следует правилам goal symbol `Module` в грамматике.
- **Heuristic:** загрузчик конкретной платформы всё равно может отказать по политике сети/CORS — это уже не язык.
- **Confidence:** high

### 4. CommonJS и interop под Node‑подобными рантаймами

- **Fact:** `require`, `module.exports`, `exports` — **не часть ECMAScript**; это поверхность класса модульных систем до стандартизации ESM у платформы. Интероп (импорт CJS из ESM и обратно) **зависит от версии Node и флагов** (`package.json` `"type": "module"` резко меняет подразумеваемое расширение файлов и трактовку `.js`).
- **Heuristic:** новые библиотеки по возможности отдавать **чистый ESM** или явно документировать dual‑package hazards.
- **Falsification trigger:** код «работает локально под одним флагом» и ломается на CI без флага — проверить `type`, расширения `.cjs`/`.mjs`, условные экспорты `exports` в манифесте пакета.
- **Confidence:** medium (края пересмотреть при мажорных релизах Node)

### 5. `import.meta` и контекст модуля

- **Fact:** `import.meta` — объект на уровне модуля с платформенно‑зависимыми полями (например `url` там, где определено).
- **Heuristic:** не подменять «путь файла» из CommonJS переменными `__filename` без адаптера — это разные модели окружения.
- **Confidence:** high

### 6. Транспиляция: зачем и где граница

- **Fact:** транспилятор меняет **исходный** синтаксис в поддерживаемый целевыми движками AST/байткод; полифиллы добавляют **объекты времени выполнения** для новых API (не путать с синтаксисом).
- **Heuristic:** если цель — только синтаксис, но добавлены helper‑рантаймы (например для классов до полной нативной семантики), измерять **реальный выход**, а не «мы настроили preset env».
- **Confidence:** high

### 7. Реализации языка и хост-среды (fundamentals)

- **Fact:** **V8** (Chromium, Node и др. встраивания), **SpiderMonkey** (Firefox), **JavaScriptCore** (Safari/WebKit) реализуют ECMAScript; **DOM и прочие host API** не входят в ECMA-262 как часть языка — это поверхность платформы.
- **Heuristic:** багфиксы и края (`Date`, `RegExp`, тайминги) могут различаться между движками — матрица CI и версии, не «работает у меня».
- **Operational follow-up:** lockfile, бандлеры, audit — слой **`kb-javascript-operational-ecosystem-v1.md`** после этого playbook.
- **Confidence:** high

## Lifecycle

- supersedes: —
- superseded_by: —
- deprecation_reason: —