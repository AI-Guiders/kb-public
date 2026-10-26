---
type: Status
title: PR Review Domain Status v1
description: 'Operational pull request review quality: risk-first reading, verification sufficiency, and merge safety.'
tags: [collaboration-git-pr, status, worlds]
language: en
world: collaboration
subworld: git-pr
---
# PR Review Domain Status v1


## Scope

Operational pull request review quality: risk-first reading, verification sufficiency, and merge safety.

## Completion State

Status: **Done v1**

Completed artifacts:

- `playbook-pr-review.md`
- `kb-pr-review-risk-rules.md`

## Definition of Done Check

- Risk-first review flow defined: done.
- Minimal reviewer/author contracts defined: done.
- High-impact rule set defined: done.
- Index/README linkage established: done.

## Active Guardrails

- Behavior and safety risks take priority over style nits.
- No merge with unresolved high-severity risk.
- Evidence beats confidence when uncertain.

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

