---
type: Evidence Card
title: Drosophila melanogaster — Филогенетика и геномы видов (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, genomes, simulans-complex, rearrangements, phylogenetics]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Филогенетика и геномы видов (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Evolution of genome structure in the Drosophila simulans species complex» — Genome Research 2021, DOI 10.1101/gr.263442.120, PMC7919458 — **полный текст прочитан** (assembly, rearrangements, tRNA, Y-chromosome, SVs)
  - annotation: «Analysis of 30 chromosome-level Drosophila genome assemblies...» — Genome Biol 2025 (центромерные сателлиты) — аннотация
  - related: Drosophila 12 Genomes Consortium (2007) — цитирована
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: перестройки/tRNA/Y); филогенетическое дерево видов — частично (общеизвестно: melanogaster group, 3-6 млн лет).

## Metadata
- card_id: kb-drosophila-species-genomes-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [genomes, simulans-complex, inversions, rearrangement, evolution]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (перестройки/структура — Genome Res 2021)
- uncertainty:
  - филогенетические даты (дивергенция видов) — не извлечены числом (общая оценка ~2-6 млн лет — классика)
  - 30 assemblies (Genome Biol 2025) — аннотация
- falsification_trigger:
  - если оценки перестроек изменятся (новые ассамблеи) — обновить
- transfer_boundary:
  - НЕ переносить в CASA: это эволюция генома; НО: «скорость перестроек ~90/млн лет (mel↔sim) и 226-354/млн лет (внутри sim-комплекса)» — для слоя 6 (эволюция), не для архитектуры

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: комплекс видов, перестройки, Y/tRNA.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Genome Res 2021 (полный текст в .cdp/scratch/PMC7919458.xml).

## Core Unit
- context:
  - близкие виды (sim-комплекс) и их геномы: как быстро меняется структура.
- signal:
  - вопрос «какие виды рядом», «как геномы различаются», «скорость эволюции структуры».
- action:
  - использовать: D. melanogaster + sim-комплекс (D. simulans, D. mauritiana, D. sechellia) — de novo ассамблеи (PacBio); 535–542 перестройки mel↔sim (~90/млн лет), 113–177 внутри (~226–354/млн лет); 95% в гетерохроматине; в эухроматине — X-связные (63% между; 12/13 внутри); инверсии: 23/25/21 (sim/mau/sec); In(3R)84F1–93F6 (13.6 Mb, mel-specific, Sturtevant 1926); 9 общих инверсий (4 — у yakuba/ananassae → линия melanogaster); tRNA 295–303, 4 антикодон-сдвига; Y: 70–80% экзонов восстановлено, дупликации (41 от других хромосом, 22 общие), ARY >3 копий у sechellia/mauritiana; Wolbachia (полные геномы mau/sec).
- outcome:
  - геномная структура быстро меняется (перестройки, X-обогащение), но синтения/гены консервативны; близкие виды — «модель» видообразования.
- lesson:
  - близкие виды демонстрируют **быструю структурную эволюцию при консервативной функциональной основе** — для CASA: изменчивость/эволюция в рамках инвариантов.

## Fundamentals (самодостаточный опорный слой)

### 1) Виды и геномы
- D. melanogaster + sim-комплекс (simulans/mauritiana/sechellia) — de novo (PacBio), Wolbachia/митохондриальные геномы.
- 30+ хромосомных ассамблей Drosophila (Genome Biol 2025 — аннотация; центромерные сателлиты).

### 2) Перестройки
- mel↔sim: 535–542 (~90/млн лет); внутри: 113–177 (226–354/млн лет).
- 95% — гетерохроматин; эухроматин — X (63% / 12 из 13).
- Инверсии: 23 (sim), 25 (mau), 21 (sec); In(3R) 13.6 Mb — mel-specific (Sturtevant 1926, подтверждено); 9 общих (4 — у yakuba/ananassae, 5 — только sim); парные: sim-mau 5, sim-sec 3, mau-sec 4.
- 460-kb X-инверсия (sec+mau, 45 генов).

### 3) tRNA и Y-хромосома
- tRNA: 295 (mel) – 303 (sec); 4 антикодон-сдвига (аллоакцепторные); предыдущие «потери» — артефакты ассамблей.
- Y: 66/58/64 из 83 экзонов (70–80%); дупликации (41; 22 общие; ARY >3 у sec/mau); Ppr-Y — единственный без дупликаций.

## Operationalization
- first_adoption_task: слой 6 (филогенетика/геномы): структура/перестройки; при CASA — «инварианты vs изменчивость».
- validation_check: даты дивергенции — TODO (классика 2–6 млн лет); филогения группы melanogaster — TODO.
- success_criterion: карточка покрывает 6.1 (филогенетика/геномы видов) с полным текстом.
- rollback_or_mitigation: при новых ассамблеях — обновить.

## Lifecycle
- deprecation_reason: —

