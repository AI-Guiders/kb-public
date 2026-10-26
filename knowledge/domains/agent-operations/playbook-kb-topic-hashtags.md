---
type: Playbook
title: 'Playbook: KB / ADR topic hashtags v1'
description: '**Domain:** agent-operations'
tags: [kb-tags, agent-operations, ssot, playbook, domains, living]
---
# Playbook: KB / ADR topic hashtags v1

**Domain:** agent-operations  
**Дата:** 2026-07-18  
**Статус:** Accepted (MLP: `knowledge_tags` modes + cache + aliases; Core ≥ 2.1.8)  

**Связь:** [`note-canon-map-dynamic-inventory.md`](../../work/projects/door-to-singularity/cascade-ide/note-canon-map-dynamic-inventory.md) · ADR 0176 · L0 `agent-equal-standing-v1` · `META/kb-topic-tag-aliases.json` · скрипт `knowledge/scripts/tag-knowledge-canon.py`

---

## Одна строка

В шапке — **тема** + **роль**; агент зовёт **`knowledge_tags`** (inventory / lookup / explain / resolve). SSOT — `#ssot` или `policy: cite_ssot`. Не переписывать канон — cite.

---

## Два слоя тегов

| Слой | Примеры | Зачем |
|------|---------|--------|
| **Тема** | `#equal-standing` `#adcm` `#harness` `#kb-taxonomy` | «про что» |
| **Роль** | `#ssot` `#research` `#living` `#playbook` `#adr` `#note` | статус документа |

Размещение: `**Tags:** #adcm #harness #ssot #playbook`

- Тема = kebab-case, **без** `#canon/`.
- `#ssot` = формулировка канона; elsewhere — cite.
- Не тегать scratch (indexer пропускает `scratch/` и `.revisions`).

---

## Tool: `knowledge_tags` (MLP)

| Arg | Смысл |
|-----|--------|
| `mode` | `auto` (default) · `inventory` · `lookup` · `explain` · `resolve` · `aliases` |
| `tag` / `query` | тег (`#adcm`) или фраза/alias; `query` перекрывает `tag` |
| `ssot_only` | только hits с `#ssot` |
| `include_related` | co-occurrence тем (default true) |
| `refresh` | сбросить кэш индекса |
| `subdir` / `limit` | сузить обход / 1–500 |

Поведение:

1. `inventory` — теги с `file_count` / `ssot_count`.
2. `lookup` — hits, `#ssot` первыми + preview + related.
3. `explain` — SSOT locus + preview + `also` + related + `policy`.
4. `resolve` — фраза → `#tag` (`alias` / `alias_fuzzy` / `tag`).
5. Aliases: built-in Core + override `knowledge/META/kb-topic-tag-aliases.json`.
6. Кэш по stamp (count + max mtime); write/delete knowledge → invalidate.

Core: `KnowledgeTagIndex` + `NotesStorage.QueryKnowledgeTags` (≥ 2.1.8).

---

## Как пользоваться (агент)

1. Неясная фраза → `mode=resolve` или сразу `explain` с `query`.
2. Знаешь тег → `lookup` / `explain`.
3. Несколько hits → бери `ssot: true` / `policy: cite_ssot`.
4. Новый файл → темы + роль; при каноне — `#ssot` только на locus.

Одноразовая разметка: `python knowledge/scripts/tag-knowledge-canon.py --knowledge-root …/knowledge`.

---

## Seed registry (ручные SSOT)

| Topic | SSOT loci (в индексе `knowledge_tags`) |
|-------|-----------|
| `#equal-standing` | [`note-equal-standing-index.md`](note-equal-standing-index.md) → hot `agent-equal-standing-v1`; ADR 0166 §2 |
| `#adcm` | [`playbook-agent-driven-context-management.md`](playbook-agent-driven-context-management.md); ADR 0166/0175 |
| `#kb-tags` | этот playbook |
| `#kb-taxonomy` | `META/kb-taxonomy.md` |
| `#fs-relocate` / `#agent-affordances` | [`note-fs-relocate-affordances-index.md`](../../work/projects/door-to-singularity/cascade-ide/note-fs-relocate-affordances-index.md) → ADR 0176 |
| `#canon-map` | [`note-canon-map-dynamic-inventory.md`](../../work/projects/door-to-singularity/cascade-ide/note-canon-map-dynamic-inventory.md) |
| `#historiography` | SEE historiography note (тот же path) |
| `#dialogue-delta` | [`note-dialogue-delta-effectiveness.md`](note-dialogue-delta-effectiveness.md) |

CIDE ADR `**Tags:**` размечены локально в `cascade-ide/docs/adr/` (0166/0175/0176); federated scan ADR tree — ещё нет (индекс сейчас только `agent-notes/knowledge`).

---

## Не сейчас

- Массовый `#ssot` на весь KB.
- CASA concept-net runtime.
- Префикс `#canon/`.
- Federated multi-root index (открытый вопрос canon-map).

