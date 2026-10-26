---
type: Evidence Card
title: 'Drosophila melanogaster — Питание: голод, насыщение, цепи (evidence card v1)'
tags: [biology-drosophila, worlds, kb, evidence, feeding, hunger, satiety, neuropeptide, motivation]
language: ru
epistemic: fact (из полного текста)
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Питание: голод, насыщение, цепи (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Neural basis of hunger-driven behaviour in Drosophila» — Open Biology 2019, DOI 10.1098/rsob.180259, PMC6451361 — **полный текст прочитан** (секции: neural coding of hunger/satiety, modulation of feeding circuits, olfactory circuits, locomotion, microstructure)
  - related: Sci Adv 2026 (VPM4 — карточка 4.2), eLife 2023 (Behavioral dissection of hunger states) — аннотации
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро); молекулярные детали (DILP-типы) — частично.

## Metadata
- world: biology.drosophila
- layer: world
- tags: [feeding, hunger, satiety, dilp, akh, npf, snpf, motivation, mb]
- status: draft

## Epistemic Linkage
- evidence_type: paper (review, полный текст)
- confidence: high (сигналы/цепи из Open Biol 2019)
- uncertainty:
  - некоторые связи «непрямые» (авторы: dashed lines — механизм не полностью ясен)
  - DA-WED структурная пластичность (ветвление при аминокислотном голоде) — описана, механизм не раскрыт
  - микроструктура кормления — отдельные исследования
- falsification_trigger:
  - если «голод → периферийная сенситизация» будет пересмотрена (новые данные) — обновить
  - если MB-интеграция голода/сытости опровергнута — сузить
- transfer_boundary:
  - НЕ переносить в CASA как «модуль голода»: но **конкуренция мотиваций** (DA-WED: белок vs сахар; MB: learned vs innate; sleep vs foraging) — сильный материал для CASA (приоритеты/арбитраж) после синтеза

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: сигналы, периферийная/центральная модуляция, мотивации.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — Open Biol 2019 (полный текст в .cdp/scratch/PMC6451361.xml).

## Core Unit
- context:
  - питание: как голод/сытость кодируются и модулируют сенсорику/поведение; арбитраж мотиваций.
- signal:
  - вопрос «как муха решает есть/не есть», «что такое голод на уровне цепей», «конкуренция мотиваций».
- action:
  - использовать: **сигналы**: DILPs (8, инсулин-аналоги; IPC; satiety; ↓при голоде), Upd2 (лептин-аналог; жировое тело→JAK/STAT→GABA→IPC), AKH (глюкагон-аналог; голод), NPF (голод; ↑при голоде), sNPF, DH44 (аминокислоты/питательный сахар), 5HT; **периферийная модуляция**: Gr5a ↑ (DopEcR/TH-VUM DA), Gr66a ↓ (sNPF→GABA→OA-VL), Ir76b ↑ (аминокислоты), Or85a ↓ (DTKR/TK), ACV-ORNs ↑ (sNPFR, InR-регуляция); **центральные**: Fdg (command — полная программа), IN1, ISNs (AKHR; кодируют голод), DA-WED (белковый голод: FB-LAL ↑белок, PLP ↓сахар — **конкуренция**; DopR2/DopR1), MP1 (DA-MB; NPF→↓MP1 → разблокировка learned food-seeking), 5 MBON-путей (innate food seeking), MB — интегратор голода/сытости; **локомоция**: AKH→AKHR (2–4 SEZ; гиперактивность), OA-VUM1/2 (темп: Octβ3R/OAMB); **микроструктура**: sips 0.16 s, ISI 0.08 s, bursts; 4h — IBI↓, 8h — sips/burst↑; насыщение: 10 мин — IBI↑/bout↓.
- outcome:
  - голод/сытость — глобальные нейропептидные состояния, модулирующие периферию (сенсоры) и центральные цепи (команды/MB) → перенастройка поведения; **арбитраж мотиваций** (белок vs сахар, сон vs поиск пищи).
- lesson:
  - «мотивация» у мухи = **пептидные сигналы + модуляция сенсорики + MB-интеграция**; конкуренция мотиваций — явная (DA-WED, sleep/foraging) — для CASA: арбитраж потребностей — реальный механизм, не абстракция.

## Fundamentals (самодостаточный опорный слой)

### 1) Сигналы голода/сытости
- DILP2/3/5 (IPC) — satiety; при голоде накапливаются в IPC, ↓в гемолимфе; Upd2 (жировое тело) — лептин-аналог (JAK/STAT→GABA→IPC); AKH — голод; NPF — голод (аппетит); sNPF — локальный; DH44 — пост-ингстивный (аминокислоты/сахар); 5HT — в MB (MP1).
- Модуляторный, дальнего действия (пептиды).

### 2) Периферийная модуляция
- Сахар (Gr5a): ↑ при голоде; DopEcR + TH-VUM (DA) — вероятный источник; NPF — инициатор (непрямо).
- Горькое (Gr66a): ↓ при голоде; sNPF (LNC)→GABA; AKH — upstream/параллельно; OA-VL (TA+OA) — потенцирует в накормленных.
- Дрожжи (Ir76b): ↑ при аминокислотном голоде (специфично: Gr5a не меняется).
- Обоняние: ACV-ORNs ↑ (sNPFR; InR↓ → sNPFR↑); Or85a (высокий ACV) ↓ (DTKR ← TK от LNs).

### 3) Центральные цепи
- Fdg (2 нейрона) — command: полная программа (PER→pumping→retraction); активация сахаром только при голоде; IN1 (12 cholinergic) — активация при сахарозе; ISNs (4, AKHR) — кодируют голод (активация → потребление у сытых).
- DA-WED (2/полушарие): аминокислотный голод → активность ↑ + удлинение медиальных ветвей (структурная пластичность!) → FB-LAL (белок, DopR2) / PLP (сахар, DopR1) — **конкуренция**.
- MB: MP1 (DA) — NPF-ингибирование (голод) → разблокировка learned food-seeking; 5 MBON-путей (MP1-MVP2-M4/6, α3, β2β'2a, α'2, γ2α'1) — innate food seeking; DAN-регуляция сигналами голода/сытости — MB = интегратор.

### 4) Локомоция и микроструктура
- AKH→AKHR (2–4 SEZ, OA) — гиперактивность при голоде; InR — подавление DILPs.
- Личинки: NPF (толерантность), OA-VUM1/2 (темп: OAMB/Octβ3R — контраст).
- Микроструктура: 0.16 s sip, 0.08 s ISI; 4h — IBI↓; 8h — sips/burst↑; насыщение (10 мин) — IBI↑, bout↓.

## Operationalization
- first_adoption_task: слой 5 (питание): сигналы/цепи/арбитраж; при CASA — «мотивационные модули с арбитражем» (материал для сравнения после синтеза).
- validation_check: MBON-пути (5) — сверить с BANC (MBON-типы) — TODO; DA-WED пластичность — TODO.
- success_criterion: карточка покрывает 5.7 (питание) с полным текстом.
- rollback_or_mitigation: при пересмотре «MB=интегратор» — обновить.

## Lifecycle
- deprecation_reason: —

