# CASE (Computer-Aided Software Engineering) — fundamentals v1
**Tags:** #software-case-workbench #kb #worlds #case #uml #mda #rose

**Назначение:** что такое CASE как класс продуктов и идей, что дошли до рынка, почему волна спала, что осталось жить — без ностальгии по UML-диаграммам ради диаграмм.

**Статус:** v1, справочно. **epistemic_basis:** synthesis + industry consensus; детали вендоров — `inference` где не цитирован первоисточник.

**Связь:** [`map-case-reading.md`](map-case-reading.md) · [`matrix-case-to-guiders-transfer.md`](matrix-case-to-guiders-transfer.md)

---

## 1. Одна строка

**CASE** — desktop-class **workbench** для разработки ПО через **явную модель системы** (структура, поведение, зависимости, иногда процесс), с **несколькими синхронизированными видами**, **traceability** артефактов и обещанием **round-trip** между моделью и кодом. Rational Rose — иконический продукт волны; класс шире одного вендора.

---

## 2. Словарь

| Термин | Смысл |
|--------|--------|
| **Upper CASE** | Анализ и проектирование **до** кода: requirements, structure, behavior, interfaces |
| **Lower CASE** | Генерация, тесты, рефакторинг, reverse engineering **из/в** модель |
| **I-CASE** | Интеграция upper+lower через общий **repository** и lifecycle |
| **Workbench** | Длинная сессия, графы, drill-down, review-before-commit — не dashboard tile |
| **Round-trip** | Изменение в модели → код; изменение в коде → модель (синхронизация) |
| **4+1 views** (Kruchten) | Logical, Development, Process, Physical + Scenarios — multi-view на одну систему |
| **MDA** (OMG, ~2000s) | Model-Driven Architecture: PIM → PSM → code через transforms (CASE 2.0) |
| **ALM** | Application Lifecycle Management — то, куда **утекли** traceability и workflow после CASE |

---

## 3. Хронология (сжато)

| Эпоха | Что произошло |
|-------|----------------|
| **1970s–80s** | Structured methods; первые diagram tools; **Stoneman/APSE**, IPSE — интеграция инструментов (см. historiography B) |
| **1980s–90s** | **ICASE** конференции; OOAD: Booch, Rumbaugh (OMT), Jacobson (OOSE) |
| **1997** | **UML 1.x** — унификация нотаций (OMG) |
| **1990s–2000s** | **Rational Rose**, Together, Paradigm Plus, Select, erwin (данные), RequisitePro (требования) |
| **2003** | IBM покупает Rational — пакет RUP + tools |
| **2000s** | **MDA**, MOF, XMI — мечта machine-readable transforms между слоями |
| **2001+** | **Agile Manifesto** — удар по big design upfront и «модель как gate» |
| **2010s+** | Массовый рынок → **IDE + git**; ниши: Sparx EA, IBM Rhapsody, Archetyx, SysML, regulated SE |

**Параллельная ветка (не синоним CASE, но родня):** KBSA/KBSE — intelligent assistant + repository (см. historiography A). К ~1990 KBSE встроили в CASE-нарратив («KB внутри workbench»).

---

## 4. Что CASE реально дал индустрии

| Достижение | Где живёт сегодня |
|------------|-------------------|
| **Визуальная архитектура** как дисциплина | Architecture reviews, C4, dependency graphs (часто не UML) |
| **Multi-view** | 4+1, viewpoints, «diagram для аудитории» |
| **Traceability** requirement ↔ design ↔ code ↔ test | ALM (Jira links), compliance packs |
| **Component / module thinking** | Packages, bounded contexts, microservices (другая нотация) |
| **Reverse engineering** | IDE structure view, Roslyn, dependency audits |
| **Нотация UML** | Ограниченно: sequence/class в доках; не source of truth в agile |
| **Process templates** | RUP light → Scrum/Kanban (процесс без Rose DB) |
| **Desktop workbench posture** | Всё ещё норма для CAD/CASE-class задач (см. friction-book ch.24) |

---

## 5. Почему волна спала (главные убийцы)

1. **Model–code drift** — модель устаревала быстрее, чем её обновляли; «врущие обои».
2. **Ceremony tax** — диаграммы ради gate, не ради мышления.
3. **Round-trip failure** — codegen хрупкий; reverse eng неполный; merge hell.
4. **Agile** — working software over comprehensive documentation.
5. **Vendor lock-in** — proprietary repository (Rose DB) vs git.
6. **Wrong default** — model as SSOT **вместо** code; в реальности code победил.
7. **Web/demo channel** — продавали лёгкую витрину; production осталась на desktop, но без честной модели.

**Не причина провала:** идея «видеть систему целиком перед ship» — она осталась, сменила нотацию и инструменты.

---

## 6. Где CASE **не** умер

| Домен | Почему модель жива |
|-------|---------------------|
| **Safety-critical** (авионика, медицина, automotive) | Сертификация требует traceability |
| **Embedded / realtime** | Rhapsody, state machines, code gen под стандарт |
| **Enterprise architecture** | Sparx EA, ArchiMate — governance, не daily dev |
| **Data modeling** | ER tools → schema migrations (другой слой CASE) |
| **Platform / fleet ops** | Много репо, политики, pins — **estate** снова не помещается в один IDE buffer |

---

## 7. CASE vs соседние классы

| Класс | Фокус | Отличие от CASE |
|-------|--------|-----------------|
| **IDE** | Edit buffer, LSP, debug | Один проект; слабый estate |
| **ALM** | Tickets, pipeline, links | Workflow; слабый live model |
| **Code graph / ADE** | Retrieval, agents, diff | Исполнение; слабый decision environment |
| **KBSA assistant** | Transform rules, proof | Ближе к codegen; мало deliberation UI |
| **CASE workbench** | **Vision + decision** на estate | Модель, views, impact, review session |

Guiders **CASE pillar** = Vision/Decision Environment для protocol estate, не «ещё один UML editor».

---

## 8. AI era — почему час мог настать

| Rose-era bottleneck | AI-era counter |
|---------------------|----------------|
| Human draws model | Agent + generated manifests maintain vectors |
| Drift undetected | Conformance CI, adoption drift gates |
| NL ↔ formal failed | Machine specs (`*.spec.json`) + tests, not NL→UML |
| Capture tax (IBIS) | Pain→ADR promote; briefing not separate Compendium |
| One architect | High throughput pair + hygiene |

**Риск повторить провал:** снова сделать модель **декорацией** без enforced sync. **Антидот:** SSOT under test, not hand-curated diagram.

---

## 9. Минимальный канон (читать дальше)

См. [`map-case-reading.md`](map-case-reading.md): Kruchten 4+1, Brown IPSE mistakes, Finkelstein ICASE, OMG UML/MDA (критически), agile postmortems, modern ALM lessons.

---

## 10. Границы этой карточки

- Не каталог вендоров 2026.
- Не учебник UML notation.
- Не замена ADR-0023 — продуктовая норма в guiders-platform.

