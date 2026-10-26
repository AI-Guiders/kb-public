---
type: Evidence Card
title: 'Drosophila — SPIN (superior protocerebrum intrinsic neurons): конвергенция-дивергенция валентности (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, spin, valence, convergence-divergence, glucl-alpha, arbitration]
language: ru
epistemic: fact (полный текст, 2 датасета, согласованные результаты)
world: biology
subworld: drosophila
---
# Drosophila — SPIN (superior protocerebrum intrinsic neurons): конвергенция-дивергенция валентности (evidence card v1)

## Provenance
- paper: «Convergence-divergence circuits for multimodal integration of innate and learned opponent valences» — Front Syst Neurosci 2026, DOI 10.3389/fnsys.2026.1822122, PMC13190573 — **полный текст прочитан** (методы + все результаты).
- datasets: hemibrain v1.2.1 + FlyWire v783; пороги: hemibrain ≥75 синаптических сайтов (well-traced), ≥5 синапсов (motif); FlyWire ≥40, ≥2 (≈5× z-разрешение); фильтр <2 синапсов — выброшен.
- created_at: 2026-09-19; updated_at: 2026-09-19.

## Metadata
- world: biology.drosophila
- layer: world
- status: draft

## Epistemic Linkage
- confidence: high (топология/NT/структура); medium (поведенческая интерпретация — гипотезы авторов)
- transfer_boundary: SPIN — **не** LH/MB/CX; это отдельный слой (третий порядок валентности) между LH/MB и FB; для CASA — **bottleneck/гейт валентности** (не память!).

## Core Unit
- context: как муха вычисляет «насколько это хорошо/плохо» из мультимодальных входов; арбитраж приоритетов; что за «bottleneck» между LH/MB и FB.
- signal: «SPIN», «SMP353», «SIP015», «как проверяется P(x)», «механизм AND», «валентность», «арбитраж».
- action: использовать **топологию** (LHON→SPIN many-to-one; SPIN→FBt one-to-many; MBON→SPIN many-to-many; OPN→SPIN one-to-one), **NT-логику** (ACh=+val, Glu=−val; 75% SPIN ингибиторные/модуляторные; GluClα доминирует), **механизм** (dendritic compartments, shunting inhibition, GluClα multiplicative = coincidence/AND), **приоритеты** (innate aversion > attraction; learned > innate; социальное > еда — арбитраж!).
- outcome: SPIN = «autoencoder-bottleneck»: мультимодальные входы (LHON innate + MBON learned) → низкоразмерная валентность → FBt (CX, context-dependent action selection) + DANs + модуляторы (глобальное вещание).
- lesson: **валентность — низкоразмерный скаляр, вычисляемый конвергенцией + оппонентной NT-полярностью + шунтовым мультипликативным торможением**; приоритеты зашиты в дендритную организацию (аверсивное ближе к аксону/блокирует).

## Fundamentals

### 1) SPIN — определение и масштаб
- SPIN = нейроны с >85% синапсов в SP (SMP/SIP/SLP/CRE); hemibrain: 1 411 (правый); FlyWire: 2 844 (L+R: 1 479/1 365); порог well-traced: 75 сайтов (hemibrain) / 40 (FlyWire).
- CRE (crepine) — традиционно не SP, но связан с MB/FB как SP (эволюционно консервативно; wiring efficiency с MB).

### 2) Топология (4 типа сетей — РАЗНЫЕ на разных стадиях!)
- **LHON→SPIN: many-to-one** (каждый LHON → специфичный SPIN-кластер; НЕ на всю популяцию) — конвергенция.
- **SPIN→FBt: one-to-many** (дивергенция; FBt — главный выход; FBc-входы — малы).
- **MBON→SPIN: many-to-many** (смешанная — MB-обучение широко вещается).
- **OPN→SPIN: one-to-one** (labeled-line для прямых обонятельных; в основном mPN — мультигломерулярные).
- Итог: разные стадии — разные модели (интеграция/смешанная/labeled-line) — «diverse networks for different stages».

### 3) NT-профиль (КЛЮЧЕВОЕ для механизма)
- SPIN: **глутамат обогащён, ацетилхолин обеднён** (vs мозг); **GluClα — доминирующий глутаматный рецептор** (Croset/Davie/Janssens/Li) → **глутаматергические SPIN — преимущественно ИНГИБИТОРНЫЕ**; Glu+GABA → **>50% SPIN ингибиторные**; ингибиторные+модуляторные = **3/4 SPIN**.
- NT-логика валентности: **ACh LHON = привлекательное** (еда: yeast/fruit glomeruli), **Glu LHON = отвратительное** (токсины, температура, влажность, феромоны/социальное). SMP353: excitatory attractive (ACh) + inhibitory aversive (Glu).
- MBON-логика та же: **MBON14 (attractive) = ACh; MBON07 (aversive) = Glu** — «design conserved across development» (Eschbach 2021).

### 4) SMP353 (пример: attractive-кодирующий) и SIP015 (aversive)
- SMP353 (cholinergic, 1 тип): входы — LHON (innate) + MBON07/14 (learned, LTM!); выход — **FBt layer 6 (dorsal FB)** + DANs + модуляторы.
- SIP015 (glutamatergic, 4–6 нейронов/полушарие): зеркальная (inhibitory LHON + excitatory MBON), **aversive**; механо-канал: **WEDPN3/6A/12/8C → LHPD2d1 (Glu) → SIP015** (wind/acoustic — aversive-biased).
- **Дендритная организация SMP353**: входы/выходы разделены (компартментализация); **inhibitory (aversive) — shunting (GluClα, хлорид-проницаемый)**; **«multiplicative disinhibition... for multiplication to signal spatiotemporal contingency»** = **coincidence detection**; приоритеты: innate aversion > attraction; learned > innate (зашиты в структуру/расположение входов).

### 5) Поведение/смысл
- SPIN-FBt (layer 6) — **context-dependent action selection** (foraging/metabolism/sleep — homeostasis); SPIN→DANs+modulatory — глобальное влияние (вещание).
- **Арбитраж**: социальные сигналы (Glu LHON LHPV4b9) подавляют foraging (конкурирующие цели!); hunger → γ-DAN → MBON07/14 → SMP353 (state-зависимость).
- «Autoencoder»-аналогия: конвергенция (сжатие) → bottleneck (SPIN = низкоразмерное) → дивергенция (вещание).

## Operationalization
- first_adoption_task: для CASA — «valence gate»: конвергенция мультимодальных сигналов → скаляр (валентность) → выход в action selection (FBt-аналог) + учитель (DAN-аналог); **NT-полярность = знак (награда/наказание)**; **шунтовое мультипликативное торможение = AND-гейт**; **приоритеты (аверсивное > аппетитное; learned > innate) — зашиты в структуру**.
- validation_check: поведенческая интерпретация (гипотезы авторов) — не проверена мной; связь SPIN↔CX (FBt) — подтверждена; совместимость с cLTM (LH→SPIN→FB) — да.
- success_criterion: карточка покрывает SPIN-слой (определение/топология/NT/механизм/поведение) из полного текста.

## Lifecycle

