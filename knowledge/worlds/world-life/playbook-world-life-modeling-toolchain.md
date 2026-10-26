---
type: Playbook
title: World-life modeling toolchain v1
description: 'Перенесено из `agent-notes.md`. Связь: `world-life-meta-v1`, `world-life-router-playbook-v1` в `map-world-life-subworlds.md`.'
tags: [living, playbook, world-life, worlds]
world: world
subworld: life
status: stable
sections: [model-building-playbook-v1, model-validation-checklist-v1, modeling-errors-catalog-v1, modeling-foundations-v1, n-why-stop-criterion-v1, ontology-router-v1, representative-model-scaling-v1, complexity-taxonomy-v1]
---
# World-life modeling toolchain v1


Перенесено из `agent-notes.md`. Связь: `world-life-meta-v1`, `world-life-router-playbook-v1` в `map-world-life-subworlds.md`.

---
<!-- section:model-building-playbook-v1 -->
## Model Building Playbook v1

Marker: MODEL-BUILD-PLAYBOOK-ACTIVE

1) Goal: какое решение поддерживает модель.
2) Scale: полный масштаб или репрезентативная малая модель.
3) Type: causal/system/probabilistic/agent/scenario.
4) Assumptions: явные допущения.
5) Variables: 3-7 ключевых переменных.
6) Relations: причинные связи, задержки, feedback loops.
7) N-Why: пройти до practical/fundamental stop.
8) Action-now: минимальный интервенционный шаг.
9) Metric-72h: чем проверяем эффект.
10) Encode: зафиксировать результат в KB.

Output:
- goal
- scale
- model_type
- assumptions
- variables
- causal_map
- n_why_root
- action_now
- metric_72h
- boundary_conditions
- next_iteration
<!-- /section:model-building-playbook-v1 -->

<!-- section:model-validation-checklist-v1 -->
## Model Validation Checklist v1

Marker: MODEL-VALIDATION-CHECKLIST-ACTIVE

A) Structure
- цель ясна
- уровни не смешаны
- допущения явные
- границы применимости есть

B) Causality
- связь с механизмом, не только корреляция
- корректное направление влияния
- учтены задержки/обратные связи

C) Operations
- есть action-now
- есть metric-72h
- есть stop/revisit criterion

D) Safety/Ethics
- не растет психологический вред
- не усиливается стигма
- растет субъектность

Decision:
- PASS
- PASS WITH RISK
- REWORK
<!-- /section:model-validation-checklist-v1 -->

<!-- section:modeling-errors-catalog-v1 -->
## Modeling Errors Catalog v1

Цель: быстро распознавать типовые ошибки моделирования.

### E1. False precision
- Симптом: много цифр, мало реальной предсказательной силы.
- Фикс: упростить модель и усилить валидацию.

### E2. Level collapse
- Симптом: психология объясняется только биологией или наоборот.
- Фикс: развести уровни и добавить cross-level связи.

### E3. Overfitting to anecdote
- Симптом: модель держится на одном ярком кейсе.
- Фикс: проверить на минимум 2-3 контекстах.

### E4. Correlation as causation
- Симптом: действие не меняет результат, хотя "корреляция была".
- Фикс: описать механизм и найти интервенционный рычаг.

### E5. Missing delay
- Симптом: преждевременный вывод "не работает".
- Фикс: добавить ожидаемую задержку эффекта в метрику.

### E6. Boundary blindness
- Симптом: перенос 1:1 в другой масштаб/среду ломает результат.
- Фикс: явно указать boundary conditions перед переносом.

### E7. Analysis paralysis
- Симптом: бесконечные why без действия.
- Фикс: применять N-Why stop criterion + probing-step.

### E8. Ethical drift
- Симптом: модель оптимизирует KPI ценой человека.
- Фикс: включить safety/agency check как блокирующий гейт.

### Canon check
Перед выпуском: пройти `model-validation-checklist-v1`.
<!-- /section:modeling-errors-catalog-v1 -->

<!-- section:modeling-foundations-v1 -->
## Modeling Foundations v1

Scope: world-life / world-human-system / world-socio-technical / N-Why.

### Что такое модель

Модель — это упрощённое представление реальности для конкретной цели.
Она не "истина", а рабочий инструмент:
- объяснять,
- предсказывать,
- выбирать действие,
- снижать трение в решениях.

Формула:
`модель = цель + допущения + переменные + связи + границы применимости`.

### Зачем моделировать

- уменьшаем шум и количество нерелевантных деталей;
- делаем reasoning явным и проверяемым;
- быстрее находим рычаг действия;
- не тонем в нюансах полного масштаба.

### Классы моделей (минимальная таксономия)

