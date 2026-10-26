---
type: Note
title: evidence-plan — план полного evidence-синтеза (biology.drosophila)
description: '**world-id:** `biology.drosophila` · **Статус:** активен (2026-09-19) · **Цель:** собрать ВСЁ известное о Drosophila melanogaster как reference implementation от природы'
tags: [biology-drosophila, worlds, evidence, plan, reference-implementation]
language: ru
world: biology
subworld: drosophila
---
# evidence-plan — план полного evidence-синтеза (biology.drosophila)

**world-id:** `biology.drosophila` · **Статус:** активен (2026-09-19) · **Цель:** собрать ВСЁ известное о Drosophila melanogaster как reference implementation от природы

---

## Метод (как делаем evidence)

1. **Тема = единица работы**: каждая тема (подслой) получает отдельную evidence-карточку `kb-<topic>-evidence.md` (по `templates/cards/template-kb-evidence.md` — Layer contract: Provenance/Metadata/Epistemic Linkage/Core Unit/Fundamentals/Operationalization/Lifecycle).
2. **Поиск**: PubMed eutils (esearch → esummary) — систематические запросы по теме; приоритет: обзоры (reviews) + ключевые оригинальные работы + свежие (2023–2026). Запросы с полями: `[tiab]`, `review[pt]`, диапазоны дат.
3. **Полные тексты (фундаментальный проход)**: для отобранных работ — **Europe PMC fullTextXML** (`https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` — OA-статьи; проверка OA: `isOpenAccess` / PMC OA API). Для не-OA (издатель запрещает XML) — только аннотация, помечаем честно. Скрининг по заголовкам = отбор, НЕ проход.
4. **Карточка**: факты из ПОЛНОГО текста с привязкой к секции/месту; таблица «факт | источник | тип | год | DOI/PMID | уверенность» + противоречия + не найдено + TODO.
5. **Слой**: карточки тем агрегируются в слой (обновление kb-файла слоя).
6. **Честность**: покрытие (сколько просмотрено/прочитано полных текстов), что НЕ нашли, противоречия; «проверено» = карточка с источником + полный текст.

## Карта тем (по слоям)

### Слой 1 — Геном и развитие
- [x] 1.1 Геном: структура, размер, гены, транспозоны, сборки (dm6) — `kb-drosophila-genome-evidence.md` (скрининг+источники; TODO: полные тексты OA по геному, число генов FlyBase, доля ТЭ)
- [x] 1.2 Развитие: сегментация (бикоид, гэп, pair-rule, Hox), Нобель 1995 — `kb-drosophila-development-evidence.md` (полный текст PLoS Genet 2021 прочитан; TODO: Hox-обзоры, секции 7/9)
- [x] 1.3 Нейрогенез: нейробласты, линии, гемилинейджи, birth-order код — `kb-drosophila-neurogenesis-evidence.md` (полный текст Nature 2026 DOI 10.1038/s41586-026-10797-w прочитан; TODO: точный список 17 TF, секция brain)
- [x] 1.4 Метаморфоз: личинка→имаго, имагинальные диски, гормоны (экдизон/ЮГ) — `kb-drosophila-metamorphosis-evidence.md` (полные тексты Genetics 2022 DOI 10.1093/genetics/iyac020 + Genetics 2025 DOI 10.1093/genetics/iyaf211; TODO: JH-титры)
- [x] 1.5 Детерминация пола: sxl→tra→dsx/fru, хромосомная детерминация — `kb-drosophila-sex-determination-evidence.md` (полный текст Front Mol Neurosci 2023 DOI 10.3389/fnmol.2023.1284367; TODO: sxl-сплайсинг отдельным источником)

### Слой 2 — Клетки и типы
- [x] 2.1 Транскриптомные атласы (FCA, головной мозг, VNC): охват, кластеры, методы — `kb-drosophila-atlas-evidence.md` (полный текст Cell Genom 2026 DOI 10.1016/j.xgen.2025.101103: мета-атлас 329 466 нейронов 9.8×, 246→4 167 типов; FCA Science 2022 — OA:N, аннотация)
- [x] 2.2 Иерархия типов (Schlegel/FAFB, FlyWire codex): таксономия, число типов — `kb-drosophila-celltypes-evidence.md` (полный текст Nature 2024 DOI 10.1038/s41586-024-07686-5: 8 453 типа, 120 линий/183 гемилинейджи, стереотипия, 68% валидация, snowflake; TODO: суперкласс-составы)
- [x] 2.3 Глия: типы, функции, сигнализация — `kb-drosophila-glia-evidence.md` (полный текст Front Cell Dev Biol 2026 DOI 10.3389/fcell.2026.1775639: классы, две волны, BBB; TODO: доля глии в BANC)
- [x] 2.4 Связка транскриптом↔коннектом (Tango-seq и др.): методы, покрытие — в `kb-drosophila-atlas-evidence.md` (8/8 типы=гемилинейджи, birth-order реконструкция) + `kb-drosophila-neurogenesis-evidence.md` (R²=0.71, 122 группы)

