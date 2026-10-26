---
type: Playbook
title: 'Cursor: coordinator + local Task workers'
description: '**Domain:** `agent-operations`'
tags: [agent-operations, cursor, cdp, orchestration, subagent, living, playbook]
---
# Cursor: coordinator + local Task workers

**Domain:** `agent-operations`  
**Status:** living · 2026-09-12  
**Audience:** operator + coordinator agent (Composer / Cursor Agent)

**Связь:**

- threading / lanes — [`playbook-cursor-chat-threading.md`](playbook-cursor-chat-threading.md)
- inbox / session-close — [`../../personal/operator-guides/playbook-cursor-chat-inbox.md`](../../personal/operator-guides/playbook-cursor-chat-inbox.md)
- [`note-cdp-autoship-coordinator-bridge.md`](note-cdp-autoship-coordinator-bridge.md) — KB background ship (FileWatcher), not manual agent push
- multi-agent writes — [`playbook-multi-agent-write.md`](playbook-multi-agent-write.md)
- PF throughput — [`playbook-pf-body-not-biped.md`](playbook-pf-body-not-biped.md)

---

## Одна строка

**Один coordinator-чат (Legacy Pro feel) + локальные Task sub-agents с CDP MCP на implement; WORK-md = контракт; ship/push = ритуал coordinator после verify, не worker по умолчанию.**

---

## Проблема

| Модель | Плюс | Минус |
|--------|------|-------|
| Один длинный чат | arc, steer, «как раньше» | Conversation >70K, recall деградирует |
| UoW-чат на каждый эпик | чистый контекст | оператор прыгает между тредами; arc теряется |
| Inbox + work | дисциплина capture | work-чат всё ещё отдельный тред |

**2026-09:** локальные `Task` sub-agents снова получают **полный CDP MCP** (`GetDynamicTools` / `CallDynamicTool`, `user-cdp/*`). Cloud workers не используем.

---

## Роли

```text
Operator ↔ Coordinator (этот чат)
                 │
                 ├─ slice WORK md / ADR pointer
                 ├─ Task worker × N  (parallel OK)
                 ├─ parent: diff · cdp_test · smoke · steer
                 └─ KB edits → **KbAutoShip** watcher (no manual push)
```

| Роль | Делает | Не делает |
|------|--------|-----------|
| **Coordinator** | intent, WORK slices, dispatch, review, merge conflicts, deploy gate, logical commits | Не обязан сам писать весь код, если worker справился |
| **Worker** | implement по WORK md, unit tests, локальный smoke | push без явного UoW; архитектурный pivot; второй эпик «заодно» |
| **Operator** | steer, approve risky push, session-close | — |

---

## Когда coordinator+workers vs UoW-чат

| Ситуация | Выбор |
|----------|--------|
| Закрытый vertical slice, touch list известен | **Worker** |
| Архитектура / «а если иначе» | **Coordinator** (Plan) |
| Operator хочет править каждый diff inline | **UoW-чат** или coordinator без worker |
| 2–3 независимых эпика (0218 + LUS + docs) | **Workers параллельно** |
| Dig-only / research | `explore` worker или coordinator |

UoW-чат **не мёртв** — fallback когда нужен плотный human-in-loop на каждом шаге.

---

## Контракт: WORK md

Каждый dispatch опирается на файл (не на простыню в чате):

- `knowledge/domains/agent-operations/WORK-*.md` или project WORK
- обязательные секции: context, touch list, tests, smoke, done criteria, non-goals
- seed одной строкой: *Implement WORK … per attached md*

Coordinator **создаёт/обновляет** WORK; worker **исполняет**; coordinator **не trust blindly**.

---

## Dispatch template (копипаст coordinator → Task)

```text
Full Repository Path: D:\Experiments\Personal Cursor Folder\open\cdp-mcp
(or guiders-core / agent-notes — as per WORK md)

Read first: D:\Experiments\agent-notes\knowledge\domains\agent-operations\WORK-<id>.md

Habitat (mandatory):
- Mutate SSOT: cdp_buffer (not Cursor Write for agent-notes / canon)
- Shell: cdp_shell_* (terminal_* only if CDP down)
- Git: go=git_scene → git_git_preflight → logical commits via git_plan (CDP git organ)
- Test: cdp_test / cdp_build per WORK
- Deploy: cdp_deploy mode=rollout only if WORK says so

Scope: WORK md only. Non-goals in WORK are hard stops.

Return:
1. Files changed (paths)
2. Test output summary
3. Smoke results if run
4. Open risks / not done items
5. Suggested commit message(s) — do NOT push unless WORK explicitly allows
```

**subagent_type:** `generalPurpose` · **run_in_background:** true для длинных эпиков, false если coordinator ждёт сразу.

---

## Coordinator после return

1. **Diff review** — стыки (router ↔ Core, gateway ↔ handlers).
2. **cdp_test** — затронутые проекты из WORK.
3. **Smoke** — MCP/live checks из WORK.
4. **Steer** — если miss: новый worker с уточнённым WORK, не resume с пол-листа правок в чате.
5. **Code ship** — parent: logical commits + push после verify (operator grant). **KB** — не руками; ждём/включаем KbAutoShip watcher.

---

## Параллельные workers

- Разные repos / непересекающиеся paths → **OK параллельно**.
- Один repo, одни файлы → **очередь** или один worker.
- Parent собирает merge conflicts — workers не координируются между собой.

---

## Context budget

- Summary **сжимает**, не обнуляет — страшно только если arc не в KB/WORK. Решения → md, чат = steer.
- Coordinator **session-close** при Conversation >70K ([`playbook-cursor-chat-inbox.md`](../../personal/operator-guides/playbook-cursor-chat-inbox.md)) — не паника, а hygiene.
- Workers стартуют clean — это и есть выигрыш.
- Side topics (Colony, статьи) — coordinator; не тащить в worker prompt.

### Conversation search (Cursor harness)

| Layer | Когда |
|-------|--------|
| **`SearchConversations`** (agent tool) | Если есть в harness — «где обсуждали X» без UUID |
| **Ctrl+K** (Agents window) | Оператор ищет старый тред |
| **`@Chats`** | Явно подтянуть один прошлый чат |
| **`agent-transcripts/*.jsonl` + Grep** | Fallback когда tool нет в сессии (Ask/subagent часто без него) |
| **`search_opencode_text`** (dbhub) | OpenCode-сессии, не Cursor |

Tool **не во всех сессиях** (rollout); не полагаться как на CDP MCP.

---

## Anti-patterns

| Anti-pattern | Почему плохо |
|--------------|-------------|
| Worker без WORK md | импровизация, CDP bypass |
| Worker push KB «чтобы закрыть» | KbAutoShip должен; ручной push только code repos |
| Coordinator сам ковыряет 500 строк при живом worker | дубль, drift |
| Resume worker для steer | дешевле новый dispatch + delta в WORK |
| Cloud sub-agent | out of scope для этого оператора |

---

## Пример (0218 recall facade)

1. Coordinator: WORK md уже есть.
2. `Task`: implement 0218, tests, no deploy unless green.
3. Parent: `KnowledgeCorpusRecallSmokeTests` + citizen tests + `cdp_deploy` if needed.
4. Parent: logical commit guiders-core + cdp-mcp + agent-notes mirror + push.

---

## Changelog

- **2026-09-12:** v1 — подтверждён CDP MCP у локального Task worker (`cdp_health` smoke).

