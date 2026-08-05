# Note: Conversational Information Gain (CIG) — фундамент для Dialogue Δ (v0)
**Tags:** #agent-operations #domains #note #research


**Domain:** agent-operations / dialogue-research  
**Статус:** research digest — **не** product ADR  
**Дата:** 2026-07-18  
**Источник:** Chen, Lau, Frermann — *CIG: Measuring Conversational Information Gain in Deliberative Dialogues with Semantic Memory Dynamics* (arXiv:2604.15647; ACL Long 2026). Code/data: https://github.com/mrknight21/memcig-analysis  

**Связь:** [`note-dialogue-delta-effectiveness-v0.md`](note-dialogue-delta-effectiveness-v0.md) · ADCM · ADR 0175 (TopicDecisions.New) · SEDM Evaluate

---

## Одна строка

**CIG = насколько реплика двигает общее понимание цели/темы**, измеряемое относительно **уже сказанного** (semantic memory of claims), а не относительно вежливости, длины или TF–IDF.

Корневая цитата (Meadow & Yuan, 1997): information impact = *change in the knowledge base of the recipient* — почти дословный фундамент нашего Dialogue Δ.

---

## Зачем бумага (их проблема)

Классические метрики deliberation (DQI, civility, argument structure) ловят **форму**, не **информационный прогресс**:

- цивильно можно топтаться на месте («bureaucratic talk»);
- ценное может вылезти из неформальной реплики.

Нужен критерий: *продвинулось ли коллективное знание по теме?*

---

## Определение и три оси (+ overall)

**CIG (overall, 1–4):** насколько ответ двигает shared understanding / progress toward goal, учитывая prior knowledge + preceding dialogue.

| Ось | Вопрос | 1 → 4 (сжато) |
|-----|--------|----------------|
| **Novelty** | Новое ли относительно уже известного в диалоге? | повтор → нюанс → evidence/пример → новый фрейм/принцип |
| **Relevance** | Насколько связано с целью/темой? | off-topic → косвенно → side issue → прямо в ядро |
| **Implication Scope** | Как далеко обобщает? (deliberation-flavored) | local/procedure → case-bound → generalizing → universal principle |

**Важно из бумаги:**

- CIG ≠ «качество разговора вообще». Coordination / reiteration → низкий CIG, даже если полезны для процесса.
- Novelty **намеренно независима** от Relevance и «величины импакта».
- Scope — **ось стиля deliberation**, не гарантированный драйвер informativeness (см. эмпирику ниже).

### Chi (2009) под шкалой CIG

| CIG level | Концептуальный сдвиг |
|-----------|----------------------|
| 3 Incremental | **assimilation** — детали внутри той же рамки |
| 4 Insightful | **accommodation** — пересборка рамки / новый принцип |

Это прямо ложится на наши классы Δ: Fact/Bound внутри Frame vs Reframe.

---

## Операционализация: Semantic Memory (Mem0-like)

Без представления «что уже установлено» Novelty не измерить. Пайплайн (Fig.1):

```text
utterance
  → Extract atomic claims (LLM; снять hedge/filler; сохранить speaker)
  → Retrieve top-k similar claims (vector)
  → NLI relations: equivalent | forward_entail | backward_entail | contradiction | neutral
  → Action: ADD | UPDATE | NONE  (только same-speaker subset — чтобы не схлопнуть спор)
  → Memory state = контекст для скоринга CIG / осей
```

| Action | Когда |
|--------|--------|
| **ADD** | нет same-speaker кандидатов или только neutral |
| **NONE** | equivalence или backward_entail (уже покрыто) |
| **UPDATE** | contradiction → replace; forward_entail → merge в более specific claim |

**Смысл для нас:** `NONE` ≈ наш **noop** на уровне claim; `ADD/UPDATE` ≈ Δ в knowledge base. Счётчики ADD/UPDATE коррелируют с human CIG лучше длины и surprisal.

---

## Эмпирика (что доказали, без магии)

**Данные:** 80 сегментов × 2 корпуса (INSQ TV-дебаты; FORA community). Аннотация: topic + memory summary + 3 предыдущих реплики (не полный лог).

**Согласие:** Krippendorff α ~0.51–0.67 по осям — moderate-to-high.

**Что объясняет overall CIG (ordinal regression / AIC):**

- **Novelty + Relevance** — основной сигнал.
- **Implication Scope** почти не помогает предсказывать perceived CIG; в INSQ ablation Scope даже чуть лучше. Scope лучше читать как **стиль** (local testimony vs principle), не как «выше = информативнее». Конкретный lived fact (низкий Scope) может быть высокоинформативен.

**Автоскоринг:** GPT-5 при том же контексте, что у людей, MAE сравним / лучше human LOO. Memory summary ≈ full transcript для предсказания CIG (компактная замена истории — важно для токенов).

**Прокси vs memory dynamics (Pearson |r| с human CIG):**

