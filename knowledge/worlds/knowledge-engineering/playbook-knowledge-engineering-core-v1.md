<!-- markdownlint-disable MD022 MD032 -->

# Knowledge Engineering Playbook v1

## Purpose

Meta-domain for transforming raw experience into reliable, reusable knowledge across all worlds.

## Scope
- Ingestion from transcripts, revisions, incidents, and experiments
- Normalization into consistent knowledge units
- Quality gates for promotion to canonical knowledge
- Lifecycle management: update, deprecate, archive
- Explicit linkage to epistemic methodology

## Relation to General Methodology
- This playbook is coupled to [`../../epistemic-playbook.md`](../../epistemic-playbook.md) and [`world-modeling-playbook.md`](world-modeling-playbook.md).
- Every promoted knowledge unit must include:
  - epistemic basis (`fact`, `inference`, `hypothesis`)
  - evidence type and source
  - confidence and uncertainty
  - falsification trigger
  - transfer boundary (where it applies / does not apply)

## Ingestion Pipeline
- Collect: extract candidate fragments from notes/revisions/transcripts.
- Classify: label as `incident`, `decision`, `pattern`, `anti-pattern`, `runbook`, `glossary`.
- Normalize: convert to a standard card format.
- Route: assign to world-layer playbook or router-layer playbook.
- Promote: add only units that pass quality gates.

## Normalization Contract
- Use structure: `context -> signal -> action -> outcome -> lesson`.
- Keep one card for one reusable unit of knowledge.
- Prefer operational language and measurable checks.
- Preserve provenance (where/when this came from).

## Promotion Quality Gates
- Repeatability: appears in more than one concrete case OR has strong first-principles support.
- Verifiability: has a practical check in real workflow.
- Boundary clarity: includes explicit applicability limits.
- Non-duplication: does not restate an existing card without added value.
- Operational value: reduces time-to-decision or failure rate.

## Deprecation and Archive Rules
- Mark as deprecated when falsified or superseded.
- Keep deprecated cards searchable with reason and replacement.
- Archive raw context; keep active playbooks concise.
- Preserve incident lineage for postmortem learning.

## Evidence and Confidence Contracts
- Evidence types: code/log trace, controlled experiment, official docs, repeated field observation.
- Confidence is not binary; keep explicit levels and revision date.
- High confidence without strong evidence is not promotable.
- Promote hypothesis only with clear validation plan.

## Operating Rhythm
- Micro: after significant task/incident, generate or update 1-3 cards.
- Weekly: deduplicate and reclassify overlapping cards.
- Biweekly: run deprecation review and boundary checks.
- Monthly: publish one KE delta summary.

## Metrics
- Time from incident to reusable card.
- Card reuse rate in future tasks.
- Duplicate-card rate.
- Deprecated-card rate with clear replacements.
- Reduction in repeated incident classes.

## Revisit Triggers
- Repeated rediscovery of the same solution.
- Growing archive with low retrieval value.
- Frequent misclassification between world-layer and router-layer.
- High confidence statements with weak provenance.

## Validation Snapshot v1 (Operational Evidence)

- Section-level updates (`upsert`) reduce risk compared to full overwrite in multi-agent, high-churn flows.
- Revision retention policy and periodic compacting are required to prevent archive bloat and retrieval slowdown.
- Hot-context-first loading with archive-on-demand improves continuity after context compression events.
- Index-first restoration (`knowledge-index -> playbook -> latest batch`) is more stable than chat-history reconstruction.

## Domain Definition Of Done (Knowledge Engineering)

Knowledge engineering meta-domain is "done v1" when:
- normalization template is stable (`templates/template-knowledge-card-v1.md`);
- KE playbook has explicit pipeline, gates, metrics, and evidence contracts;
- at least two large extraction batches exist and are index-linked;
- revision/retention hygiene is documented and routable;
- recovery path after compression is documented via artifact-first restoration.

<!-- markdownlint-enable MD022 MD032 -->

