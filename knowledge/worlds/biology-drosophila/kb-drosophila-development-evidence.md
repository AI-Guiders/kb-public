---
type: Evidence Card
title: 'Drosophila melanogaster — Развитие: сегментация, Gap/Hox, Pair-rule (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, development, segmentation, hox]
language: ru
epistemic: fact (для механизмов из обзора), inference (обобщения)
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Развитие: сегментация, Gap/Hox, Pair-rule (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Patterning with clocks and genetic cascades: Segmentation and regionalization of vertebrate versus insect body plans» — PLoS Genetics 2021, DOI 10.1371/journal.pgen.1009812, PMC8516289 — **полный текст прочитан** (Europe PMC fullTextXML, 383 KB; секции 10 «Regionalization in Drosophila: Gap and Hox gene regulation», 12 «Segmentation in Drosophila: Pair-rule and segment polarity gene regulation» — фундаментальный проход)
  - classic: Нобель 1995 (Lewis, Nüsslein-Volhard, Wieschaus — генетический контроль сегментации) — классический факт, проверен ранее (слой 1, раунд 14)
  - known: каскад материнские эффекты (bicoid, nanos) → гэп (hunchback, Krüppel, knirps) → pair-rule (even-skipped, fushi tarazu) → сегмент-полярность (engrailed, wingless, hedgehog) → Hox — канон из каркаса слоя 1 (подтверждается обзором 2021)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст обзора прочитан (ключевые секции по дрозофиле); классика (Нобель 1995/бикоид) — по канону каркаса, без отдельного полного текста (помечено в confidence); специализированные Hox-обзоры (полные тексты) — TODO.

## Metadata
- world: biology.drosophila
- layer: world
- tags: [development, segmentation, gap-genes, hox, pair-rule, french-flag, zelda]
- status: draft

## Epistemic Linkage
- evidence_type: paper (review, полный текст) + classic
- confidence: high (механизмы сегментации по обзору 2021: stripe-specific enhancers, Zelda/Opa, Hb-градиент); medium (классика/детали бикоид-nanos — по каркасу, без полного текста)
- uncertainty:
  - секции 7/9 обзора (long-germ morphogens, механизмы) — извлечены не полностью (парсинг заголовков с <italic>) — текст доступен в файле, TODO: дочитать
  - специфика регуляции bicoid/nanos (молекулярные детали) — не в этом обзоре; нужен отдельный источник
  - Hox-коллинеарность у дрозофилы (по Hox-обзору) — не закрыто отдельным полным текстом
- falsification_trigger:
  - если новые работы покажут, что сегментация дрозофилы не French Flag + stripe-specific enhancers, а существенно иная (например, динамическая/волновая) — обновить (обзор сам отмечает «much more dynamic», «temporal mode»)
  - если Zelda/Opa-модель ранней/поздней сети будет опровергнута — обновить
- transfer_boundary:
  - не переносить в CASA как «доказательство» — это биология развития (зона genetic — «innate catalog @ T=0»); механизмы сегментации — про развитие, не про архитектуру взрослой НС; сверка только после полного синтеза

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: каскад сегментации, механизмы, ключевые гены — достаточно для рассуждения без первоисточника.
- **Core Unit + Operationalization** — триггер и применение (для слоя 1 и зоны genetic).
- **Источник** — обзор 2021 (полный текст в .cdp/scratch), классика — по канону.

## Core Unit
- context:
  - слой 1: «как из генома вырастает НС» — сегментация и регионализация эмбриона; CASA-зона genetic: что закодировано на T=0.
- signal:
  - вопрос про раннее развитие: как из оплодотворённого яйца возникает сегментированное тело и нервная система.
- action:
  - использовать: каскад (материнские → гэп → pair-rule → сегмент-полярность → Hox); French Flag с Hb-мастер-градиентом; stripe-specific enhancers (Bcd/Cad, дозозависимость); Zelda (ранняя сеть) / Opa (поздняя) — pioneer-факторы; 7-stripe/zebra-элементы; frequency doubling; Hox — инициализация gap-генами, уточнение кросс-регуляциями и pair-rule.
- outcome:
  - механистическая картина сегментации (дискретная, французский флаг + специфические энхансеры, а не reaction-diffusion) — основа для понимания, откуда берётся «чертёж» тела.
- lesson:
  - сегментация дрозофилы — НЕ элегантный reaction-diffusion, а «неэлегантная» сборка из дискретных дозозависимых энхансеров + две волны (ранняя/поздняя) с pioneer-факторами — важная честность: биология использует много мелких правил, а не один красивый закон.

## Fundamentals (самодостаточный опорный слой)

### 1) Каскад сегментации (классика + обзор 2021)
- Порядок: материнские эффекты (bicoid, nanos) → гэп-гены (hunchback, Krüppel, knirps) → pair-rule (even-skipped, fushi tarazu) → сегмент-полярность (engrailed, wingless, hedgehog) → гомеотические Hox (Antennapedia/Bithorax комплексы).
- Нобель 1995 (Lewis, Nüsslein-Volhard, Wieschaus) — генетический контроль сегментации (классика).

### 2) Механизм: French Flag, не reaction-diffusion
- Морфогенные градиенты: Hb — мастер-градиент (модуляция материнского Hb смещает домены gap-генов — согласуется с French Flag).
- Gap-гены: инициализация градиентами + кросс-регуляции между собой (уточнение) + **динамика** («much more dynamic», временной режим — как у short-germ) — обзор 2021 подчёркивает динамичность.
- **Pair-rule — «неэлегантно»**: каждый стрип (или пара) — отдельный **stripe-specific enhancer**, дозозависимый от градиентов gap + материнских (Bcd, Cad), разных по позиции вдоль AP-оси. НЕ реакция-диффузия (искушение вычислителей опровергнуто экспериментально).

### 3) Две волны паттернинга
- Ранняя сеть: активация Zelda (pioneer-фактор); поздняя сеть: Opa; Dichaete — переход. В мутантах по этим факторам frequency doubling (удвоение частоты) pair-rule теряется.
- Поздние «7-stripe»/«zebra» энхансеры: драйвят полный паттерн (7 стрипов) в репортерных тестах — перепроводка сети.

### 4) Hox и регионализация
- К концу бластодермы gap-гены инициализируют Hox; Hox уточняются кросс-регуляциями между собой и модулируются периодической экспрессией pair-rule.
- Регионализация = градиенты → gap → Hox (сегменты/сегментные идентичности).

## Operationalization
- first_adoption_task: использовать в слое 1: каскад + механизм (French Flag/stripe-specific) как «как закодирован чертёж»; при работе с CASA — зона genetic: «innate catalog @ T=0» = геном кодирует программу развития (не взрослую схему).
- validation_check: при новых работах по динамике сегментации (временной режим) — обновить; проверить Hox-коллинеарность отдельно.
- success_criterion: карточка покрывает 1.2 (каскад, механизмы, две волны, Hox) с источником (полный текст обзора) и границами.
- rollback_or_mitigation: при фальсификации French Flag/stripe-specific — обновить Fundamentals, отметить в Lifecycle.

## Lifecycle
- deprecation_reason: —