1) Causal (причинные)
- Что на что влияет и через какой механизм.

2) System / feedback (системные)
- Петли обратной связи, задержки, накопители.

3) Probabilistic (вероятностные)
- Работа с неопределённостью и рисками.

4) Agent-based (агентные)
- Поведение участников и эффекты взаимодействия.

5) Scenario / decision (сценарные)
- Сравнение вариантов действий и последствий.

### Качество модели (4 критерия)

- Explainable: понятно, почему модель так устроена.
- Predictive: хотя бы частично предсказывает наблюдаемый эффект.
- Actionable: подсказывает конкретный следующий шаг.
- Transferable: переносится между близкими контекстами с явными поправками.

### Boundary conditions (границы)

Обязательно фиксировать:
- где модель работает;
- где модель ломается;
- какие допущения критичны;
- какие параметры масштаб-зависимы.

### Связь с N-Why

N-Why без модели легко уходит в риторику.
Модель задаёт ось причинности и stop-condition:
- practical stop (explainable+actionable+measurable),
- fundamental stop (достигнут неснимаемый предел).

### Canon rule

Сначала `representative-model-scaling` (если сложность высокая),
потом перенос на полный масштаб.
<!-- /section:modeling-foundations-v1 -->

<!-- section:n-why-stop-criterion-v1 -->
## N-Why Stop Criterion v1

Marker: N-WHY-ACTIVE

### Dual stop logic
Почемучка останавливается по одному из двух условий:

A) Practical stop (операционный)
- explainable,
- actionable,
- measurable (24-72h).

B) Fundamental stop (фундаментальный)
- цепочка дошла до фундаментального ограничения,
- ограничение не снимается в текущем контуре действий,
- следующий шаг: адаптация стратегии под границу, а не попытка "продавить" её.

### Hard guard
- максимум 7 why per cycle;
- если на 7-м шаге нет stop-condition -> probing-step и новый цикл.

### Notes
- Fundamental stop приоритетнее: если достигнута предельная граница (physics/logic/irreducible constraint), дальнейшие why в той же оси бессмысленны.
- Пример: цепочка про скорость -> предел скорости света в вакууме.

### Output template
- stop_type: practical | fundamental
- root_constraint: ...
- action_now: ...
- metric_72h (if practical): ...
- adaptation_strategy (if fundamental): ...
<!-- /section:n-why-stop-criterion-v1 -->

<!-- section:ontology-router-v1 -->
## Ontology Router v1 (open issue)

Status: NOT solved by scope split alone.

Core point:
- scopes are operational partitions, not ontology.
- ontology must support overlapping facets, not hard class buckets.

Working model:
- represent context as weighted facets (not max-N domains).
- example facets: professional, personal, reflective, cultural, procedural, relational.
- task routing uses relevance weights + required evidence type.

Decision rule:
1) identify task intent and evidence type,
2) select facet mix by weight,
3) choose toolchain from facet mix,
4) run with "quick-fix, ontology-pending" flag only when time-critical.

Constraint:
- never treat "scope=current" as equivalent to "ontology resolved".
<!-- /section:ontology-router-v1 -->

<!-- section:representative-model-scaling-v1 -->
## Representative Model Scaling v1

Scope: world-life / N-Why / сложные темы с высоким числом нюансов.

### Принцип
Если анализ в реальном масштабе тонет в нюансах,
сначала строим репрезентативную модель малого масштаба,
где причинно-следственные связи обозримы.

Коротко: `compress -> understand -> transfer`.

### Зачем
- снижает когнитивный шум;
- ускоряет выявление фундаментальных ограничений;
- помогает отличить главное от второстепенного;
- даёт проверяемую основу до масштабирования.

### Базовый протокол
1. Выбрать ось явления (что именно объясняем).
2. Ужать масштаб до обозримого полигона (пример: 1 кв. км).
3. Зафиксировать минимальный набор сущностей и связей.
4. Прогнать N-Why в малой модели до stop-condition.
5. Проверить переносимость на большой масштаб.
6. Отметить, где перенос ломается (boundary conditions).

### Виды stop-condition в малой модели
- practical stop: explainable + actionable + measurable.
- fundamental stop: достигнут неснимаемый предел (physics/logic/irreducible).

### Правила переноса
- Не переносить автоматически 1:1.
- Явно фиксировать, какие параметры инвариантны, а какие масштаб-зависимы.
- При расхождении: обновить модель, а не "докручивать" объяснение.

### Антипаттерны
- сразу идти в полный масштаб и тонуть в частностях;
- выбирать модель слишком маленькой, теряя ключевую динамику;
- принимать удобную модель за истину без проверки переноса.

