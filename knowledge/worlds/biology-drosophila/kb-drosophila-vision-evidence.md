---
type: Evidence Card
title: 'Drosophila melanogaster — Зрение: коннектом зрительной доли (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, vision, optic-lobe, visual-system, connectome]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Зрение: коннектом зрительной доли (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Connectome-driven neural inventory of a complete visual system» — Nature 2025, DOI 10.1038/s41586-025-08746-0, PMC12119369 — **полный текст прочитан** (inventory, cell typing, architecture, NT-classification, specialized cells, driver lines, matching FlyWire)
  - annotation: «The organization of visual pathways in the Drosophila brain» — Cell 2026 (DOI по PII S0092867426009414) — аннотация (трассировка фоторецепторы→optic lobes→central brain)
  - related: NeurIPS 2025 «Connectome-Based Modelling Reveals Orientation Maps in the Drosophila Optic Lobe» — аннотация (рекуррентные связи предпочтительно между нейронами сходной селективности)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: 732 типа, 15 колончатых, NT, DRA, 582 lines); Cell 2026 — аннотация (качнуть — TODO).

## Metadata
- card_id: kb-drosophila-vision-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [vision, optic-lobe, medulla, lamina, lobula, t4, columnar, vpn]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (инвентарь/типы — Nature 2025)
- uncertainty:
  - ламина — неполная (stair-step, сегментация), R7/R8 — недоучтены (R7/R8_unclear)
  - соединения только между named (~53% completion) — числа связей — занижены
  - матчинг с FlyWire — «nearly complete, yet preliminary» (13% many-to-one/one-to-many)
- falsification_trigger:
  - если центральный мозг/левый OL будут добавлены (полный самец) — пересмотреть инвентарь
  - если NT-предсказания (7 классов) уточнены — обновить
- transfer_boundary:
  - НЕ переносить как «зрение = зрительная доля»: VPN-выходы идут в центральный мозг; для CASA — «слоистая локальная обработка + проекционные выходы» — материал для реорганизации (зрение как модуль с локальными слоями)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: структура/типы/архитектура зрения.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Nature 2025 (полный текст в .cdp/scratch/PMC12119369.xml).

## Core Unit
- context:
  - зрение: полный коннектом правой зрительной доли самца (тот же мозг — MCNS): инвентарь, типы, архитектура, NT.
- signal:
  - вопрос «как устроено зрение», «сколько типов в зрительной доле», «как зрение связано с центральным мозгом».
- action:
  - использовать: **732 типа / 778 экземпляров** (OL); 4 группы: ONIN (оптическая доля внутренние), ONCN (связывающие), VPN (проекционные→central), VCN (центрифугальные←central); **15 колончатых типов** (L1–L5, C2/C3, Mi1/4/9, T1, Tm1/2/20) — почти каждая колонка (892 координаты); **слои+колонки** = ретинотопия (медулла → lobula → lobula plate); **T4a–d** (849/846/883/860) — 4 слоя lobula plate (направленное движение); Mi1=887; **NT**: нейросеть, 7 классов, 59 типов/2M синапсов тренировка, валидация EASI-FISH (66 типов); **DRA** (поляризованный свет): R7d/R8d → специализированные медулла-нейроны; НЕТ DRA-ONCN; **accessory medulla** — часы (не ретинотопия); **582 split-GAL4** → >300 типов (инструментарий); **архитектура**: локальные слои + VPN-выходы в центральный мозг; ~2/3 нейронов мозга — зрительные (Cell 2026); orientation maps — рекуррентные связи между нейронами сходной селективности (NeurIPS 2025).
- outcome:
  - зрение = локальная слоистая обработка (ретинотопия: слои × колонки) + компактный набор проекционных выходов (VPN) в центральный мозг; NT — предсказан; инструменты — есть.
- lesson:
  - **локальные слоистые процессоры с ретинотопией + малочисленные проекционные выходы** — инженерный образ «зрительного модуля»: большая часть вычислений локальна, наружу — только результат (для CASA: не «весь сенсорный поток в общий процессор», а «локальные конвейеры + выжимка»).

## Fundamentals (самодостаточный опорный слой)

### 1) Объём и метод
- Полный CNS самца (мозг+VNC) — 66 срезов × 20 µm, FIB-SEM (7 микроскопов, ~1 год); proofreading зрительных регионов одной стороны: 2 584 дня (~10 person-years).
- Ограничения: ламина неполная (stair-step), R7/R8 недоучтены; named-связи ~53% completion.

### 2) Инвентарь
- 732 типа / 778 экземпляров; ONIN/ONCN/VPN/VCN; 15 колончатых типов; 892 гексагональные координаты (медулла), экватор; T4a–d → lobula plate (4 слоя); Mi1=887.
- Специализированные: DRA (поляризованный свет), accessory medulla (часы).

### 3) Архитектура
- Слои (lamina→medulla→lobula→lobula plate) × ортогональные колонки = ретинотопия; connections между слоями — через специфические пары (L1–Mi1 и др.).
- NT: 7 классов (ACh, Glu, GABA, His, DA, OA, 5HT); валидация FISH/EASI-FISH.

### 4) Связь с центральным мозгом
- VPN (visual projection) — выходы в central brain; VCN — обратные (центрифугальные); Cell 2026: трассировка фоторецепторы→OL→central brain, многослойная архитектура путей (аннотация).
- Матчинг с FlyWire: предварительный (13% не-1:1).

## Operationalization
- first_adoption_task: функциональная глубина «зрение» (слой 5/архитектура): OL-модель; при CASA — «локальный зрительный конвейер + VPN-выжимка».
- validation_check: Cell 2026 (полный текст) — TODO; ориентационные карты (NeurIPS) — TODO (физиология).
- success_criterion: карточка покрывает зрение (полный текст Nature 2025) с честными границами.
- rollback_or_mitigation: при полном самце (central+левый OL) — обновить.

## Lifecycle
- deprecation_reason: —

