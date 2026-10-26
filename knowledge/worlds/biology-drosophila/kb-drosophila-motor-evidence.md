---
type: Evidence Card
title: 'Drosophila melanogaster — Моторика: распределённое управление движением (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, motor, backward-walking, mdn, distributed-control, vnc]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Моторика: распределённое управление движением (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Distributed control of motor circuits for backward walking in Drosophila» — Nat Commun 2020, DOI 10.1038/s41467-020-19936-x, PMC7710706 — **полный текст прочитан** (MDN, MF-типы, LBL40/LUL130, эпистаз, кинематика)
  - related: eLife 2018 (сенсо-моторные преобразования ON/OFF — аннотация), Curr Biol 2024 (тредмиллы — аннотация)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: MDN→локальные цепи, фазы шага); другие моторные программы (ходьба вперёд, полёт) — TODO.

## Metadata
- card_id: kb-drosophila-motor-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [motor, backward-walking, mdn, distributed-control, vnc, leg-circuits]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (Nat Commun 2020 — оптогенетика+эпистаз+кинематика)
- uncertainty:
  - только обратная ходьба (MDN); передняя ходьба/полёт — другие программы
  - MF-типы — 29/33 (не все); другие сегментные цепи — частично
- falsification_trigger:
  - если «распределённое» окажется «каскадом с одним центром» (новые данные) — обновить
- transfer_boundary:
  - НЕ переносить как «мотор = VNC»: мозг (CX/MB) модулирует через DNs; НО: **распределённое управление с делегированием** — прямой материал для CASA (моторные подсистемы, не центральный процессор)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: MDN→локальные цепи, фазы.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Nat Commun 2020 (полный текст в .cdp/scratch/PMC7710706.xml).

## Core Unit
- context:
  - как организуется движение: нисходящая команда (MDN) → локальные цепи → конкретные движения.
- signal:
  - вопрос «как муха двигает ногами», «есть ли центральный генератор», «что делает одна команда».
- action:
  - использовать: **MDN** (descending) — активация → обратная ходьба; НЕ монолитная программа: MDN → **MF-типы** (интернейроны) → сегментные цепи; **82 split-GAL4 = 29/33 MF-типов** (систематическая классификация); **LBL40** (T3, 14B lineage, пара) → **стибание голени** (tibia flexion, stance/силовой ход задних ног); **LUL130** (сегментарные локальные, T1–T3) → **подъём ноги** (leg lifting, swing); **эпистаз**: независимое подавление — разные фазы (stance/swing); активация LBL40 → flexion, LUL130 → lifting (обезглавленные!); кинематика: 200 fps, DeepLabCut, 6 ног × 4 сустава (body-coxa, coxa-trochanter, femur-tibia, tibia-tarsus); задние ноги доминируют (MDN-триггер).
- outcome:
  - **нисходящая команда (малая) + локальные сегментные цепи (делегирование)**: MDN не «программирует» шаг, а рекрутирует локальные модули (LBL40/LUL130) с конкретными ролями (stance/swing).
- lesson:
  - моторное управление = **команда → локальные модули с специфическими функциями** (не центральная программа) — для CASA: «motor primitives» + делегирование; управление движением — снизу вверх (локальные), не сверху вниз (полная программа).

## Fundamentals (самодостаточный опорный слой)

### 1) MDN и обратная ходьба
- MDN (нисходящий нейрон) — активация (CsChrimson) → обратная ходьба; оптогенетика+эпистаз (GtACR2 470nm/CsChrimson 660nm) — независимый контроль.

### 2) MF-типы и локальные цепи
- 82 split-GAL4 (29/33 MF-типов); trans-Tango от MDN; функциональная визуализация — ответы на MDN.
- LBL40 (T3): стибание голени — stance; LUL130 (T1–T3): подъём ноги — swing; сегментная специфичность (T3 сильнее).

### 3) Кинематика
- 6 ног × 4 сустава; DeepLabCut; задние ноги — доминантный вклад в MDN-триггер; обезглавленные — локальные цепи работают без мозга (делегирование!).

## Operationalization
- first_adoption_task: функциональная глубина F3 (моторика): распределённое управление; при CASA — «моторные примитивы + делегирование».
- validation_check: передняя ходьба/полёт (другие DNs) — TODO; центральные генераторы — TODO.
- success_criterion: карточка покрывает моторику (полный текст Nat Commun 2020).
- rollback_or_mitigation: при новых программах — обновить.

## Lifecycle
- deprecation_reason: —

