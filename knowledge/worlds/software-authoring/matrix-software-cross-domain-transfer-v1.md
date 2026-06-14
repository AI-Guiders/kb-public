<!-- markdownlint-disable MD060 -->

# Software Cross-Domain Transfer Matrix v1

## Purpose

Маршрутизация **неявных** и смешанных software-задач: когда симптом в одном слое (Skia, ViewModel, «сделай красиво», биндинг Avalonia) требует **другого** playbook/kb — прежде всего **структуры (OOA&D)** vs **оформления (HCI)** vs **стека (.NET/Avalonia)** vs **процесса (Git/Roslyn)**.

Не заменяет Domain Entry Map в `index-knowledge-router-v1.md`; даёт **компактную таблицу переноса** после выбора домена «software».

**Версия:** v1.0 · 2026-05-17

---

## Transfer contract

- Переносить **принципы и порядок чтения**, не копировать API/паттерны из чужого мира без проверки.
- Перед любым cross-world шагом: [`../knowledge-engineering/matrix-do-not-transfer-v1.md`](../knowledge-engineering/matrix-do-not-transfer-v1.md) (жёсткие deny).
- Культура/формулировки в UI-текстах: при необходимости [`../knowledge-engineering/matrix-culture-routing-v1.md`](../knowledge-engineering/matrix-culture-routing-v1.md).
- Порядок загрузки при срабатывании матрицы: **`status-software-authoring-v1` → эта матрица (строка) → целевой playbook → kb по вопросу**.
- Эпистемика: не объявлять «архитектуру готова» без проверки сборки/Roslyn там, где менялся C#.

---

## Fast symptom router (агент)

**Troubleshooting-вход мира:** [`troubleshooting/playbook-software-authoring-troubleshooting-v1.md`](troubleshooting/playbook-software-authoring-troubleshooting-v1.md) (таблица синхронна с этой секцией).

| Симптом в запросе или коде | Сначала | Потом (если нужно) | Не делать |
|----------------------------|---------|---------------------|-----------|
| `switch` / `enum Kind` / `ItemKind` в renderer, handler, VM | `playbook-ooad-agent-operational-v1.md` | `playbook-domain-nouns-verbs-decomposition-v1.md` | ещё одна ветка в том же `switch` |
| God-class / ViewModel > ~800 строк / Control «всё умеет» | шаг 5 OOA&D (слои) + nouns-verbs | `code-writing-principles-v1.md` | выносить 20 микро-классов без домена |
| «Сделай визуал», карточки, layout, цвет, шрифт | **HCI** (`playbook-hci-core-v1`, `ui-ux-playbook`) для UX-контракта | **OOA&D**, если растёт discriminated union | Nielsen вместо типов |
| Новый экран / панель / overview / wizard | полный 7-шаговый OOA&D | Avalonia playbook при выборе контролов | сразу пиксели без словаря домена |
| Ошибка биндинга, тема, Dock, `axaml` | `playbook-avalonia-dock-ui-v1.md` | HCI только для copy/иерархии | полный OOA&D |
| CSxxxx / analyzer / «почини warning» | `playbook-csharp-roslyn-mcp-diagnostics-v1.md` | code action, не ручной костыль | редизайн домена |
| «Как в авиации / PFD / cockpit / scan pattern» | `kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md` | HCI + Avalonia для IDE | перенос регламентов FAA в код-ревью |
| DDD / Clean / «настоящая архитектура» | `status-software-authoring-v1` + OOA&D | Track C в `map-engineering-reading-v1.md` **после** анализа | папки по моде без сущностей |
| Только цвет/отступ/1 строка в одном методе | `code-writing-principles-v1.md` | — | OOA&D-проход |
| Compositor уже отдаёт `*Snapshot` / DTO | nouns-verbs: **presentation догоняет domain** | `SceneBuilder` + `ISkia*Entity` | дублировать домен в Control |
| Производительность `Draw` / jank | профиль hot path, кэш layout | не плодить сущности на кадр | OOA&D «с нуля» |
| Коммит, ветка, submodule | `playbook-git-workflow-v1.md` | — | структура классов |
| Интеграция API / MCP / Telegram | `software-integration-kb` | — | UI entity model |

---

## Matrix (детально)

### A. Presentation → structure (Skia, custom draw, hit-test)

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| Второй `if` по kind в `Draw`/`Measure` | полиморфизм, Information Expert | `ISkiaChatEntity` + классы сущностей | один новый вид = один тип, не enum-ветка |
| Общий record + дискриминатор на 4+ формы UI | noun/verb таблица | отдельные типы на форму | enum только без разного поведения |
| Control > 400 строк, цикл + switch | оркестратор + `SceneBuilder` | Control: scroll, theme, hit dispatch | не тащить padding карточки в Control |
| Hit-test с `switch` по kind | `CreateHit()` у сущности | hit-модель с `SelectThreadId` и т.д. | не смешивать hit с layout-математикой в одном методе |
| «Как на макете / картотека» | сущность `TopicCard` + поля summary/badges | HCI для иерархии текста | не рисовать без типа «карточка» |

**Канон-пример:** Cascade IDE `Views/Chat/Skia/` — domain в `ChatSurfaceCompositor`, presentation в `SkiaChat*`.

### B. Application layer → domain (MVVM, ViewModel, commands)

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| ViewModel знает Skia-координаты | разделение слоёв GRASP | VM → snapshot; Skia → entities | VM не рисует |
| Дублирование полей snapshot и VM | один источник истины | compositor / snapshot | не третий слой «ради удобства» |
| 50+ команд в одном VM | Controller / feature slice | отдельные VM или handlers по фиче | не god-VM «пока не больно» |
| `async` логика + UI state в одном файле | application vs presentation | сервис + тонкий VM | не Extract Class без границы |

