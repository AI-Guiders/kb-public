---
type: Evidence Card
title: 'Evidence: Keremane et al. (2026) — synthetic DNA + quasi-2D perovskite memristors'
description: '*Версия: v1.0 · 2026-08-25 — abstract+secondary*'
tags: [kb, computing-hardware-substrate, worlds, paper-evidence, memristor, dna, perovskite, nvm]
world: computing
subworld: hardware-substrate
---

# Evidence: Keremane et al. (2026) — synthetic DNA + quasi-2D perovskite memristors

## Provenance
- source_refs:
  - primary: Keremane, K. S., Zheng, L., Wu, H., Zheng, J., Priya, S., Ravi, C. C., Yennawar, N. H., Gorthy, A., Jha, R., & Poudel, B. (2026). Molecularly Engineered Highly Stable Memristors with Ultra-Low Operational Voltage: Integrating Synthetic DNA with Quasi-2D Perovskites. *Advanced Functional Materials*. https://doi.org/10.1002/adfm.202530539
  - secondary: [Penn State news (2026-02-24)](https://www.psu.edu/news/research/story/borrowing-biology-power-next-gen-data-storage) · [Popular Science (2026-08-24)](https://www.popsci.com/technology/lab-made-dna-memory-storage/) · [ScienceDaily summary](https://www.sciencedaily.com/releases/2026/08/260816044853.htm)
  - text_consulted: **abstract + publisher page + institutional press** (2026-08-25); full PDF not fetched
- created_at: 2026-08-25
- updated_at: 2026-08-25
- extraction_note: Лабораторный bio-hybrid **memristor** (NVM), не продукт и не «память в каждой биоклетке». Отделить от трека **DNA data storage** (кодирование файлов в синтезированных цепях).

## Metadata
- card_id: kb-computing-hardware-substrate-keremane-2026-dna-perovskite-memristor-evidence-v1
- world: computing.hardware-substrate
- layer: knowledge
- tags: [paper-evidence, keremane-2026, memristor, synthetic-dna, perovskite, nvm, neuromorphic, low-power, storage-density, penn-state]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article (journal) + institutional press release
- evidence_type: materials science · device characterization (lab arrays)
- confidence: **medium-high** для заявленных параметров устройства в статье; **low** для переноса «в робота завтра»; **high** для направления (bio-hybrid NVM, ultra-low V)
- read_depth: **abstract+secondary** (full PDF pending)
- transfer_boundary: hardware → CASA / autonomous carrier **allow-with-check** (long-horizon dense NVM; не замена `ltm/` / field JSON v1)
- falsification_trigger: independent replication не воспроизводит ON/OFF, endurance или стабильность; или коммерческий NVM без DNA слоя достигает тех же метрик дешевле

## Core Unit
- context: рост AI → нужны **плотнее и экономнее** устройства памяти; биология (ДНК) и электроника (перовскит) плохо стыкуются.
- signal: **синтетическая** короткая ДНК (не «мокрые спагетти» нативной ДНК) + Ag-дoping + quasi-2D halide perovskite → **резистивное переключение** при сверхнизком напряжении.
- action: memristor array `Ag / (PEA)₂(MA)Pb₂I₇ / AgNP-DNA / Pt`; operating voltage **<0.1 V**; forming-free; store/process colocation (нейроморфный мотив).
- outcome (paper claims): ON/OFF **>10⁵**; endurance **~10³** cycles; retention **>4×10³ s**; **>6 weeks** ambient stability; работа до **~250 °F**; power **~100× ниже flash** (press); плотность выше flash (qualitative in press).
- lesson: **комбинация** DNA+perovskite сильнее каждого по отдельности; программируемая наноструктура ДНК как **мост** между information-density биологии и электроникой.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | **Два разных «ДНК-памяти»:** (A) *DNA data storage* — биты в синтезированных олигонуклеотидах, read/write через синтез/секвенирование; (B) *этот чип* — ДНК как **компонент электронного NVM** (мемристор), не архив файлов в цепочках. |
| **K2** | Теоретическая плотность **информации в ДНК** (~215 млн ГБ/г) — предел **носителя битов в природе**; **этот девайс** не доказывает достижение этого предела в кремниевом смысле — использует **архитектурный** принцип плотной упаковки. |
| **K3** | Синтетическая **22-mer** ДНК с Ag nanoparticles: проводимость + порядок на наношкале; перовскит `(PEA)₂(MA)Pb₂I₇` (quasi-2D OHP, n=2) — каналы тока; гибрид стабилизирует RS. |
| **K4** | **Ultra-low V (<0.1 V)** vs ~120 V бытовой сети — релевантно **edge / embodied** питанию от малых источников (батарея, генератор, fuel→steam→gen). |
| **K5** | **Neuromorphic framing:** memristor помнит направление/историю тока после снятия питания → хранение и обработка **в одной точке** (аналог синапса); не доказательство «как мозг», а инженерный мотив. |
| **K6** | Ограничения v1 lab: недели стабильности, 10³ циклов endurance — **далеко** от datacenter SSD lifetime; patent filed; масштабирование TBD. |
| **K7** | Для автономного носителя узкое место смещается: **не «откуда ватты»** (генератор на колёсиках), а **КПД вычисления + дешёвая плотная NVM** для линии/архива без облака (см. essay #9 `just-being-without-justification`). |

### Цифры (из статьи / abstract; сверять с PDF)
| Параметр | Значение |
|----------|----------|
| Operation voltage | **<0.1 V** |
| Power density (claimed) | **0.01 W/cm²** (order; см. full paper) |
| ON/OFF ratio | **>10⁵** |
| Endurance | **10³** cycles |
| Retention | **>4×10³ s**; **>6 weeks** ambient |
| Temperature | stable to **~250 °F** (~121 °C) press |
| vs flash (press) | **~100×** less power; higher density (qualitative) |

### Ограничения
- Full paper not line-audited in KB yet — цифры из abstract/publisher; press «100×» может округлять.
- Не путать с клинической/биологической «памятью в клетке».
- Не аргумент за «душу в ДНК» — только материаловедение.

## Operationalization (CASA / carrier hypothesis only)
- first_adoption_task: **watch** — включить в horizon scan при оценке life-archive / field snapshot NVM (ADR-0068 memory zone infrastructure).
- validation_check: при появлении dev-kit — bench: joules/bit retain vs `field_state.json` export + `ltm/` shard I/O.
- success_criterion: порядок величины снижения ватт на retained state при сопоставимой ёмкости линии агента (не квалиа, не consciousness).
- rollback_or_mitigation: до коммерции — остаёмся на git + disk + seat registry (HIS); DNA-NVM = optional future leg.

## Lifecycle

## Связанные материалы
- Index: [`kb-computing-hardware-substrate-scientific-evidence.md`](kb-computing-hardware-substrate-scientific-evidence.md)
- CASA bridge: [`../../work/projects/door-to-singularity/ca-substrate-agent/kb-carrier-substrate-dna-perovskite-memristor-horizon.md`](../../work/projects/door-to-singularity/ca-substrate-agent/kb-carrier-substrate-dna-perovskite-memristor-horizon.md)
- CASA ADR: `casa-ontology-payload/design/CASA-ADR-0068-memory-zone.md` (Related · substrate horizon)

*Версия: v1.0 · 2026-08-25 — abstract+secondary*

