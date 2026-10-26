---
type: Evidence Card
title: 'Drosophila melanogaster — Центральный комплекс: координация мультимодальной навигации (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, central-complex, navigation, ring-attractor, copy-and-shift, integration]
language: ru
epistemic: fact (из полного текста; вычислительная модель — гипотезы авторов, но на данных)
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Центральный комплекс: координация мультимодальной навигации (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «How the insect central complex could coordinate multimodal navigation» — eLife 2021, DOI 10.7554/eLife.73077, PMC8741217 — **полный текст прочитан** (copy-and-shift, optimal integration, steering, frames)
  - related: eLife 2021 (5.4 — коннектом CX), Sun et al. 2020 (модель), Nat Commun 2026 (F2 — FB goal), iScience 2020 (F4 — AOTU)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: вычислительная модель — copy-and-shift, RA-интеграция, steering-контроллер); часть литературы — цит.

## Metadata
- world: biology.drosophila
- layer: world
- tags: [central-complex, navigation, ring-attractor, copy-and-shift, optimal-integration, steering]
- status: draft

## Epistemic Linkage
- evidence_type: paper (вычислительный обзор/модель — полный текст)
- confidence: high (eLife 2021 — модель воспроизводит поведение мух/муравьёв; коннектомные ограничения — в 5.4)
- uncertainty:
  - модель (не экспериментальная физиология!) — «возможная» архитектура; конкретные веса/гейты — гипотезы
  - «оптимальность» — как в F2 (теоретическая рамка)
- falsification_trigger:
  - если физиология опровергнет copy-and-shift (иной механизм сдвига) — обновить
- transfer_boundary:
  - НЕ переносить как «так точно работает» (модель); НО: **архитектурные принципы** (рамки, взвешенная интеграция, П-контроллер, рабочая память) — сильный референс для CASA

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: copy-and-shift, интеграция, steering.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — eLife 2021 (полный текст в .cdp/scratch/PMC8741217.xml).

## Core Unit
- context:
  - как CX координирует мультимодальную навигацию (обоняние, ветер, PI, зрение) в единое поведение.
- signal:
  - вопрос «как CX интегрирует сигналы», «как работает steering», «что такое copy-and-shift».
- action:
  - использовать: **copy-and-shift**: направленные сигналы (PI/хемотаксис/анемотаксис) приводятся к общей рамке (global head direction); перенос из нестабильной рамки (ветер — egocentric) в стабильную (небесный компас — geocentric) — сдвиг бампа (WPN), рабочая память желаемого направления; триггеры — «особое сенсорное переживание + мотивационное состояние» (tangential inputs в FB — контекстная сеть); **оптимальная интеграция**: ring attractor (RA) интегрирует желаемые направления с **весами по достоверности** (gating ON/OFF; веса ∝ концентрации запаха k·C·COH; PI взвешивается относительно home-вектора — как у муравьёв Wystrach); выход RA — единственный desired heading → steering; **steering-контроллер**: CPU1 (16, i=0..15) = **desired − current** (CD−CC), левые (0–7)/правые (8–15), θM = kmotor·(Σleft−Σright) — **П-контроллер (error→motor)**; **гомологи**: муха (обоняние: MB-валентность→CX) vs муравьи (PI+odour — единая модель); гейты: OFF-ответ (хемотаксис/gradient) vs ON-ответ (анемотаксис/upwind).
- outcome:
  - CX = **центр координации навигации**: приведение к общей рамке → взвешенная интеграция (RA) → ошибка (desired−current) → моторный выход (L−R).
- lesson:
  - **архитектура решений**: (1) контекстные триггеры (special sensory + motivation) → переключение режимов; (2) взвешенная интеграция сигналов по достоверности (не просто сумма!); (3) П-контроллер (error = желаемое − текущее; motor = асимметрия); (4) рабочая память желаемого направления — для CASA: это «policy → error → action» с confidence-весами — близко к P6 (арбитраж) и P7 (аттракторы)!

## Fundamentals (самодостаточный опорный слой)

### 1) Copy-and-shift
- Все сигналы направления → общая рамка (глобальная голова); сдвиг = активация WPN (upwind относительно heading); перенос egocentric→geocentric (clutch pose у муравьёв); рабочая память желаемого направления; срабатывает при «особых» событиях (визуальная новизна, ветер, мотивация).

### 2) Оптимальная интеграция (RA)
- Желаемые направления (PI, chemotaxis, anemotaxis) — гейты OFF/ON, веса по концентрации; RA (8 нейронов, рекуррентность WE2E, нелинейность g(c)=max(0,ρ+c)) — интегрирует; выход = единственный CDH → steering. У муравьёв: PI + odour (Buehlmann) — «оптимальное» взвешивание.

### 3) Steering
- CPU1_i = CDH_i − CCH_i (i=0..15); левые 0–7, правые 8–15; θM = kmotor·(Σleft − Σright); CCH = I-TB1 (глобальный компас); 16 wedges — дискретизация 360° (22.5°).

### 4) Гомологи/единая модель
- Муха: AL→LH/MB→CX; муравьи: PI (след) + odour; модель воспроизводит гоминг муравьёв (Buehlmann 2012) и хемотаксис мух (volcano-среда).

## Operationalization
- first_adoption_task: функциональная глубина F5 (ориентация-динамика): CX-координация — модель; при CASA — «confidence-weighted integration + П-контроллер + контекстные триггеры» (P6/P7 связка).
- validation_check: физиология copy-and-shift — по мере данных (F2 Nat Commun 2026 — частично: FB goal = desired heading!); steering-нейроны (CPU1) — физиология (5.4).
- success_criterion: карточка покрывает CX-координацию (полный текст eLife 2021).
- rollback_or_mitigation: при опровержении модели — обновить (модель ≠ факт).

## Lifecycle
- deprecation_reason: —

