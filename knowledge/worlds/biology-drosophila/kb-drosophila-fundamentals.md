---
type: KB
title: 'KB fundamentals: Drosophila melanogaster (biology.drosophila) v1'
description: '**Назначение:** самодостаточный опорный слой определений (агент не обязан каждый раз открывать первоисточник).'
language: ru
world: biology
subworld: drosophila
---
# KB fundamentals: Drosophila melanogaster (biology.drosophila) v1

**Назначение:** самодостаточный опорный слой определений (агент не обязан каждый раз открывать первоисточник).

**Мир:** biology.drosophila
**Связь:** status-drosophila.md → playbook-drosophila-operational.md → **этот файл** → evidence-карточки при необходимости.

---

## Scope

- Полный evidence-синтез D. melanogaster как «reference implementation от природы»: геном → развитие → клетки/типы → коннектом → физиология → поведение → эволюция.
- Правило прохода: фундаментальный проход ПОЛНЫХ текстов (Europe PMC fullTextXML / PMC OA); карточки kb-*-evidence.md с Layer contract; честные границы.
- Правило слоёв: status → operational → fundamentals (этот) → evidence.

## Core concepts

### Слой 1 — Геном и развитие (evidence: genome, development, neurogenesis, metamorphosis, sex-determination)
- Геном: ~180 Mb, ~14k генов, dm6, 2n=8; ТЭ ~часть; Canton S — стандарт; one-fly (NAR 2020).
- Развитие: French Flag (градиенты Bcd/Cad), gap-динамика, stripe-энхансеры, Zelda/Opa pioneer, 7-stripe/zebra, frequency doubling; Hox-сегментация.
- Нейрогенез: нейробласты → линии → гемилинейджи (Notch A/B); **17 TF — глобальный код birth order**; Broad — терминальный селектор (14A); две волны (первичные/вторичные, Imp/dati).
- Метаморфоз: имагинальные диски (эмбрион → личинка → эверсия), 20E-каскад (E74/E75/BRC), клей Sgs; регенерация (Jnk/Dilp8).
- Пол: sxl→tra→dsx/fru; dsx/fru — инструктивные; P1 (20), aSP-f/g (cVA); диморфизм.

### Слой 2 — Клетки и типы (evidence: celltypes, atlas, glia)
- **8 453 типа** (FlyWire, консенсус); 120 линий = 183 гемилинейджи = 88% (30 233) центральных нейронов; singleton 59% типов; стереотипия (синапсы R≥0.92; рёбра 53% кросс-датасет); «снежинка» >50% рёбер; 68% валидация hemibrain-типов.
- Мета-атлас: 329 466 нейронов (9.8×), 246 → 4 167 транскриптомных подтипов; **8/8 типы = гемилинейджи** (Ptx1+VGlut = SMPad1).
- Глия: 3 класса (NPG: ALG/EG; CG; PG/SPG — BBB), две волны, lateral glioblast; доля ~13k (из данных).

### Слой 3 — Коннектом (evidence: banc-connectome, celltypes, insect-connectomes)
- BANC (♀, мозг+шнур, 4×4×45 nm, ~160k нейронов, 38.6 person-years; ламина/ocellar — нет); FAFB; MCNS (♂); MANC (♂).
- NT-предсказание: 8 классов (ACh 48%, Glu 15%, GABA 13%, His 4.7%, DA 5.4%, OA 2.4%, 5HT 1.6%, TA 0.1% — из данных).
- Архитектура: adjusted influence (~24e9 пар), локальные петли сенсор→эффектор (reafference), 17 AN/DN кластеров (3 165), 13 CNS-сетей, subsumption; bottleneck выхода (efferent 0.5%).
- Другие насекомые: полный коннектом — только D. melanogaster; CX консервативен.

### Слой 4 — Физиология (evidence: neurotransmitters, plasticity, electrical-synapses)
- Котрансмиссия (VPM4: OA+Glu), авторецепторы (OAα2R/mGluR), слоёное ингибирование (MBON-11/GluClα/Rdl).
- Электрические синапсы: GF→TTMn (shaking-B, 1.14 мс), Frazzled/DCC-регуляция сборки GJ (ICD/P3).
- Пластичность: структурная (s-LNv, циркадианная), методы-ловушки; LTP/LTD — MB (слой 5).

### Слой 5 — Поведение (evidence: cx-navigation, sleep, learning-memory, courtship-song, escape, aggression, feeding)
- Навигация: CX (ring attractor: EPG 16 wedges; FB 9×9 >200 типов; векторные вычисления — базис 4×90°; 3 мотива; мультимодальный компас).
- Сон: множественные состояния, slow-wave, dFB (sleep need), ER5; гомеостатическая «потребность».
- Обучение: MB (KC sparse, MBON, DAN-учитель; OA=состояние/DA=валентность; APL; VPM4).
- Песня: sine/pulse, fast/slow; генетика (QTL 3R 42%), QST>FST.
- Эскап: GF (GJ, 1.14 мс); агрессия: VPM4-эскалация + тормоза; питание: пептиды (DILP/Upd2/AKH/NPF), DA-WED (конкуренция мотиваций), Fdg-команды.

### Слой 6 — Эволюция (evidence: species-genomes, sexual-selection, evodevo, courtship-song)
- sim-комплекс: перестройки 535–542 (90/млн лет), X-обогащение, In(3R) 13.6 Mb; tRNA/Y.
- Половой отбор: polyandry/monogamy (Fst/π/DFE — 115 поколений); песня — направленный отбор.
- Эво-дево: консервация Hox, 17TF, FB, OA, dsx/fru; «стабильный каркас + пластичный репертуар».

## Anti-patterns

- **Саммари вместо полных текстов** (урок: фундаментальный проход = полные тексты).
- **«Типы = атомы»** (ложно: singleton 59%, 32% невалидированных — типы = устойчивые кластеры с вариацией).
- **«Нейрон = один NT»** (ложно: котрансмиссия OA+Glu и др.).
- **«Центральный контроллер»** (ложно: distributed control, супервизоры MB/CX, локальные петли).
- **Пластичность как «переобучение»** (ложно: локальная/предсказуемая; обучение — отдельный модуль).

## Relation to repository / tools

- Источники: Europe PMC fullTextXML (рабочий путь); PubMed esummary — только скрининг; OA:N — полный текст недоступен (FCA Science 2022).
- Скрипты в .cdp/scratch (fetch_*/extract_* .ps1) — конвейер: поиск → скачивание → извлечение секций → карточка.

## Evidence and updates

- Карточки (17): genome, development, neurogenesis, metamorphosis, sex-determination, celltypes, atlas, glia, banc-connectome, insect-connectomes, neurotransmitters, plasticity, electrical-synapses, cx-navigation, sleep, learning-memory, courtship-song, escape, aggression, feeding, species-genomes, sexual-selection, evodevo (23 файла).
- `Проверено:` 2026-09-19 (раунд 6): все темы evidence-plan.md 1.1–6.4 покрыты полными текстами (или честными аннотациями — 3.4, частично 5.5).
- Синтез: kb-drosophila-synthesis.md (законы 1–6, уточнения, пределы).

**Status:** active

