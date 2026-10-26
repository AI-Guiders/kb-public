---
type: Evidence Card
title: Drosophila melanogaster — Коннектомы других насекомых (evidence card v1, annotations)
tags: [biology-drosophila, worlds, kb, evidence, insect-connectomes, comparative, annotation]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Коннектомы других насекомых (evidence card v1, annotations)

## Provenance (происхождение)
- source_refs:
  - annotation-only: полные коннектомы мозга других насекомых НЕ существуют (на 2026); частичные/неполные: пчела (первичные/проекционные нейроны, не полный мозг), кузнечик/саранча (CX-части, 5.4), таракан (CX, Bender 2010 — цит. в 5.4), комар/дрозофила-родственники (частичные)
  - eLife 2021 (5.4): CX-нейропили консервативны (locusts, bees, cockroaches) — полный текст
  - eLife 2021 (5.4): FB «highly conserved across insects» (Strausfeld 2012) — цит.
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: ЧЕСТНАЯ граница: в этом проходе полные тексты коннектомов других насекомых не читались (их нет как полных EM-коннектомов); карточка — аннотационная.

## Metadata
- card_id: kb-drosophila-insect-connectomes-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [insect-connectomes, comparative, annotation, cx-conservation]
- status: draft

## Epistemic Linkage
- epistemic_basis: annotation (отсутствие полных коннектомов)
- evidence_type: annotation
- confidence: medium (отсутствие — известно, но «нет» сложно доказать; регулярно появляются частичные)
- uncertainty:
  - полные коннектомы других насекомых могут появиться (следить; e.g. Apis mellifera — ongoing; Locusta — CX)
  - «консервация CX» — морфологическая/функциональная, не EM-уровень
- falsification_trigger:
  - если появится полный коннектом пчелы/муравья — обновить (и пересмотреть сравнение)
- transfer_boundary:
  - НЕ использовать «муха — единственный вид с коннектомом» как доказательство: «на 2026 — единственный ПОЛНЫЙ»; сравнение с другими видами — на уровне CX/морфологии

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: статус коннектомов.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — аннотации + eLife 2021 (5.4).

## Core Unit
- context:
  - есть ли полные коннектомы других насекомых (пчела/муравей/кузнечик).
- signal:
  - вопрос «только ли у дрозофилы есть коннектом», «насколько репрезентативна муха».
- action:
  - использовать: D. melanogaster — единственный ПОЛНЫЙ коннектом CNS (мозг+шнур: FAFB/BANC/MCNS); другие — частичные (пчела: первичные/проекционные нейроны MB; кузнечик: CX/LO; таракан: CX); CX-структуры консервативны (5.4); BANC+FAFB+MANC — 3 независимых реконструкции (D. melanogaster).
- outcome:
  - сравнение «насекомое vs насекомое» возможно только на уровне CX/отдельных систем; полный EM-уровень — только D. melanogaster.
- lesson:
  - «reference implementation» дрозофилы — уникален по полноте; для CASA — сравнивать с ограничением (нет второго полного экземпляра).

## Fundamentals (самодостаточный опорный слой)

### 1) Статус
- Полные: D. melanogaster (FAFB — мозг; MANC — самец, шнур; BANC — самка, мозг+шнур; MCNS — самец, шнур).
- Частичные (не полные): пчела (первичные/проекционные нейроны, MB-части), кузнечик (CX/compass-части), таракан (CX), комары/муравьи (частичные/в процессе).

### 2) Консервация CX
- EB/PB/FB/NO — у всех насекомых (5.4: locusts, bees, cockroaches); FB — «highly conserved» (Strausfeld 2012, цит. в 5.4).
- Кольцевой аттрактор — предложен у пчелы/кузнечика (5.4 цит.).

## Operationalization
- first_adoption_task: слой 3 (сравнение видов): ограничение «только D. melanogaster полный».
- validation_check: следить за Apis/Locusta EM — TODO (обновлять).
- success_criterion: карточка честно фиксирует границы сравнения (3.4).
- rollback_or_mitigation: при появлении полного коннектома другого вида — пересмотреть.

## Lifecycle
- deprecation_reason: —

