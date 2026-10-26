---
type: Playbook
title: 'Playbook — TaskKnowledge: ADR → analytics → DAG → execute'
description: '**Status:** draft · experimental'
tags: [agent-operations, domains, living, playbook]
---

﻿# Playbook — TaskKnowledge: ADR → analytics → DAG → execute

**Status:** draft · experimental  
**Date:** 2026-07-17  
**EnvInvariant:** [`note-taskknowledge-flow.md`](note-taskknowledge-flow.md)

---

## Purpose

Процедура хода после ADR/идеи — **после** того, как среда (MCP + store) доступна.

## Environment first (обязательно)

1. MCP `agent-task-knowledge` в Cursor (`D:\agent-task-knowledge-mcp\AgentTaskKnowledgeMcp.exe`).
2. `man` — TOC и траектория.
3. `ensure_store` на целевом `workspace_path`.
4. Только потом analytics / tasks / реализация.

Не начинать «работу по ADR» без `route_next`/`tasks` в среде.

## Scope

- В scope: эпик / ADR перед кодом; продолжение после compact.
- Out of scope: failures; KB канон; Jira.

## Store

`{workspace}/.task-knowledge/` — layout template: `templates/work/template-taskknowledge-workspace-layout.md`.

Шаблоны:
- `templates/work/template-taskknowledge-analytics.md`
- `templates/work/template-taskknowledge-task.md`

## Practical order

1. **Env:** MCP + `ensure_store`.
2. **Analytics:** `analytics_upsert` (скелет из template).
3. **Tasks:** `task_upsert` на каждый узел (criterion обязателен).
4. **route_next** — взять ready.
5. **read_card** → execute в `member_paths`.
6. **task_upsert** `status=done` + evidence в verify section.
7. Повтор `route_next`.

## Core rules

1. Среда раньше работы.
2. Нет analytics/DAG → нет большой реализации по ADR.
3. Task `to_be` ≠ копипаст ADR.
4. Не писать карточки в `knowledge/` канон.
5. Имена артефактов без `v0`/`v1` суффиксов.