### C. HCI / UX → implementation

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| «Неудобно», «не видно», «запутано» | эвристики Nielsen/Norman | `playbook-hci-core-v1` | не переименовывать 30 классов |
| Плотность информации, overview | progressive disclosure | HCI + структура overview-сущностей | не всё в один scroll |
| Тексты кнопок, ошибки, тон | `kb-russian-language-rules-v1` при RU | copy в ресурсах | не law/psychology без матрицы культуры |
| IDE / dock / панели как продукт | `kb-ide-dx-literature-evidence-v1` | Avalonia dock playbook | не aviation regs |

### D. Aviation metaphors → IDE (Cascade)

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| PFD/MFD/«главный индикатор» | фокус внимания, scan path | `kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1` + HCI | не буквальные приборы в UI |
| CRM / cross-check | второй источник перед commit | git + review playbook | не бюрократия на каждый typo |
| TEM / go-around | откат неудачного UI-рефакторинга | ветка, маленькие коммиты | не «продолжать ломать» |

См. ADR 0021 Cascade IDE при привязке к продукту.

### E. Engineering evidence → design order

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| «Code Complete», McConnell | стиль и дефекты **после** структуры | `kb-engineering-evidence-v1` § OOA&D | не McConnell вместо noun/verb |
| GoF / паттерны | Polymorphism, Creator после CRC | `kb-ooad-fundamentals-v1` | не Singleton «на всякий» |
| Refactoring book | механические переносы **после** границ типов | Roslyn refactorings | не Move Method в god-class |

### F. Stack / tooling (не путать со структурой)

| Источник | Переносимое ядро | Целевой артефакт | Boundary check |
|----------|------------------|------------------|----------------|
| Avalonia version / Dock / theme JSON | status + avalonia playbook | csproj + `Themes/` | не OOA&D |
| `dotnet build` fail | build log + Roslyn | MCP build | не новая иерархия пакетов |
| Partial class / DependentUpon | `roslyn_sync_dependent_upon_partials` | csproj hygiene | не domain model |

---

## Load order when matrix fires

1. `worlds/software-authoring/status-software-authoring-v1.md`
2. **Эта матрица** — выбрать строку Fast symptom router.
3. Целевой **playbook** (OOA&D operational, nouns-verbs, HCI, Avalonia, Roslyn, Git — одна главная).
4. Один **kb** только под явный вопрос (теория GRASP, Avalonia fundamentals, …).
5. При смешении миров (текст UI + структура): **два playbook максимум**, не весь корпус.

---

## Non-transfer zones

- **HCI-эвристика → имена классов:** «понятнее» не значит `ManagerHelperUtils`.
- **Aviation regulation → обязательный процесс разработки:** только метафоры внимания.
- **DDD buzzwords → папки без сущностей:** сначала словарь домена (шаг 1 OOA&D).
- **Git hygiene → архитектура:** коммиты не заменяют слои.
- **Один успешный рефакторинг в репо A → тот же cut-paste в модуль B** без snapshot/compositor в B.
- **Визуальный референс (скрин макета) → поля без доменного имени:** назвать сущность, потом пиксели.

---

## Agent checklist (перед коммитом структурного рефакторинга)

- [ ] Словарь существительных/глаголов явно согласован с snapshot/compositor.
- [ ] Нет нового `switch` по kind для разной **формы** UI.
- [ ] Control/оркестратор < ~300–400 строк или обоснован в ответе.
- [ ] `roslyn_get_diagnostics` по затронутым `.cs` — errors = 0.
- [ ] HCI-требования (если были) отражены в layout, не только в цвете.

---

## Validation snapshot v1

- Матрица наиболее полезна при **смешанных** запросах («карточки как в референсе» + рост `ChatPanelViewModel`).
- Ложное срабатывание: полный OOA&D на однострочный CSS-цвет — отсекается Fast symptom router.
- Следующее расширение v1.1: строки для `software.ml-applied` (OCR/barcode UI), `software-integration-kb`, тестовые контуры (xUnit → не redesign).

## Related

| Документ | Роль |
|----------|------|
| `playbook-ooad-agent-operational-v1.md` | 7 шагов |
| `playbook-domain-nouns-verbs-decomposition-v1.md` | быстрый контракт |
| `index-knowledge-router-supplement-v1.md` | `router-software-transfer-matrix` |
| `agent-notes.md` | `software-cross-domain-transfer-stub-v1`, `route-context-hints-v1` |

<!-- markdownlint-enable MD060 -->

<!-- section:language-world-resolution-v1 -->
## Language, tooling & UI resolution (шаг −1 / −2)

**Карта:** `kb-software-authoring-language-worlds-v1.md`

| Шаг | Сигнал | World tag |
|-----|--------|-----------|
| −1 | синтаксис, idioms, async, nullable | `software.authoring.dotnet.csharp` |
| −1 | **CSxxxx, analyzer, code action, rename, symbol, `roslyn_*`** | `software.authoring.dotnet.tooling.roslyn` |
| −1 | `composer.json` / `.php` | `software.authoring.php` |
| −2 | `Avalonia.*`, `*.axaml` | `…csharp.desktop-ui.avalonia` |
| −2 | `UseWPF` / WinForms / MAUI | `…desktop-ui.wpf` / `.winforms` / `.maui` |

**Roslyn ≠ C#:** диагностика и рефакторинг через MCP — **tooling.roslyn**; не смешивать с OOA&D и не считать «частью языка».

**Порядок:** authoring + matrix → csharp **и/или** tooling.roslyn → desktop-ui.* → HCI.
<!-- /section:language-world-resolution-v1 -->

