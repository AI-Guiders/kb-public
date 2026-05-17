# Playbook: существительные → сущности, глаголы → методы v1

**Назначение:** общий принцип декомпозиции кода и UI-рендеринга для агента. Не привязан к одному модулю (чат, Skia, MCP). **Связь:** `worlds/software-authoring/code-writing-principles-v1.md` (инженерные принципы), домен **software.authoring**.

**Версия:** v1.0 · 2026-05-17 — зафиксировано после рефакторинга Cascade IDE chat surface (`SkiaChatMessage`, `SkiaChatConfirmation`, `SkiaChatTopicCard` вместо `ItemKind` + god-`switch`).

---

## Контракт (одна строка)

**Существительные в предметной области = именованные типы (сущности). Глаголы = методы этих сущностей (или сервисов), а не ветки в одном процедурном методе.**

---

## Когда применять (триггеры)

- В задаче или в коде фигурируют **отдельные понятия** (сообщение, тема, уточнение, карточка, заказ, сессия) — до правки пикселей/логики спросить: **есть ли тип?**
- Появляется **второй** `if` по `kind` / `type` / `enum` для **разной формы** одного слоя (отрисовка, layout, hit-test) → **новая сущность**, не ещё одна ветка.
- Файл control/presenter/renderer **растёт** за счёт `switch` по дискриминатору — вынести **сущности + Measure/Draw** (или аналог), control оставить оркестратором.
- Задача сформулирована как «сделать визуал X» — **сначала** модель сущностей из домена (уже есть в snapshot/DTO/compositor), **потом** отрисовка.

---

## Правила

### 1. Существительные → сущности

| В речи / домене | В коде (плохо) | В коде (хорошо) |
|-----------------|----------------|-----------------|
| Сообщение | `ItemKind.Message` + поля в общем record | `Message` / `SkiaChatMessage` с `Title`, `Text`, … |
| Уточнение | `Kind == Confirmation` | `Confirmation` |
| Карточка темы | `TopicCard` как enum-ветка | `TopicCard` как класс: `Measure`, `Draw` |
| Режим «в фокусе» | ещё один `Accent` | поле сущности `IsFocused` или подтип |

**Прилагательные и статусы** (`pending`, `active`, `focused`) — поля или малые value-объекты у сущности, не размытый `string Accent` на всё подряд.

### 2. Глаголы → методы

| Действие | Плохо | Хорошо |
|----------|-------|--------|
| Измерить высоту | 80 строк в `BuildLayout` с `switch` | `entity.Measure(context)` |
| Нарисовать | `DrawOperation` с ветками по kind | `entity.Draw(context, top, layout)` |
| Открыть тему | флаг в общем hit | `CreateHit()` у сущности / явный `SelectThreadId` в hit-модели |

Оркестратор (control, scene builder) **не знает деталей** отрисовки каждого вида — только цикл по `ISkiaChatEntity` / списку полиморфных сущностей.

### 3. Слои

1. **Домен / snapshot** (уже есть: `ChatSurfaceEntry`, `ChatThreadOverviewItem`) — источник истины по данным.
2. **Сцена / presentation** — `SceneBuilder` собирает список сущностей UI-слоя.
3. **Сущность** — layout + draw + hit.
4. **Control** — scroll, theme, input, цикл `foreach (placed) entity.Draw(...)`.

Не смешивать шаги 3 и 4 в одном классе на сотни строк.

### 4. Анти-паттерн «быстрое закрытие задачи»

RLHF и короткие сессии толкают к **патчу в существующий switch** — задача закрыта, структура отложена. Этот playbook — **явный стоп-кран**: если сущность названа в домене, она должна появиться в коде слоя отображения **до** тюнинга цветов и отступов.

---

## Быстрый чеклист перед коммитом

- [ ] Каждое **существительное** из UI/домена имеет **тип** (класс/record), а не только значение enum.
- [ ] Каждый **глагол** (measure, draw, hit, open, send) — **метод**, а не очередная ветка `if (kind == …)`.
- [ ] Второй похожий `kind` в одном renderer → вынос в сущность или shared helper **с именем домена**, не «ещё case».
- [ ] Control / ViewModel **&lt; ~300–400 строк** на оркестрацию; детали — в сущностях и builder.

---

## Пример (Cascade IDE, chat Skia)

**Было:** `ItemKind`, `ItemSnapshot`, `SkiaChatLayout.BuildLayout` + `DrawOperation` с `switch` по kind.

**Стало:**

- `SkiaChatSceneBuilder` → `Message`, `Confirmation`, `TopicCard`, …
- `ISkiaChatEntity`: `Measure`, `Draw`, `CreateHit`
- `SkiaChatSurfaceControl` — только theme, scroll, hit-test, цикл отрисовки

См. `cascade-ide/Views/Chat/Skia/`.

---

## Связанные документы

- `worlds/software-authoring/code-writing-principles-v1.md` — SOLID, узкие типы, композиция
- `worlds/hci-ux-dx/playbook-hci-core-v1.md` — когда трогать UI/UX
- `worlds/software-dotnet-avalonia/playbook-avalonia-dock-ui-v1.md` — Avalonia/Skia в Cascade IDE

<!-- section:ooad-foundation -->
## Фундамент: OOA&D

Этот playbook — **сжатая операционная выжимка** классического **объектно-ориентированного анализа и проектирования** (noun/verb analysis, CRC, GRASP).

| Слой | Файл |
|------|------|
| Теория и источники (Larman, UML, связь с DDD/GoF) | `kb-ooad-fundamentals-v1.md` |
| Пошаговый проход для агента (7 шагов) | `playbook-ooad-agent-operational-v1.md` |
| Статус домена | `status-software-authoring-v1.md` |

**Правило:** при новой подсистеме или рефакторинге renderer — сначала **операционный OOA&D-проход**, затем этот чеклист при коммите.
<!-- /section:ooad-foundation -->
