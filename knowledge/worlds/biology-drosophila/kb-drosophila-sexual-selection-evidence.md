---
type: Evidence Card
title: 'Drosophila melanogaster — Половой отбор: эволюция и механизмы (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, sexual-selection, polyandry, fitness, dsx-fru]
language: ru
epistemic: fact (из полного текста)
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Половой отбор: эволюция и механизмы (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Sexual selection, genomic evolution and population fitness in Drosophila pseudoobscura» — Proc R Soc B 2025, DOI 10.1098/rspb.2024.2744, PMC11961267 — **полный текст прочитан** (эволюционный эксперимент: Enhanced Polyandry vs Enforced Monogamy; Fst, π, DFE)
  - paper: G3 2025 (карточка 5.1) — песня QST>FST (половой отбор на песню)
  - related: Nature 2026 (1.5) — dsx/fru (половой диморфизм), cVA
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: Fst/π/DFE); поведенческие механизмы (полиандрия vs моногамия — дизайн) — частично.

## Metadata
- world: biology.drosophila
- layer: world
- tags: [sexual-selection, polyandry, monogamy, fst, dfe, pseudoobscura]
- status: draft

## Epistemic Linkage
- evidence_type: paper (ориг., полный текст)
- confidence: high (Fst/π/DFE — Proc R Soc B 2025)
- uncertainty:
  - «полиандрия улучшает/ухудшает фитнес» — в тексте: E-линии эффективнее пургуют на 3/4, M — на X (естественный отбор) — интерпретация нюансна
  - конкретные гены под отбором — частично
- falsification_trigger:
  - если эволюционный эксперимент не воспроизведён — обновить (одна система)
- transfer_boundary:
  - НЕ переносить в CASA: половой отбор — эволюционный процесс; НО: «песня — под отбором (QST>FST, 5.1)» + «dsx/fru — генетическая основа диморфизма (1.5)» — для слоя 6: поведение эволюционирует через отбор на конкретные гены

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: эксперимент, Fst/π, DFE.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Proc R Soc B 2025 (полный текст в .cdp/scratch/PMC11961267.xml).

## Core Unit
- context:
  - половой отбор: эволюционные эксперименты (полиандрия vs моногамия) — геномные последствия.
- signal:
  - вопрос «как половой отбор влияет на геном/фитнес», «полиандрия полезнее моногамии?».
- action:
  - использовать: D. pseudoobscura, линии Enhanced Polyandry (M — «monogamy»? в тексте M=E? — уточнить: M = Enforced Monogamy, E = Enhanced Polyandry); G85→G200: **Fst ↑ (пики >0.25: хр.3 22.5–23.5 Mb, X, новая зона хр.4 3.65–13.65 Mb)**; **π ↓** (3:22.5–23.5, XL, XR — сильный отбор); **DFE**: E — эффективнее пургут на 3/4; M — на X (естественный отбор может объяснить); результаты — эволюция генома за ~115 поколений.
- outcome:
  - режим полового отбора (полиандрия/моногамия) меняет генетический ландшафт (Fst/π/DFE) — отбор оставляет следы; взаимодействие полового/естественного отбора.
- lesson:
  - половой отбор — **экспериментально наблюдаемый** процесс с геномными следами; поведение (спаривание) — мишень отбора (связь с 5.1: песня) — для CASA: поведенческие программы — под давлением отбора (эволюционируемы).

## Fundamentals (самодостаточный опорный слой)

### 1) Эксперимент
- D. pseudoobscura: линии «Enforced Monogamy» (M) vs «Enhanced Polyandry» (E); Illumina 30×; G85 и G200 (115 поколений эволюции).

### 2) Геномные следы
- Fst: ↑ G85→G200; пики >0.25: 3:22.5–23.5 Mb (конец хромосомы 3), X (XL/XR), новая 4:3.65–13.65 Mb.
- π: ↓ (3:22.5–23.5; XL; XR) — консистентно с отбором; различия между M/E.
- DFE: E — ↓доля делеций на 3/4 (пургинг эффективнее); M — ↓на X (возможно, естественный отбор).

### 3) Связь с поведением
- Песня: QST>FST (5.1) — направленный отбор на pulse mode; dsx/fru — генетическая основа диморфизма (1.5); cVA/феромоны (1.5).

## Operationalization
- first_adoption_task: слой 6 (половой отбор): эксперимент/следы; при CASA — «поведение — мишень отбора».
- validation_check: гены под отбором (кандидаты) — TODO; поведенческие механизмы (полиандрия) — TODO.
- success_criterion: карточка покрывает 6.3 (половой отбор) с полным текстом.
- rollback_or_mitigation: при пересмотре интерпретации (DFE) — обновить.

## Lifecycle
- deprecation_reason: —

