---
type: Note
title: 'Note: Inquiry Mode — карта обсуждения на PFD/MFD/Forward (v0)'
description: '**Domain:** agent-operations / cide-product-design'
tags: [agent-operations, domains, note, research]
---
# Note: Inquiry Mode — карта обсуждения на PFD/MFD/Forward (v0)


**Domain:** agent-operations / cide-product-design  
**Статус:** research / product sketch — **не** Accepted ADR  
**Дата:** 2026-07-18  
**Provenance:** оператор — режим «как Debug», open \(H\), после ADCM / Dialogue Δ / CIG

**Связь:**

- Closed vs open \(H\) — [`note-cig-conversational-information-gain.md`](note-cig-conversational-information-gain.md)
- Dialogue Δ — [`note-dialogue-delta-effectiveness.md`](note-dialogue-delta-effectiveness.md)
- ADCM / Partition — playbook ADCM · ADR 0175
- Кокпит — cascade-ide ADR [0021](https://github.com/AI-Guiders/cascade-ide/blob/develop/docs/adr/0021-pfd-mfd-cockpit-attention-model.md) (PFD / Forward / MFD)
- SEDM — ADR 0174 (Perceive → Process → Perform)
- Historiography — [`../../work/projects/door-to-singularity/cascade-ide/note-cognitive-se-environments-historiography.md`](../../work/projects/door-to-singularity/cascade-ide/note-cognitive-se-environments-historiography.md) (KBSA / Apprentice / IPSE / IBIS → уроки)

---

## Одна строка

**Отдельный режим IDE (как Debug): участники ведут open-\(H\) обсуждение по видимой карте — Information Graph на PFD, элементы \(I\) на MFD, диалог в Forward — и из положения в \(H\) предлагают эффективный \(Q\).**

Целевая функция мета-уровня: **сигнал/ответ** (осмысленный Δ на токен/время). Терминальный «правильный ответ» заранее не дан → путь в \(Q\times H\) не ищется глобально, а **строится** локальными сплитами и meta-Δ.

---

## Именование (чтобы не смешать)

| Символ | Здесь значит | Не путать с |
|--------|--------------|-------------|
| **Goal** \(G\) | цель обсуждения (сформирована на входе в режим) | |
| **\(H\)** | пространство гипотез / нарезок «где мы можем оказаться» | |
| **\(H_0\)** | начальная затравка \(H\) после сбора | |
| **\(I\)** | сырая / собранная информация (know / don't-know, источники) | |
| **\(F = F(I)\)** | обработанные единицы: факт, гипотеза, суждение, … (KE-типы) | |
| **IG** | **Information Graph** — граф известного и связей | **не** CIG; **не** «information gain» как \(\Delta H\) |
| **\(P: I \to H_0\)** (и далее \(P\) на текущем \(H\))** | явные пути/проекции: как из \(I\)/\(F\) получается текущая нарезка \(H\) | |
| **\(Q\)** | следующий вопрос / ход диалога | |
| **CIG** | Conversational Information Gain (Chen et al.) — оценка реплики | отдельный измеритель, не граф |
| **IGAIN** / \(\Delta H\) | ожидаемое сужение \(H\) (20Q / decision tree) | пишем IGAIN в тексте, если нужна ясность |

---

## Аналогия с Debug

| Debug | Inquiry Mode |
|-------|----------------|
| Вошли в режим осознанно | То же — не default чата |
| Стеки / breakpoints / locals | IG на PFD; \(I\)/\(F\) на MFD; диалог Forward |
| Шаг меняет состояние процесса | Δ в \(I\), \(P\) или \(H\) перерисовывает карту |
| Цель: понять/починить поведение | Цель: продвинуть open \(H\) по компасу сигнал/ответ |
| Вышли — снова обычный edit | Вышли — TopicDecisions + ops (0175), обычный Intercom |

---

## Жизненный цикл сессии режима

### 1. Enter + Goal

Участники фиксируют **\(G\)** (цель обсуждения). Черновик часто готовит агент; человек правит/утверждает. Без \(G\) Relevance (CIG) и «эффективный \(Q\)» не на чем мерять.

### 2. Seed gather (затравка) — качество низкий приоритет

Фаза сбора «что знаем / не знаем» про \(G\) (субагенты, KB outline, индекс, prior TopicDecisions…).

- Формируется куча \(I\) и черновик **\(H_0\)**.
- **Не** оптимизировать CIG/красоту на этом шаге — это bootstrap, как загрузка символов перед дебагом.
- Явно помечать пробелы (*unknown*) как первоклассные узлы \(I\) — отрицательное знание.

### 3. Build IG + \(F(I)\) + \(P\)

Строится **Information Graph**:

- узлы \(I\) и/или \(F = F(I)\) с KE-типами (черновик): Fact · Hypothesis · Judgment · Constraint · OpenQuestion · Source/Anchor · …
- рёбра: supports / contradicts / elaborates / derived-from / …
- **\(P\)**: проекции «из этих \(I\)/\(F\) следует такая нарезка \(H\)» (в т.ч. начальный \(P: I \to H_0\)).

По определению режима: пока нет \(P\), нет честной карты «где мы в \(H\)».

### 4. Heat — совместная работа по карте

Раскладка внимания (целевой продукт):

| Зона | Содержимое режима |
|------|-------------------|
| **PFD** | **IG + положение в \(H\)** (маршрут обсуждения, где сплиты, где тупик) |
| **MFD** | каталог / инспектор элементов \(I\) и \(F\) (детали, якоря, источники) |
| **Forward** | диалог (Intercom) — ход \(Q\) / ответы / tool Δ |

Инвариант: изменение **любого** из \(\{I, P, H\}\) → обновление графа и панелей (live projection, не «чат отдельно, карта потом»).

### 5. Выбор \(Q\)

Имея карту и «где мы в \(H\)», участники (агент предлагает, человек калибрует) выбирают **эффективный \(Q\)**:

- closed-подзадача внутри текущего \(H\): max IGAIN (20Q);
- open: meta-Δ (перекройка \(H\)) или Partition, если local splits измельчали.

Диалог без взгляда на IG = снова «Барсик?» или ops-seed в open research.

### 6. Exit / Persist

Выход из режима → Continuity pair (TopicDecisions + Handover ops) + export/якоря (ADR 0175). Карта не обязана жить вечно; **выводы** живут.

---

## Модель данных (набросок, не wire)

```text
InquirySession
  goal: G
  mode: inquiry
  I:  set<InfoNode>          # сырьё + unknown
  F:  set<ProcessedNode>     # F(I), KE-typed
  H:  HypothesisSpace        # текущая нарезка (эволюционирует из H0)
  P:  set<ProjectionEdge>    # I/F → регионы H (и обновления P)
  IG: InformationGraph       # view over I,F,P,+links
  dialogue: topic_id         # Forward tape
```

Типы KE v0 — **открыты**; важна не таксономия навсегда, а то, что \(F\) отличим от сырого \(I\), а \(H\) — от списка фактов.

---

## Связь с уже принятыми идеями

| Идея | Роль в Inquiry Mode |
|------|---------------------|
| Open \(H\) | родной режим режима; closed \(H\) — вложенные эпизоды (verify, узкий clarify) |
| Dialogue Δ / CIG | оценка хода в Forward относительно IG-памяти |
| ADCM | Prevent = не тащить весь IG в prompt; Partition = выход/sibling с Continuity |
| TopicDecisions | снимок \(G\), Rejected/Accepted/New при exit |
| Субагенты | фаза seed gather + точечный Process на MFD, не монолог в Forward |
| SEDM | Enter/Goal ≈ Perceive; gather/IG ≈ Process; Heat dialogue ≈ Perform+Evaluate loop |

---

## Открытые вопросы

1. Имя режима в продукте: Inquiry / Explore / Deliberate / Sense?
2. KE-типы v0: минимальный набор vs полный knowledge-engineering catalog.
3. PFD: граф \(H\) vs граф \(I\) vs оба слоя (переключение как MFD pages)?
4. Кто пишет \(P: I \to H\) — агент автоматически, человек правит, или dual?
5. Стоимость live-перестройки IG на каждый ход — когда debounce / batch?
6. Связь с intent card (0173): \(F\)-узлы = карточки? или карточки ⊆ \(F\)?
7. Cursor vs CIDE: в Cursor режим может быть topic+overlay; полный PFD/MFD — CIDE-native.
8. **AN epistemic cards (`fact`/`hypothesis`/`confidence`) как \(F\)** — да, переиспользовать; graph/\(H\)-cursor — поверх (см. § носитель \(F\)).

---

## Носитель \(F\): KE-карточки AN (Fact / Confidence / …)

**Уточнение:** речь не про «механику section upsert», а про **эпистемическую схему** knowledge card — она уже есть и почти = \(F = F(I)\).

Из [`template-knowledge-card.md`](../../templates/cards/template-knowledge-card.md) · **Epistemic Linkage**:

| Поле карточки | Inquiry |
|---------------|---------|
| `epistemic_basis`: `fact` \| `inference` \| `hypothesis` | KE-тип узла \(F\) |
| `confidence`: `low` \| `medium` \| `high` | вес / осторожность сплита |
| `uncertainty` / `falsification_trigger` | OpenQuestion / 20Q-сплит «чем опровергнем» |
| `transfer_boundary` | Scope / куда нельзя тащить вывод |
| `source_refs` (Provenance) | якоря \(I\) → message/export/URL |
| Core Unit (context/signal/…) | тело узла на MFD |

Родня в TaskKnowledge: **Facts / Gaps** в analytics-шаблоне — тот же жест (установлено vs дыра), другой skin.

**Вывод:** для Inquiry **не изобретать новую KE-онтологию**. \(F\)-узлы = knowledge cards (или их session-проекция) с уже заданным epistemic_basis + confidence. IG на PFD = граф **связей между card_id**; seed \(I\) до promote может быть сырее (без полного card), Hot promote → полная карточка.

**Что всё же поверх карточек:**

| Слой | Карточка AN | Нужно ещё |
|------|-------------|-----------|
| Тип/уверенность | да (`epistemic_basis`, `confidence`) | — |
| Persist / outline | да | — |
| Рёбра / \(P: I\to H\) | слабо (supersedes ≠ supports/contradicts) | graph links / projection |
| «Где мы в \(H\)» | нет | session cursor |
| Live PFD | нет | проекция card set → граф |

**Антипаттерн:** параллельный каталог «Fact/Hypothesis v2» рядом с epistemic_basis — дубль KE, который вы уже развели для агентного Flow.

---

## Анти-паттерны

- Включить режим и сразу «оптимизировать» seed gather (дорого, рано).
- Вести Heat только в чате без видимого IG (потеря смысла режима).
- Путать IG (граф) с CIG (скоринг реплики) в UI-лейблах.
- Требовать глобальный оптимальный путь в \(Q\times H\) до начала Heat.
- Смешивать Inquiry с Debug/edit layout без явного enter/exit.

---

## Критерий заметки

Можно сказать: *«Есть sketch Inquiry Mode: Goal → seed \(I\)/\(H_0\) → IG+\(F\)+\(P\) → PFD/MFD/Forward Heat → \(Q\) из карты; open \(H\); persist через 0175»* — и указать этот файл.

