---
type: Evidence Card
title: 'Drosophila melanogaster — Избегание/эскап: GF-система, аверсивные цепи (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, escape, giant-fiber, avoidance, reflex]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Избегание/эскап: GF-система, аверсивные цепи (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: eNeuro 2025 «Frazzled/DCC Regulates Gap Junction Formation at a Drosophila Giant Synapse» DOI 10.1523/ENEURO.0202-25.2025 — **полный текст прочитан** (карточка 4.4: GF→TTMn, электрический синапс, латентность 1.14 мс)
  - annotation: Proc R Soc B 2025 (PMID 40425165) — GF-эскап (PubMed-верификация из предыдущего прохода) — аннотация
  - related: eLife 2021 CX (карточка 5.4) — выходы в premotor (LAL)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: GF-цепь — полный текст (4.4); Proc R Soc B — аннотация (полный текст TODO); аверсивные цепи (свет/механические) — частично.

## Metadata
- card_id: kb-drosophila-escape-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [escape, giant-fiber, reflex, avoidance, vnc]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста eNeuro 2025) + annotation
- evidence_type: paper (ориг., полный текст) + annotation
- confidence: high (GF-система); medium (полный обзор эскапа — нет)
- uncertainty:
  - полный каталог эскап-цепей (свет, звук, вибрация) — не собран (Proc B — аннотация)
  - GF→TTMn — модельная; другие GF-ветви (GF→PSI→DLM?) — в eNeuro упомянуты частично
- falsification_trigger:
  - если GF-модель (Frazzled-регуляция) пересмотрена — обновить
- transfer_boundary:
  - НЕ переносить как «рефлекс-архитектуру» в CASA: эскап — быстрые фиксированные пути (2-3 синапса), важны как пример «скорости» и «минимума задержки»

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: GF-цепь, латентность, электрический синапс.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — eNeuro 2025 (полный текст — карточка 4.4).

## Core Unit
- context:
  - эскап-поведение: гигантское волокно (GF) — быстрый рефлекс (уход от вибрации/удара).
- signal:
  - вопрос «как муха мгновенно улетает», «какие цепи обеспечивают минимальную задержку».
- action:
  - использовать: GF (мозг → шейный коннектив → VNC T2) → TTMn (мышцы прыжка) — 2-синапсный путь с **электрическим синапсом** (GJ, shaking-B); латентность **1.14 мс** (wt) / 1.23 мс (bilateral); ответы 79.6% (wt) / 98.4% (ICD rescue); Frazzled/DCC — регулирует сборку GJ (9.04% → 5.31% frazzled LOF); быстрый (GJ) + химический (Ichem τ~3 мс) компоненты — модель.
- outcome:
  - минимальная задержка достигается: короткий путь + электрическая передача (без химической задержки) + настройка числа GJ (Frazzled).
- lesson:
  - «скорость» = архитектурное решение (короткий путь + GJ + регуляция сборки) — для CASA: физические ограничения (задержка) решаются специализацией, не универсальностью.

## Fundamentals (самодостаточный опорный слой)

### 1) GF-цепь (эскап)
- GF: пара гигантских нейронов; дендриты в мозге (вибрационные сенсорные входы), аксоны → VNC T2 → GF-терминал → TTMn (ипсилатеральный).
- GF→TTMn: **электрический синапс** (gap junction, shaking-B) + химический компонент; латентность ~1.1–1.2 мс (wt); ответы ~80%.
- Frazzled/DCC: LOF → ↓GJ (5.31% vs 9.04%), ↑латентность, ↓ответы; ICD — полное восстановление (P3-домен транскрипции) → сборка GJ регулируется транскрипционно.

### 2) Контекст
- Другие GF-ветви (GF→PSI→DLM — размах крыльев) — известны (не детализированы здесь).
- Аверсивные цепи (свет/запах → избегание) — слой 5.2/5.7 (MB, горькое Gr66a).

## Operationalization
- first_adoption_task: слой 5 (эскап): GF-факты; при CASA — «специализированные быстрые пути» (аргумент против «всё через общий процессор»).
- validation_check: Proc R Soc B (полный текст) — TODO; GF-ветви в BANC — TODO.
- success_criterion: карточка покрывает 5.5 (эскап) с полным текстом (GF) и честными границами.
- rollback_or_mitigation: при пересмотре — обновить.

## Lifecycle
- deprecation_reason: —

