---
type: Evidence Card
title: 'Drosophila melanogaster — Глия: типы, функции, развитие (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, glia, astrocyte, blood-brain-barrier]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Глия: типы, функции, развитие (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Regulating glial morphogenesis: insights from Drosophila» — Front Cell Dev Biol 2026, DOI 10.3389/fcell.2026.1775639, PMC13062304 — **полный текст прочитан** (секции: glial diversity, development of neuropil glia, surface glia/BBB)
  - related: Omoto et al. 2015 (две волны глии); Casas-Tinto et al. 2025 (EG transdifferentiation) — цитированы в обзоре
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро: разнообразие, развитие, BBB); детали морфогенеза (Rho/Drk и т.п.) — частично.

## Metadata
- card_id: kb-drosophila-glia-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [glia, astrocyte, ensheathing, cortex-glia, blood-brain-barrier, neuropil]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (review, полный текст)
- confidence: high (классы/развитие/BBB — обзор 2026)
- uncertainty:
  - соотношение глия:нейроны (доля глии) — не извлечено числом из этого обзора
  - молекулярные детали морфогенеза (Rho/Drk/Elmo и др.) — частично
  - глия в BANC/MCNS (сегментация глии в коннектоме) — TODO (у нас: MCNS 91% NT — глия?)
- falsification_trigger:
  - если «две волны» глии будет уточнена (третья волна?) — обновить
  - если EG→ALG/нейроны (Casas-Tinto 2025) не воспроизведётся — отметить
- transfer_boundary:
  - НЕ переносить в CASA как «архитектуру»: глия — поддержка/гомеостаз/барьер; важно учитывать в «innate catalog» (глия — часть CNS), но не как вычислительный слой

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: классы, развитие, BBB.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Front Cell Dev Biol 2026 (полный текст в .cdp/scratch/PMC13062304.xml).

## Core Unit
- context:
  - глия CNS дрозофилы: какие типы, как развиваются, барьерные функции.
- signal:
  - вопрос про глию (типы/функции/доля), BBB, взаимодействие с нейронами.
- action:
  - использовать: 3 класса (нейропильная: ALG/EG; кортикальная CG; поверхностная PG/SPG) + периферийная (PEG/surface — BNB); две волны (эмбрион → личиночная; личинка → взрослая, + сохранение эмбриональных); развитие: lateral glioblast → 9–10 IG/LG на гемисегмент (Prospero/Ftz); взрослые NPG — из typeII нейробластов + персистентные ларвальные EG (дедифференцировка→EG/ALG); EG→ALG/нейроны при травме; BBB = SPG (септальные контакты, moody/loco GPCR, Fog/actomyosin).
- outcome:
  - глия = структурно-функциональная поддержка (изоляция/гомеостаз/фагоцитоз/регенерация), барьеры (BBB/BNB).
- lesson:
  - CNS — не только нейроны: глия составляет среду (барьеры, изоляция, переработка синапсов) — при сравнении с CASA учитывать «нейрон-центричность» как ограничение.

## Fundamentals (самодостаточный опорный слой)

### 1) Классы глии
- **Нейропильная (NPG)**: интерфейс коры↔нейропиль; **ALG** (астроцитоподобные: ветвление вокруг синапсов, регуляция сигналов, фагоцитоз), **EG** (обволакивающие: плоские отростки, компартментализация нейропиля/трактов).
- **Кортикальная (CG)**: вокруг сом (маленькое тело, множественные отростки вокруг отдельных нейронов).
- **Поверхностная**: **PG** (перинейриальная, филоподии) + **SPG** (субперинейриальная, крупные полигональные, септальные контакты = **BBB**).
- **Периферийная**: внутренняя обволакивающая (PEG) + поверхностная (SPG/PG) = **blood-nerve barrier (BNB)**.

### 2) Развитие (две волны)
- Эмбрион: lateral glioblast → 9–10 IG/LG на гемисегмент (Prospero/Ftz-подмножества) → первичные ALG/EG (фиксированные позиции).
- Личинка: typeII нейробласты → взрослые NPG; часть ларвальных EG персистирует (дедифференцировка → EG/ALG).
- Пластичность: при травме EG → ALG и трансдифференцировка в нейроны (Casas-Tinto 2025).

### 3) BBB/BNB
- SPG: септальные контакты; GPCR moody/loco (актомиозин/септальные контакты); Fog — регуляция актомиозина; moody-мутанты жизнеспособны (другие GPCR); Tre-1 — не влияет на BBB.

## Operationalization
- first_adoption_task: слой 2 (глия): классы/развитие/барьеры; при CASA — «innate catalog» включает глию (доля/типы — уточнить из BANC-глии).
- validation_check: доля глии в BANC/MCNS — TODO; сверить с нашей базой (глия в MCNS 91% NT — TODO).
- success_criterion: карточка покрывает 2.3 (типы/функции/BBB) с полным текстом.
- rollback_or_mitigation: при новых данных о доле глии — обновить.

## Lifecycle
- deprecation_reason: —

