# Evidence: OMG MDA Guide (2003) — Model-Driven Architecture

**Tags:** #software-case-workbench #paper-evidence #mda #omg #worlds

## Provenance

- source_refs:
  - primary: OMG (2003). *Model Driven Architecture (MDA) Guide Version 1.0.1*. Object Management Group. https://www.omg.org/cgi-bin/doc?omg/03-06-01.pdf
  - related: MOF, UML 2, CWM (contemporaneous OMG stack)
- created_at: 2026-08-30
- extraction_note: Норматив OMG guide; критический read обязателен — mass-market adoption ограничена.

## Metadata

- card_id: kb-omg-mda-2003-evidence-v1
- world: software.case-workbench
- layer: knowledge
- tags: [paper-evidence, mda, model-driven, case]
- status: active

## Epistemic linkage

- epistemic_basis: synthesis_from_primary_literature
- evidence_type: industry specification / guide
- confidence: **high** для того, что MDA **заявляло**; **high** что mass agile dev **не приняло** PIM→PSM как daily practice
- transfer_boundary: MDA transforms ≠ federation conformance CI; не копировать XMI/MOF stack
- falsification_trigger: если продукт требует «одна модель генерит всё» без test gate — повтор MDA failure mode

## Fundamentals

### K1 — Core idea

**PIM** (Platform-Independent Model) → transforms → **PSM** (Platform-Specific Model) → code/artifacts.

### K2 — Promised benefits

Portability, interoperability, maintenance via model centrality, automated consistency.

### K3 — Why it stalled (industry consensus)

- Transform tooling immature and vendor-specific
- Models drifted from code; **two SSOT** problem
- Agile favored code + tests over model maintenance
- ROI only clear in **regulated** / long-lifecycle domains

### K4 — What to salvage

**Separation of concerns** between contract (platform-neutral) and deployment-specific — родственник federation **hyperlane IR** vs planet implementation.

## Operationalization (Guiders)

| MDA concept | Federation analog |
|-------------|-------------------|
| PIM | Neutral IR, conformance schemas, MCPlane tiers |
| PSM | Planet-native port (Forge JS, CIDE .NET) |
| Transform | Conformance harness + agent maintenance, not XMI |
| Model repository | Git + generated manifests |

## Lifecycle

- related: `kb-kruchten-4plus1-1995-evidence.md`, `kb-case-fundamentals.md`