| Сигнал | ~\|r\| |
|--------|------|
| Memory changes (Relevance-gated) | 0.73 |
| Memory changes (Any) | 0.72 |
| Extracted claim count | 0.71 |
| Length / surprisal | ~0.68–0.70 |
| Entity novelty | слабо |

**Conjunctive bottleneck:** лучшая агрегация осей в overall — оператор **min**. Informativeness ограничена **самой слабой** осью: высокая Novelty при Relevance=1 не спасает. На уровне claims — слушают **top salient claims**, не среднее по всем.

**Case study модерации:** CIG как диагностика режима — в дебатах всплеск сразу после moderator act; в community — размазанный набор лагов. Для CIDE: harness pressure / steer ≠ обязан давать мгновенный Δ; зависит от режима.

---

## Limitations (честно из бумаги)

1. Аннотация на **summary + short window** — bias к тому, что попало в memory summary.
2. Ошибки LLM extract / NLI **протекают** в динамику памяти.
3. Один claim → одно действие / одна связь — недоучёт multi-link claims.
4. Два англ. moderated корпуса; не adversarial/polarized во всю силу.

Для agentic IDE это критично: auto-CIG без якорей и без калибровки оператора легко врёт (дорого по токенам и по смыслу).

---

## Карта на наш контур (Dialogue Δ / ADCM / 0175)

| CIG | Наш слой |
|-----|----------|
| Meadow–Yuan change in KB | Dialogue Δ: ход осмыслен ↔ Δ |
| Novelty 1 / memory NONE | noop / refine-only без сдвига Accepted |
| Novelty 3–4 + Relevance ≥3 | Fact / Bound / Invariant / Reframe |
| CIG 3 vs 4 (Chi) | assimilation vs accommodation ≈ детали vs Reframe |
| Implication Scope | **не** копировать слепо в agentic; у нас «импакт» ближе к *артефакт/якорь/решение*, не «universal principle» |
| Semantic memory of claims | TopicDecisions + intent cards + message anchors; не обязательно Mem0 |
| Memory change counts | кандидат на **дешёвый** telemetry round-trip (до LLM-scored CIG) |
| Conjunctive bottleneck | «новое, но off-topic» или «on-topic повтор» = слабый ход; min(Novelty, Relevance) |
| Memory summary ≈ full history | поддержка ADCM Prevent: outline/hot/claims вместо dump чата |
| Low CIG coordination | не наказывать: steering/clarify могут быть нужным процессом при низком CIG |

**Чего у CIG нет (и что нам нужно отдельно):**

- цена токена / round-trip economy;
- Partition continuity (два файла Decisions+ops);
- tool-using agent (Δ в репо/коде, не только в claims диалога);
- явный Rejected/Accepted как типы Δ (у них claims, не decision records).

CIG — **кузен измерения**, не замена ADCM и не wire schema CIDE.

---

## Практический вывод для следующих обсуждений

1. **Фундамент общий:** Δ = change in shared knowledge state (Meadow–Yuan → CIG → наша note).
2. **Для метрик v0:** сначала бинарный/грубый `memory_change?` / явный Δ-маркер; не сразу 4×4 LLM rubric на каждый turn (дорого).
3. **Оси:** Novelty∩Relevance обязательны; Scope — опционально / иначе переопределить под «artifact reach» (message anchor, ADR, TK), не Habermas-universal.
4. **Bottleneck min:** хороший candidate rule для «лишний RT»: `min(N,R) ≤ 1` или streak NONE.
5. **Не импортировать CIG как KPI скорости** — бумага сама отделяет informational gain от conversational quality / facilitation.

---

## Открыто (после digest)

- Нужен ли отдельный spike «claim memory для Intercom topic» vs достаточно TopicDecisions + anchors?
- Как считать tool Δ (появился файл/тест) в той же шкале, что conversational Novelty?
- Калибровка: оператор vs auto — кто source of truth при споре?
- Decision-tree / 20Q: когда clarification = хороший split, а когда дорогой RT (см. § ниже)?

---

## Приложение: 20 вопросов / Decision Tree ↔ CIG

**Игра:** один загадывает объект из пространства гипотез \(H\); другой задаёт (часто бинарные) вопросы. Выигрышная стратегия — **не** «угадать сразу», а каждый вопрос **максимально режет** \(H\) (классический decision tree / entropy reduction / twenty questions).

Пример: «Это животное?» → Нет → отсечён целый класс. Плохой ход: «Это мой соседский кот Барсик?» при огромном \(H\) — почти нулевой split, даже если ответ «нет» формально «нов».

### Карта на оси CIG

| Игра / дерево | CIG / Dialogue Δ |
|---------------|------------------|
| Пространство гипотез \(H\) | shared claims + Frame/Accepted + цель topic |
| Вопрос с большим split | высокая **Novelty** *относительно \(H\)* **и** высокая **Relevance** к цели угадывания |
| Ответ «Нет, не животное» | Δ = Bound / negative knowledge (сужение) — у нас это тоже Δ |
| Вопрос с крошечным split | низкая Novelty по сути (мало change in KB), хотя лексически «новый» |
| Угадайка в лоб | Scope/конкретика без редукции \(H\) — дорогой RT |
| Coordination «подожди, думаю» | низкий CIG, но может готовить хороший следующий split |

