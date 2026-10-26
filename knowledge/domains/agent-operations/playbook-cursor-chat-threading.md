---
type: Playbook
title: 'Cursor: ветвление тредов и топики без CIDE'
description: '**Domain:** `agent-operations`'
tags: [agent-operations, domains, living, playbook]
---
# Cursor: ветвление тредов и топики без CIDE


**Domain:** `agent-operations`  
**Дата:** 2026-06-25  
**Provenance:** диалог оператор + agent (Cursor); CASA Neumann listen pilot; контекст 165K/200K, billing legacy → Pro+.

**Связь:**

- pressure / checkpoint — [`playbook-context-pressure-checkpoint.md`](playbook-context-pressure-checkpoint.md)
- внешняя память — [`playbook-external-memory-workaround.md`](playbook-external-memory-workaround.md)
- итоги сессии / export — [`playbook-session-summary-and-chat-export.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md)
- PRIMARY / scope — [`playbook-project-switch.md`](playbook-project-switch.md)
- product с топиками — CIDE AEE; см. [`playbook-agent-execution-environment.md`](../../work/projects/door-to-singularity/cascade-ide/playbook-agent-execution-environment.md)

---

## Одна строка

**Cursor — одна лента; работа — ветвистая. Топики эмулируем: epic в чате + spike в отдельном треде + стык в handoff/KB, не один transcript на всё.**

---

## Проблема

В одной сессии у оператора естественно:

```text
колготки (replay, поле)
  → идея: эмоции не из manifest (W5b)
    → gate / merge
      → смежный стек (billing, mimo, …)
```

В **CIDE** это разные **топики** — общий проект, раздельный контекст.

В **Cursor** это **один чат** → Conversation 100K+ → несколько platform summarization → ответы и tools **медленные** → деградация recall начала треда.

Это не «плохая дисциплина», а **несовпадение модели продукта и когнитивного потока**.

---

## Три полосы (lanes)

| Lane | Один Cursor-чат? | Примеры | Жизнь |
|------|------------------|---------|--------|
| **Epic** | да, один длинный | Neumann listen wire-gap; один handoff-порядок | до ~60–70% context или 1–2 summary |
| **Spike** | **отдельный** короткий | «мыходрон 25с trace»; «mimo Auto vs API»; pricing Cursor | закрыть → 3–10 строк в epic/handoff |
| **Meta** | отдельный | биллинг, инструменты, «как устроен harness» | не тащить в epic с кодом |

**Epic** — одна линия кода/цели с зависимостями между шагами.  
**Spike** — гипотеза или проверка, **самодостаточная** за 1 сессию.  
**Meta** — не меняет репозиторий; не смешивать с epic, иначе +50K разговора в тот же meter.

---

## Остаться в том же чате

- следующий шаг **без** предыдущего бессмыслен (replay → разбор trace → фикс affect);
- та же **PRIMARY** / тот же handoff-эпик;
- Context Usage **&lt; ~60%** и не было **второй** platform summarization подряд;
- ответы ещё **быстрые** (субъективно &lt; ~30 с на простой ход без тяжёлого pytest).

---

## Форк: новый чат

- новая **гипотеза**, не следующий commit в той же цепочке;
- смена **lane** (epic → meta или epic → spike);
- Context **≥ ~70%** или **≥ 2** summarization в треде;
- ответы **стабильно медленные** без тяжёлых команд;
- обсуждение **&gt; ~15–20 мин** без правок кода из epic.

**Действие:** новый чат + **brief** (ниже) + при необходимости checkpoint по [`playbook-session-summary-and-chat-export.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md).

Старый чат = **архив**, не рабочая память.

---

## Сигналы (оператор видит meter; агент — proxy)

| Сигнал | Действие |
|--------|----------|
| Conversation **&gt; 100K** / **&gt; 70%** | не начинать новую крупную ветку в этом треде |
| **2+** «conversation was summarized» | рассмотреть fork или checkpoint |
| Медленные ответы после summary | **fork** с brief |
| Идея «а что если…» | spike: обсудить → **зафиксировать** → fork или вернуться к epic |
| Тяжёлый pytest / batch | **терминал оператора**, в чат — только хвост failures |

