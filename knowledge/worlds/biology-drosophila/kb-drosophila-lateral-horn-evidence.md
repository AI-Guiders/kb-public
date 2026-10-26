---
type: Evidence Card
title: 'Drosophila melanogaster — Латеральный рог: мультимодальный гейт контекстной памяти (evidence card v1)'
description: '**Данные:** `D:\Experiments\casa-data\connectomes\banc-v888\banc_888_meta.feather` (188 508 × 81) + `banc_888_edgelist_simple_v3.feather` (13 620 865 рёбер). Ключ = banc_888_id. Скрипты: `.cdp/scratch/lh_analysis_v2.py`, `lh_preclasses.py`; результат: `.cdp/scratch/lhon_inputs_v2.csv`, `lhon_report_v2.txt`.'
tags: [biology-drosophila, worlds, kb, evidence, lateral-horn, multisensory, context-gate, cltm, lh]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Латеральный рог: мультимодальный гейт контекстной памяти (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Neurogenetic dissection of the Drosophila lateral horn reveals major outputs, diverse behavioural functions, and interactions with the mushroom body» — eLife 2019, DOI 10.7554/eLife.43079, PMC6529221 — **полный текст прочитан** (44 LHON, 14 LHIN, мультимодальные входы, LH→DAN, валентность)
  - paper: «Functional and anatomical specificity in a higher olfactory centre» — eLife 2019, DOI 10.7554/eLife.44590, PMC6550879 — **полный текст прочитан** (410 in vivo клеток, категории запахов, номенклатура, супервоксели)
  - related: Nat Commun 2019 (cLTM — PMC6779902), BANC (Bates 2026 — LH в сетях), Frechter et al. 2019 (~165 типов)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полные тексты ×2 прочитаны (LH: типы, входы, выходы, функции, in vivo); синаптический уровень (BANC) — НЕ анализировался (выгрузка данных — сеть недоступна).

## Metadata
- card_id: kb-drosophila-lateral-horn-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [lateral-horn, multisensory, context-gate, cltm, lhon, lhin]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полных текстов) + open (механизм гейта)
- evidence_type: paper (ориг., полные тексты ×2)
- confidence: high (структура: Dolan 2019; функции: Frechter 2019); medium (механизм «проверки» — НЕ установлен)
- uncertainty:
  - overlap-анализ (Dolan) = прокси (не синапсы); мультимодальные стимулы in vivo (Frechter) НЕ тестировались (только запахи)
  - репликация cLTM (Nat Commun 2019) не проверялась
- falsification_trigger:
  - если BANC-анализ покажет отсутствие синаптической конвергенции на LHON — ослабить «детекторы конъюнкции»
- transfer_boundary:
  - НЕ переносить «LH = контекстный гейт» на всё: LH — также функции **наивной (врождённой) валентности — мягкие приоры, НЕ «инстинкты»** (см. секцию «Инстинкт = мягкий приор», PMC7145822); НО: **мультимодальная конвергенция + LH→DAN + не-обонятельные LHN** — сильный материал для CASA (гейт доступа по контексту)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: структура, функции, гейт-статус.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — eLife ×2 (полные тексты в .cdp/scratch/PMC6529221.xml, PMC6550879.xml).

## Core Unit
- context:
  - LH = место мультимодальной конвергенции; кандидат на «проверку контекста» для cLTM (retrieval требует ВСЕ условия).
- signal:
  - вопрос «как муха проверяет условия (свет+температура+решётка)», «что такое LH», «мультисенсорный гейт».