### Слой 3 — Коннектом
- [x] 3.1 BANC/MCNS/FAFB: реконструкции, методы, покрытие, proofread — `kb-drosophila-banc-connectome-evidence.md` (полный текст Bates Nature 2026 DOI 10.1038/s41586-026-10735-w: EM 4×4×45nm, ~160k нейронов, 38.6 person-years, NT-предсказание 8 классов; TODO: сверить 188 508/199M с метаданными v888)
- [x] 3.2 Кросс-датасетные соответствия (FAFB↔BANC↔MCNS↔MANC/Hemibrain) — частично (Schlegel 2024: 68% валидация hemibrain-типов в FlyWire — в `kb-drosophila-celltypes-evidence.md`); TODO: FAFB↔BANC↔MCNS прямые карты
- [x] 3.3 Архитектурные закономерности (bottleneck, модули, NT-профили) — в `kb-drosophila-banc-connectome-evidence.md` (adjusted influence, локальные петли, 17 AN/DN кластеров, 13 CNS-сетей, subsumption)
- [x] 3.4 Другие виды насекомых (пчёлы/муравьи — есть ли коннектомы) — `kb-drosophila-insect-connectomes-evidence.md` (аннотации: полный коннектом — только D. melanogaster; CX-консервация — eLife 2021; следить за Apis/Locusta)

### Слой 4 — Физиология и пластичность
- [x] 4.1 Нейромедиаторы: профили, рецепторы, синтез/транспорт — `kb-drosophila-neurotransmitters-evidence.md` (Bates NT-предсказание 8 классов + Sci Adv 2026 DOI 10.1126/sciadv.aec4153; TODO: доли классов)
- [x] 4.2 Модуляция: DA/OA/5HT/TA — цепи, рецепторы, функции — в `kb-drosophila-neurotransmitters-evidence.md` (VPM4 OA+Glu котрансмиссия, авторецепторы OAα2R/mGluR, слоёное ингибирование; TODO: DA/5HT-цепи — слой 5)
- [x] 4.3 Пластичность: LTP/LTD, синаптическая/гомеостатическая — `kb-drosophila-plasticity-evidence.md` (Open Biol 2026 DOI 10.1098/rsob.260120: структурная s-LNv, методы; TODO: LTP/LTD — слой 5.2)
- [x] 4.4 Электрические синапсы (gap junctions), T-bar, активные зоны — `kb-drosophila-electrical-synapses-evidence.md` (eNeuro 2025 DOI 10.1523/ENEURO.0202-25.2025: GF→TTMn, Frazzled/DCC, shaking-B; TODO: GJ-доля в BANC)

### Слой 5 — Поведение
- [x] 5.1 Ухаживание и песня: цепи, генетика, сенсорика — `kb-drosophila-courtship-song-evidence.md` (полный текст G3 2025 DOI 10.1093/g3journal/jkaf050: 37 трейтов, slow:total pulses — дифференциация, сильный QTL 3R (42%), QST>FST; цепи P1 — карточка 1.5)
- [x] 5.2 Обучение и память: MB, ассоциативное, LTM, консолидация — `kb-drosophila-learning-memory-evidence.md` (полный текст Learn Mem 2024 DOI 10.1101/lm.053839.123: OA/DA-модуляция, VPM4/APL, котрансмиссия; TODO: LTM/консолидация; Nat Commun 2026 (рабочая память) скачана — извлечь)
- [x] 5.3 Сон и циркадианка: гомеостаз, осциллятор, роль в памяти — `kb-drosophila-sleep-evidence.md` (полный текст Curr Sleep Med Rep 2026 DOI 10.1007/s40675-025-00352-w + eLife 2021: dFB R23E10 9 типов, ER5; TODO: генетика сна)
- [x] 5.4 Навигация: CX, heading, интеграция пути, компасы — `kb-drosophila-cx-navigation-evidence.md` (полный текст eLife 2021 DOI 10.7554/eLife.66039: ring attractor, EB-PB-PEN/PEG, FB 9×9 >200 типов, vector computations, 3 мотива; TODO: сверить 16/18 с BANC)
- [x] 5.5 Избегание/эскап: GF, аверсивное — `kb-drosophila-escape-evidence.md` (полный текст eNeuro 2025 (GF→TTMn, GJ, 1.14 мс — карточка 4.4); Proc R Soc B 2025 — аннотация; TODO: полный текст Proc B)
- [x] 5.6 Агрессия и социальное — `kb-drosophila-aggression-evidence.md` (полный текст Sci Adv 2026 VPM4/MBON-11 (карточка 4.2): слоёное ингибирование, авторецепторы, Rdl; социальное — Ecol Evol 2019 аннотация; TODO: обзор социального)
- [x] 5.7 Питание и метаболизм — `kb-drosophila-feeding-evidence.md` (полный текст Open Biol 2019 DOI 10.1098/rsob.180259: DILP/Upd2/AKH/NPF/sNPF, периферийная модуляция (Gr5a/Gr66a/Ir76b), Fdg/IN1/ISNs, DA-WED (конкуренция мотиваций), MB-интеграция, микроструктура)

