---
type: Note
title: Note — TaskKnowledge Flow (agent work ontology)
description: '**Status:** Proposed · capture (EnvInvariant draft; not freeze)'
tags: [agent-operations, domains, note, research]
language: ru
---

﻿# Note — TaskKnowledge Flow (agent work ontology)

**Status:** Proposed · capture (EnvInvariant draft; not freeze)  
**Date:** 2026-07-17  
**Working name:** **TaskKnowledge**  
**Aliases:** Task KE (жаргон паттерна); не AgentTaskManagement, не Jira  
**Scope:** agent-operations · reusable across CIDE / ANUI / open stack

**Граница:** TaskKnowledge = знание о **ходе работы**. Это **не** KB/agent-notes канон. Store = per-workspace **markdown** under `{workspace}/.task-knowledge/`.

**Среда (сначала):** MCP `agent-task-knowledge` → `D:\agent-task-knowledge-mcp\AgentTaskKnowledgeMcp.exe`. Ops: `man`. Траектория в `man` TOC.

**Связь:**
- Playbook — `domains/agent-operations/playbook-taskknowledge-adr-analytics.md`
- Templates — `templates/work/template-taskknowledge-*.md`
- Gap map — `domains/agent-operations/note-taskknowledge-gap-map.md`
- Product ADR (Core repo, не KB) — https://github.com/AI-Guiders/AIGuiders.AgentTaskKnowledge.Core/blob/main/docs/adr/0001-process-instance-vs-delivery-dag.md
- Section-store hygiene (AN + TK markers) — `domains/agent-operations/playbook-agent-notes-section-store-hygiene.md`
- Next-task handoff (substance, not just id) — `domains/agent-operations/playbook-taskknowledge-next-handoff.md`
- Findings JSONL — прототип полей only
- Failures — отдельный JSONL

---

## Одна строка

**Сначала MCP/store (среда), потом работа по карточкам.** ADR без analytics — не спецификация к исполнению.

---

## Решение (EnvInvariant)

1. Отдельный MCP (путь B); механика AN адаптирована (section upsert, route_next), не fork KB.
2. Store = markdown `.task-knowledge/`.
3. Flow: ensure_store → analytics → task cards → route_next → execute → verify.
4. Не Jira / не RAG по ADR / не KB канон.
5. Без суффиксов `v0`/`v1` в именах артефактов.

## MCP tools

`man` · `ensure_store` · `route_next` · `tasks` · `task_upsert` · `read_card` · `write_card` · `upsert_section` · `analytics_upsert`

## Dogfood

`D:\Experiments\agent-notes\.task-knowledge\` — после remount MCP (del/add в `mcp.json`, см. `note-cursor-mcp-remount.md`): `ensure_store` / `route_next` на этом workspace.

**Next work (после среды):** pilot CIDE ADR 0008 в cascade-ide `.task-knowledge/`.

