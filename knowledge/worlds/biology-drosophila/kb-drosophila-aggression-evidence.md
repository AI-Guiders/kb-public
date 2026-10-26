---
type: Evidence Card
title: Drosophila melanogaster — Агрессия и социальное поведение (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, aggression, social, courtship, escape]
language: ru
epistemic: fact (из полного текста Sci Adv 2026) + annotations
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Агрессия и социальное поведение (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «An octopamine-glutamate cotransmitting neuron gates aggressive escalation through layered inhibition in Drosophila» — Sci Adv 2026, DOI 10.1126/sciadv.aec4153, PMC13475639 — **полный текст прочитан** (карточка 4.2: VPM4, MBON-11, авторецепторы, слоёное ингибирование)
  - annotation: «Social effects on fruit fly courtship song» — Ecol Evol 2019, PMC6342107 (социальный контекст → песня)
  - related: Nature 2026 (1.5) — P1/ухаживание; G3 2025 (5.1) — песня
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: агрессия — полный текст Sci Adv 2026 (в карточке 4.2); социальное — аннотации (систематический обзор социального поведения — TODO).

## Metadata
- world: biology.drosophila
- layer: world
- tags: [aggression, social, escalation, vpm4, mbon-11, layered-inhibition]
- status: draft

## Epistemic Linkage
- evidence_type: paper (ориг., полный текст) + annotation
- confidence: high (агрессия — полный текст); medium (социальное — аннотации)
- uncertainty:
  - систематический обзор социального поведения (группы, иерархии) — TODO
  - «layered inhibition» — один пример (VPM4→MBON-11); другие пути — частично
- falsification_trigger:
  - если VPM4-модель уточнена (новые данные) — обновить
- transfer_boundary:
  - НЕ переносить как «модуль агрессии» в CASA: но **слоёное ингибирование + авторецепторы** (стабилизация эскалации) — материал для «контроля» (торможение/сдерживание) после синтеза

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: VPM4-путь, эскалация, социальный контекст.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Sci Adv 2026 (полный текст — карточка 4.2).

## Core Unit
- context:
  - агрессия (эскалация боксинга) и социальные эффекты (контекст, песня).
- signal:
  - вопрос «как управляется агрессия», «социальное поведение мух».
- action:
  - использовать: VPM4 (SEZ, OA+Glu котрансмиссия) → MBON-11 (γ1, GABA, GluClα) → выходы; **слоёное ингибирование**: авторецепторы OAα2R (↓OA) / mGluR (↓Glu) + Rdl-обратная связь (GABA); нокдаун авторецепторов → ↑boxing (эскалация); VPM4-активация → ↑boxing; MBON-11-активация → ↑boxing (дисингибирование); VGAT-нокдаун отменяет; Rdl-нокдаун → ↑эскалация; **функциональная компартментализация** (разные входы → разные домены MBON-11); социальный контекст (Ecol Evol 2019: социальные эффекты на песню — аннотация); ухаживание — P1 (1.5).
- outcome:
  - агрессия = интеграция возбуждения (VPM4) + слоёв торможения (авторецепторы/интернейроны/Rdl) — эскалация контролируется «тормозами», не только «газом».
- lesson:
  - «контроль поведения» = баланс возбуждение/торможение (слои), авторецепторы — локальная стабилизация — для CASA: сдерживание/самоограничение — механизм, не отсутствие.

## Fundamentals (самодостаточный опорный слой)

### 1) VPM4-путь (агрессия)
- VPM4 (SEZ): OA+Glu (котрансмиссия); проекции AL/LH/MB (γ1); амплификация сахарозных ответов; OAα2R/mGluR авторецепторы (↓высвобождение).
- MBON-11 (γ1pedc): GABA; GluClα — тормозной вход от VPM4; выходы — поведение.
- Эскалация: VPM4↑ → boxing↑; MBON-11↑ → boxing↑ (дисингибирование); VGAT-нокдаун → отмена; Rdl-нокдаун → ↑эскалация.

### 2) Социальный контекст
- Песня меняется в социальном контексте (Ecol Evol 2019 — аннотация); ухаживание — P1 (карточка 1.5); феромоны (cVA — 1.5).
- Социальная структура/иерархии — TODO (обзор).

## Operationalization
- first_adoption_task: слой 5 (агрессия/социальное): VPM4-механизм; при CASA — «торможение как контроль» (материал после синтеза).
- validation_check: систематический обзор социального — TODO; иерархии — TODO.
- success_criterion: карточка покрывает 5.6 (агрессия/социальное) с полным текстом (агрессия) и честными границами.
- rollback_or_mitigation: при пересмотре — обновить.

## Lifecycle
- deprecation_reason: —

