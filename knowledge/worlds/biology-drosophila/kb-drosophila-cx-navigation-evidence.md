---
type: Evidence Card
title: 'Drosophila melanogaster — Центральный комплекс: навигация, компас, векторные вычисления (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, central-complex, navigation, compass, ring-attractor, fan-shaped-body]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Центральный комплекс: навигация, компас, векторные вычисления (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection» — eLife 2021, DOI 10.7554/eLife.66039, PMC9477501 — **полный текст прочитан** (секции: CX connectome, EB ring neurons, ring attractor, PB, FB structure/motifs, sleep-wake, vector computations, navigation models, discussion)
  - related: Green/Turner-Evans (head direction), Stone et al. 2017 (vector basis), Seelig/Jayaraman (EPG) — цитированы
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро Main+Discussion+Methods частично); модели (path integration) — кратко; числовые детали — из текста.

## Metadata
- card_id: kb-drosophila-cx-navigation-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [central-complex, navigation, compass, ring-attractor, fan-shaped-body, vector-computation, action-selection]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (коннектом/мотивы eLife 2021); medium (функциональные интерпретации моделей — гипотезы авторов)
- uncertainty:
  - hemibrain: CX-ассоциированные регионы неполны (proofread ниже) — авторы валидировали (EB: относительные вклады устойчивы)
  - «FB = vector calculator» — гипотеза (поддерживается коннектомом, требует физиологии)
  - EPGt/P6-8P9 (краевые нейроны) — роль гипотетична
- falsification_trigger:
  - если модели vector computation не подтвердятся физиологически — сузить
  - если ring attractor будет пересмотрен (новые данные) — обновить
- transfer_boundary:
  - НЕ переносить «CX = мозг-модуль» в CASA как «процессор навигации»: это специализированная архитектура (небольшие рекуррентные сети с attractor-динамикой), НО — сильный материал для сравнения (малые сети, векторы, контекст-зависимый выбор)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: CX-структуры, кольцевой аттрактор, FB-мотивы, векторные вычисления.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — eLife 2021 (полный текст в .cdp/scratch/PMC9477501.xml).

## Core Unit
- context:
  - центральный комплекс (CX): компас, навигация, контекст-зависимый выбор действия; коннектом-выявленные мотивы.
- signal:
  - вопрос «как муха навигирует», «что такое кольцевой аттрактор», «как CX связан с выбором действий».
- action:
  - использовать: EB (ring neurons ER1-ER6 + ExR1-8; EPG-компас 16 wedges), PB (18 гломерул; EPG/EPGt/PEG/PEN/PFN/PFL/PFR), FB (**>200 типов: ~60 columnar + ~150 tangential; 9 колонн × 9 слоёв**; vΔ/hΔ 2D-сетка; FX ~20 типов), NO (3 субкомпартмента), GA; **кольцевой аттрактор** (EB-PB-PEN/PEG рекуррентные петли, 22.5° смещение, all-to-all inhibition внутри типа = шумоподавление/winner-take-all); мультимодальный компас (визуальный/поляризованный/ветер/циркадианный); **FB = vector computations** (PFN ±45° phase shift → 90° в FB; vΔ/hΔ 180° инверсия → базис 4 векторов × 90°; NO-амплитуды → TV-вектор: оптический поток при полёте, body-centered при ходьбе); сеть 3-4 слоя глубиной; мотивы: canonical feedback, parallel, linked targets; CX-выходы (PFL1-3 → LAL premotor; ExR7/8); sleep-wake (dFB R23E10, ER5, DANs); мультифункциональность (сенсоромоторное, память-направленные решения, циркадианные, питание).
- outcome:
  - навигация = компактная рекуррентная архитектура: кольцевой аттрактор (направление) + векторные вычисления (FB) + контекст-входы (тангенциальные) → выбор действия.
- lesson:
  - природа реализовала **малую сеть с аттракторной динамикой и векторной арифметикой** (небольшое число нейронов: 16 направлений, тысячи — FB) — «вычислительные примитивы» (attractor, vector, gain field) — ключевой материал для CASA (специализированные модули + контекст).

## Fundamentals (самодостаточный опорный слой)

### 1) Структуры CX
- EB: кольцо; ring neurons (ER1–ER6) — тангенциальные, большинство GABA; каждый тип — своё кольцо/аннулус; ExR (1–2 нейрона/полушарие, 8 типов).
- PB: handlebar, 9 гломерул/полушарие (18); columnar: EPG (16 wedges ↔ гломерулы), EPGt (краевые), PEG/PEN/PFN/PFL/PFR.
- FB: крупнейший; ~60 columnar типов (PB-FB-*, FX, vΔ, hΔ) + ~150 tangential; 9 колонн × 9 слоёв (варьирует по типу).
- NO: парные, 3 субкомпартмента; вход в CX (LNO-ингибиторные).
- GA, LAL, CRE, BU — вспомогательные.

### 2) Кольцевой аттрактор (компас)
- EPG-бamp (16 wedges) = head direction; поддерживается рекуррентными петлями EB-PB (EPG→PB→PEG/PEN→EB); PEN-фазовый сдвиг ±45° — обновление при повороте; 22.5° между полушариями; EPGt — сшивание краёв.
- All-to-all inhibition внутри ring-типов: шумоподавление/winner-take-all (быстрое) или баланс (медленное); «suppression hierarchy».
- Тетеррование: визуальный (BU), поляризованный свет (ER4m), ветер (ER1_b/ER3a_b ← WPN ← APN), циркадианный (TuBu06/DN1pB → ER5), моторный; электротонические дистанции — веса.

### 3) FB: рекуррентная сеть для векторных вычислений
- PFN: ±45° контралатеральный сдвиг → левый/правый bump ~90° в FB; NO-входы модулируют амплитуды.
- vΔ (вертикальные, ~1 колонна), hΔ (горизонтальные, 2 колонны ~180°); 3 мотива (same-column, half-width jump, both); PCA → 903 матрицы → 3 мотива.
- Базис: 4 вектора × 90° (неинвертированный PFN1 + инвертированный PFN2); NO-амплитуды → TV-вектор (allocentric; оптический поток при полёте; body-centered при ходьбе через head-body преобразование).
- Сеть 3–4 слоя (PFN→vΔ/hΔ→выход); пути к PFL1-3 (LAL premotor) и FX (ROB/SMP/CRE).

### 4) Выходы и контекст
- CX выходы: PFL1-3 (FB→LAL), ExR7/8; FB2B_b feedback (gain control); «linked targets» — рекуррентные субсети.
- Контекст: сенсоромоторное состояние (ExFl1), память-направленные решения (MB↔CX), циркадианные, sleep-wake (dFB R23E10 9 типов: FB6A/C/E/G/I/Z, FB7A/K; DANs PPL1 — wake), питание.
- Числовая вариация: EPG 2–4/гломерул, PEN/PFN ×2 в R4/R6 — зеркальная симметрия; синаптическая компенсация (больше нейронов = меньше синапсов).

## Operationalization
- first_adoption_task: слой 5 (навигация) + 3 (архитектура): CX-мотивы; при CASA — «кольцевой аттрактор + векторная арифметика» как примитивы; «контекст-зависимый выбор» — через тангенциальные входы.
- validation_check: сверить 16 wedges/18 гломерул с BANC-данными — TODO; FB 9×9 — TODO.
- success_criterion: карточка покрывает 5.4 (CX-навигация) с полным текстом.
- rollback_or_mitigation: при пересмотре моделей — обновить (гипотезы отмечены).

## Lifecycle
- deprecation_reason: —

