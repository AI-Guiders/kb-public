---
type: Evidence Card
title: 'Mus musculus — MICrONS: функциональный коннектом зрительной коры (evidence card v1)'
tags: [biology-mus-musculus, worlds, kb, evidence, microns, visual-cortex, wiring-rule]
language: ru
world: biology
subworld: mus-musculus
---
# Mus musculus — MICrONS: функциональный коннектом зрительной коры (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Functional connectomics spanning multiple areas of mouse visual cortex» — Nature 2025, DOI 10.1038/s41586-025-08790-w, PMC11981939 — **полный текст прочитан** (data release: imaging, co-registration, cell types, comparison with Drosophila)
  - paper: «Functional connectomics reveals general wiring rule in mouse visual cortex» — Nature 2025, DOI 10.1038/s41586-025-08840-3, PMC11981947 — **полный текст прочитан** (like-to-like: axonal/synaptic scales, GLMM)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полные тексты прочитаны (ядро: объём/методы + like-to-like правило); сопутствующие статьи (4) — аннотации.

## Metadata
- card_id: kb-mus-musculus-microns-evidence-v1
- world: biology.mus-musculus
- layer: world
- tags: [microns, visual-cortex, like-to-like, wiring-rule, functional-connectomics]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полных текстов)
- evidence_type: paper (ориг., полные тексты)
- confidence: high (MICrONS — Nature 2025)
- uncertainty:
  - фрагмент коры (1 200×1 100×500 µm³), НЕ весь мозг — границы переноса
  - функциональные единицы — 2P (GCaMP6s) + RNN «digital twin» — приближение
  - like-to-like — статистика (GLMM), не причинность; только возбуждающие (GCaMP6s в excitatory)
- falsification_trigger:
  - если wiring rule не воспроизведётся (другие области/виды) — обновить
- transfer_boundary:
  - НЕ переносить «wiring rule» на дрозофилу напрямую: у дрозофилы — стереотипный каталог (коннектом одной мухи = другие), у мыши — гетерогенность (в статье прямо: отличие!)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: объём, методы, правила.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Nature 2025 (полные тексты в .cdp/scratch/PMC11981939.xml, PMC11981947.xml).

## Core Unit
- context:
  - MICrONS — крупнейший функциональный коннектом (структура+функция) млекопитающего: зрительная кора мыши.
- signal:
  - вопрос «что известно о коннектоме мыши», «как устроена кора», «есть ли правила соединения».
- action:
  - использовать: **объём**: 1 200×1 100×500 µm³, слои 2–6, junction V1+AL/LM/RL; один мыш, GCaMP6s (возбуждающие), 14 сканов; **115 372 функциональных единиц → ~75 909 уникальных нейронов**; RNN-«digital twin» (in silico); ко-регистрация (2 934 фидуциала, остаток 3.8 µm; 19 181 ROI → 15 439 EM-нейронов); **типы**: морфология+коннективность; >900k синаптических связей (proofread); soma/nucleus — предикция классов; **wiring rule (like-to-like)**: axonal scale — Ld ↑ с функциональным сходством (feature weights + RF); **synaptic scale — только feature similarity, НЕ RF distance** (Hebbian!); synapse multiplicity и cleft volume ↑ с feature similarity; like-to-like — широко (области/слои), но RF-эффект исчезает на синаптическом уровне; **сравнение с дрозофилой (из статьи)**: у дрозофилы 20% типов EM были новыми (не описаны ранее); **стереотипия: коннектом одной мухи применим к другим; у мыши — гетерогенность, иначе**.
- outcome:
  - кора = слои+области, функциональная организация (like-to-like), НО без жёсткой стереотипии; правило: **похожая функция → связь** (на уровне синапсов — только функция, не пространство).
- lesson:
  - **универсальное правило сборки**: «подобное соединяется с подобным» (feature similarity) — на синаптическом уровне; у дрозофилы это дополнительно усилено стереотипией (каталог); для CASA: связность по сходству представлений — кандидат-принцип (аналог: аттракция по вложениям).

## Fundamentals (самодостаточный опорный слой)

### 1) Данные
- Один мыш; 14 2P-сканов (awake, head-fixed, treadmill); GCaMP6s; стимулы: естественные видео + параметрические (Monet/Trippy), POV-Unreal; oracle-видео ×10.
- EM: кора 1 200×1 100×500 µm³ (V1+AL/LM/RL), слои 2–6.

### 2) Функция+структура
- 2P → EM ко-регистрация (средний остаток 3.8 µm); 115k функциональных единиц; RNN-модель (feature weights 512-d, readout location); пороги CCmax>0.4, CCabs>0.2, gOSI>0.25.

### 3) Like-to-like (правило соединения)
- Axonal: Ld ↑ с feature similarity и ↓RF distance; Synaptic: Nsyn/Ld ↑ только с feature similarity; multiplicity/cleft ↑ с similarity; RF-эффект — на аксонном уровне, НЕ на синаптическом.

### 4) Сравнение с дрозофилой (из статьи)
- Дрозофила: 20% типов EM новы (не описаны); стереотипия (одна муха → другие); мышь: гетерогенность — коннектом одной мыши НЕ переносится (крупные популяции, вариация).

## Operationalization
- first_adoption_task: мир мыши (слой 1.2 плана — MICrONS полные тексты ✅); сравнительный анализ (дрозофила↔мышь: стереотипия vs гетерогенность).
- validation_check: сопутствующие 4 статьи (дендритные подтипы, ингибиторные типы) — TODO; гиппокамп — TODO.
- success_criterion: карточка покрывает MICrONS (полные тексты) с честными границами (фрагмент коры).
- rollback_or_mitigation: при новых релизах — обновить.

## Lifecycle
- deprecation_reason: —