**Bottleneck min снова:** вопрос off-topic (Relevance↓) или повтор уже отсечённого (Novelty↓) — слабый ход, даже если длинный.

**Scope в CIG ≠ размер отсечения.** Implication Scope у Chen et al. — обобщение до «public principle». В дереве «животное?» — огромный **информационный** scope (много гипотез), но локальный акт. Для token economy важнее **expected information gain** (насколько режет \(H\)), не Habermas-universal.

### Формула наивности (ориентир, не KPI)

Хороший clarification / ход в исследовании:

\[\text{ценность} \propto \Delta H \times \mathbf{1}_{\text{on-goal}}\]

где \(\Delta H\) — сужение пространства гипотез (или рост empirically content / falsifiability), on-goal = Relevance к Frame.

Плохой round-trip: \(\Delta H \approx 0\) при полной цене agent turn (токены + время).

### Связь с научным мышлением

Поппер: хороший тест — **рискованный**, может сильно сузить теорию. Слабый ad hoc — иммунизация без роста содержания. То же, что «Барсик?» вместо «животное?».

### Для agentic / ADCM

| Ситуация | Decision-tree чтение |
|----------|----------------------|
| Pressure без тактики | вопрос без split — не режет \(H\) |
| Clarify batch [0031] | несколько бинарных сплитов дешевле серии полных turns |
| TopicDecisions.Rejected | явные отсечённые классы = ветки дерева, уже пройденные |
| Partition | смена \(H\) / новой игры, когда текущее дерево исчерпано или lane другая |
| Tool/verify | empirically «чёрный лебедь» — сильный split в пространстве «код работает?» |

**Не путать:** не каждый ход должен быть бинарным вопросом; implement-ход тоже может резать \(H\) (появился артефакт). Критерий — **Δ в общем KB**, не форма «да/нет».

---

## Два режима поиска: closed \(H\) vs open \(H\)

Ветка ADCM сама показала предел аналогии с 20Q. Целевая функция на мета-уровне понятна (**сигнал/ответ**, Δ на токен, осмысленность хода), но **терминальный результат** («правильная» архитектура) заранее не дан → глобальный путь в \(Q \times H\) **не вычислим вперед**.

| | **Closed \(H\)** | **Open \(H\)** |
|--|------------------|----------------|
| Что это | объект/ответ уже в фиксированном \(H\) | \(H\) растёт и перекраивается от ходов |
| Пример | «какая кнопка», verify red/green, угадайка | «а что если не silent compact?» → ADCM → 0175 → Δ |
| Цель | точка в \(H\) (угадали / починили) | улучшить мету (сигнал/ответ), открыть пригодное знание |
| Хороший вопрос/ход | max **split** \(\Delta H\) при Relevance к цели | **local IG** *или* **meta-Δ** (перекройка карты \(H\)) |
| Плохой ход | крошечный split при полной цене turn | полный turn при \(\Delta H \approx 0\) *и* без сдвига рамки |
| Когда остановиться | ответ ∈ \(H\) / тест зелёный | local splits измельчали; нужен Partition / новый meta-вопрос |
| CIG Novelty 3 vs 4 | чаще assimilation внутри рамки | Insightful/accommodation = смена Frame (редко, дорого, ценно) |
| Continuity (0175) | ops + короткий Accepted | TopicDecisions критичны: Rejected = отпиленные ветки **старой** карты |

### Три суррогата вместо «найти путь заранее» (open \(H\))

1. **Локальный IG** — CIG / дерево внутри *текущего* \(H\) (как 20Q на подзадаче).
2. **Мета-Δ** — ход, который меняет саму нарезку \(H\) (ADCM вместо compact; Decisions+ops вместо одного handoff). Не каждый ход; ловить и якорнить.
3. **Сохранение пройденного** — Rejected/Accepted/якоря, чтобы следующий чат не оплачивал те же ветки снова.

Оптимизируем не расстояние до известного финала, а **качество движения в неизвестном**: компас (сигнал/ответ) без карты сокровищ.

### Смешение режимов — частая ловушка

Агент в open-research отвечает так, будто \(H\) closed: сыпет ops-seed и first moves (угадайка «куда кликнуть»), пока оператор ещё нарезает карту. Симптом: высокий «actionable», низкий meta-Δ. Лечится явным маркером режима хода (Perceive/Process vs Perform) и приоритетом TopicDecisions над Handover ops при Partition.

---

## Критерий заметки

Можно сказать: *«CIG разобран; 20Q = closed \(H\); open \(H\) = исследование с компасом; суррогаты local IG / meta-Δ / continuity»* — и указать этот файл + arXiv:2604.15647 + Dialogue Δ note.

