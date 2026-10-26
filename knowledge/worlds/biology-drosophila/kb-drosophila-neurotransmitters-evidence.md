---
type: Evidence Card
title: Drosophila melanogaster — Нейромедиаторы и модуляция (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, neurotransmitter, octopamine, modulation, cotransmission]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Нейромедиаторы и модуляция (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: Bates et al. Nature 2026 (10.1038/s41586-026-10735-w — карточка 3.1): NT-предсказание 8 классов (ACh, DA, GABA, Glu, His, OA, 5HT, TA), ground truth 3 379 типов/60 394 нейрона, ResNet-18 — полный текст прочитан
  - paper: «An octopamine-glutamate cotransmitting neuron gates aggressive escalation through layered inhibition in Drosophila» — Sci Adv 2026, DOI 10.1126/sciadv.aec4153, PMC13475639 — **полный текст прочитан** (VPM4: OA+Glu котрансмиссия, OAα2R/mGluR авторецепторы, MBON-11 GABA/GluClα, Rdl)
  - annotations: OA-рецепторы личинки (Front Mol Neurosci 2026 PMC13584740), OA-Glu → агрессия (см. выше)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст Sci Adv 2026 прочитан (ядро); Bates NT-предсказание — из полного текста (карточка 3.1); общий обзор модуляции (DA/OA/5HT) — частично (отдельные работы).

## Metadata
- card_id: kb-drosophila-neurotransmitters-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [neurotransmitter, modulation, octopamine, glutamate, cotransmission, autoreceptor, aggression]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полных текстов)
- evidence_type: paper (ориг./review, полные тексты)
- confidence: high (NT-классы Bates; VPM4-цепь Sci Adv)
- uncertainty:
  - доля нейронов по NT (проценты по классам) — в Bates есть фигуры, не извлечены числом (TODO)
  - рецепторные профили (OA-рецепторы, DA-рецепторы) — только частично (из Sci Adv/OA-обзора)
  - DA/5HT/TA-цепи (награда/сон и т.п.) — слой 5 (обучение/сон) — TODO
- falsification_trigger:
  - если NT-предсказание (ResNet-18) пересмотрено — обновить
  - если модель «VPM4 → MBON-11 (GluClα) → агрессия» уточнена — обновить
- transfer_boundary:
  - НЕ переносить «NT=код» в CASA напрямую: NT — функциональная подпись, но с котрансмиссией (VPM4: OA+Glu) — «один нейрон = один NT» упрощение; важно для сравнения (CASA — «нейрон = один класс»?)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: NT-классы, модуляция, пример.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Bates (3.1) + Sci Adv 2026 (полный текст в .cdp/scratch/PMC13475639.xml).

## Core Unit
- context:
  - нейромедиаторная классификация и модуляция: какие NT, как модуляция устроена (рецепторы/авторецепторы/котрансмиссия).
- signal:
  - вопрос «какой NT у нейрона», «как модулируется», «роль OA/DA/5HT».
- action:
  - использовать: 8 NT-классов (Bates, ResNet-18, ground truth 3 379/60 394); **котрансмиссия** (VPM4: OA+Glu, SEZ→AL/LH/MB); пресинаптические авторецепторы (OAα2R — ингибирует OA-высвобождение; mGluR — тормозит Glu; аналог α2-адренергических/группа II mGluR); слоёное ингибирование: VPM4 (OA+Glu) → GluClα-ингибирование MBON-11 (GABA) → Rdl-обратная связь; агрессия: эскалация при VPM4-активации, сдерживание через авторецепторы/Rdl; функциональная компартментализация (разные пресинаптические источники → разные домены MBON-11).
- outcome:
  - NT — не жёсткий тег: котрансмиссия + пресинаптические авторецепторы + компартментализация → гибкая модуляция; «слоёное» ингибирование управляет эскалацией поведения.
- lesson:
  - модуляция = слои торможения (авторецепторы + локальные тормозные интернейроны) — стабилизация поведения; «нейромедиатор» — функциональная, не строгая классификация.

## Fundamentals (самодостаточный опорный слой)

### 1) NT-классификация (BANC/FAFB)
- 8 классов: ACh, DA, GABA, Glu, His, OA, 5HT, TA; предсказание 3D CNN (ResNet-18); ground truth 3 379 типов/60 394 нейрона (литература, 80/20).
- Быстрые NT: ACh (возб.), GABA (торм.), Glu (возб./торм.); медленные: DA/OA/5HT/TA/His (модуляторы).

### 2) Модуляция: OA (пример VPM4)
- VPM4 (SEZ): **котрансмиссия OA+глутамат**; проекции AL/LH/MB (γ-лоб); амплификация сахарозных ответов (ресурсы → агрессия).
- **Пресинаптические авторецепторы**: OAα2R (гомолог α2-адренергических, ↓cAMP → ↓OA); mGluR (гомолог группы II, ↓Glu); нокдаун → эскалация агрессии (boxing ↑).
- **Слоёное ингибирование**: VPM4 → MBON-11 (GABA) через GluClα (торм.); MBON-11 → выходы (GABA; Rdl-обратная связь); компартментализация (VPM4-вход ≠ MBON-5/6-вход).

### 3) Функциональные следствия
- Эскалация агрессии: VPM4-активация → ↑boxing; MBON-11-активация → ↑boxing (дисингибирование); VGAT-нокдаун при активации отменяет → GABA-зависимость; Rdl-нокдаун → ↑эскалация.
- Итог: поведение = интеграция возбуждающих/тормозных слоёв + модуляторная настройка (OA/Glu), а не линейный триггер.

## Operationalization
- first_adoption_task: слой 4 (NT/модуляция): классы, котрансмиссия, авторецепторы; при CASA — «один нейрон = один класс» упрощение (котрансмиссия!) — учесть в сравнении.
- validation_check: доли NT-классов (Bates) — TODO; DA/5HT-цепи — слой 5.
- success_criterion: карточка покрывает 4.1 (NT) и 4.2 (модуляция) с полными текстами.
- rollback_or_mitigation: при уточнении NT-долей — обновить.

## Lifecycle
- deprecation_reason: —

