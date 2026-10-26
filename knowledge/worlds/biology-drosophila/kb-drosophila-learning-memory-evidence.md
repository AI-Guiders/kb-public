---
type: Evidence Card
title: 'Drosophila melanogaster — Обучение и память: MB, OA/DA-модуляция (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, mushroom-body, learning, memory, octopamine, dopamine]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Обучение и память: MB, OA/DA-модуляция (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Octopamine in the mushroom body circuitry for learning and memory» — Learning & Memory 2024, DOI 10.1101/lm.053839.123, PMC11199948 — **полный текст прочитан** (секции: OANs in learning/memory, morphology, cotransmitters, function (VPM4, APL))
  - paper: «Neural dynamics for working memory and evidence integration during olfactory navigation» — Nat Commun 2026, DOI 10.1038/s41467-026-75945-2, PMC13518903 — скачана, TODO извлечь (рабочая память/навигация)
  - related: Schwaerzel/DA-аверсив, Burke/OA-награда (цитированы)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро); детали KC-пластичности (долговременная/кратковременная) — частично; LTM/консолидация — TODO (слой 5.2 доп).

## Metadata
- card_id: kb-drosophila-learning-memory-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [learning, memory, mushroom-body, kenyon-cell, octopamine, dopamine, apl, vpm4]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (review, полный текст)
- confidence: high (OA-модуляция/функции из Learn Mem 2024); medium (общая механика обучения — по частям)
- uncertainty:
  - KC-пластичность (механизм совпадения DA/OA + запах) — частично (цитировано, не детализировано)
  - LTM/консолидация/реконсолидация — не покрыта этим обзором (TODO)
  - OA vs DA роли (награда) — историческая дискуссия, обзор склоняется: DA — ключевая для аппетита/аверсии, OA — «сладкий вкус»/состояние
- falsification_trigger:
  - если модель «OA=состояние, DA=обучение» пересмотрена — обновить
  - если VPM4/APL-функции уточнены — обновить
- transfer_boundary:
  - НЕ переносить как «CASA-обучение»: MB — ассоциативное (запах↔награда), не «общая память»; НО: sparse coding + feedback inhibition + модуляторные каналы (OA/DA) — материал для сравнения архитектур памяти

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: MB-структура, OA/DA-модуляция, котрансмиссия, примеры (VPM4/APL).
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Learn Mem 2024 (полный текст в .cdp/scratch/PMC11199948.xml).

## Core Unit
- context:
  - обучение и память в MB: как кодируется, кто модулирует (OA/DA), примеры функций.
- signal:
  - вопрос «как муха учится», «что такое MB», «роль OA/DA».
- action:
  - использовать: MB = Kenyon cells (KC, sparse coding), MBON (выходы), DAN (DA-входы, награда/наказание), OAN (OA); **котрансмиссия** (все OANs: Glu/GABA/ACH + пептиды; VM-кластер — VGlut+; APL — GABA+); **дуальное высвобождение** (DCV — экстрасинаптически + SV/t-bars — классически); VPM4 (proboscis extension, OAMB в GRNs, подавление hunger-driven tracking через MBON-γ1pedc, переключение поиск→кормление, OA→PAM→MBON-β'1 — полёт); APL (feedback inhibition, sparse coding, подавление аверсивного обучения, активность ↓ обучением); история: OA=награда (пчёлы VUMmx1) → пересмотр: DA — и аппетит и аверсия; OA — «сладкий вкус»/состояние.
- outcome:
  - обучение = совпадение (запах ↔ DA/OA-модуляция) в MB; OA — состояние/мотивация, DA — валентность; MBON — выходы (поведенческая значимость).
- lesson:
  - память = **ассоциативный механизм с модуляторными каналами** (DA-валентность, OA-состояние) + sparse-кодирование KC — для CASA: «награда» = внешний сигнал, модулирующий пластичность; но не «обучение» в смысле общего обучения.

## Fundamentals (самодостаточный опорный слой)

### 1) MB-архитектура (кратко)
- KC (~2 000/полушарие): sparse coding (малое число активных на запах), грибовидное тело (calyx→peduncle→γ/αβ/α'β' лопасти).
- MBON (~35 типов): выходы в компартменты; DAN (PAM/PPN, ~100+) — DA-входы (награда/наказание); OAN (5 типов в MB) — OA-входы.

### 2) OA-нейроны и котрансмиссия
- OA из TA (все OANs содержат TA — сам по себе модулятор); + ≥1 классический NT (многие Glu, некоторые GABA/ACH) + пептиды.
- VM-кластер: ~все VGlut+ (Glu — котрансмиттер); APL: GABA+.
- Дуальное высвобождение: DCV (экстрасинаптически, модуляция) + SV/t-bars (классически, синапсы) — FlyWire-верифицировано (t-bars/SVs/DCVs в MB-каликсах/лопастях).

### 3) Функции (два типа с известной ролью)
- **VPM4**: proboscis extension к сахару (OAMB в сахарных GRNs — ↑сенсорные ответы); ↓hunger-driven odor tracking через MBON-γ1pedc; переключение поиск→кормление; OA→PAM→MBON-β'1 — ↑полёт (Manjila 2019).
- **APL**: feedback inhibition на KC (компартмент-специфично) — sparse coding; подавляет аверсивное обучение; активность ↓ после обучения.

### 4) OA vs DA (историческая эволюция модели)
- Пчёлы: OA (VUMmx1) — награда; затем Drosophila: OA-активация заменяет сахар (Schroll 2006, Burke 2012) НО только при интактном DA; DA — и аппетит, и аверсия (dDA1R); OA — «сладкий вкус» (восприятие награды), не питательная ценность.
- Вывод: DA — валентность/обучение; OA — состояние/вкус/мотивация.

## Operationalization
- first_adoption_task: слой 5 (обучение): MB-механизм + OA/DA; при CASA — ассоциативная память с модуляторами (сравнить с CASA-памятью).
- validation_check: LTM/консолидация — TODO; рабочая память (Nat Commun 2026 — скачана) — следующий шаг.
- success_criterion: карточка покрывает 5.2 (MB/обучение) с полным текстом; границы честны (LTM — TODO).
- rollback_or_mitigation: при пересмотре OA/DA-модели — обновить.

## Lifecycle
- deprecation_reason: —

