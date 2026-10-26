---
type: Playbook
title: 'Playbook: First-contact attractor v1'
description: Cold habitat contact = **open → onboard scan → plan**, not unbound invent.
---
# Playbook: First-contact attractor v1

- tags: `#cdp` `#playbook` `#agent-operations` `#habitat`
- cite: cdp-mcp `.cdp/domain/onboard.md` · `man tool=first_contact`

## Rule

Cold habitat contact = **open → onboard scan → plan**, not unbound invent.

1. `cdp_open(path)` (or restore desk)
2. `go=onboard_desk` / `op=scan` — entrypoints + verticals + next[]
3. Follow tip (Open entrypoint / README) or `find_usages`
4. Only then `go=plan` / wave seed

## Desk wire

When `phase ∈ {explore, recall, clarify}` and no scan, desk `next[]` keeps `n-onboard` in **top-3** under Cap=8.

## Escape

Known repo + fresh scan already on disk → `op=scene` is enough; still prefer tip before invent.