### Слой 6 — Эволюция
- [x] 6.1 Филогенетика видов, геномы видов — `kb-drosophila-species-genomes-evidence.md` (полный текст Genome Res 2021 DOI 10.1101/gr.263442.120: sim-комплекс, 535–542 перестройки, X-обогащение, In(3R) 13.6 Mb, tRNA/Y)
- [x] 6.2 Видообразование: песня, изоляция, гибриды — в `kb-drosophila-courtship-song-evidence.md` (G3 2025: QST>FST, сильный QTL)
- [x] 6.3 Половой отбор: диморфизм, предпочтения — `kb-drosophila-sexual-selection-evidence.md` (полный текст Proc R Soc B 2025 DOI 10.1098/rspb.2024.2744: polyandry/monogamy G85→G200, Fst/π/DFE)
- [x] 6.4 Эво-дево: Hox, консервативные каскады, гены поведения — `kb-drosophila-evodevo-evidence.md` (синтез из полных текстов 1.2/1.3/5.4/5.2/1.5/5.1: консервация Hox, 17TF, FB, OA, dsx/fru)

### Слой 7 — Синтез (после тем)
- [x] 7.1 Агрегация: законы 1–6 ↔ evidence — `kb-drosophila-fundamentals.md` (сводный опорный слой L1–L6 + Anti-patterns + указатели на 23 evidence-файла) + `kb-drosophila-synthesis.md` (законы 1–6 подтверждены/уточнены evidence-проходом)
- [x] 7.2 Честная карта уверенностей по темам — в `kb-drosophila-synthesis.md` (раздел «Карта уверенностей (7.2)»: 22/27 high с полным текстом, 3 medium, TODO по каждой теме)
- [x] CASA-сверка (после reflect) — `gap-casa-m6.md` + «Правка 2 (раунд 7)»: 9 новых уточнений из evidence-прохода, P6 (арбитраж мотиваций) и P7 (аттракторные примитивы) — кандидаты, приоритеты P1/P5/P4 обновлены
- [ ] 7.3 Reference-сводка «как работает» (лего-инструкция)

### Функциональная глубина (F) — «что за что отвечает» (доп. к слоям 3–5)
- [x] F1 Зрение (коннектом зрительной доли) — `kb-drosophila-vision-evidence.md` (Nature 2025: 732 типа, 15 колончатых, 892 колонки, T4a–d, NT 7 классов, DRA, 582 линии)
- [x] F2 Принятие решений/рабочая память — `kb-drosophila-decision-evidence.md` (Nat Commun 2026: FB goal-бамп, evidence integration (ramping), персистентность 5–10 с, оптимальность к статистике шлейфа, рекуррентность h∆K21↔PFG)
- [x] F3 Моторика/двигательное управление — `kb-drosophila-motor-evidence.md` (полный текст Nat Commun 2020 DOI 10.1038/s41467-020-19936-x: MDN→MF-типы (29/33), LBL40 (stance/tibia flexion), LUL130 (swing/leg lifting), эпистаз, кинематика 6×4; обезглавленные — делегирование)
- [x] F4 Визуальные пути (фоторецепторы→central brain) — `kb-drosophila-visual-pathways-evidence.md` (полный текст iScience 2020 DOI 10.1016/j.isci.2020.101590: MeTu-l/-c топографические vs MeTu-m нетопографический (medulla+lobula, Bui-супрессия), R7→MeTu (transTango), AOTU→bulb→EB (TuBu→R), консервация; Cell 2026 — PMC:NONE (аннотация))
- [x] F5 Ориентация-динамика (физиология CX) — `kb-drosophila-cx-coordination-evidence.md` (полный текст eLife 2021 DOI 10.7554/eLife.73077: copy-and-shift (рамки egocentric→geocentric), оптимальная интеграция (RA: веса по достоверности, гейты ON/OFF), steering-контроллер (CPU1 = desired−current, θM=kmotor·(ΣL−ΣR) — П-контроллер); + F2/F4/5.4)
- [x] F6 Память: LTP/LTD, консолидация — `kb-drosophila-plasticity-evidence.md` (полные тексты Sci Rep 2022 DOI 10.1038/s41598-022-14413-5 (след в MBON-γ1pedc — субклеточный компартмент, LTD-подобное ↓веса, prediction-error-петля g1→g5+DA, SVM: только g1 информативен) + Nat Commun 2019 DOI 10.1038/s41467-019-12436-7 (cLTM — мгновенная, без синтеза белка, вне MB, DA-зависимая; два пути LTM))

## Статус по слоям (кратко)
- Слои 1–7: ✅ (evidence-проход завершён, 2026-09-19)
- Функциональная глубина: F1–F2 ✅; F3–F5 — в работе (Europe PMC 503 — повтор); F6 — TODO
- Сравнительный анализ: каркас + личинка (Science 2023) + MICrONS (Nature 2025) ✅; C. elegans — аннотации (Cook 2019 OA:N)

## Правила
- Каждый факт в слое → ссылка на evidence-карточку (или DOI/PMID).
- «Не найдено/противоречие» — фиксируется, не замалчивается.
- Порядок строгий: evidence → слой → синтез → CASA (после полного синтеза).

