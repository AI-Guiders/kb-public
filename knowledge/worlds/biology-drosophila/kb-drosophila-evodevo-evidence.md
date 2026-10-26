---
type: Evidence Card
title: 'Drosophila melanogaster — Эво-дево: консервативные каскады, гены поведения (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, evo-devo, hox, conservation, developmental-cascades]
language: ru
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Эво-дево: консервативные каскады, гены поведения (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - synthesis (все факты — из ПОЛНЫХ текстов, проверенных в этом проходе; источники указаны):
  - PLoS Genet 2021 (карточка 1.2, DOI 10.1371/journal.pgen.1009812) — Hox/gap-каскады, консервация
  - Nature 2026 (карточка 1.3, DOI 10.1038/s41586-026-10797-w) — 17 TF birth-order код «conserved in brain»
  - eLife 2021 (карточка 5.4, DOI 10.7554/eLife.66039) — FB/модули «highly conserved across insects»
  - Learn Mem 2024 (карточка 5.2, DOI 10.1101/lm.053839.123) — OA в MB у всех насекомых
  - Front Mol Neurosci 2023 (карточка 1.5, DOI 10.3389/fnmol.2023.1284367) — dsx/fru
  - G3 2025 (карточка 5.1, DOI 10.1093/g3journal/jkaf050) — песня/отбор
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: карточка — синтез фактов из уже прочитанных полных текстов (без новых скачиваний); все утверждения атрибутированы исходным статьям.

## Metadata
- card_id: kb-drosophila-evodevo-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [evo-devo, hox, conservation, developmental-cascade, evolution]
- status: draft

## Epistemic Linkage
- epistemic_basis: synthesis (из полных текстов)
- evidence_type: synthesis
- confidence: high (каждый факт — из полного текста указанной статьи)
- uncertainty:
  - «консервация» — по морфологии/функции, не по полному набору молекулярных деталей (границы)
  - эволюция НС других насекомых (пчела/муравей/кузнечик) — частично (5.4 цитирует; полных коннектомов нет)
- falsification_trigger:
  - если «консервация 17 TF кода» будет сужена (не все насекомые) — обновить
- transfer_boundary:
  - НЕ переносить как «закон эволюции НС»: это консервация конкретных каскадов/структур; для CASA — «инварианты развития» (Hox, birth-order, FB-модули) — материал для сравнения архитектур

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: консервация каскадов/структур.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — указанные карточки.

## Core Unit
- context:
  - эво-дево: что консервативно (каскады, структуры), что эволюционирует (песня, поведение).
- signal:
  - вопрос «насколько консервативна НС», «что меняется между видами».
- action:
  - использовать: **консервация**: Hox-каскады/сегментация (1.2), 17 TF birth-order (1.3 — VNC+brain), FB/кольцевой аттрактор (5.4 — «highly conserved across insects», у locusts/bees/cockroaches), OA в MB у всех насекомых (5.2), dsx/fru — половой диморфизм (1.5), CX-нейропили (5.4); **эволюция**: песня/половой отбор (5.1, 6.3), перестройки генома (6.1), поведенческая пластичность (условия).
- outcome:
  - «каркас» (развитие/каскады/CX) консервативен; «надстройка» (поведение/песня/морфология) — эволюционирует под отбором.
- lesson:
  - инварианты развития + эволюционируемое поведение = **«стабильная архитектура, пластичный репертуар»** — ключевая рамка для CASA (архитектура консервативна, поведение — вариативно).

## Fundamentals (самодостаточный опорный слой)

### 1) Консервативные каскады развития
- Hox/gap/сегментация (1.2): French Flag, stripe-энхансеры, Zelda/Opa — базовая программа у насекомых.
- Birth-order: 17 TF код (1.3) — консервирован в VNC и brain (внутри вида); гемилинейджи (Notch A/B) — принцип.

### 2) Консервативные структуры НС
- CX: EB/PB/FB/NO у всех насекомых (5.4: locusts, bees, cockroaches); ring attractor — общий принцип (пчела/кузнечик).
- MB: OA-иннервация у всех (5.2: fruit flies, blowflies, bees, locusts, crickets, cockroaches, hawkmoths) — консервативная функция.

### 3) Гены поведения и их эволюция
- dsx/fru — диморфизм (1.5); песня — генетическая архитектура + отбор (5.1: QST>FST, сильный QTL); slow/fast pulse — межвидовое? (Clemens 2018 — внутри вида).
- 17 TF-код — возможная межвидовая консервация (не проверено — TODO).

## Operationalization
- first_adoption_task: слой 6 (эво-дево): консервация/эволюция; при CASA — «стабильный каркас + пластичный репертуар».
- validation_check: межвидовая консервация 17 TF — TODO; полные коннектомы других видов — нет (3.4).
- success_criterion: карточка покрывает 6.4 (эво-дево) с атрибуцией к полным текстам.
- rollback_or_mitigation: при сужении консервации — обновить.

## Lifecycle
- deprecation_reason: —

