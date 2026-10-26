---
type: KB
title: Knowledge Engineering Knowledge Set v1 (Operations Rules)
description: 'Set: 20 cards.'
tags: [kb, knowledge-engineering, worlds]
language: ru
verified:
  - by: human:operator
    at: 2026-10-17
epistemic: '`fact`'
world: knowledge
subworld: engineering
sections: [ke-archive-order-and-doc-versioning-v1]
---
# Knowledge Engineering Knowledge Set v1 (Operations Rules)


Set: 20 cards.  
Focus: knowledge-engineering operational reliability (retention, section updates, restore protocol, archive discipline).

---

## Card 01
- world: knowledge-engineering.operations
- confidence: `high`
- signal: full-file overwrite risks accidental memory loss in collaborative edits
- action: prefer section upsert or append for routine updates
- transfer_boundary: full write allowed only with read-merge-write guardrail

## Card 02
- world: knowledge-engineering.operations
- confidence: `high`
- signal: section markers enable deterministic targeted updates
- action: keep stable `section_id` contracts for operational blocks
- transfer_boundary: marker drift invalidates automated upsert safety

## Card 03
- world: knowledge-engineering.revisions
- confidence: `high`
- signal: revision volume grows rapidly in active multi-agent workflow
- action: enforce retention windows (keep-last/daily/weekly/monthly)
- transfer_boundary: retention must protect referenced audit anchors

## Card 04
- world: knowledge-engineering.revisions
- confidence: `high`
- signal: uncontrolled archive growth reduces retrieval usability
- action: trigger compaction by threshold (count/size) with pre-summary
- transfer_boundary: never compact without preserving decision-critical lineage

## Card 05
- world: knowledge-engineering.loading
- confidence: `high`
- signal: full archive load at chat start causes noise and slows routing
- action: load hot context first, fetch deep archive on explicit need
- transfer_boundary: deep pull only for missing facts/history

## Card 06
- world: knowledge-engineering.loading
- confidence: `high`
- signal: context compression events break continuity in long threads
- action: restore via artifact path (index -> playbook -> latest batch)
- transfer_boundary: do not rely on chat memory as primary recovery source

## Card 07
- world: knowledge-engineering.indexing
- confidence: `high`
- signal: new files without index linkage become practically invisible
- action: synchronize README + canonical knowledge-index on each batch
- transfer_boundary: batch is not complete until both indexes are updated

## Card 08
- world: knowledge-engineering.indexing
- confidence: `medium`
- signal: long index blocks become hard to scan under pressure
- action: keep status artifact per domain for fast restart
- transfer_boundary: status artifact supplements, not replaces detailed index

## Card 09
- world: knowledge-engineering.classification
- confidence: `high`
- signal: mixed-world cards reduce reusability and increase contradiction risk
- action: one card -> one world -> explicit transfer boundary
- transfer_boundary: cross-world fusion requires conflict note

## Card 10
- world: knowledge-engineering.classification
- confidence: `medium`
- signal: operational and narrative fragments frequently co-mingle
- action: move narrative history to cold archive, keep hot layer operational
- transfer_boundary: narrative can return only with explicit task need

## Card 11
- world: knowledge-engineering.quality-gates
- confidence: `high`
- signal: high-confidence claims appear with weak provenance
- action: block promotion without source and falsification trigger
- transfer_boundary: confidence cannot exceed evidence class

## Card 12
- world: knowledge-engineering.quality-gates
- confidence: `high`
- signal: duplicate cards emerge during rapid batching
- action: run periodic dedupe with supersedes/superseded_by fields
- transfer_boundary: dedupe cannot delete unique boundary information

## Card 13
- world: knowledge-engineering.multi-agent
- confidence: `high`
- signal: concurrent edits by rotating agents create race-like update risks
- action: favor additive updates + section upserts over monolithic rewrites
- transfer_boundary: monolithic rewrite requires explicit lock/protocol

## Card 14
- world: knowledge-engineering.multi-agent
- confidence: `medium`
- signal: trust-driven "continue without stopping" mode increases throughput and drift risk
- action: pair large batches with strict completion checklist
- transfer_boundary: speed mode invalid without post-batch sync checks

## Card 15
- world: knowledge-engineering.restore
- confidence: `high`
- signal: environment-level context compression can feel like abrupt reset
- action: maintain compact domain-status artifacts for deterministic restart
- transfer_boundary: status must be updated before declaring domain done