- action:
  - использовать: **структура (Dolan 2019)**: 44 LHON типа (26 ACh, 13 GABA, 9 Glu; **3 типа — двойные NT**: AV2a1/a4 — ACh+GABA, AV2b1/b2 — ACh+GABA, AV7a1 — ACh+Glu!); **14 LHIN** из НЕ-обонятельных областей: **WED-PN1–6** (слух/механо), **LO-PN1–2** (зрение/лобула), **GNG-PN1** (вкус/SEZ), **VNC-PN1** (восходящий — механо/феромоны) + из литературы 4 термо + 2 вкусовых; **конвергенция валентностей** на одних LHON (аверсивные DA2/DL4/VA7l + аттрактивная VM1 → AV1a1, AV6b1); **LH→DAN** (LHON аксоны рядом с дендритами PAM/PPL1! — «may be upstream of DANs... tune MB coding or act as reward/punishment»); **LHON→SLP/SIP/SMP** (те же области, что MB); **единственный LHON в CX — PV5k1** (вход от механо/ветра WED-PN3! — мост LH→CX); **нет прямых нисходящих в VNC**; **валентность**: 15 линий (из 89) → оптогенетически подход/избегание; покрытие: 165 «core» LH-типов (Frechter), split-GAL4 ~63/165.
  - **функция (Frechter 2019)**: 587 клеток in vivo patch-clamp (410 в анализе: 242 LHON, 84 LHLN, 84 PN); **иерархическая номенклатура** (tract/anatomy group/cell type; 25 входных+25 выходных супервокселей); **LH кодирует категории запахов** (ROC-селективность, временная динамика, супервоксель-категория); **«not all LHNs respond to odors»** — часть LH-нейронов — не-обонятельные (кандидаты в контекстные!); LHON/LHLN — высокое входное сопротивление, низкая ёмкость (дешевле спайки, чем PN).
  - **гейт-статус**: cLTM (Nat Commun 2019) требует при retrieval: AMMC (механо), глаза/оптическая доля (зрение), LH-нейроны (smpr/slpr/vlpr), ePN+iPN; **MB-V2/MB — диспенсабельны**; «любое несовпадение контекста → PI=0». **Механизм (порог/AND/веса) — НЕ установлен**.
- outcome:
  - LH — мультимодальный узел: входы из всех сенсорных модальностей; часть нейронов — не-обонятельные; связь с DAN (DA!); выходы в SLP/SMP/CX; **структурная база для «AND-гейта» есть, механизм неизвестен**.
- lesson:
  - **контекстный гейт доступа** = мультимодальная конвергенция + DA-записанный эталон + LH-интеграция (предположительно); для CASA: **память с контекстным ключом (все модальности), LH-аналог = гейт, а не хранилище**; LH→DAN — «врождённый сигнал в обучающий контур» (пред-обучение/мотивация!).

## Fundamentals (самодостаточный опорный слой)

### 1) Типы LH (Dolan 2019)
- LHON 44 типа (ACh 26 / GABA 13 / Glu 9; 3 двойных); LHIN 14 (из других областей); LHLN (локальные); 165 core (Frechter).

### 2) Мультимодальные входы
- WED-PN1–6 (механо/слух), LO-PN1–2 (зрение), GNG-PN1 (вкус), VNC-PN1 (восходящий), + термо/вкус (лит.); кузнечик: LH-клетки на обоняние+зрение (Gupta & Stopfer).

### 3) Функции
- Категории запахов (in vivo); валентность (подход/избегание — оптогенетика); выходы в SLP/SIP/SMP; нет прямых DNs; LH→DAN; PV5k1→CX.

### 4) Гейт cLTM (статус)
- Необходимо: AMMC+зрение+вкус+обоняние→LH; не нужно: MB. Механизм: НЕИЗВЕСТЕН (порог/AND/веса); BANC-анализ (синаптическая конвергенция на LHON) — НЕ сделан (сеть).

## Operationalization
- first_adoption_task: понимание «контекстного гейта» для CASA; при CASA — «контекст-адресованная память (вектор условий) + гейт + DA-эталон».
- validation_check: BANC-анализ (выгрузка — сеть; TODO); физиология мультимодальных ответов LH у дрозофилы — НЕТ (TODO); репликация cLTM — TODO.
- success_criterion: карточка покрывает LH (полные тексты ×2 + cLTM-связь) с честным «механизм неизвестен».
- rollback_or_mitigation: при BANC-анализе — обновить; при опровержении — сузить.

## Lifecycle
- deprecation_reason: —

---

## BANC-анализ v888 (2026-09-19, appendix): синаптическая конвергенция на LHON

**Данные:** `D:\Experiments\casa-data\connectomes\banc-v888\banc_888_meta.feather` (188 508 × 81) + `banc_888_edgelist_simple_v3.feather` (13 620 865 рёбер). Ключ = banc_888_id. Скрипты: `.cdp/scratch/lh_analysis_v2.py`, `lh_preclasses.py`; результат: `.cdp/scratch/lhon_inputs_v2.csv`, `lhon_report_v2.txt`.

