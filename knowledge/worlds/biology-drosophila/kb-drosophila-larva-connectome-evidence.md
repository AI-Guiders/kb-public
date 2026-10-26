---
type: Evidence Card
title: Drosophila melanogaster — Коннектом личинки (полный мозг, Science 2023) (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, larva, connectome, remodeling, comparative]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Коннектом личинки (полный мозг, Science 2023) (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «The connectome of an insect brain» — Science 2023, DOI 10.1126/science.add9330, PMC7614541 — **полный текст прочитан** (reconstruction, 4 connection types, 93 types, hubs, recurrence, efference copy)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: полный мозг личинки, non-canonical соединения, хабы/рекуррентность, efference copy); детали по регионам — частично.

## Metadata
- card_id: kb-drosophila-larva-connectome-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [larva, connectome, science-2023, remodeling, learning-center, efference-copy]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (полный коннектом — Science 2023)
- uncertainty:
  - 25% синапсов — «orphans» (мелкие фрагменты) — веса известных связей могут отличаться (авторы: не изменят сильные пути)
  - EM — 1-я личинка (6 ч), не все возрасты
- falsification_trigger:
  - если реконструкция будет пересмотрена (новый релиз) — обновить
- transfer_boundary:
  - НЕ переносить личиночные числа на взрослых; НО: «non-canonical соединения» и «MB как узел» — проверены и во взрослых (BANC) — для сравнительного анализа личинка↔имаго (ремоделирование)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: полный мозг личинки, 4 типа связей, MB-центричность.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Science 2023 (полный текст в .cdp/scratch/PMC7614541.xml).

## Core Unit
- context:
  - полный коннектом мозга личинки (первый «полный мозг насекомого») — база для сравнения с имаго (ремоделирование) и с C. elegans (минимальный каталог).
- signal:
  - вопрос «как устроен мозг личинки», «что меняется при метаморфозе», «какие типы соединений бывают».
- action:
  - использовать: **3 016 нейронов** (480 входных + 2 536 мозговых), **~548 000 синапсов**; >99% нейронов реконструированы; 75% синапсов связаны; **4 типа соединений**: a-d 66.6%, **a-a 25.8%** (аксонная модуляция!), d-d 5.8%, d-a 1.8%; 71.8% нейронов получают аксонную модуляцию; **93 типа** (кластеризация по коннективности); **хабы**: 506 a-d / 100 a-a / 10 d-d / 8 d-a; **73% in-out хабов — у MB** (пост-к MBON / пре-к DAN); **рекуррентность**: DAN 57%, MB-FBN 51%, MBON 45%, CN 42% — рекуррентные петли обучения; KC — 0.1% (входы не рекуррентны); **efference copy**: 37% DNsVNC и 66% DNsSEZ синапсируют на мозг (копии моторных команд), DANs получают обратную связь от DNs; non-canonical a-a соединения — в обучении/действиях (DAN→KC, KC→KC — латеральное торможение через mAChR-B).
- outcome:
  - мозг личинки = сенсорные входы (PN) → MB (обучение: DAN-учитель, рекуррентные петли) → выходы (pre-DN/DN); **efference copy** — петля «действие → обучение».
- lesson:
  - **действие участвует в обучении напрямую** (efference copy в DAN!) — для CASA: обратная связь от действия к учителю — реальный механизм (аналог «намерение→дельта» IOP!).

## Fundamentals (самодостаточный опорный слой)

### 1) Объём
- Полный CNS личинки (1-я стадия, 6 ч): 3 016 нейронов, ~548k синапсов; >99% реконструированы; 75% синапсов связаны (25% — orphan-фрагменты).

### 2) 4 типа соединений (важно!)
- a-d 66.6%, a-a 25.8%, d-d 5.8%, d-a 1.8% — НЕ только аксодендритные; **аксонная модуляция** у 71.8% нейронов; 95 нейронов (3.8%) — большая аксонная модуляция (KC, DAN, pre-DN); d-a — в основном обратные (63% — взаимные с a-d; корреляция сортировки −0.61).
- 95% пар — один тип связи; мультиплексные — реже (но a-d+a-a — «пост- и пресинаптический контроль»).

### 3) Типы и хабы
- 93 типа (иерархическая кластеризация по коннективности; NBLAST 0.80 — морфология согласуется).
- Хабы: 506 a-d (в-хабы — ближе к выходам, out-хабы — к сенсорике); **73% in-out хабов — у MB**; 23% — CN (интеграция MB+LH — learned+innate).

### 4) Рекуррентность и efference copy
- DAN 57% / MB-FBN 51% / MBON 45% / CN 42% — петли обучения; KC 0.1% — сенсорные входы линейны.
- DNs → мозг: efference copy (37% VNC, 66% SEZ) — DANs получают от DNs (обратная связь от мотора к обучению).

## Operationalization
- first_adoption_task: сравнительный анализ (личинка↔имаго: ремоделирование; C. elegans: минимальный каталог); CASA: efference copy → IOP-аналог.
- validation_check: сравнение «4 типа связей» с взрослыми (BANC — есть ли a-a/d-d?) — TODO.
- success_criterion: карточка покрывает личинку (полный текст Science 2023).
- rollback_or_mitigation: при новых реконструкциях — обновить.

## Lifecycle
- deprecation_reason: —

