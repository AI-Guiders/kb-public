---
type: Evidence Card
title: 'Evidence: Kruchten (1995) — The 4+1 View Model of Architecture'
description: 'Одна диаграмма не обслуживает всех stakeholders: разработчик, интегратор, performance engineer, клиент видят **разные срезы** одной системы.'
tags: [software-case-workbench, paper-evidence, kruchten, architecture, worlds]
language: ru
epistemic: synthesis_from_primary_literature
world: software
subworld: case-workbench
---
# Evidence: Kruchten (1995) — The 4+1 View Model of Architecture


## Provenance

- source_refs:
  - primary: Kruchten, P. (1995). The 4+1 view model of architecture. *IEEE Software*, *12*(6), 42–50. DOI [10.1109/52.469759](https://doi.org/10.1109/52.469759)
  - alternate: Kruchten, P. (2000). *The Rational Unified Process: An Introduction* (2nd ed.) — expanded 4+1 treatment
- created_at: 2026-08-30
- extraction_note: Карточка по опубликованной модели + широко цитируемым secondary summaries; line-level quotes — сверять с IEEE PDF при споре.

## Metadata

- world: software.case-workbench
- layer: knowledge
- tags: [paper-evidence, architecture-views, case, multi-view]
- status: active

## Epistemic linkage

- evidence_type: peer-reviewed article
- confidence: **high** для структуры пяти видов; **medium** для границ «что входит в logical view» в конкретных методологиях
- transfer_boundary: 4+1 описывает **software architecture presentation**, не org chart и не fleet ops напрямую — перенос через аналогию views (см. matrix-case-to-guiders-transfer)
- falsification_trigger: если Fleet/Planet/Live scopes не мапятся ни на один view + scenarios без ad hoc полей — пересмотреть scope model

## Fundamentals

### K1 — Problem

Одна диаграмма не обслуживает всех stakeholders: разработчик, интегратор, performance engineer, клиент видят **разные срезы** одной системы.

### K2 — Five views

| View | Stakeholders | Содержание |
|------|--------------|------------|
| **Logical** | End-user, analysts | Functionality, domain objects |
| **Process** | Integrators, performance | Concurrency, processes, tasks |
| **Development** | Programmers, build | Module organization, layers |
| **Physical** | System engineers, deploy | Nodes, networks, mapping |
| **+ Scenarios** | All | Use cases / stories **склеивают** views |

### K3 — Scenarios as glue

Scenarios (use cases) — **+1**: они валидируют согласованность между views и дают entry point для понимания.

### K4 — Notation independence

Views можно выражать UML или иначе; важна **роль view**, не конкретная нотация.

### K5 — CASE lineage

4+1 — интеллектуальный фундамент **multi-view workbench**: один estate, несколько synchronized projections — ядро CASE без привязки к Rose.

## Operationalization (Guiders)

| 4+1 view | Federation scope analogy |
|----------|--------------------------|
| Logical | Protocol semantics, hyperlane contracts |
| Development | Repo/module layout per planet |
| Process | CI waves, release trains, agent+human pair flow |
| Physical | Runners, registry, deploy targets (Live) |
| Scenarios | Briefing / conformance vectors («ship this pin» story) |

Fleet / Planet / Live — **operational zoom**, не копия 4+1 один-к-одному; 4+1 учит **не одним dashboard**.

## Lifecycle

- related: `kb-case-fundamentals.md`, `matrix-case-to-guiders-transfer.md`, GUIDERS-ADR-0023

