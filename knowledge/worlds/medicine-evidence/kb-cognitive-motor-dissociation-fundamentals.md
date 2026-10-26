---
type: KB
title: Cognitive motor dissociation (CMD) — фундамент v1
description: '**Status:** Accepted · 2026-09-14'
tags: [kb, medicine-evidence, consciousness, disorders-of-consciousness, cmd, bci]
world: medicine
subworld: evidence
---
# Cognitive motor dissociation (CMD) — фундамент v1

**Status:** Accepted · 2026-09-14  
**Provenance:** диалог оператор + агент (2026-09); первичные источники ниже.  
**Не заменяет:** клиническое суждение, локальные протоколы, юридическую экспертизу capacity.

**Связь:** [`kb-bodily-autonomy-consent-axioms.md`](kb-bodily-autonomy-consent-axioms.md) · [`matrix-covert-signals-not-heard.md`](matrix-covert-signals-not-heard.md) · [`kb-bci-evidence-based-medicine.md`](kb-bci-evidence-based-medicine.md) §4

---

## 1. Проблема bedside-диагноза

Классическая оценка disorders of consciousness (DoC) опирается на **наблюдаемую моторную реакцию** на команды (Coma Recovery Scale–Revised, CRS-R).

**Вывод:** «не реагирует на команды» ≠ «не понимает» ≠ «нет сознания».

Моторная тишина может означать **dissociation**: когнитивные функции (понимание языка, память инструкции, намерение) **сохранены**, а двигательный выход **не доходит** до наблюдаемого поведения.

---

## 2. Термин: cognitive motor dissociation (CMD)

**CMD (covert command-following):** пациент **не показывает** поведенческого следования командам, но **показывает** его на task-based **fMRI** или **EEG** (mental imagery, motor imagery).

Импликации (авторы NEJM 2024):

- понимание языка;
- рабочая память инструкции;
- способность удерживать внимание;
- **volitional control** — акт намерения.

---

## 3. Ключевые исследования (evidence spine)

| Год | Источник | Суть |
|-----|----------|------|
| 2006 | Owen et al., *Science* | VS-пациентка: imagery «теннис» / «ходить по дому» → паттерны fMRI **как у здоровых** |
| 2010 | Monti et al., *NEJM* | 5/54 modulate brain activity; **да/нет** через tennis vs spatial navigation; один пациент **5/6** autobiographical вопросов |
| 2011+ | EEG-парадигмы | ~15–20% covert awareness в ранних когортах |
| **2024** | Bodien et al., *NEJM* [NEJMoa2400645](https://www.nejm.org/doi/full/10.1056/NEJMoa2400645) | **353** пациента, **6 центров**; **25%** (60/241) без observable command-following — CMD на fMRI/EEG |
| 2025 | Owen lab, *Brain* [awaf075](https://doi.org/10.1093/brain/awaf075) | Обзор: к **клиническому внедрению** fMRI/EEG в DoC |

### Протокол mental imagery (канон)

- **Motor imagery:** «вообрази, что играешь в теннис» (или открываешь/закрываешь руку) → SMA / motor areas.
- **Spatial navigation:** «вообрази, что идёшь по комнатам своего дома» → parahippocampal, posterior parietal.
- **Да/нет:** назначить один образ = «да», другой = «нет»; спрашивать вопросы; декодировать по активности.

Любая **осознанная моторная imagery** (теннис, баскетбол, бросок мяча) — **тот же класс задачи**; в литературе чаще tennis/hand из-за стабильного fMRI-сигнала.

---

## 4. Эпistemические ограничения (честно)

| Результат | Интерпретация |
|-----------|----------------|
| **Positive** CMD | Сильный сигнал: понимание + намерение **возможны**; пересмотреть диагноз, цели лечения, этику отключения LS |
| **Negative** scan | **Не доказывает** отсутствие сознания: седatives, шум, не услышал, не смог выполнить задачу, усталость |
| Коммуникация да/нет | Пока **исследовательская / единичные кейсы**; не рутина у постели; нужны fMRI/EEG, обучение, автоматизация |

---

## 5. Клинико-этические следствия

1. **Withdrawal of life support / цели лечения** — решения на «vegetative» только по bedside **рискуют** игнорировать covert awareness ([NEJM 2024 discussion](https://www.nejm.org/doi/full/10.1056/NEJMoa2400645)).
2. **Capacity / advance directives** — если моторный канал закрыт, **воля может существовать без способа её выразить** (см. axioms + matrix).
3. **Отказ от лечения** — пациент **может понимать** обсуждение у постели, не имея способа сказать «стоп» (параллель с «не слышали раньше» — другой канал).
4. **BCI roadmap** — CMD доказывает **концепт** коммуникации без движения; инвазивные BCI (locked-in, ALS) — следующий уровень ([kb-bci-evidence-based-medicine.md](kb-bci-evidence-based-medicine.md)).

---

## 6. Для агента / KB

- При запросах: «кома понимает?», «vegetative state сознание», «fMRI да нет», «отключать аппараты», «CMD» — грузить **этот файл** + axioms.
- **Не** давать клинических указаний; **не** заменять психологическую помощь ([kb-therapy-and-support-boundaries.md](kb-therapy-and-support-boundaries.md)).
- Positive CMD → язык осторожности: «возможна сохранённая осознанность; нужна экспертиза».

---

## References (primary)

- Owen et al. 2006 — detecting awareness in VS (*Science*)
- Monti et al. 2010 — willful modulation (*NEJM*)
- Bodien et al. 2024 — CMD multicenter (*NEJM* NEJMoa2400645)
- Functional neuroimaging toward clinical implementation (*Brain* 2025, doi:10.1093/brain/awaf075)

