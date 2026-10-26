---
type: Evidence Card
title: 'Drosophila melanogaster — Детерминация пола: sxl→tra→dsx/fru, диморфизм (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, sex-determination, doublesex, fruitless, dimorphism]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Детерминация пола: sxl→tra→dsx/fru, диморфизм (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Molecular and cellular origins of behavioral sex differences: a tiny little fly tells a lot» — Front Mol Neurosci 2023, DOI 10.3389/fnmol.2023.1284367, PMC10622783 — **полный текст прочитан** (секции: Introduction, P1 neurons, aSP-f/aSP-g pheromone pathway)
  - classic: каскад Sxl→Tra→Dsx/Fru — классика (Cline & Meyer; Baker et al.), в каркасе слоя 1; в обзоре 2023 подтверждён как «two sex determination genes fru and dsx play instructive role» — но детали каскада (sxl/tra) — классика, без полного текста (отмечено)
  - paper (доп.): «Sex determination gene transformer regulates the male-female difference in Drosophila fat storage» — eLife 2021, PMC8594944 — упомянута (tra-функции вне поведения; полный текст не читался)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст обзора 2023 прочитан (ключевые секции); каскад Sxl/Tra — классика; детали транскрипции (sxl-сплайсинг, tra-сплайсинг) — TODO отдельный источник.

## Metadata
- card_id: kb-drosophila-sex-determination-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [sex-determination, sxl, transformer, doublesex, fruitless, p1, cva, dimorphism]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из обзора), classic (каскад)
- evidence_type: paper (review, полный текст) + classic
- confidence: high (dsx/fru инструктивны, P1, aSP-f/g — из обзора 2023); medium (каскад Sxl/Tra — классика без полного текста в этом проходе)
- uncertainty:
  - точный механизм sxl-сплайсинга (X:A → Sxl → Tra) — классика, не извлечена
  - fru-изоформы (FruM) и их функции в разных кластерах — частично (обзор упоминает FruM-самки без P1)
  - диморфизм коннектома: MANC/BANC диморфные типы — связь (1.3 Nature 2026 «sex differences across the nerve cord» — отдельно)
- falsification_trigger:
  - если P1-модель «essential» будет восстановлена (новые эксперименты) — обновить (обзор прямо говорит: не essential)
  - если каскад Sxl/Tra будет дополнен (новые факторы) — обновить
- transfer_boundary:
  - НЕ переносить как «программу пола» в CASA: это биология развития/поведения; для CASA важно: половой диморфизм — часть врождённой структуры (диморфные типы/цепи), но сравнение — после синтеза

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: каскад, инструктивные гены, примеры (P1, aSP), диморфизм.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Front Mol Neurosci 2023 (полный текст в .cdp/scratch/PMC10622783.xml).

## Core Unit
- context:
  - как пол детерминируется и как задаёт диморфизм поведения/структуры; связь с коннектомом (полные карты — можно картировать).
- signal:
  - вопрос «почему самцы/самки различаются в поведении/цепях», «как задаётся пол».
- action:
  - использовать: каскад Sxl→Tra→Dsx/Fru (классика); fru/dsx — инструктивные гены полового диморфизма; P1 (20 male-specific на полушарие, FruM+DsxM) — инициация ухаживания, НО не essential (FruM-самки ухаживают без P1; обезглавленные самки с VNC-активацией генерируют песню); aSP-f/aSP-g — переключатель поведенческого пола в феромонном пути cVA (Or67d→DA1→aSP; FruM маскулинизирует дендриты; самка — аттракция, самец — репульсия).
- outcome:
  - механизм: пол = транскрипционный каскад → инструктивные TF (Dsx/Fru) → диморфные нейронные типы/цепи (P1, aSP-f/g) → диморфное поведение.
- lesson:
  - диморфизм — не «бонус», а генетически программируемая часть НС: один ген (fru) может переключать поведенческий пол в феромонном пути; коннектом позволяет картировать диморфные цепи (сильный прецедент для «innate»).

## Fundamentals (самодостаточный опорный слой)

### 1) Каскад детерминации пола (классика)
- X:A соотношение → Sxl (самки ON, самцы OFF) → Tra (ON у самок) → альтернативные сплайсинг-продукты **DsxF/DsxM** и **FruF/FruM** (fru — тра-независимый частично: FruM у самцов).
- Результат: dsx/fru — инструктивные транскрипционные факторы, задающие половой диморфизм (морфология и поведение).
- Вне поведения: tra также регулирует жировое депо (eLife 2021 — fat storage).

### 2) Поведенческий диморфизм (обзор 2023)
- **P1 (мужские)**: 20 нейронов на полушарие, FruM+DsxM; открыты скринингом мозаичных самок (ухаживание за самкой — единственная маскулинизированная группа, значимо чаще у ухаживающих самок, p<0.0001).
- **P1 НЕ обязателен**: FruM-самки (Demir & Dickson 2005) ухаживают без P1; обезглавленные самки с VNC-активацией генерируют квази-нормальную пульс-песню (Clyne & Miesenböck 2008) — VNC может поддерживать песню.
- **cVA-путь**: cVA (мужской ejaculatory bulb → семенная жидкость; подавляет привлекательность для самцов; для самок — аттракция/агрегация). Путь: Or67d → DA1 → aSP-f (DC1) / aSP-g. FruM маскулинизирует дендриты aSP-g/aSP-f: одна и та же сенсорная линия → разное поведение по полу (привлечение/отталкивание).
- Кластеры (P1, aSP-f/g) — примеры: один TF (FruM) переключает поведенческий пол.

### 3) Связь с коннектомом
- D. melanogaster — одна из немногих видов с полным коннектомом мозга (Scheffer 2020; Dorkenwald 2021; BANC) → найденные для поведения нейроны сразу картируют в цепях.
- Половой диморфизм: MANC/BANC — диморфные типы; Nature 2026 (1.3) — «sex differences across the nerve cord» (отдельная карточка).

## Operationalization
- first_adoption_task: в слой 1 (пол) и слой 5 (поведение): каскад + примеры; при CASA — зона genetic: пол = часть врождённого каталога (диморфные типы/цепи).
- validation_check: сверить sxl-сплайсинг (отдельный источник — TODO); проверить диморфные типы в BANC/MANC (слой 3).
- success_criterion: карточка покрывает 1.5 (каскад/инструктивные гены/примеры) с полным текстом и границами.
- rollback_or_mitigation: при восстановлении «P1 essential» — обновить (обзор уже склоняется к не-essential).

## Lifecycle
- deprecation_reason: —

