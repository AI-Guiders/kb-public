# Evidence: Brown & McDermid (1992) — Learning From IPSE's Mistakes

**Tags:** #software-case-workbench #paper-evidence #ipse #case #worlds

## Provenance

- source_refs:
  - primary: Brown, A. W., & McDermid, J. A. (1992). Learning from IPSE's mistakes. *IEEE Software*, *9*(2), 22–28. DOI [10.1109/52.121777](https://doi.org/10.1109/52.121777)
  - context: IPSE (Integrated Project Support Environment), PCTE, Stoneman/APSE lineage
- created_at: 2026-08-30
- extraction_note: Ключевые тезисы по статье и цитированию в SE literature; детальные таблицы IPSE projects — в полном PDF.

## Metadata

- card_id: kb-brown-ipse-mistakes-1992-evidence-v1
- world: software.case-workbench
- layer: knowledge
- tags: [paper-evidence, ipse, integration, case-failure]
- status: active

## Epistemic linkage

- epistemic_basis: synthesis_from_primary_literature
- evidence_type: peer-reviewed retrospective / lessons learned
- confidence: **high** для диагноза «framework без семантики»; **medium** для обобщения на все integrated environments
- transfer_boundary: статья про **1980s IPSE**, не про git-native monorepo 2026 — перенос принципов, не буквальная архитектура
- falsification_trigger: если federation hyperlanes превращаются в обязательный mega-framework без escape hatch — повтор IPSE mistake

## Fundamentals

### K1 — IPSE dream

Единая среда: общий object management (OMS), tool bus, process support — **все инструменты** через одну интегрированную платформу.

### K2 — What went wrong

| Mistake | Lesson |
|---------|--------|
| **Integration = shared datastore** | Файлы/объекты в одном repo **≠** semantic integration |
| **Framework before tools** | Платформа съела бюджет до ценности для разработчика |
| **Process language as gate** | Enactment хрупок; люди обходят |
| **Vendor / standards gridlock** | PCTE interoperability на бумаге, friction в жизни |
| **Ignored how devs actually work** | Лёгкие **toolsets** победили тяжёлые IPSE |

### K3 — What survived

Идея **lifecycle memory** и tool integration — в ALM, IDE plugins, CI — но **победила модульность**, не обязательный APSE.

### K4 — Brown/McDermid prescription (сжато)

Интеграция должна быть **семантической** (meaning, relationships, consistency rules), **incremental**, и **optional** — не «войти в среду или уйти».

## Operationalization (Guiders)

| IPSE mistake | Federation antidote |
|--------------|---------------------|
| Mega-environment | Planets sovereign; hyperlanes optional pin |
| OMS without meaning | Typed IR + conformance specs, not «one DB» |
| Framework tax | L1 machine telemetry before L3 workbench UI |
| Mandatory process | Pain→ADR waves, not Marvel enactment |
| Embassy as capital | Forge/CIDE prove lane; no planet is law |

## Lifecycle

- related: `note-cognitive-se-environments-historiography-v0.md` (ветвь B), `kb-case-fundamentals-v1.md`, Constitution «neighbors not war»

