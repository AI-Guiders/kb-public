---
type: Evidence Card
title: 'Drosophila melanogaster — Пластичность памяти: LTD-механизм, компартменты, консолидация (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, plasticity, ltm, memory-trace, compartment, consolidation, mb]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Пластичность памяти: LTD-механизм, компартменты, консолидация (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Visualization of learning-induced synaptic plasticity in output neurons of the Drosophila mushroom body γ-lobe» — Sci Rep 2022, DOI 10.1038/s41598-022-14413-5, PMC9213513 — **полный текст прочитан** (homer-GCaMP, MBON-g1, SVM-декодирование, shibire-блокада)
  - paper: «Long-term memory is formed immediately without the need for protein synthesis-dependent consolidation in Drosophila» — Nat Commun 2019, DOI 10.1038/s41467-019-12436-7, PMC6779902 — **полный текст прочитан** (cLTM: CXM/RICIN/dCREB2b, MB-независимость, dDA1)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полные тексты прочитаны (пластичность: ассоциативная локализована в g1; консолидация: cLTM — без белкового синтеза).

## Metadata
- card_id: kb-drosophila-plasticity-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [plasticity, memory-trace, mbon, g1, ltd, consolidation, cLTM]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полных текстов)
- evidence_type: paper (ориг., полные тексты)
- confidence: high (Sci Rep 2022 — функц. визуализация постсинапса+поведение; Nat Commun 2019 — фармако-генетика)
- uncertainty:
  - только аверсивное обонятельное обучение (короткая память; γ-лобус); другие валентности/сроки — не проверены (авторы: LTM — a/a'-лобусы)
  - cLTM — специфичный тип (контекстный); «без консолидации» — для этого типа, НЕ отменяет классическую консолидацию
- falsification_trigger:
  - если «г1-единственность» не подтвердится для других задач (награда/долгий срок) — обновить (авторы сами указывают)
- transfer_boundary:
  - НЕ переносить «одна синаптическая связь = память» на всё; НО: **субклеточные единицы (компартменты) как единицы памяти** + **prediction-error-петля** + **два пути LTM** — сильный материал для CASA

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: след памяти, два пути LTM.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Sci Rep 2022 + Nat Commun 2019 (полные тексты в .cdp/scratch/PMC9213513.xml, PMC6779902.xml).

## Core Unit
- context:
  - где и как хранится память: пластичность KC→MBON; локализация; консолидация.
- signal:
  - вопрос «какой синапс меняется», «есть ли LTD/LTP», «нужна ли консолидация».
- action:
  - использовать: **ассоциативная пластичность — в ОДНОМ компартменте**: MBON-γ1pedc>α/β — подавление постсинаптического ответа на CS+ (аверсивно-спаренный запах); **не-ассоциативная адаптация** — в g2–g4 (обобщённая, к любому запаху), g5 — почти без ответов; **SVM-декодирование**: только удаление g1 → шанс (50%) — g1 = единственный индикатор выученного; **поведение (shibire)**: блокада g1 ИЛИ g5/b'2 → нет различения CS+/CS-; g1 = место пластичности, g5 = downstream (противоположная валентность — feedforward ингибирование g1→g5: **баланс approach/avoidance**); **модель (Springer/Nawrot)**: ↓вес KC→MBON-g1 при совпадении CS+ с PPL1-γ1pedc (аверсивный DAN) → prediction-error (feedforward g1→g5 + feedback к DAN) — **насыщение + extinction** (TD-подобно!); **субклеточность**: «whole neurons are not the functional units» — **компартменты = независимо модулируемые единицы памяти** (не энграммы-клетки); **cLTM (Nat Commun 2019)**: формируется **немедленно, БЕЗ синтеза белка** (CXM/RICIN/dCREB2b не влияют), **rutabaga-нормален** (не через классический cAMP), **НЕ требует MB** (OK107/C772 блокады — retrieval цел), **DA-зависим** (TH-Gal4 Shits + dDA1-мутанты — нет cLTM); **отличается от ARM** (radish-нормален) и от классического LTM (MB+белок+консолидация).
- outcome:
  - **след памяти = субклеточный компартмент** (KC→MBON-g1), не клетка; механизм — LTD-подобное ↓веса при CS-US совпадении + prediction-error-петля (TD); **два пути долгосрочной памяти**: (1) классический (консолидация, белок, MB — «медленный»), (2) cLTM (немедленный, без белка, вне MB, DA — «быстрый»).
- lesson:
  - память: (а) **локальный синаптический след** (компартмент!), (б) **обучение = error signal (DA) + снижение веса** (анти-геббовское! аверсия), (в) **prediction-error-петля** (TD-подобная — насыщение+extinction), (г) **два трека LTM** — для CASA: дельта-обучение с предсказанием (TD) + отдельные треки «быстрой/медленной» памяти.

## Fundamentals (самодостаточный опорный слой)

### 1) След памяти (Sci Rep 2022)
- CS-US совпадение (KC sparse + DA-учитель) → ↓вес KC→MBON-γ1pedc (постсинаптический кальций ↓ — homer-GCaMP); специфично к CS+ (не CS-); без адаптации в g1 (в отличие от g2–g4: не-ассоциативная, обобщённая адаптация).

### 2) Поведение/декодирование
- SVM (псевдо-популяции 5 MBON): g1 — критичен; g2–g5 — не информативны для CS+/CS-.
- Shibire: блокада g1 или g5/b'2 → нет избегания CS+; g1→g5 (feedforward) — баланс валентностей (подход/избегание), результат баланса весов.

### 3) Модель и субклеточность
- Springer/Nawrot: ↓KC→MBON-g1 + g1→g5 (FF-ингибирование) + g1→DAN (feedback) = prediction-error; насыщение кривой обучения + extinction.
- Компартменты (аксонные) — функциональные единицы; «энграмма» = субклеточная, не клеточная.

### 4) Два пути LTM (Nat Commun 2019)
- Классический: контекст-независимая LTM — MB, белок, консолидация (spaced).
- cLTM: контекстная — без белка (CXM/RICIN/dCREB2b), без MB (OK107/C772), DA-зависимая (TH/dDA1), radish-нормальна (≠ARM), холодостойкая через 24 ч.

## Operationalization
- first_adoption_task: функциональная глубина F6 (память: LTP/LTD, консолидация) — закрыто; при CASA — «TD-подобное обучение + субклеточные следы + два трека памяти».
- validation_check: LTM a/a' (классический путь) — детали (не читала отдельно); reward-обучение — TODO; сон-консолидация (eLife 2015/eNeuro 2025) — в 5.2/5.3.
- success_criterion: карточка покрывает пластичность+консолидацию (полные тексты ×2).
- rollback_or_mitigation: при расширении (другие задачи) — обновить.

## Lifecycle
- deprecation_reason: —

