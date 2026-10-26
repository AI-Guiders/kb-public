---
type: Playbook
title: 'Playbook: rhetoric & pragmatics v1'
description: '**Домен:** rhetoric.pragmatics'
tags: [rhetoric-pragmatics, playbook, worlds, living]
world: rhetoric
subworld: pragmatics
---
# Playbook: rhetoric & pragmatics v1


**Домен:** rhetoric.pragmatics  
**Fundamentals:** [`kb-rhetoric-pragmatics-fundamentals.md`](kb-rhetoric-pragmatics-fundamentals.md)  
**Fundamental pass map:** [`map-rhetoric-pragmatics-fundamental-pass.md`](map-rhetoric-pragmatics-fundamental-pass.md)

## Когда загружать

- Запрос про **речевую ситуацию**, жанр, регистр, «как писать для X», уместность тона.
- Смешение disclaimer / спор / самоотчёт в одном тексте.
- Расширение XL или тегов `speech_situation` — нужен **theory spine**, не только operational map.

## Фундаментальный проход (канон)

**Не** перетегирование всех playbooks. **Чтение первоисточников → evidence-карточка → fundamentals synthesis.**

1. Открыть [`map-rhetoric-pragmatics-fundamental-pass.md`](map-rhetoric-pragmatics-fundamental-pass.md) — tier текущего прохода.
2. Читать **primary** (открытый текст или institutional PDF с пометкой в `extraction_note`).
3. Создать/обновить `kb-*-evidence-v1` по [`template-kb-evidence.md`](../../templates/cards/template-kb-evidence.md).
4. Обновить [`kb-rhetoric-pragmatics-scientific-evidence.md`](kb-rhetoric-pragmatics-scientific-evidence.md) и spine fundamentals.
5. Применить к operational: тег `speech_situation` на playbook / scenario XL — не дублировать теорию в playbook.

## Операционный чеклист (перед ответом человеку)

1. **Зафиксировать речевую ситуацию** (audience, goal, genre, channel, stakes, distance) — см. [`template-speech-situation-metadata.md`](../../templates/cards/template-speech-situation-metadata.md).
2. **Сверить с карточкой** — primary vs `when citing to human`; `forbidden_moves`.
3. **Не смешивать** FAQ-disclaimer, define-by-negation, debate rhetoric без запроса.
4. **Лексика** — без внутренних мемов (pressure, §-отсылки) для внешнего читателя.

## Антипаттерны

- Определять явление **от противного** («не X, не Y») когда достаточно прямого описания.
- Тянуть **клинический** или **legal** регистр в самоотчёт / TG.
- Путать **fundamental pass** с inventory тегов в `domains/`.

