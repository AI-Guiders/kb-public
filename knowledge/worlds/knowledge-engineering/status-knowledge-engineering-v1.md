# Knowledge Engineering Domain Status v1

## Scope

Meta-domain for transforming volatile operational experience into durable, reusable knowledge assets.

## Completion State

Status: **Done v1**

Completed artifacts:

- `playbook-knowledge-engineering-core-v1.md`
- `templates/template-knowledge-card-v1.md`
- `kb-knowledge-engineering-mixed-worlds-rules-v1.md`
- `kb-knowledge-engineering-multiworld-rules-v1.md`
- `kb-knowledge-engineering-culture-routing-rules-v1.md`
- `kb-knowledge-engineering-country-conflicts-rules-v1.md`
- `kb-knowledge-engineering-operations-rules-v1.md`
- `personal/bookshelf-corpus-vs-router-gaps-v1.md` (личный снимок корпуса vs роутер; personal-слой, не публичный дефолт)
- `matrix-culture-routing-v1.md`
- `matrix-do-not-transfer-v1.md`

## Definition of Done Check

- Ingestion pipeline and quality gates: done.
- Card normalization template: done.
- World separation and transfer boundaries: done.
- Multi-batch evidence corpus: done.
- Semantic-primary migration (batch-01..04 + digest lineage): done.
- Index synchronization to canonical notes: done.

## Active Guardrails

- Новые/правки **любого** `worlds/<slug>/` под kb-public: **`playbook-kb-world-public-authoring-v1.md`** (без scope, `work/`, внутренних брендов, машинных путей).
- Artifact-first restore after compression (`index -> playbook -> latest batch -> status`).
- Section-level update preference over full overwrite for routine operations.
- Revision retention/compaction policy is mandatory.
- One card = one reusable unit, one primary world.

## Maintenance Policy

- Refresh cadence: periodic operational review (biweekly/monthly depending on churn).
- Triggered refresh:
  - repeated duplicate-card growth,
  - restore failures after compression,
  - retention threshold breaches,
  - repeated cross-world misclassification.

## Alias Window

Closed. Legacy aliases were retired after semantic-primary stabilization.

## Next Domain Handoff

Knowledge engineering meta-domain closed at v1.  
Next step: naming/index cleanup reduction and alias retirement by maintenance cycle.