**Метод:** LHON = cell_class=='lateral_horn_output_neuron' (1 080 нейронов); категории пре-входов: olf (AL-PN/local/centrifugal/output), vis (visual_projection/centrifugal), mech (wedge_projection/chordotonal/campaniform/hair_plate/bristle/johnstons), gust (gust/taste), thermo (thermosensory), sez (subesophageal_zone_projection — отдельно, не чистая модальность).

**Результаты (1 080 LHON, 129 914 рёбер):**
- **≥2 модальности: 708 (65.6%)** при ≥1 синапсе; **361 (33.4%)** при ≥3 синапсах.
- ≥3 модальности: 323 (30%) any / 94 (8.7%) strong; 4 модальности: 27.
- По модальностям (LHON с входом): olf 1 011 (94%), **vis 511 (47%)**, **mech 307 (28%)**, **sez 243 (22.5%)**, gust 13, thermo 9.
- Топ-комбо: **mech|olf|vis 199 (18%)**, olf|vis 181, olf|sez 124, mech|olf 76.
- Топ пре-типы: AL-PN (DA1_lPN 493, VA1v_adPN 396, V_ilPN 360...), LH-локальные (LHPV2a1_c 766), KCg-m (649 — MB!), MBON (2 234 рёбер), LHCENT (588), LPLC2 (лобула — 281), WED-PN (1 319 рёбер).

**Вывод:** структурная база для «детекторов конъюнкции» — **подтверждена на синаптическом уровне** (2/3 LHON мультимодальны; 199 трёхмодальных — механо+обоняние+зрение — кандидаты в AND-детекторы). **Механизм (порог/AND/веса) — НЕ проверен** (нужна физиология); cLTM-поведение (Nat Commun 2019) — согласуется (мультимодальность + DA + LH), но причинность гейта не доказана коннектомом.

**Ограничения:** категоризация по cell_class/super_class (не все модальности аннотированы; 64k рёбер — pre без cell_class — внутренние); sez — смешанная; мультимодальность ≠ конъюнкция (нет проверки одновременности/порога).

---

## BANC-анализ v888 — follow-up (2026-09-19): LHON→DAN, трёхмодальные, выходы

**1) LHON → DAN (проверка «врождённый сигнал в обучающий контур»):** 1 834 рёбра, **482 LHON (45%) → 283 DAN (94% из 301 DAN!)**. Оба контура: **PAM (награда) И PPL1 (наказание)** (PPL201 181, PAM04 179, PAM06 150, PAM08 144, PAM05 136, PAM01 131, PAM02 127, PAM11 102, PPL107 95...). Топ-пары: LHPV10d1→PPL107 (104), LHAD2b1→PPL201 (92), LHMB1→PPL105 (50), CRE011→PAM08 (45). **Dolan-гипотеза («LHON may be upstream of DANs... reward or punishment») — подтверждена на синаптическом уровне, оба полюса.**

**2) Трёхмодальные LHON (mech|olf|vis, n=217):** **все — cell_type=NaN, NT=NaN** (аннотация подтипов/NT неполная для них; ограничение данных, не отсутствие).

**3) Выходы LHON (130 860 рёбер):**
- **LHON → CX: 269 LHON, 2 371 рёбра** (central_complex_input 2 171 + output 203) — мост LH→CX **массовый** (LHPV6q1 220, LHPV5l1 147, CRE103b 141, LHPV10d1 97...) — не только PV5k1 (Dolan: «one cell type to CX» — коннектом: 269!).
- **LHON → DN: 491 LHON, 2 592 рёбра** — ⚠️ **расхождение с Dolan 2019** («no direct descending output»): в BANC прямые LHON→descending_neuron есть (Dolan — световая микроскопия, часть типов; коннектом полнее).
- **LHON → MB: KC 5 096, MBON 1 397, MB-DAN 1 834** — LH↔MB полный цикл.
- Реципрокность: LHON→WED-PN 885, LHON→lobula_tangential 751+columnar 532 (зрение), LHON→AL-PN 4 433.

**Обновлённый вывод:** LH — не просто «инстинктивная область»: это **мультимодальный узел с прямыми связями: (а) в DA-контур (94% DAN — оба полюса валентности), (б) в CX (269 LHON!), (в) в мотор (491 LHON → DN), (г) в MB (KC/MBON/MB-DAN)**. Для CASA: LH-аналог = **интегратор контекста с прямыми выходами в учителя (DA), аттрактор (CX) и мотор (DN)** — «гейт с полным подключением».

