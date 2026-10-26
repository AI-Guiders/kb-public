---
type: Map
title: Gap map — Findings JSONL → TaskKnowledge md / MCP v0
description: '**Date:** 2026-07-17'
tags: [agent-operations, domains, note, research]
language: en
---

﻿# Gap map — Findings JSONL → TaskKnowledge md / MCP v0

**Date:** 2026-07-17  
**Decision:** md store; Findings = field prototype only.

| Capability | Findings JSONL today | TaskKnowledge target |
|------------|----------------------|----------------------|
| Task as_is/to_be/why/DAG | yes | md task card |
| criterion / part / sources | missing (text hacks) | first-class in md |
| Analytics card | no | `analytics/*.md` |
| route_next | no (manual list) | port AN route scoring → ready tasks |
| Hash memo | memos.jsonl | optional `memos/*.md` + hash frontmatter |
| Section upsert | no | port AN section markers |
| Concurrent append lock | JsonlExclusiveAppend | file lock / atomic write for md |
| man / thin MCP | yes | new MCP tool surface |
| KB templates | via AN read | keep in AN KB |

## Port from AN first (ordered)

1. read / write / upsert_section on files under `.task-knowledge/`
2. route_next (status + blocked_by)
3. revisions optional
4. skip: knowledge roots, hot L0, memory_health

## Keep as-is

- agent-failures JSONL
- agent-notes for templates/playbooks/canon

