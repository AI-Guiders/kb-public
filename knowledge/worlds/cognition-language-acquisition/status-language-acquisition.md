---
type: Status
title: Child language acquisition (L1) — status v1
description: 'Empirical и теоретический контур **усвоения первого языка ребёнком**: child-directed speech, типы feedback, lexical mapping (conventionality, contrast, context). **Не** CLD/SLP клиника; **не** CASA teacher/sleep spec.'
tags: [cognition-language-acquisition, status, worlds]
world: cognition
subworld: language-acquisition
---
# Child language acquisition (L1) — status v1


## Scope

Empirical и теоретический контур **усвоения первого языка ребёнком**: child-directed speech, типы feedback, lexical mapping (conventionality, contrast, context). **Не** CLD/SLP клиника; **не** CASA teacher/sleep spec.

## Completion state

Status: **Done v1 (full pass on available PDFs; 2 paywall gaps)**

Artifacts:

- [`README.md`](README.md) — мир `cognition.language-acquisition`
- [`kb-language-acquisition-fundamentals.md`](kb-language-acquisition-fundamentals.md)
- [`kb-language-acquisition-scientific-evidence.md`](kb-language-acquisition-scientific-evidence.md)
- [`playbook-language-acquisition-operational.md`](playbook-language-acquisition-operational.md)
- [`matrix-language-acquisition-transfer.md`](matrix-language-acquisition-transfer.md)
- Evidence (per paper): [`kb-language-acquisition-snow-1972-evidence.md`](kb-language-acquisition-snow-1972-evidence.md), [`kb-language-acquisition-snow-1977-evidence.md`](kb-language-acquisition-snow-1977-evidence.md), [`kb-language-acquisition-demetras-1986-evidence.md`](kb-language-acquisition-demetras-1986-evidence.md), [`kb-language-acquisition-saxton-1997-evidence.md`](kb-language-acquisition-saxton-1997-evidence.md), [`kb-language-acquisition-clark-lexicon-principles-evidence.md`](kb-language-acquisition-clark-lexicon-principles-evidence.md)

## Guardrails

- Не импортировать findings в CASA `correction_kind` / sleep bench без engineering bridge.
- Указывать **read_depth** (full / partial / abstract) — см. scientific-evidence index. **partial** = не abstract-only, но PDF не целиком (paywall).
- Спорные зоны (motherese correlations, universal negative evidence) — **debate**, не «прописная истина».

## Router

- Domain Entry Map: `index-knowledge-router.md` · Child language acquisition (L1)

*Версия: v1.0 · 2026-05-31*

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

