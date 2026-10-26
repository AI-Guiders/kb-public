---
type: Evidence Card
title: 'Drosophila melanogaster — Геном: структура, размер, гены, транспозоны, сборки (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, genome]
language: ru
epistemic: fact (для проверенных чисел), inference (для обобщений организации)
world: biology
subworld: drosophila
supersedes: [нет (первая карточка темы 1.1; предыдущий черновик evidence-1-1-genome.md — заменён этим каноном)]
---
# Drosophila melanogaster — Геном: структура, размер, гены, транспозоны, сборки (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: Adams MD et al. — «The genome sequence of Drosophila melanogaster», Science 2000 (PMID 10731132) — первый полный геном животного (после C. elegans); полный текст за пейволлом, использована аннотация (UniProt UP000000803, BDGP FAQ)
  - database: FlyBase Release 6 (dm6, с 2014) — flybase.org — референсная сборка/аннотация
  - database: UniProt UP000000803 (proteome D. melanogaster) — «180 Mb, approximately 14,000 protein-coding genes» — проверено ранее (раунд 14)
  - paper: «Multi-Scale Organization of the Drosophila melanogaster Genome», Genes 2021 (PMID 34071789) — обзор, полный текст OA
  - paper: «Near complete assembly of Drosophila melanogaster Canton S strain genome», Nat Commun 2025 (PMID 41339366) — полный текст OA
  - paper: «One fly-one genome: chromosome-scale genome assembly of a single outbred Drosophila melanogaster», NAR 2020 (PMID 32491177) — полный текст OA
  - paper: «Transposable elements in Drosophila», Mobile DNA 2020 (PMID 32636946) — обзор ТЭ, полный текст OA
  - paper: «P Transposable Elements in Drosophila and other Eukaryotic Organisms», Microbiol Spectr 2015 (PMID 26104714) — обзор
  - paper: «piRNA Biogenesis in Drosophila melanogaster», Trends Genet 2017 (PMID 28964526) — обзор
  - paper: «Establishment of H3K9-methylated heterochromatin...», Nat Rev Mol Cell Biol 2022 (PMID 35562425) — обзор
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: карточка собрана в первичном проходе: скрининг PubMed (esearch→esummary) + ранее проверенные источники (UniProt/FlyBase/Adams); ПОЛНЫЕ ТЕКСТЫ OA-статей (Genes 2021, Mobile DNA 2020, Nat Commun 2025, NAR 2020) — прочитать при углублении темы (в этом проходе — аннотации+заголовки, честно отмечено в confidence).

## Metadata
- world: biology.drosophila
- layer: world
- tags: [genome, drosophila, dm6, transposable-elements, assembly, heterochromatin]
- status: draft (первичный проход)

## Epistemic Linkage
- evidence_type: paper + database
- confidence: high (ядро: 180 Mb/14k генов/dm6/4 хромосомы); medium (детали организации 3D/TAD — по обзорам, без полного текста в этом проходе)
- uncertainty:
  - полное число генов FlyBase (dm6) — не проверено напрямую (TODO: flybase.org)
  - доля генома из транспозонов — не зафиксирована числом (TODO: Mobile DNA 2020 полный текст)
  - полные тексты OA-статей не прочитаны в этом проходе (только аннотации/заголовки)
- falsification_trigger:
  - если новая сборка/аннотация FlyBase изменит 180 Mb/~14k генов — обновить (dm7/новые релизы)
  - если Canton S (2025) станет новым референсом вместо dm6 — обновить строку референса
- transfer_boundary:
  - не переносить в CASA как «доказательство архитектуры» — это база «что закодировано» (зона genetic ADR-0062/0059), сравнение только после полного синтеза; классика (Morgan/Нобель) — историческая, не инженерное доказательство

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — самодостаточный опорный слой: числа, сборки, организация — агент не обязан открывать первоисточник на каждый шаг.
- **Core Unit + Operationalization** — сжатый триггер и применение (для сверки с CASA-зоной genetic).
- **Источник** — для сверки формулировок, не обязательный шаг в operational-контуре.

## Core Unit
- context:
  - мир дрозофилы как reference implementation: слой 1 — «как из генома вырастает НС»; CASA-зона genetic требует «что закодировано на T=0».