**Ограничение:** «трёхмодальные» — без типовых имён (NaN); причинность (AND/порог) — не проверена (физиология); категории — по cell_class/super_class.

---

## ⚠️ Приоритет и новизна (2026-09-19, честная переоценка): наш анализ ≠ первооткрытие

**Найдено (полный текст прочитан):** PMC13190573 — «Convergence-divergence circuits for multimodal integration of innate and learned opponent valences» (Front Syst Neurosci 2026, DOI 10.3389/fnsys.2026.1822122).

**Что уже опубликовано (до/вместо нас):**
- **LHON мультимодальность — да, известно**: «LHONs and SPINs receive broad multimodal inputs»; «Each LHON input to SMP353 forms a definitive valence signal by multimodal integration» (unimodal + multimodal convergent integration).
- **Механизм «как проверяется» — ПРЕДЛОЖЕН (2026)**: SPIN SMP353 — single-cell integration opponent valences; **dendritic compartmentalization** (входы/выходы разделены); **shunting inhibition (GluClα)**; **«multiplicative disinhibition... for multiplication to signal the spatiotemporal contingency»** = **coincidence detection / AND-подобный механизм**; NT-логика: **ACh LHON = привлекательное (еда), Glu LHON = отвратительное (токсины/социальные/температура)**; MBON (learned) → SPIN (MBON07/14 — LTM!); механо-канал: **WEDPN3/6A/12/8C → LHPD2d1 (Glu) → SIP015** (wind/acoustic); конвергенция LHON/MBON → SPIN → **FBt (CX, layer 6) + MB DANs + модуляторы** («autoencoder-like», convergence-divergence); hunger → γ-DAN → MBON07/14 → SMP353.
- **Цифры «% LHON мультимодальных» — НЕ публиковались** (эта работа — SPIN-слой, hemibrain+FlyWire, без BANC-процентов).

**Что новое у нас (BANC v888, не найдено в литературе):** 65.6% LHON мультимодальных (708/1080), 33.4% strong, 199 трёхмодальных (mech|olf|vis); LHON→DAN 482 LHON → 94% DAN (PAM+PPL1); LHON→CX 269; LHON→DN 491 (расхождение с Dolan).

**Переоценка:** концепция «мультимодальная конвергенция в LH + конвергенция-дивергенция + NT-оппонентная логика» — **уже в науке (2026)**; наш вклад — **количественный слой на BANC v888 + LHON→DAN/DN-цифры** (не первооткрытие, но подтверждение/расширение). **«Как проверяется» — ответ уже есть в литературе (GluClα + dendritic + coincidence) — использовать!**

---

## «Инстинкт» у дрозофилы = мягкий приор (2026-09-19, проверено: PMC7145822)

**PMC7145822** (eLife 2020, «Differential Role for a Defined LH Neuron Subset in Naïve Odor Valence» — полный текст прочитан):
- **PD2a1/b1 — холинергические LH-нейроны** (R37G11-GAL4, 6–7 нейронов): **наивное избегание** (без обучения! 7/12 запахов: silencing → ↓avoidance).
- **НО приор НЕ жёсткий**: (а) **концентрация**: эффект при 10⁻², исчезает при 10⁻³ (мухи при этом МОГУТ conditioning!); (б) **state**: **голод полностью подавляет эффект** (без изменения нейронного ответа!); (в) **время**: 40 с — нет эффекта, 80 с — есть; (г) **initial preference** — не зависит от PD2a1/b1 (первый импульс — другой механизм).

**Вывод (инженерный):** «врождённое» у дрозофилы = **мягкий приор валентности** (категории: ACh=еда+, Glu=токсины/социальное−), НО: контекст-зависимый (state), концентрация-зависимый, время-зависимый, переписываемый обучением (MBON→LHON; MBON > uPN в SMP353; learned > innate в SPIN). **Жёсткая только архитектура** (каталог/связи/NT/примитивы/воронка) — не поведение. **Модель: «доска с приорами»** (не инстинкты, не чистая доска).

**Для CASA:** не проектировать жёсткие «стимул→ответ»; проектировать: архитектура (жёсткая) + приоры валентности (мягкие, переписываемые) + state-модуляция (голод→приоритеты) + обучение (TD/efference/контекст-гейт). Приоритеты (aversive>appetitive, learned>innate) — структурные смещения, не константы.

