---
type: Evidence Card
title: 'Drosophila melanogaster — Сон: состояния, гомеостаз, схемы (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, sleep, sleep-states, homeostasis, dfb]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Сон: состояния, гомеостаз, схемы (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Current Evidence for Sleep States in Drosophila: Findings and Implications» — Current Sleep Medicine Reports 2026, DOI 10.1007/s40675-025-00352-w, PMC13031250 — **полный текст прочитан** (секции: multiple sleep states, arousal threshold, microbehaviors, neural/physiological correlates, circadian day/night, durations, number of states, functions, commonalities)
  - related: eLife 2021 CX (карточка 5.4): dFB R23E10 (9 типов), ER5 (sleep need), DANs — полный текст прочитан
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан; молекулярная генетика сна (ген-мутанты) — частично; «sleep need»-механизм — в eLife 2021.

## Metadata
- card_id: kb-drosophila-sleep-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [sleep, sleep-states, arousal, dfb, slow-wave, homeostasis]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (review, полный текст)
- confidence: high (состояния/маркеры — обзор 2026); medium (число состояний — нет консенсуса, отмечено авторами)
- uncertainty:
  - число состояний: HMM 4 / 4 (presleep-early-mid-late) / ≥2 — нет консенсуса
  - функции (память/гомеостаз/энергия/клиренс) — гипотезы, не доказаны для каждого состояния
  - генетика (heritability, sex-specific) — отмечена, детали не извлечены
- falsification_trigger:
  - если консенсус о состояниях изменится — обновить
  - если «slow-wave = sleep pressure» окажется видоспецифичным — сузить
- transfer_boundary:
  - НЕ переносить в CASA «сон» как вычислительный элемент: сон — гомеостатический/энергетический режим; НО: «dFB кодирует sleep need через возбудимость» — пример «потребностной» регуляции (нужда → поведение) — материал для зоны «потребности»

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: состояния, маркеры, схемы.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Curr Sleep Med Rep 2026 (полный текст в .cdp/scratch/PMC13031250.xml).

## Core Unit
- context:
  - сон дрозофилы: состояния, критерии, схемы (dFB), функции.
- signal:
  - вопрос «спит ли муха», «что такое sleep need», «как сон управляется».
- action:
  - использовать: 5-мин порог (Shaw), arousal threshold, microbehaviors (proboscis extension, antenna, haltere); LFP 5–10 Hz (sigma-like), slow-wave <4 Hz (R5/EB, ZT13–16), ArcLight; GCaMP6f (первые 5 мин — ↑, потом ↓ + ↓ коннективность); метаболизм (глубже → ниже); день/ночь (ночь глубже); HMM 4 состояния; active sleep (1–5 мин, wake-like, REM-аналог; индуцируется dFB-стимуляцией; RNA-seq: axonal guidance/synapse); dFB R23E10 (9 типов FB6A/C/E/G/I/Z, FB7A/K) — sleep need (возбудимость/спонтанная активность), индуцирует сон; DANs — wake; ER5 — tracking sleep need (осцилляции).
- outcome:
  - сон — не единое состояние: множественные глубины, маркеры (LFP/microbehavior/metabolism), гомеостатический контроль (dFB/ER5).
- lesson:
  - «потребность» (sleep need) кодируется в нейронах (возбудимость) и модулируется DA/OA — это пример **гомеостатической обратной связи** (не обучение) — для CASA: потребности ≠ память.

## Fundamentals (самодостаточный опорный слой)

### 1) Состояния и критерии
- 5-мин иммобильность — стандартный порог; arousal threshold ↑ с глубиной; microbehaviors: PE (чаще в глубоком), антенна, халтера (droop в глубоком).
- Глубина: ~10 мин — глубочайшая; 20 мин — легче; 30 мин — второй пик; 45–60 мин — как <5 мин; модели: пик 12–15 мин.
- День/ночь: ночь глубже (11–40 Hz ↓, метаболизм ↓); генетическая корреляция день/ночь низкая.

### 2) Нейронные корреляты
- LFP: ↓ при сне; 5–10 Hz (sigma-like); slow-wave <4 Hz (R5/EB, ZT13–16, sleep pressure); ArcLight-осцилляции (delta, ZT8–12/0–3, пик 13–16).
- GCaMP6f: первые 5 мин — ↑, затем ↓ + ↓ коннективность активных нейронов.
- Состояния: ≥2 (+wake); HMM: deep/light/early wake/full awake; 4-фазное (presleep/early/mid/late); active sleep (1–5 мин, wake-like; dFB-индукция; RNA-seq ↑ axonal guidance/synapse).

### 3) Схемы (из eLife 2021)
- dFB tangential (R23E10): 9 типов (FB6A/C/E/G/I/Z, FB7A/K), слои 6–7; sleep need (возбудимость/спонтанная активность), активация → сон; DANs (PPL1) — wake; ER5 (EB) — sleep need tracking (осцилляции); связь с циркадианными (TuBu06/DN1pB).

### 4) Функции (гипотезы)
- Память (консолидация/реконсолидация), синаптический/клеточный гомеостаз, энергия, иммунитет, клиренс отходов (PE — waste clearance); slow-wave — сенсорное отключение; активный сон — REM-аналог (не идентичен).

## Operationalization
- first_adoption_task: слой 5 (сон): состояния/маркеры/схемы; при CASA — «потребности» (гомеостаз) отдельно от памяти.
- validation_check: сверить с BANC (dFB-типы) — TODO; генетика сна — TODO.
- success_criterion: карточка покрывает 5.3 (сон) с полным текстом.
- rollback_or_mitigation: при консенсусе о состояниях — обновить.

## Lifecycle
- deprecation_reason: —