- signal:
  - вопрос про базу закодированного: размер генома, число генов, сборка, организация, мобильные элементы.
- action:
  - использовать: ~180 Mb (120 эухроматин + 60 гетерохроматин), ~14 000 белок-кодирующих генов, dm6, 4 пары хромосом (2n=8, XY), мультимасштабная организация (TAD/3D/инсуляторы), ТЭ (P-элементы, piRNA-сайленсинг, H3K9-гетерохроматин).
- outcome:
  - база для слоёв 1.2–1.5 (развитие, нейрогенез, метаморфоз, пол) и для зоны genetic; границы (число генов по определению, доля ТЭ) — зафиксированы.
- lesson:
  - геном — «программа», но с оговорками: 14k генов — белок-кодирующие; полная аннотация больше; референс dm6, но есть штаммовые сборки (Canton S 2025).

## Fundamentals (самодостаточный опорный слой)

### 1) Геном: размер и гены

- **~180 Mb** (120 Mb эухроматин + 60 Mb центрический гетерохроматин), **~14 000 белок-кодирующих генов** — UniProt UP000000803, BDGP FAQ, Adams et al. 2000 (PMID 10731132). Источник: база + Science 2000.
- **4 пары хромосом (2n=8)**: 2L/2R, 3L/3R, 4 (малая), X/Y — классика (Morgan/Bridges, 1910-е).
- **Референсная сборка: FlyBase Release 6 (dm6)** — с 2014; актуальная аннотация.
- Геном — первый секвенированный геном животного после C. elegans (Adams 2000).

### 2) Сборки (современные)

- **Canton S — «near complete»** (полные теломеры/центромеры), Nat Commun 2025 (PMID 41339366) — штамм-вариант, не референс.
- **One fly — one genome**: хромосомная сборка из одной особи (outbred), NAR 2020 (PMID 32491177).
- Низкозатратная long-read сборка референса — G3 2018 (PMID 30018084) — метод.

### 3) Организация генома

- Мультимасштабная: TAD/хроматиновые домены, 3D-организация, инсуляторы — Genes 2021 (PMID 34071789), Biochem Soc Trans 2025 (PMID 41151055), IJMS 2024.
- Эпигенетика — модельная система (Insects 2021, PMID 34680653).
- **Гетерохроматин**: H3K9-метилированный — роль в дифференцировке/поддержании тканей (Nat Rev Mol Cell Biol 2022, PMID 35562425).

### 4) Транспозоны

- **Обзор ТЭ дрозофилы**: семейства, динамика, регуляция — Mobile DNA 2020 (PMID 32636946) — ключевой обзор.
- **P-элементы**: механизмы, инструмент (трансгенез) — Microbiol Spectr 2015 (PMID 26104714); историческая P-инвазия — Genetics 2016 (PMID 27516614).
- **piRNA-биогенез** — защита генома от ТЭ (Trends Genet 2017, PMID 28964526).

### 5) Противоречия / нюансы

- Число генов: 14k = белок-кодирующие (консервативная оценка); полная аннотация FlyBase включает ncRNA/псевдогены — цифры различаются по определению «ген».
- Canton S (2025) — штамм-вариант; референс остаётся dm6.

### 6) Не найдено / TODO

- Полное число генов FlyBase (dm6 release notes) — проверить напрямую.
- Доля генома из ТЭ (%) — вытащить из Mobile DNA 2020 (полный текст).
- Полные тексты OA-статей (Genes 2021, Mobile DNA 2020, Nat Commun 2025, NAR 2020) — прочитать в углублении.

## Operationalization
- first_adoption_task: использовать числа (180 Mb/14k/dm6/4 пары) как базу слоя 1 и зоны genetic; при работе с CASA — сверять формулировки «innate catalog @ T=0» с этим ядром.
- validation_check: при изменении FlyBase-релизов (dm7 и т.п.) — перепроверить референс; при новом обзоре ТЭ — обновить долю.
- success_criterion: карточка покрывает 1.1 (структура/размер/гены/ТЭ/сборки) с источниками и границами; TODO явны.
- rollback_or_mitigation: при фальсификации (новые данные) — обновить Fundamentals, отметить в Lifecycle.

## Lifecycle
- deprecation_reason: —

