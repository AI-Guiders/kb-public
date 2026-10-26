---
type: Status
title: HCI Domain Status v1
description: Human-computer interaction baseline for interface usability, accessibility, cognitive load, and conversational interaction quality.
tags: [hci-ux-dx, status, worlds]
language: ru
world: hci
subworld: ux-dx
---
# HCI Domain Status v1


## Scope

Human-computer interaction baseline for interface usability, accessibility, cognitive load, and conversational interaction quality.

## Completion State

Status: **Done v1**

Completed artifacts:

- `playbook-hci-core.md`
- `map-hci-reading.md`
- `kb-hci-usability-and-dialog-rules.md`
- `kb-ui-ux-literature-evidence.md` — литературный синтез Norman / Nielsen / Shneiderman / Krug (классика UI/UX; пересечение с DE/DX при IDE)

## Definition of Done Check

- Core interaction contracts defined: done.
- Reading map and evidence routing defined: done.
- Operational rule set defined: done.
- Index/README linkage established: done.

## Active Guardrails

- Reduce cognitive load before adding process.
- Keep state visible and errors recoverable.
- Measure outcomes by user task success, not by ritual completion.

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

