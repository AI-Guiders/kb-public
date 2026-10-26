---
type: KB
title: Rhetoric & pragmatics — fundamentals v1
description: Синтез spine (не замена evidence-карт). При споре — первоисточник в `kb-*-evidence-v1`.
tags: [rhetoric-pragmatics, kb, worlds, fundamentals]
world: rhetoric
subworld: pragmatics
---
# Rhetoric & pragmatics — fundamentals v1


Синтез spine (не замена evidence-карт). При споре — первоисточник в `kb-*-evidence-v1`.

## Provenance

- synthesis_from: Bitzer 1968, Bakhtin 1986, Grice 1975, Vatz 1973, SEP speech acts (cards in this world)
- operator_insight: speech_situation axes, wetware case report bleed (2026-08-22)
- updated_at: 2026-08-23

## 1. Рабочее ядро: речевая ситуация

**Речевая ситуация** — кортеж контекста, который задаёт **уместную** форму высказывания:

| Поле | Смысл |
|------|--------|
| **Exigence / цель** | Что должно измениться; зачем говорим (Bitzer: exigence как организующий принцип) |
| **Audience / аудитория** | Кто может отреагировать и принять изменение |
| **Constraints** | Уже в ситуации + внесённые говорящим (жанр, нормы, канал, время) |
| **Genre / жанр** | Relatively stable тип utterance (Бахтин: speech genre) |
| **Channel / канал** | TG, KB, cockpit, суд, копипаст-блок |
| **Stakes / ставки** | Цена ошибки тона или содержания |

**KB operational tuple** (теги на карточках) — практическая сжатая форма того же кортежа: `template-speech-situation-metadata.md`.

## 2. Два опорных первоисточника (pilot)

### Bitzer — rhetorical situation

Риторическое высказывание **отвечает на ситуацию**, которая **требует** риторического ответа. Три составляющие: **exigence**, **audience**, **constraints**. Ситуация **предписывает** тип, структуру и уместность ответа.

→ Детали: [`kb-bitzer-rhetorical-situation-1968-evidence.md`](kb-bitzer-rhetorical-situation-1968-evidence.md)

### Bakhtin — speech genres

Язык в живой речи организован в **речевые жанры** — относительно стабильные типы высказываний (от реплики до романа). Жанры **общая вербальная природа** utterance; риторические и бытовые жанры — не «особый случай литературы», а слой языка.

→ Детали: [`kb-bakhtin-speech-genres-1986-evidence.md`](kb-bakhtin-speech-genres-1986-evidence.md)

### Vatz (1973) — counterpoint Bitzer

Ритор **не только отвечает** на ситуацию — он **выбирает** salience, язык и «что считать ситуацией». Без явного \(P\) агент часто **создаёт** FAQ/defensive ситуацию (disclaimer, define-by-negation) вместо ситуации оператора.

→ Детали: [`kb-vatz-rhetorical-situation-1973-evidence.md`](kb-vatz-rhetorical-situation-1973-evidence.md)

### Grice (1975) — cooperative principle

Contribution должна соответствовать **accepted purpose** обмена (родственник `goal` + `genre` в speech_situation). Maxims Quantity/Manner/Manner: «добавить disclaimer на всякий случай» = не кооперативно к friend_tg self-report.

→ Детали: [`kb-grice-cooperative-principle-1975-evidence.md`](kb-grice-cooperative-principle-1975-evidence.md)

### Speech acts / illocution (SEP synthesis)

Жанр ≈ стабильный тип utterance (Бахтин); **illocutionary force** ≈ что делает высказывание (directive vs report vs express). Смешать playbook-directive с case_report — register bleed.

→ Детали: [`kb-pragmatics-speech-acts-sep-evidence.md`](kb-pragmatics-speech-acts-sep-evidence.md)

## 3. Смешение ситуаций (провал модели и агента)

Корпус и RLHF смешивают жанры с **разными constraints**:

| Жанр в корпусе | Типичные moves |
|----------------|----------------|
| FAQ / support | disclaimer, softening |
| Дебат / комменты | define-by-negation, «но это не значит» |
| Академия | hypothesis + limitation |
| Самоотчёт / дневник | прямое описание, мат, близкая дистанция |

Без явной ситуации модель **сэмплирует все moves** → каша. Операционное исправление: `speech_situation` в \(P\) и на KB-карточке, оси `situation_purity` в XL.

## 4. Operationalization

- Перед текстом для человека: заполнить speech_situation (шаблон).
- Playbook в `domains/` — **как действовать**; этот мир — **почему жанр важен**.
- Fundamental pass: [`map-rhetoric-pragmatics-fundamental-pass.md`](map-rhetoric-pragmatics-fundamental-pass.md)

## Falsification trigger

Если operational теги не улучшают register_fit в XL пилоте vs baseline — пересмотреть enum и связку с первоисточниками, не раздувать теги.