Дополняет L1 в [`playbook-context-pressure-checkpoint.md`](playbook-context-pressure-checkpoint.md); meter Cursor — **ground truth** для оператора.

---

## Brief для нового чата (шаблон)

```markdown
[PRIMARY:<project-id>]  <!-- опционально; см. project-switch -->

Epic: <одна строка>
Сделано: <2–5 буллетов>
Не трогать: <WIP, gitignored store, …>
Репо / ветка: <path, branch @ commit>
Store / runtime: <если есть>
Сейчас: <один измеримый шаг>
Стык: <путь к handoff/scratch в KB или design/>
```

Пример (CASA):

```markdown
[PRIMARY:CASA]
Epic: Neumann listen wire-gap post-merge
Сделано: W5b affect emergent; develop @50f703c; kolgotki+myhodron replay ok
Не трогать: listen_beat_apply/verify WIP (stash)
Репо: casa-ontology-payload, develop
Store: agents/von-neumann
Сейчас: Lalabook G0 / curriculum flip п.5
Стык: design/CASA-scratch-dima-concept-zone-handoff.md
```

Агент **не обязан** видеть старый тред, если brief + handoff достаточны.

---

## Куда писать стык (вне чата)

Приоритет:

1. **Handoff / scratch в репо задачи** — `design/CASA-scratch-*-handoff.md`, wire-gap checklist (решения эпика).
2. **KB `agent-operations`** — сквозные протоколы (этот файл); не дублировать построчный transcript.
3. **`knowledge/temp/`** — черновик spike до согласования ([`playbook-external-memory-workaround.md`](playbook-external-memory-workaround.md)).
4. **Project card / note** в `knowledge/work/projects/…` — если решение переживает спринт.

После spike: **3 буллета в epic-handoff**, spike-чат закрыть.

---

## Паттерн «идея следом» (колготки → эмоции)

Допустимо **в одном epic**, если:

- идея **прямое продолжение** wire-gap (W5b после kolgotki pilot);
- контекст ещё не раздут.

Предпочтительнее **fork со стыком**, если:

- идея ≥ 5 сообщений обсуждения **без** коммита;
- меняется **слой** (сенсомотор → биллинг IDE);
- epic уже **&gt; 60%** context.

```text
Обсудили W5b в epic → коммит → 3 строки в handoff
Meta «Cursor Ultra» → отдельный чат, не 142K в epic
```

---

## Billing (после legacy Cursor, ориентир 2026-08)

Длинный чат дороже **каждый** ход (весь Conversation в запросе). Fork + brief:

- снижает **included usage** на Pro+ / on-demand cap;
- не заменяет scoped pytest и default **Auto/Composer** на рутине.

См. операторский выбор: Pro+ + spending cap on-demand; Ultra — только если Pro+ стабильно не хватает **каждый** месяц.

**После legacy Pro (ориентир ~2026-08):** агентный контур без foreign card — [playbook-rf-llm-cloudru-foundation-models.md](playbook-rf-llm-cloudru-foundation-models.md) (Cloud.ru FM + VS Code **Roo Code** или **CascadeIDE**). KZ/Plus — опционально для нативного Codex CLI, не обязателен для FM API.

---

## Обязанности агента

- при смене lane **предложить** fork или checkpoint, не молча тащить meta в epic;
- при fork **набросать** brief для копипаста в новый чат;
- решения epic **писать** в handoff/KB ([`playbook-external-memory-workaround.md`](playbook-external-memory-workaround.md)), не полагаться на transcript;
- не гонять **full suite** в agent-turn; scoped tests + терминал.

---

## Anti-patterns

- один чат на «всё за день» без handoff;
- spike без фиксации итога в epic;
- platform summary как замена brief + handoff;
- «новый агент на каждый вопрос» — избыточно; fork по **lane** и **meter**, не по каждому сообщению.

---

## Канон

`knowledge/domains/agent-operations/playbook-cursor-chat-threading.md`

