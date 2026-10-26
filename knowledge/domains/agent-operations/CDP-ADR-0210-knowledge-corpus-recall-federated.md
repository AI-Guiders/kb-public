---
type: Note
title: 'CDP-ADR-0210: Federated knowledge corpus recall (pointer)'
description: '**Status:** accepted (direction)'
tags: [agent-operations, cdp, adr, kb-tags, recall, hci, mlp, canon-map]
language: ru
---
# CDP-ADR-0210: Federated knowledge corpus recall (pointer)

**Status:** accepted (direction)  
**SSOT:** [`cdp-mcp/docs/adr/CDP-ADR-0210-knowledge-corpus-recall-federated.md`](../../../../PersonalCursorFolder/open/cdp-mcp/docs/adr/CDP-ADR-0210-knowledge-corpus-recall-federated.md)

---

## One line

**Corpus recall не зависит от workspace.** `knowledge_tags` (MLP) + новый `mode=search` ищут по **всему** `knowledge/` primary root; `[PRIMARY]` / `[SCOPE]` / `active_scope` только **поднимают** релевантный слой в выдаче, не режут корpus.

## Зачем в agent-notes

- Canon Map (`note-canon-map-dynamic-inventory.md`) → MLP shipped, но **facet gateway** резал индекс до `worlds/` → `personal/ai-incidents` не находился.
- `search_agent_notes` ≠ corpus; HCI (ADR 010) = optional external FTS; **in-proc default** = этот ADR.
- PML (`worlds/engineering-pml/`, supplement `router-pml`) — smoke-test federated recall.

## Архитектурный затык (кратко)

| Gap | Суть |
|-----|------|
| G1 | Имя `search_agent_notes` → hot file, не KB |
| G2 | `workspace_path required` при уже настроенном primary root |
| G3–G4 | CDP facet inject `subdir=worlds` → index не видит `personal/` / `work/` |
| G5 | Cursor без `cdp_open` → нет session inject |
| G6 | Три «HCI»: code / optional FTS / MLP — путаются |

## F# Modeling

**v1 — нет.** Реализация в `AgentNotes.Core` (C#). Опционально позже: `Platform.Modeling.Memory.Recall` (типы для Citizen/GDL), без переписывания индекса.

## Связи

- [`playbook-kb-topic-hashtags.md`](playbook-kb-topic-hashtags.md)
- [`note-canon-map-dynamic-inventory.md`](../../work/projects/door-to-singularity/cascade-ide/note-canon-map-dynamic-inventory.md)
- [ADR 010](../../adr/010-kb-markdown-fts-index-boundary.md) — external HCI boundary
- [ADR 008](../../adr/008-workspace-scope-map-hot-mcp-and-public-cut.md) — scope map

