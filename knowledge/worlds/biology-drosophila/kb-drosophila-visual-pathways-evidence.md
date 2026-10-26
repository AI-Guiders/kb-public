---
type: Evidence Card
title: 'Drosophila melanogaster — Визуальные пути: топографический vs нетопографический (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, visual-pathways, aotu, metu, topographic, navigation]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Визуальные пути: топографический vs нетопографический (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Parallel Visual Pathways with Topographic versus Nontopographic Organization Connect the Drosophila Eyes to the Central Brain» — iScience 2020, DOI 10.1016/j.isci.2020.101590, PMC7648135 — **полный текст прочитан** (MeTu-типы, AOTU-домены, TuBu→EB, эволюция)
  - related: Nature 2025 (F1 — зрительная доля: MeTu/LC10), Cell 2026 (PMID 42691997 — аннотация, PMC:NONE)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: параллельные пути, R7→MeTu, домены, TuBu→R); Cell 2026 — аннотация (полный текст недоступен).

## Metadata
- card_id: kb-drosophila-visual-pathways-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [visual-pathways, metu, aotu, tubu, eb, topographic, navigation]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (iScience 2020 — транс-синаптические/GRASP/клоновый анализ)
- uncertainty:
  - только «передний визуальный путь» (AOTU); лобулярные пути (LC→PVLP) — другие (частично)
  - «фильтрация ориентиров/небесных тел» — гипотеза авторов (функция — предложение)
- falsification_trigger:
  - если «прямые R7→MeTu» не подтвердится (только часть MeTu) — сузить; если домены пересмотрены — обновить
- transfer_boundary:
  - НЕ переносить как «всё зрение»: это медиальный (медуллярный) путь; НО: **параллельные каналы (топо/нетопо) + доменная сегрегация** — материал для CASA (несколько зрительных каналов с разной организацией)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: пути, домены, консервация.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — iScience 2020 (полный текст в .cdp/scratch/PMC7648135.xml).

## Core Unit
- context:
  - как зрение из глаза попадает в центральный мозг: параллельные пути (AOTU — передний; PVLP/PLP — лобулярные).
- signal:
  - вопрос «как визуальная информация идёт в мозг», «что такое AOTU/MeTu», «топография».
- action:
  - использовать: **путь**: medulla → **AOTU** (SU: superior unit / LU: large unit) → **bulb** (BU) → **EB** (R-нейроны); **MeTu-типы**: MeTu-l/-c — **топографические** (дендриты M6, аксоны — ограниченные домены SU-la/ca/cp); **MeTu-m — НЕтопографические** (дендриты 3 слоя медуллы + коллатераль в лобулу — интегрирует medulla+lobula; широкие аксоны через SU-m → **Bui** — контралатеральное ингибирование!); **R7 (UV) → MeTu** (transTango: прямые синапсы; R8 — нет; Ort-mCD8: 3/5 доменов SU); **топография**: a-p медуллы ↔ d-v SU (НЕ d-v медуллы!); **TuBu** (8–12/класс): домен-специфичные дендриты, GRASP — строгое сопоставление MeTu↔TuBu внутри доменов; **TuBu→R**: TuBu-l→R4d (полное совпадение), TuBu-c→R2 (частичное); R3—Bui; **доменная идентичность сохраняется, топография в bulb теряется** («targeting plasticity»); **эволюция**: передний визуальный путь консервативен (кузнечики/пчёлы/жуки — поляризованный свет/небесная ориентация); **функция** (предложение): фильтрация ориентиров/небесных тел для heading-решений.
- outcome:
  - зрение → центральный мозг через **параллельные каналы**: топографический (пространство → навигация) и нетопографический (интеграция medulla+lobula, супрессия ипсилатерального — через Bui).
- lesson:
  - **несколько каналов с разной организацией** (топо/нетопо) + **доменная сегрегация на каждом уровне** (не смешивание!) — для CASA: параллельные сенсорные каналы с сохранением идентичности, топография — только для навигационных, не для всех.

## Fundamentals (самодостаточный опорный слой)

### 1) Путь
- Medulla (M6) → MeTu → AOTU (SU: 5 доменов; LU) → TuBu → bulb (BUi/BUs) → EB (R2/R3/R4d/R5).
- Другой путь: lobula → LC → PVLP/PLP (лобулярные, другие каналы).

### 2) MeTu и топография
- MeTu-l/-c: M6-дендриты, ограниченные аксоны (SU-la/ca/cp); a-p↔d-v (SU) — топография; MeTu-m: 3 слоя+лобула, SU-m, Bui — нетопографический, супрессия.

### 3) Консервация
- AOTU-путь — у orthopterans/hymenopterans/beetles (поляризованный свет, небесная ориентация); Drosophila — «поведенческий генералист» — у других могут быть сложнее (гомологи SU).

## Operationalization
- first_adoption_task: функциональная глубина F4 (визуальные пути): параллельные каналы; при CASA — «каналы с сохранением доменной идентичности».
- validation_check: Cell 2026 (полный текст — недоступен, аннотация) — TODO при появлении PMC; лобулярные пути — TODO.
- success_criterion: карточка покрывает визуальные пути (полный текст iScience 2020).
- rollback_or_mitigation: при новых данных (Cell 2026) — обновить.

## Lifecycle
- deprecation_reason: —