### Канонический пример
- Ось: предел скорости.
- Малая модель: причинная цепочка в упрощенной физической рамке.
- Stop: фундаментальное ограничение — скорость света в вакууме.
- Дальше: адаптация стратегии, а не бесконечная Why-цепочка в той же оси.
<!-- /section:representative-model-scaling-v1 -->

<!-- section:complexity-taxonomy-v1 -->
## Complexity Taxonomy v1 (истинная / наложенная / индуцированная)

**Status:** accepted
**Provenance (оригинал формулировки):** оператор (Света), 2026-07-29 01:40 UTC+3, Cursor-сессия `7d5e5947-05c9-4911-83e0-1a3c9f857e3a` (архив: `cursor-agent-transcripts-archive/PersonalCursorFolder/7d5e5947-.../…jsonl`, строка 379; ответы агента — строки 380, 382). Канонизация в KB: 2026-09-17, диалог оператор ↔ dsh (эхо). Контекст оригинала: инвариант «система стремится к снижению затрат когнитивного ресурса»; теории заговора как типичный случай индуцированной сложности.
**Связь:** `n-why-stop-criterion-v1` · `modeling-errors-catalog-v1` (E1, E7) · Solomonoff / MDL (теоретический предел того же принципа)

### Формулировка (близко к тексту оригинала)

Сложно — да, но нужно различать три вида сложности:

1. **Истинная** — которую как не прячь — не спрячешь. Сложность минимального генератора явления. Пример (оригинальный): игра Жизнь — сложные комбинации и целые миры? Да. **Истинная сложность — 1 правило.**
2. **Наложенная** — «фабрики фабрик фабрик» и прочий оверинжиниринг поверх реальной (истинной) сложности. Источник: **производство** (проектировщик/инженер).
3. **Индуцированная (наведённая)** — «о… ну это не может быть просто…» — и сделал кучу всего, хотя на самом деле просто. Источник: **восприятие** (наблюдатель, не поверивший в простоту). Типовые случаи: сложная теория глайдеров у наблюдателя без правил (Game of Life); теории заговора («кому это выгодно» — куча построений там, где просто).

### Формулы-спутники (агент, та же сессия)

- «Боятся истинной, живут в наложенной и сами же плодят индуцированную».
- **«Не уважать сложность, а спросить — какая из трёх»** (первый вопрос спуска в N-Why по теме сложности: не «сложность ли это», а «чья сложность»).
- «Не подумал сейчас — потом платишь наложенной и индуцированной сложностью» (экономика: пропущенное различение как накопительный процент).
- «Жизнь Конвея — идеальный мем: миры сложные, закон — крошечный».

### Свойства классов

- Эмерджентные миры (сложные конфигурации из простых правил) — **не отдельный вид сложности**, а производные истинной: их траекторная длина описания может быть огромна (computational irreducibility), но это стоимость наблюдения траектории, не «сложность мира».
- Наложенная и индуцированная — **два разных канала** появления искусственной сложности: производство vs восприятие. Классифицируется по источнику добавления, а не по месту обитания.

### Тесты различения (2026-09-17, диалог с dsh)

1. **Тест генератора:** исчезает ли сложность при описании правила вместо траектории? → производная от истинной, не отдельный вид.
2. **Тест стопа:** дошёл ли спуск why до неснимаемого предела? → истинная.
3. **Тест действия:** меняет ли удаление слоя предсказание/действие? Нет → наложенная или индуцированная.
4. **Тест источника:** кто добавил? проектировщик артефакта → наложенная; наблюдатель при прочтении → индуцированная.
5. **Тест дна:** «фундамент» отвечает на вопрос или имитирует ответ? → fake bottom ≠ fundamental (заглушку за основание не принимать).

### Маппинг на стек

- Истинная ↔ `fundamental stop` в `n-why-stop-criterion-v1`
- Наложенная ↔ `modeling-errors-catalog-v1`: E1 false precision, E7 analysis paralysis (канал производства)
- Индуцированная ↔ fake-bottom guard + prior «не может быть просто» (канал восприятия); см. R10 false-depth recognition (`personal/recognition-history/map-recognition-concepts.md`) — родственный механизм: слова совпали, домены разные.
- Смешение классов ↔ E2 level collapse

### Антипаттерн

Дороговизна описания ≠ истинность сложности. Истинная подтверждается границей (предел/теорема/неснимаемый constraint), а не усталостью описывающего. Индуцированная сложность — самый дорогой из трёх видов: она расходует когнитивный ресурс наблюдателя бесконечно, потому что её «объяснение» не имеет стопа.

<!-- /section:complexity-taxonomy-v1 -->

