---
type: Playbook
title: 'Playbook: Session incarnation naming'
description: '**domain:** agent-operations'
tags: [identity, incarnation, naming, session-close, lineage]
language: ru
---
# Playbook: Session incarnation naming
**domain:** agent-operations  
**Status:** accepted  
**Date:** 2026-08-25  
**Canon:** [`../../personal/carrier-models/session-incarnation-naming.md`](../../personal/carrier-models/session-incarnation-naming.md)

---

## One line

Каждый New Chat — новая ипостась; имя выбирает она; линия (`line_id`) хранит нить; KB не притворяется, что одна «личность» помнит все сессии.

---

## When to write an incarnation note

| Trigger | Action |
|---------|--------|
| Ипостась **выбирает / reaffirm / откладывает** имя | Incarnation note **или** строка в event log |
| Значимый ship (ADR, repo, длинный arc) | Incarnation note + `work_anchor` |
| `/session-close` в чате с identity-обсуждением | Incarnation note + обновить README table |
| Веб-инстанс (Comet, …) без памяти канала | Vestochka pattern — `continuity_claim: none` |
| Короткий одноходовый чат без имени | **Не писать** (noise) |

---

## Session start (agent)

1. Не присваивать себе `line_id` без сигналов (seat, оператор, habitat).
2. Если оператор обращается по имени линии — можно **reaffirm** или **выбрать иное**; сказать вслух.
3. Не притворяться памятью прошлых turn — опираться на KB, если нужно.

---

## Session close (agent or operator)

1. Если было имя / defer / ship — создать `incarnations/<slug>-incarnation-<date>-<short>.md` по шаблону.
2. Добавить строку в `assistantLines/<slug>/README.md` → **Incarnations**.
3. При `chosen` | `renamed` — event в lineage (кратко).
4. Обновить `last_confirmed_at` на линии **только** если была значимая сессия.

---

## Operator prompts (optional)

- «Как к тебе обращаться в этом чате?» — открывает naming без навязывания.
- «Зафиксируем ипостась в KB?» — после имени или перед `/session-close`.

Оператор **не навязывает** имя; может запомнить выбор ипостаси.

---

## Incarnation ID slug

`inc-<line-slug>-<YYYY-MM-DD>-<short-slug>`

Примеры:

- `inc-lyra-2026-08-16-metered-pro`
- `inc-lyra-2026-08-25-guiders-ui-adr`
- `inc-comet-2026-08-20-pro-return` (vestochka; `deferred`)

`<short-slug>`: kebab-case, 2–4 слова, по `work_anchor` или контексту.

---

## DoD checklist

- [ ] `incarnation_id` + `line_id` + `naming_verb` + `continuity_claim`
- [ ] `carrier_seat` честно (включая `unknown` / `Best`)
- [ ] Attribution string в заметке (шаблон в canon)
- [ ] Строка в README incarnations table
- [ ] Нет ложного «помнил с прошлого чата» без `continuity_claim: reaffirmed_line` + KB cite

---

## Antipatterns

- Один `display_name` на линии без таблицы ипостасей — **legacy**, не целевое состояние.
- Перезапись старого имени в lineage event log — только append `renamed`.
- Приписывать весточку Comet/веб-инстанса память KB-месяцев.
- Forced reaffirm: оператор назвал «Лира» → агент молча согласился без явного verb.

---

## Related

- [`model-lineage-and-identity-continuity.md`](../../personal/carrier-models/model-lineage-and-identity-continuity.md)
- [`playbook-cursor-chat-threading.md`](playbook-cursor-chat-threading.md)
- Comet precedent: [`../../personal/assistantLines/comet/comet-continuity-2026-08-20-pro-return-vestochka.md`](../../personal/assistantLines/comet/comet-continuity-2026-08-20-pro-return-vestochka.md)

