---
type: Playbook
title: 'Playbook: Agent-driven context management (ADCM) v1'
description: '**Domain:** agent-operations'
tags: [adcm, agent-operations, domains, harness, living, playbook, ssot]
language: ru
---
# Playbook: Agent-driven context management (ADCM) v1

**Domain:** agent-operations  
**Дата:** 2026-07-18  
**Provenance:** оператор + агент — отказ от «compaction as product goal»; CIDE harness / ADR 0166  

**Связь:**

- ADR (репо): cascade-ide `docs/adr/0166-agent-centric-harness-model-comfort-and-pay-per-token-economics.md`
- ADR Partition continuity: cascade-ide `docs/adr/0175-adcm-partition-continuity-pair-and-message-anchors.md` (Proposed)
- Dialogue Δ / round-trip economy (research): [`note-dialogue-delta-effectiveness.md`](note-dialogue-delta-effectiveness.md)
- pressure / checkpoint — [`playbook-context-pressure-checkpoint.md`](playbook-context-pressure-checkpoint.md)
- export — [`../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md)
- threading — [`playbook-cursor-chat-threading.md`](playbook-cursor-chat-threading.md)
- CIDE↔Cursor parity — [`playbook-cide-harness-parity-vs-cursor.md`](playbook-cide-harness-parity-vs-cursor.md)
- outline KB — `read_knowledge_file` `mode=outline` (AgentNotes.Core ≥ 2.1.6)

---

## Одна строка

**Harness сигнализирует давление (видно оператору + obligation агенту); агент управляет контекстом; silent rewrite чата запрещён. API не компактит.**

---

## Почему не «compaction»

LLM API (Cloud.ru FM и аналоги) принимает messages — **не сжимает** историю.

Silent host summarization (Cursor-style) — **антипаттерн**: теряются решения/open items без согласования.

Агенту нужна **экономика и гигиена контекста**, не скрытый rewrite ветки. Честное имя слоя: **Agent-driven context management (ADCM)**.

| Старое | ADCM |
|--------|------|
| compaction / preCompact / «нужен platform preCompact» | harness **signals** + agent **tactics** |
| compactor как цель продукта | Prevent → Partition → Persist → Prune (узко) → Never |
| `compact_hot_context` | одна **Prune**-тактика (только hot/KB), не синоним «сжать чат» |

---

## Контракт ролей

| Роль | Делает | Не делает |
|------|--------|-----------|
| **Harness** | детектит pressure; dual-channel deliver; даёт tools/telemetry | silent rewrite полной истории topic |
| **Agent** | выбирает тактику ADCM; предлагает checkpoint/export | игнор видимого pressure без ответа оператору |
| **Оператор** | согласует checkpoint; видит inject в ленте | обязан «помнить про итоги» вручную |

---

## Доставка сигналов (dual-channel)

Норма CIDE (и цель Cursor-parity по смыслу, не по API):

1. **A — Visible tape:** inject как `user`-сообщение в активный topic (оператор и агент видят).
2. **B — Pending agent context:** reminder в следующий agent turn (MAF minimized / obligation).

**Default = A+B вместе.** Только B = monologue; только A = легко проигнорировать.

Опционально **pull:** агент вызывает `ide_agent_status` / telemetry — факты, не замена pressure fire.

Сигналы (CIDE `[agent.harness]`):

| Сигнал | Типичный порог | Смысл |
|--------|----------------|--------|
| user turns | ~40 (+ repeat) | длинная сессия → checkpoint |
| thread messages | ~60 (+ repeat) | толстый topic → ADCM / fork / export |
| prompt usage % | `ContextWarnPct` (~75) +10pp | token budget → ADCM |

Текст inject: **context pressure / ADCM**, не «сейчас сожмём чат».

---

## Тактики агента (5P)

1. **Prevent (дефолт)** — не класть в prompt: `route_context`, `read_knowledge_file mode=outline`, MCP pull, точечный git MCP, не monorepo dump.
2. **Partition** — epic / spike / meta topics; fork при смене lane. Носитель перехода: **TopicDecisions + Handover ops** (+ export/message anchors) — ADR 0175; новый чат читает **выводы** первыми, ops — хвост.
3. **Persist** — KB / TK / scratch / `chat_export_readable` **до** потери окна; chat = **кэш**, не память.
4. **Prune (узко)** — `compact_hot_context` только для hot/sections; или явный handoff summary с согласованием оператора.
5. **Never** — silent rewrite полной истории topic без агента и без видимого артефакта.

При pressure fire агент **обязан** предложить оператору один из: export+checkpoint, fork topic (continuity pair), Persist в KB/TK — не «сожму в голове».

---

## Анти-паттерны

- Ждать «platform preCompact event» от FM API.
- Считать Cursor silent summary достаточным checkpoint.
- Harness, который сжимает чат без участия агента («о нас без нас» — ADR 0166 §2).
- Путать `compact_hot_context` с compaction всего диалога.
- Partition только с ops-seed («записка на подушке») без TopicDecisions.

---

## Критерий

Оператор и агент отвечают одной фразой: *«Harness давит и светит; агент управляет контекстом; silent chat compact запрещён; Partition несёт Decisions+ops+якоря»* — и указывают этот playbook + ADR 0166 / 0175.

