---
type: Transfer Matrix
title: Aviation investigation → SE / Platform — transfer matrix v1
description: '**Назначение:** перенос **духа расследования** из авиации в software/platform ops — сильнее, чем типичный retro.'
tags: [aviation-human-factors, matrix, worlds, investigation, transfer, guiders]
language: ru
world: aviation
subworld: human-factors
---
# Aviation investigation → SE / Platform — transfer matrix v1


**Назначение:** перенос **духа расследования** из авиации в software/platform ops — сильнее, чем типичный retro.

**Связь:** [`kb-aviation-incident-investigation-fundamentals.md`](kb-aviation-incident-investigation-fundamentals.md) · pain inventory · ADR-0023 · fleet thesis · **habitat procedure:** [`../../domains/agent-operations/playbook-habitat-incident-investigation.md`](../../domains/agent-operations/playbook-habitat-incident-investigation.md)

---

## Transfer contract

- Переносим **принципы** (layers, independence, recommendations, just culture), не FAA/ICAO compliance theater.
- `epistemic_basis` на findings: fact / inference / hypothesis.
- См. [`matrix-do-not-transfer.md`](../knowledge-engineering/matrix-do-not-transfer.md).

---

## Matrix

| Aviation investigation | Transferable core | SE / Guiders example | Boundary |
|------------------------|-------------------|----------------------|----------|
| **Annex 13 independence** | Investigator ≠ same chain of command | Drift CI, external conformance repo, agent as clerk not judge of self | Not full NTSB legal status |
| **Safety objective** | Learn, not punish first | Pain → ADR, not «кто накосячил» Slack thread | Negligence still accountable |
| **Swiss cheese / HFACS** | Multi-layer causation | TP + CI + alliance + human merge aligned | Don't over-formalize HFACS codes |
| **Mandatory reporting** | Near-miss valuable | G-xxx/N-xxx open on friction, not only prod fire | Avoid reporting fatigue |
| **Recommendations tracking** | AD/SB equivalent | ADR + roadmap wave + alliance row updated | Track closure |
| **Public reports** | Industry learns | Public federation docs, conformance specs | No secrets in public KB |
| **LOSA / proactive** | Observe normal ops | Adoption drift gate before release | Not surveillance culture |
| **Just Culture** | Error vs reckless | Pair «ошиблись — поправим» vs repeated negligence | No blamelessness shield |
| **Readback of findings** | Shared mental model | Briefing before ship; investigation summary to pair | Not bureaucracy on every bug |

---

## SE postmortem vs aviation (честное сравнение)

| | Blameless retro (SRE) | Aviation investigation | Guiders target |
|---|----------------------|------------------------|----------------|
| Depth | Often technical stack | Org + human + tech | Pain + layers in ADR |
| Independence | Weak | Strong | Machine drift CI + constitution |
| Near-miss | Optional | Systemic capture | Pain inventory |
| Output | Action items | Recommendations + regulation | ADR + wave + conformance |
| Pair | Rare | CRM in cockpit | human+agent PM/PF review |

**Цель:** ближе к aviation **духу**, чем к «five whys до одного root cause».

---

## Product hooks (Wave 6+)

- **Investigation briefing** view: layers diagram for incident (CASE MFD)  
- **EICAS** after near-miss cluster (aviation displays)  
- **Recommendation tracker**: pain closed ↔ ADR ↔ pin  

---

## Version

v1.0 — 2026-08-30

