---
type: Evidence Card
title: 'Drosophila melanogaster — Коннектом BANC: реконструкция, NT, влияние, модули (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, banc, connectome, architecture, influence]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Коннектом BANC: реконструкция, NT, влияние, модули (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Distributed control circuits across a brain-and-cord connectome» — Nature 2026, DOI 10.1038/s41586-026-10735-w, PMC13518251 — **полный текст прочитан** (секции: unified open-source connectome, metric of influence, modules for local feedback control, Linking DNs/ANs, AN/DN behaviour modules, specialization, interactions, CNS networks, Discussion; методы NT-предсказания)
  - related: FlyWire/FAFB (Schlegel 2024 — карточка 2.2), MANC (самец) — упомянуты
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (Main + Discussion + методы NT); детали методов (сегментация) — кратко; числа из текста.

## Metadata
- card_id: kb-drosophila-banc-connectome-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [connectome, banc, em, neurotransmitter, influence, modules, descending, ascending, cns-networks]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (факты Bates 2026)
- uncertainty:
  - BANC — самка (♀ 188 508 нейронов/199M синапсов — по нашим данным); ламина/ocellar ganglion отсутствуют (есть в FAFB) — охват неполный
  - «influence» — линейная аппроксимация (авторы честны: линейная динамическая система; не учитывает нелинейности)
  - 17 AN/DN кластеров — порог/метод (deepSplit=0, minClusterSize=8) — конвенция, не биологическая «истина»
- falsification_trigger:
  - если новые (неврологические) эксперименты опровергнут «локальные петли сенсор→эффектор» как доминанту — обновить
  - если NT-предсказания (ResNet-18, 8 классов) пересмотрены (доля точности) — обновить
- transfer_boundary:
  - НЕ переносить «модули/сети» как готовую онтологию CASA: это кластеры по конвенции; но архитектурные выводы (локальные петли, междун centrality AN/DN, subsumption) — сильный материал для сравнения с CASA (после синтеза)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: BANC, NT, влияние, модули, сети.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Nature 2026 (полный текст в .cdp/scratch/PMC13518251.xml).

## Core Unit
- context:
  - полный коннектом мозг+нервный шнур (BANC): как реконструирован, что в нём, какие архитектурные закономерности.
- signal:
  - вопрос про полный чертёж НС, архитектуру сенсор→движение, модули/сети, NT-профили.
- action:
  - использовать: BANC (EM 4×4×45 nm, GridTape, 7 010 секций, ~160k нейронов, 155 proofreaders/38.6 person-years; ламина/ocellar — нет); NT-предсказание (ResNet-18, 8 классов: ACh/DA/GABA/Glu/His/OA/5HT/TA; ground truth 3 379 типов/60 394 нейрона); adjusted influence (~24e9 пар, линейная аппроксимация); локальные петли сенсор→эффектор (реафферентация) + длинные петли; AN/DN (3 165) → **17 поведенческих кластеров**; betweenness AN/DN/VNC-intrinsic выше; 13 CNS networks (спектральная, 50 568 нейронов; leg VNC — крупнейшая; L/R visual+olfactory); 10/13 сетей > median влияния на эффекторы (CX/olfactory — нет); архитектура: модули из локальных петель + селективные длинные связи, subsumption (один модуль рекрутирует/подавляет).
- outcome:
  - архитектура = распределённые модули (не «сэндвич»); локальные петли (reafference) + длиннодистанционные пути через AN/DN; иерархия модулей (subsumption).
- lesson:
  - природа реализовала **воплощённое/распределённое управление**, а не центральный исполнительный «сэндвич» — это прямой вызов классике и релевантно CASA (архитектура управления).

## Fundamentals (самодостаточный опорный слой)

### 1) BANC: реконструкция и охват
- Serial-section EM (GridTape), 4×4×45 nm, 7 010 секций; brain + nerve cord (самка); ~160 000 нейронов (ожидаемое); CNN-сегментация + ручная верификация; 155 proofreaders, ~3.5 года, ~38.6 person-years.
- Ограничения: ламина и ocellar ganglion отсутствуют (есть в FAFB); открытый (open-source) набор.

