---
type: Note
title: 'Note: Dialogue Δ — эффективность диалога и round-trip economy (v0)'
description: '**Domain:** agent-operations'
tags: [agent-operations, dialogue-delta, domains, ssot, note, research, living]
language: ru
---
# Note: Dialogue Δ — эффективность диалога и round-trip economy (v0)

**Domain:** agent-operations  
**Статус:** research / living — **не** Accepted product ADR  
**Дата:** 2026-07-18  
**Provenance:** оператор + агент — после ADCM Partition (ADR 0175); фокус: токены и время, не «ещё одна конституция»  

**Связь:**

- ADCM — [`playbook-agent-driven-context-management.md`](playbook-agent-driven-context-management.md)
- Partition continuity — cascade-ide ADR [0175](https://github.com/AI-Guiders/cascade-ide/blob/develop/docs/adr/0175-adcm-partition-continuity-pair-and-message-anchors.md) (TopicDecisions слот **New**)
- **CIG digest (фундамент):** [`note-cig-conversational-information-gain.md`](note-cig-conversational-information-gain.md) — Chen et al. arXiv:2604.15647
- **Inquiry Mode sketch:** [`note-inquiry-mode-information-graph.md`](note-inquiry-mode-information-graph.md) — режим как Debug; IG на PFD, \(I\) на MFD, диалог Forward
- **Historiography SEE/KBSA/IBIS:** [`../../work/projects/door-to-singularity/cascade-ide/note-cognitive-se-environments-historiography.md`](../../work/projects/door-to-singularity/cascade-ide/note-cognitive-se-environments-historiography.md)
- SEDM Evaluate — cascade-ide ADR 0174
- Intent card — ADR 0173
- Checkpoint/export — [`../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md)
- Pay-per-token harness — ADR 0166

---

## Одна строка

**Взаимодействие осмысленно ⇔ появилось что-то новое (Δ) хотя бы для одной стороны или для артефакта lane; иначе это кандидат в лишний round-trip.**

«Новое» включает сужение и отрицательное знание, не только «добавить в backlog».

Фундамент в литературе: Meadow & Yuan (1997) *change in knowledge base* → CIG (Novelty/Relevance/Scope + semantic memory of claims). См. digest выше.

**Режимы поиска** (см. CIG note, § closed vs open \(H\)): угадайка/verify = closed \(H\) (max split); ветка вроде ADCM = open \(H\) (компас сигнал/ответ, путь в \(Q\times H\) заранее не дан) — local IG + meta-Δ + continuity.

---

## Зачем (токены и время)

На pay-per-token и при длинных agentic-сессиях дорог не только «толстый контекст», но и **ходы без Δ**: уточнения, согласие без содержания, повтор уже Accepted, pressure без тактики, пересказ без якоря.

ADCM режет **объём** контекста (Prevent/Partition/…).  
Dialogue Δ режет **число бесполезных оборотов** и качество Continuity (что писать в TopicDecisions.New).

Это **не** замена ADCM и **не** KPI «максимум решений в час». Это гипотеза механики: *замечать noop и round-trip, где не надо*.

---

## Что считается Δ (черновик таксономии)

| Класс Δ | Смысл | Пример |
|---------|--------|--------|
| **Fact / artifact** | появился проверяемый объект | путь, SHA, измерение, export, якорь |
| **Bound** | явно отклонили | «не silent compact» |
| **Invariant** | явно приняли | dual-channel A+B |
| **Angle / question** | новый вопрос или угол | «два файла Decisions+ops» |
| **Negative knowledge** | зафиксировали незнание | «не знаем wire schema — spike» |
| **Reframe** | та же тема, другая рамка | executor≠role, phase of one cycle |
| **Noop** | хода нет | пересказ Accepted; «ок» без сдвига; повтор без тактики |

**Не Δ (обычно):** вежливость без содержания; повтор inject без выбора 5P; ops-список без сдвига Frame/Rejected/Accepted/New.

---

## Гипотеза механики (ещё обсуждать)

### После закрытого хода

Микро-слот (агент или оператор, коротко):

1. **Δ?** — 1–3 пункта *что изменилось* **или** явно `noop` / `refine-only`.
2. Опционально **якорь** (message_id / export span) — иначе «новое» легко врёт.
3. Питает TopicDecisions.New при Partition/Persist (ADR 0175).

Смотреть на **закрытый** ход, не на каждое слово (молчание / «думаю» могут готовить Δ).

### Round-trip economy — что детектить

| Сигнал (кандидат) | Подозрение |
|-------------------|------------|
| N ходов подряд с `noop` / refine-only | кружение; предложить смену угла, Partition, Persist или stop |
| Вопрос, ответ на который уже в Accepted | лишний RT; указать якорь / Decisions |
| Уточнение без смены Frame | возможно дешёвый канал (одна реплика) вместо полного agent turn |
| Pressure inject → только prose без тактики | ADCM miss; дорогой оборот без Δ |
| Повтор одного и того же clarification | clarification debt; свернуть в batch [0031] или в карточку |

Количественные пороги (**TBD**, не фиксировать в v0):

- `noop_streak` (ходы)
- доля ходов с якоренным Δ за topic
- медиана tool-calls на Δ (грубо)
- токены prompt+completion на последний якоренный Δ

Пороги и формулы — предмет следующих обсуждений; v0 фиксирует **идею счётчиков**, не цифры.

### Кто считает

| Кто | Роль |
|-----|------|
| **Агент** | честно маркирует Δ / noop; не притворяется продуктивностью |
| **Harness** | опционально telemetry (streak, pressure→no-tactic); **не** silent rewrite |
| **Оператор** | калибрует «это был нужный refine» vs «кружим» |

Оценка может быть **качественной** (метка noop) раньше, чем количественной (токены/Δ). Смешивать рано.

---

## Связь с Continuity pair (0175)

| Слой | Dialogue Δ |
|------|------------|
| TopicDecisions.New | каноническое место накопленного Δ lane |
| Handover ops | не место для Δ-смысла; только если ops *сам* новое (появился SHA) |
| Export + anchors | доказательная база «эта фраза = этот Δ» |

Default Partition: сначала выводы (в т.ч. New), потом ops — иначе снова «записка на подушке».

---

## Открытые вопросы (сознательно не закрыты)

1. Пороги `noop_streak` и единица «хода» (user turn? agent turn? tool round?).
2. Как не наказать законный refine / Socratic ход?
3. Нужен ли UI chip «Δ / noop» в Intercom или достаточно discipline + TopicDecisions?
4. Связь с intent card (0173): каждая карточка = Δ? или карточка ⊃ несколько Δ?
5. Авто-оценка Δ моделью vs только явная метка агента/оператора (стоимость vs честность).
6. Cursor vs CIDE: одинаковая норма, разный telemetry.
7. Не превратить Δ в toxic productivity — критерий *осмысленности*, не *скорости*.

---

## Анти-паттерны

- KPI «больше Δ любой ценой» (мусорные «новые» факты).
- Наказывать паузу мышления как noop.
- Подменять ADCM (объём контекста) одним только Δ (число оборотов).
- Считать silent host summary за Δ.
- Писать New без якоря, когда спор о формулировке вероятен.

---

## Критерий заметки (пока)

Оператор и агент могут сказать: *«Есть отдельная research-заметка: осмысленность хода ↔ Δ; лишний round-trip надо уметь замечать; цифры и UI — ещё обсуждать»* — и указать этот файл + ADCM + 0175.