## Card 16
- world: knowledge-engineering.restore
- confidence: `high`
- signal: restoration from transcript alone is costly and noisy
- action: prioritize canonical notes and indexed knowledge files as source of truth
- transfer_boundary: transcript mining reserved for unresolved ambiguity

## Card 17
- world: knowledge-engineering.evidence
- confidence: `high`
- signal: operational lessons emerge from tool traces, not only prose
- action: treat tool-call history as first-class provenance
- transfer_boundary: untraceable claims remain provisional

## Card 18
- world: knowledge-engineering.evidence
- confidence: `medium`
- signal: archive extract quality depends on focused query strategy
- action: use targeted keyword passes and normalize into cards
- transfer_boundary: broad sweep without normalization is not promotable

## Card 19
- world: knowledge-engineering.governance
- confidence: `high`
- signal: domain closure without maintenance policy leads to silent decay
- action: add refresh triggers and handoff statement per domain
- transfer_boundary: closure status expires without refresh cadence

## Card 20
- world: knowledge-engineering.governance
- confidence: `high`
- signal: cleanup pressure appears after rapid expansion
- action: split "finish domain" and "cleanup pass" into separate phases
- transfer_boundary: no structural cleanup during active evidence ingestion

---

## Source Footing

- Archive revision extracts (retention, revision hygiene, layered loading).
- Tool-trace patterns from long operational transcript (append/upsert/restore behavior).
- Operational incidents around context compression and recovery workflow.

<!-- section:ke-archive-order-and-doc-versioning-v1 -->
## Порядок ревизий, версионирование текста и BOM (v1)

- **Порядок ревизий в `knowledge/.revisions/` читается по префиксу имени** (`YYYYMMDD-HHMMSS`), **не по `LastWriteTime`**: время записи у ревизий трогается копированием/бэкапом. Проверено 2026-10-17: старейшая по имени — `20260308-…-upsert-index-knowledge-router.md`, старейшая по mtime — файл от `2026-04-11`.
- **Документ не версионируется сам.** «v0.2» в заголовке и раздел «что изменилось» — это работа git; в тексте допустимо только «создан/обновлён», и то по нужде.
- **Код-идентификатор в прозе не живёт** («см. S4», «§ 3.2»): ссылаемся **именем раздела**.
- **Ссылка на канон — только после чтения канона.** Правило, приписанное файлу, проверяется по этому файлу; иначе это ложный провенанс.
- **BOM в начале файла делает первую строку невидимой для анкорных правил** (шаблон `^`): тот же механизм, которым молча «уводило» маркер публикации. Проверено: в файле с BOM анкорный поиск заголовка на первой строке даёт 0 совпадений.
- **BOM пишет инструмент, и это баг с известной причиной.** `AIGuiders.AgentNotes.Core` → `NotesStorage.cs`: запись идёт через `File.WriteAllText(path, content, Encoding.UTF8)`, а `Encoding.UTF8` — кодировщик **с** BOM (его `GetPreamble()` = `EF BB BF`); парный «без BOM» — `new UTF8Encoding(false)`. Незаметно потому, что чтение там же идёт через `Encoding.UTF8`, а `ReadAllText` BOM **срезает**: изнутри цикл «прочитал без BOM → записал с BOM» выглядит одинаково. Механизм подтверждён и зондами живого MCP, и исходником **той сборки, что запущена** (`AgentNotes.Core 2.2.5+50f2d620`; `NotesStorage.cs` в ней не менялся). Мера: писать без BOM + тест «после записи BOM нет»; до этого — снимать побайтово (`EF BB BF`) после записи.
- **Утверждение о работающем коде — по коммиту из бинаря, не по соседнему чекауту.** Номер версии линию не доказывает: `ProductVersion`/`FileVersion` из dll даёт коммит (`2.2.5+50f2d620`), и уже по нему строка проверяется в исходниках. Соседний чекаут может быть на день новее сборки и с тем же номером версии (оплачено 2026-10-17).
- **Замер BOM ловит сам себя, если мерить культурой.** `StartsWith` со строкой из символа U+FEFF в .NET culture-sensitive: U+FEFF считается игнорируемым, и на чистом файле получаешь «BOM есть». Мерить побайтово или через `StringComparison::Ordinal`.
<!-- /section:ke-archive-order-and-doc-versioning-v1 -->

