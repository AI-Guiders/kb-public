---
type: Evidence Card
title: Drosophila melanogaster — Электрические синапсы (gap junctions), GF-система (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, gap-junction, innexin, electrical-synapse, giant-fiber]
language: ru
epistemic: fact (из полного текста eNeuro 2025)
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Электрические синапсы (gap junctions), GF-система (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Frazzled/DCC Regulates Gap Junction Formation at a Drosophila Giant Synapse» — eNeuro 2025, DOI 10.1523/ENEURO.0202-25.2025, PMC12570126 — **полный текст прочитан** (GF→TTMn electrical synapse, shaking-B, Frazzled ICD/P3 rescue, моделирование)
  - paper: «The innexin 7 gap junction protein contributes to synchronized activity in the Drosophila...» — Front Neural Circuits 2025, PMC12062127 — аннотация (innexin7 — синхронизация)
  - paper: «Innexin expression and localization in the Drosophila antenna...» — Cell Tissue Res 2024, PMC11424723 — аннотация
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст eNeuro 2025 прочитан; innexin7/antenna — по аннотациям (TODO полные тексты при необходимости); систематический обзор электрических синапсов дрозофилы — не найден (отмечено).

## Metadata
- world: biology.drosophila
- layer: world
- tags: [electrical-synapse, gap-junction, innexin, giant-fiber, frazzled, shaking-b]
- status: draft

## Epistemic Linkage
- evidence_type: paper (ориг., полный текст) + annotations
- confidence: high (GF-система из eNeuro 2025); medium (общая картина — нет систематического обзора)
- uncertainty:
  - распространённость/доля электрических синапсов в BANC/MCNS — не оценена (нет обзора; gap junctions в EM — обнаружение затруднено)
  - innexin7/antenna — только аннотации
  - специфика других электрических синапсов (кроме GF) — не покрыта
- falsification_trigger:
  - если модель «Frazzled/P3 транскрипционный домен → сборка GJ» будет пересмотрена — обновить
  - если обнаружение GJ в EM (BANC) даст новую картину — обновить
- transfer_boundary:
  - НЕ переносить как «деталь архитектуры» в CASA: электрические синапсы — быстрая передача (GF-эскап), важны для «скорости»; в CASA — аналог «wire», но масштаб/роль уточнить

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: GF-цепь, GJ-молекулы, Frazzled-регуляция.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — eNeuro 2025 (полный текст в .cdp/scratch/PMC12570126.xml).

## Core Unit
- context:
  - электрические синапсы (gap junctions) у дрозофилы: молекулы (innexins), примеры, роль.
- signal:
  - вопрос про электрическую передачу, GJ, GF-эскап-систему.
- action:
  - использовать: GF→TTMn (гигантское волокно → мышцы крыла/прыжка) — электрический синапс (shaking-B innexin); контроль 9.04% терминала (контроль) vs 5.31% (frazzled LOF); Frazzled/DCC регулирует сборку GJ через ICD (P3-транскрипционный домен); latency 1.14 ms (wt) / 1.23 (bilateral); response frequency 79.6%; модель (химическая+электрическая, ggap от объёма GJ); innexin7 — синхронизация; антенна — innexin (гемиканалы/ГК).
- outcome:
  - электрическая передача — быстрые фиксированные пути (рефлексы/эскап), молекулярно регулируемая сборка (Frazzled) — не просто «пассивный провод».
- lesson:
  - GJ — не редкий артефакт: в GF-системе они формируют быстрый рефлекторный канал (латентность <2 мс), их количество регулируется (развитие/возраст) — «проводная» архитектура с настройкой.

## Fundamentals (самодостаточный опорный слой)

### 1) Молекулы и типы
- Innexins (shak-B/innexin6 и др.) — gap junction белки; «giant synapse» GF→TTMn — shaking-B(neural+16) изоформа.
- Innexin7 — синхронизация активности (Front Neural Circuits 2025); антенна — гемиканалы/ГК (Cell Tissue Res 2024).

### 2) GF-система (эскап)
- GF: мозг → шейный коннектив → VNC (T2) → ипсилатеральный терминал с TTMn.
- Электрический синапс: GJ-объём ~9.04% терминала (контроль) vs 5.31% (frazzled LOF) / ~1% (shak-B2); латентность 1.14 мс (wt); response frequency 79.6%.
- Модель: химическая (Ichem, τrise 0.1 мс/τdecay 3 мс) + электрическая (ggap от % заполнения, сигмоида) — показывает роль GJ в латентности/декременте.

### 3) Frazzled/DCC-регуляция сборки GJ
- Frazzled LOF: нарушена навигация аксонов (bilateral/stuck-in-brain) + GJ-объём ↓ → латентность ↑, ответы ↓.
- **ICD (внутриклеточный домен) Frazzled почти полностью восстанавливает** (латентность 0.97 мс, ответы 98.4%); P3/транскрипционный активационный домен необходим (FraE1354A — не резюмирует) → Frazzled регулирует сборку GJ через транскрипцию.

## Operationalization
- first_adoption_task: слой 4 (электрические синапсы): GF/GJ-факты; при CASA — «скоростные каналы» (эскап) vs «медленные» (химические) — двухскоростная архитектура.
- validation_check: GJ-доля в BANC (EM) — TODO; обзор электрических синапсов — TODO.
- success_criterion: карточка покрывает 4.4 (GJ/GF/Frazzled) с полным текстом; границы честны.
- rollback_or_mitigation: при пересмотре модели — обновить.

## Lifecycle
- deprecation_reason: —