### 2) Нейротрансмиттерное предсказание
- 3D CNN (ResNet-18): 8 классов (ACh, DA, GABA, Glu, His, OA, 5HT, TA); ground truth из литературы: 3 379 типов, 60 394 нейрона (FAFB/MANC/hemibrain); 80/20 split.

### 3) Метрика влияния (adjusted influence)
- Линейная динамическая система: стационарный отклик на постоянную стимуляцию; вес = доля синапсов от входного пула постсинаптической клетки; фильтр <5 синапсов; масштабирование (max eigenvalue 0.99); **~24 млрд парных оценок** предвычислено; согласуется с дистанционными метриками (network distance).

### 4) Сенсоры→эффекторы: локальные петли
- Сенсоры/эффекторы распределены по телу (моторные нейроны глаз/антенн/рта/передней кишки — brain; ног/крыльев/халитер/брюшка/репродуктивных/задней кишки — VNC; эндокринные — оба).
- **Большинство групп эффекторов получают сильнейшее влияние от сенсоров того же отдела** (напр., pharynx: моторные ↔ сенсорные — петля реафферентации); локальные петли почти в каждом отделе.
- Длинные петли: pharynx-моторные ← crop/labellum/proboscis сенсоры — ограничение кормления (crop наполняется — стоп).

### 5) AN/DN и поведенческие модули
- AN/DN участвуют в большинстве кратчайших путей сенсор→эффектор (betweenness выше всех суперклассов; VNC intrinsic — высокий: 33% сенсоров/3.4% эффекторов в VNC vs 16%/0.47% в brain).
- 3 165 AN/DN → PCA-UMAP по прямым связям → **17 кластеров** (поведенческие модули: head-orienting, walking, threat-response, visceral control...); 9.3% с известными функциями совпадают.
- Специализация/координация: сходство влияний — cell type > cluster > разные кластеры; внутри кластера — разнообразие (разные сенсорные входы/моторные выходы).

### 6) Взаимодействия модулей и 13 сетей
- Паттерн влияний между кластерами: сильнейшие (≥85th percentile) — пример: proprioceptive ↔ threat-response ↔ walking (WPNs/VNC-интернейроны).
- **Архитектура: локальные сенсор-моторные петли + селективные длинные пути; иерархия (subsumption): модуль рекрутирует/подавляет другой** — аналогии с робототехникой.
- **13 CNS networks** (спектральная кластеризация, 50 568 proofread нейронов): abdominal VNC, leg VNC (крупнейшая), dorsal VNC, lateral/inferior/posterior brain, L/R visual, L/R olfactory, flange median bundle и др.; 10/13 > median влияния на ≥1 эффекторную группу; CX-связанная и обонятельные сети — не имеют (P=9.3e-10).

### 7) Обсуждение: против «сэндвича»
- Классика: sensing→cognition→action (центральный исполнительный; CX/MB — «исполнительные»).
- Альтернативы: экологическая теория (без среднего слоя) vs **воплощённое познание**: модульная распределённая архитектура, тесно связанная с телом; роль внутренних представлений ограничена (efference copy, memorized snapshots).

## Operationalization
- first_adoption_task: в слой 3 (коннектом): BANC-факты как ядро; при CASA — архитектура (модули/петли/subsumption/13 сетей) — главный материал для сравнения (после синтеза).
- validation_check: сверить наши числа (188 508/199M) с текстом (BANC v888 — подтверждается «~160k» — уточнить: BANC v888 = 188 508? — TODO сверить с метаданными); NT-точность — TODO.
- success_criterion: карточка покрывает 3.1 (реконструкция/NT) и 3.3 (архитектура) с полным текстом.
- rollback_or_mitigation: при новых релизах BANC — обновить числа; influence-метрика — помнить линейность.

## Lifecycle
- deprecation_reason: —

