# Асинхронность и цикл событий (Promises, задачи, платформенные хуки)

**Назначение:** единая картина **асинхронного поведения языка** (Promises, async/await) и **порядка исполнения задач** — микрозадачи vs задачи, взаимодействие с таймерами и I/O в типичных платформах. Мир **`software.javascript`**; детали браузерной **TaskQueue** и libuv — ориентировочно и с отсылкой к целевому движку.

**Порядок загрузки:** `status-javascript-v1.md` → `playbook-javascript-operational-v1.md` → этот файл.

---

## Provenance

- source_refs: `spec:ECMA-262` (Promise objects, async functions, microtask jobs); `whatwg:HTML` (очереди задач в браузере — на уровне концепций); `kb:internal` synthesis 2026-05-10
- created_at: 2026-05-10
- updated_at: 2026-05-10

## Metadata

- card_id: kb-javascript-async-and-event-loop-v1
- world: software.javascript
- layer: world
- tags: promise, async-await, microtask, event-loop
- status: active

## Epistemic Linkage

- epistemic_basis: fact + inference
- confidence: high для ordering microtasks vs текущей синхронной порции; medium для конкретной наносекундной упорядоченности I/O в Node без измерения

## Core Unit

- **context:** смешение синхронной ментальной модели с кодом, полным `await`.
- **signal:** «then сработал до / после setTimeout», двойной вызов после `await`, гонки инициализации.
- **action:** явная диаграмма **какой колбэк в какой очереди** для критичных путей.
- **outcome:** детерминированные тесты асинхронных инвариантов.
- **lesson:** **микрозадачи Promise очищаются до следующей макрозадачи стандартного браузерного цикла** (ориентир WHATWG), что объясняет типовые интервью‑паззлы.

### 1. Promises: три состояния и единичный переход

- **Fact:** объект Promise находится в состоянии pending/fulfilled/rejected; переход **единожды**; затем цепочки `then`/`catch`/`finally` планируются как **реакции**.
- **Heuristic:** ошибка, брошенная синхронно в executor, эквивалентна reject; не ловить — получим unhandled rejection там, где платформа его репортит.
- **Confidence:** high

### 2. Цепочки `then` и развёртывание `thenable`

- **Fact:** `Promise.resolve` может принимать значение или thenable и разворачивает вложенные обещания до устойчивого состояния согласно алгоритму `PromiseResolveThenableJob`.
- **Heuristic:** интеграции со старыми библиотеками с нестандартными thenable — источник редких deadlock‑подобных циклов; минимальный reproduce обязателен.
- **Confidence:** high

### 3. `async function` и `await`

- **Fact:** `await` приостанавливает выполнение асинхронной функции через преобразование к Promise и возобновление после разрешения с привязкой к модели `AsyncFunction` в спецификации.
- **Heuristic:** ошибки внутри `async` функции, не обёрнутые `try/catch`, становятся rejection возвращаемого Promise.
- **Confidence:** high

### 4. Очередь микрозадач

- **Fact:** реакции Promises и многие операции вроде `queueMicrotask` планируются как **микрозадачи**, исполняющиеся после завершения текущей синхронной работы и перед отдачей управления для визуальных обновлений/макрозадач на уровне конкретной реализации event loop.
- **Heuristic:** никогда не строить бесконечную рекурсию микрозадач без освобождения стека (риск зависания вкладки/event loop starvation).
- **Confidence:** high для концепции; medium для платформенной нумерации

### 5. `setTimeout`, `setImmediate` (где есть), I/O

- **Fact:** макрозадачи типа таймеров **не** выполняются до полного дренажа микрозадач в типичной модели браузера; в Node порядок между таймерами, `setImmediate` и I/O определяется libuv и фазами — не переносить ментальную модель вкладки один в один.
- **Heuristic:** бенчмарки «что быстрее» между `setTimeout(0)` и `queueMicrotask` — про **разные гарантии**, не про скорость абсолютную.
- **Confidence:** medium для Node edge cases

### 6. Отмена через `AbortSignal`

- **Fact:** стандартная поверхность **`AbortController`** / `AbortSignal` для отмены сетевых и других операций внешне к языку, но критично к async‑коду.
- **Heuristic:** не хранить только `boolean cancelled` глобально, если операция поддерживает Abort — прокидывать сигнал вниз по стеку вызовов.
- **Confidence:** high

### 7. Обработка ошибок в async‑шине

- **Fact:** `unhandledrejection` / `rejectionHandled` (в браузере) и аналогичные хуки процесса в Node — сигнал о нарушенном контракте обработки ошибок.
- **Heuristic:** централизовать политику логирования rejections в точке входа приложения, не в каждой библиотеке по‑разному.

## Lifecycle

- supersedes: —
- superseded_by: —
- deprecation_reason: —
