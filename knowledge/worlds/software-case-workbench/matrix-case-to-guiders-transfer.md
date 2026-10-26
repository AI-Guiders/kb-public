---
type: Transfer Matrix
title: CASE → Guiders Platform — transfer matrix v1
description: '**Назначение:** что **брать** из CASE-наследия в продукт; что **не повторять**; mapping на federation primitives.'
tags: [software-case-workbench, matrix, worlds, case, guiders, transfer]
language: ru
world: software
subworld: case-workbench
---
# CASE → Guiders Platform — transfer matrix v1

**Назначение:** что **брать** из CASE-наследия в продукт; что **не повторять**; mapping на federation primitives.

**Связь:** [`kb-case-fundamentals.md`](kb-case-fundamentals.md) · ADR-0023 · три столпа (Aviation = pair; Agent Env = CDP; **CASE = этот matrix**)

---

## Принцип переноса

Брать **posture и дисциплину**, не **нотацию и vendor lock-in**:

- ✅ multi-view, traceability, briefing, desktop workbench, impact before ship  
- ❌ UML as SSOT, Rose DB, NL→formal, ceremony gates, «model или код»

---

## Матрица

| CASE concept | Брать? | Guiders mapping | Anti-pattern |
|--------------|--------|-----------------|--------------|
| **Architecture model** | ✅ | Adoption alliance, hyperlane graph, planet topology | Hand-drawn UML only |
| **4+1 views** | ✅ | Fleet / Planet / Live scopes | One dashboard KPI |
| **Repository** | ✅ | Git + generated MD/specs + CI validator | Proprietary Rose DB |
| **Round-trip** | ✅ | Conformance `*.spec.json`, drift CI, pin ↔ reality | Fragile codegen only |
| **Impact analysis** | ✅ | Release briefing (pins, pains, alliance row) | «Спроси чат» |
| **Traceability** | ✅ | G-xxx/N-xxx → ADR → package wave | Jira orphan links |
| **Reverse engineering** | ✅ | AdoptionReport scan, registry audit | One-time diagram |
| **Upper CASE (design)** | ✅ | Vision/Decision Environment | BDUF quarter gate |
| **Lower CASE (codegen)** | ⚠️ selective | Agent drafts code; human+pair review | Model→prod без test |
| **Process enactment** | ❌ as core | Roadmap waves — light, not Marvel rules | «Нельзя merge пока…» |
| **MDA transforms** | ❌ v1 | Machine vectors + tests, not PIM/PSM XMI | OMG enterprise cosplay |
| **Web dashboard** | ❌ as workbench | ANPM ingress slice only | «Fleet ops in browser» |

---

## Три столпа — кто что закрывает

| Потребность CASE-эры | Столп | Примитив |
|----------------------|-------|----------|
| Видеть estate | **CASE** | Scopes, graph, briefing |
| Держать модель честной | **Agent Env** + CI | Agent maintains vectors; gates judge |
| Не утонуть в индикации | **Aviation** | PM/PF pair, PFD/MFD/EICAS |
| Провод пары | **MCPlane** | Pulse, `next[]`, tiers |

---

## Rose → Federation (конкретная таблица)

| Rational Rose / CASE promise | Federation now |
|------------------------------|----------------|
| Class / component diagram | Package + hyperlane dependency graph |
| Use case | Pain inventory item → user outcome |
| Sequence (interaction) | Conformance invocation vectors |
| State machine | Planet lifecycle / release train (informal) |
| Requirements trace | Pain → ADR → commit |
| Model check | Conformance harness red/green |
| Team repository | Git monorepos + generated alliance |
| Workbench UI | CIDE/Glass embassy (Wave 6) |

---

## Do-not-transfer (из historiography + CASE)

См. также [`matrix-do-not-transfer.md`](../knowledge-engineering/matrix-do-not-transfer.md) (KE global).

| Исторический провал | Наш контроль |
|---------------------|--------------|
| Capture tax (IBIS) | Promote on strong Δ; seed gather low quality OK |
| Framework tax (IPSE) | Hyperlanes, not mega-APSE |
| Expert system | Assistant under human+agent pair |
| NL→formal end-to-end | Specs + tests, not chat→UML |
| Model wallpaper | Drift = EICAS; dark cockpit when synced |
| Post-incident shallow root cause | Pain→ADR with **layer map** (Reason); investigation briefing |

---

## Открытые вопросы (product)

1. Graph-native (alliance) vs table-native (pain) — default MFD?  
2. Явные IBIS edges в cards или достаточно Fact/Hypothesis?  
3. Minimum L2 slice to accept ADR-0023?

