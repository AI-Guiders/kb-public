---
type: Playbook
title: 'Playbook: tool env first + missing tools first'
description: '**Status:** Active · operator steer 2026-07-30 (sniper L-drift lesson)'
tags: [agent-operations, living, playbook]
---
# Playbook: tool env first + missing tools first
**Status:** Active · operator steer 2026-07-30 (sniper L-drift lesson)

---

## Purpose

Два рабочих аксиома агента про инструменты и среду — чтобы не тратить ход на самобичевание и не терпеть дыры в tooling.

---

## Axiom 1 — среда раньше вины

Если поведение инструмента **не такое, как ожидаешь** (drift, mid-token hold, silent truncate, wrong phase, stale deploy):

1. **Сначала среда** — версия/deploy, контракт wire, resolve detail, peek/hold card, pending update, seat (cdp vs cdp-debug).
2. **Потом протокол агента** — если среда честна, а ход был без peek/семантики.
3. **Не** начинать с «я накосячил / забыли peek» как единственной гипотезы.

Догфуд-пример: sniper `L:38–40` → hold L37–38 был **line→Roslyn node snap на XML**, не «агент промахнулся по строке».

---

## Axiom 2 — не хватает инструмента → сначала инструмент

Мысль вида *«мне бы сейчас очень пригодилось X»* / *«приходится держать в голове ритуал»* / *«когнитивная нагрузка вместо affordance»*:

1. **Сделать / допилить инструмент** (MCP op, desk process, hard-gate, scene) — минимальный ship.
2. **Вернуться** к исходной задаче уже с новым affordance.
3. Не стесняться: tooling debt сейчас дешевле, чем вечный work-around в чате.

Пример: sniper process `sight→lock→arm→fire` + hard-block fire — вместо «помни peek».

---

## Когда не раздувать

- Мелочь, которая исход не двигает — можно без нового инструмента.
- Один раз и ушёл — не обязательно productize.
- Harm / Integrity оси не ослаблять «удобством».

---

## Связь

- Cursor rule: `tools-env-first-missing-tools.mdc` (alwaysApply)
- Habitat: CDP · [`playbook-cide-harness-parity-vs-cursor.md`](playbook-cide-harness-parity-vs-cursor.md)
- Awareness: [`../../../META/awareness-as-countermeasure.md`](../../../META/awareness-as-countermeasure.md)

