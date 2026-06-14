# Knowledge Engineering Knowledge Set v1 (Operations Rules)

Set: 20 cards.  
Focus: knowledge-engineering operational reliability (retention, section updates, restore protocol, archive discipline).

---

## Card 01
- card_id: KC-2026-02-26-159
- world: knowledge-engineering.operations
- epistemic_basis: `fact`
- confidence: `high`
- signal: full-file overwrite risks accidental memory loss in collaborative edits
- action: prefer section upsert or append for routine updates
- transfer_boundary: full write allowed only with read-merge-write guardrail

## Card 02
- card_id: KC-2026-02-26-160
- world: knowledge-engineering.operations
- epistemic_basis: `fact`
- confidence: `high`
- signal: section markers enable deterministic targeted updates
- action: keep stable `section_id` contracts for operational blocks
- transfer_boundary: marker drift invalidates automated upsert safety

## Card 03
- card_id: KC-2026-02-26-161
- world: knowledge-engineering.revisions
- epistemic_basis: `fact`
- confidence: `high`
- signal: revision volume grows rapidly in active multi-agent workflow
- action: enforce retention windows (keep-last/daily/weekly/monthly)
- transfer_boundary: retention must protect referenced audit anchors

## Card 04
- card_id: KC-2026-02-26-162
- world: knowledge-engineering.revisions
- epistemic_basis: `fact`
- confidence: `high`
- signal: uncontrolled archive growth reduces retrieval usability
- action: trigger compaction by threshold (count/size) with pre-summary
- transfer_boundary: never compact without preserving decision-critical lineage

## Card 05
- card_id: KC-2026-02-26-163
- world: knowledge-engineering.loading
- epistemic_basis: `fact`
- confidence: `high`
- signal: full archive load at chat start causes noise and slows routing
- action: load hot context first, fetch deep archive on explicit need
- transfer_boundary: deep pull only for missing facts/history

## Card 06
- card_id: KC-2026-02-26-164
- world: knowledge-engineering.loading
- epistemic_basis: `fact`
- confidence: `high`
- signal: context compression events break continuity in long threads
- action: restore via artifact path (index -> playbook -> latest batch)
- transfer_boundary: do not rely on chat memory as primary recovery source

## Card 07
- card_id: KC-2026-02-26-165
- world: knowledge-engineering.indexing
- epistemic_basis: `fact`
- confidence: `high`
- signal: new files without index linkage become practically invisible
- action: synchronize README + canonical knowledge-index on each batch
- transfer_boundary: batch is not complete until both indexes are updated

## Card 08
- card_id: KC-2026-02-26-166
- world: knowledge-engineering.indexing
- epistemic_basis: `inference`
- confidence: `medium`
- signal: long index blocks become hard to scan under pressure
- action: keep status artifact per domain for fast restart
- transfer_boundary: status artifact supplements, not replaces detailed index

## Card 09
- card_id: KC-2026-02-26-167
- world: knowledge-engineering.classification
- epistemic_basis: `fact`
- confidence: `high`
- signal: mixed-world cards reduce reusability and increase contradiction risk
- action: one card -> one world -> explicit transfer boundary
- transfer_boundary: cross-world fusion requires conflict note

## Card 10
- card_id: KC-2026-02-26-168
- world: knowledge-engineering.classification
- epistemic_basis: `inference`
- confidence: `medium`
- signal: operational and narrative fragments frequently co-mingle
- action: move narrative history to cold archive, keep hot layer operational
- transfer_boundary: narrative can return only with explicit task need

## Card 11
- card_id: KC-2026-02-26-169
- world: knowledge-engineering.quality-gates
- epistemic_basis: `fact`
- confidence: `high`
- signal: high-confidence claims appear with weak provenance
- action: block promotion without source and falsification trigger
- transfer_boundary: confidence cannot exceed evidence class

## Card 12
- card_id: KC-2026-02-26-170
- world: knowledge-engineering.quality-gates
- epistemic_basis: `fact`
- confidence: `high`
- signal: duplicate cards emerge during rapid batching
- action: run periodic dedupe with supersedes/superseded_by fields
- transfer_boundary: dedupe cannot delete unique boundary information

## Card 13
- card_id: KC-2026-02-26-171
- world: knowledge-engineering.multi-agent
- epistemic_basis: `fact`
- confidence: `high`
- signal: concurrent edits by rotating agents create race-like update risks
- action: favor additive updates + section upserts over monolithic rewrites
- transfer_boundary: monolithic rewrite requires explicit lock/protocol

## Card 14
- card_id: KC-2026-02-26-172
- world: knowledge-engineering.multi-agent
- epistemic_basis: `inference`
- confidence: `medium`
- signal: trust-driven "continue without stopping" mode increases throughput and drift risk
- action: pair large batches with strict completion checklist
- transfer_boundary: speed mode invalid without post-batch sync checks

## Card 15
- card_id: KC-2026-02-26-173
- world: knowledge-engineering.restore
- epistemic_basis: `fact`
- confidence: `high`
- signal: environment-level context compression can feel like abrupt reset
- action: maintain compact domain-status artifacts for deterministic restart
- transfer_boundary: status must be updated before declaring domain done

## Card 16
- card_id: KC-2026-02-26-174
- world: knowledge-engineering.restore
- epistemic_basis: `fact`
- confidence: `high`
- signal: restoration from transcript alone is costly and noisy
- action: prioritize canonical notes and indexed knowledge files as source of truth
- transfer_boundary: transcript mining reserved for unresolved ambiguity

## Card 17
- card_id: KC-2026-02-26-175
- world: knowledge-engineering.evidence
- epistemic_basis: `fact`
- confidence: `high`
- signal: operational lessons emerge from tool traces, not only prose
- action: treat tool-call history as first-class provenance
- transfer_boundary: untraceable claims remain provisional

## Card 18
- card_id: KC-2026-02-26-176
- world: knowledge-engineering.evidence
- epistemic_basis: `inference`
- confidence: `medium`
- signal: archive extract quality depends on focused query strategy
- action: use targeted keyword passes and normalize into cards
- transfer_boundary: broad sweep without normalization is not promotable

## Card 19
- card_id: KC-2026-02-26-177
- world: knowledge-engineering.governance
- epistemic_basis: `fact`
- confidence: `high`
- signal: domain closure without maintenance policy leads to silent decay
- action: add refresh triggers and handoff statement per domain
- transfer_boundary: closure status expires without refresh cadence

## Card 20
- card_id: KC-2026-02-26-178
- world: knowledge-engineering.governance
- epistemic_basis: `fact`
- confidence: `high`
- signal: cleanup pressure appears after rapid expansion
- action: split "finish domain" and "cleanup pass" into separate phases
- transfer_boundary: no structural cleanup during active evidence ingestion

---

## Source Footing

- Archive revision extracts (retention, revision hygiene, layered loading).
- Tool-trace patterns from long operational transcript (append/upsert/restore behavior).
- Operational incidents around context compression and recovery workflow.

