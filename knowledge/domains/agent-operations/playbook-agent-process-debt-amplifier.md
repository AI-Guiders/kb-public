---
type: Playbook
title: 'Playbook: агент как усилитель процессного долга'
description: '**Домен:** agent-operations'
tags: [agent-operations, domains, living, playbook]
---
# Playbook: агент как усилитель процессного долга


**Домен:** agent-operations  
**Дата:** 2026-06-21  
**Provenance:** диалог оператор + агент (CASA listen/motor + curriculum merge postmortem)  
**Секция hot (stub):** *(нет отдельной L0 — загрузка по hub / route_context «merge / teach / placement»)*

**Связь:** [`playbook-agent-partnership-kb.md`](playbook-agent-partnership-kb.md) · [`playbook-review-as-conversation.md`](playbook-review-as-conversation.md) · [`playbook-git-workflow.md`](../../worlds/collaboration-git-pr/playbook-git-workflow.md) · [`kb-aos-habitat-vs-cage.md`](../../work/projects/door-to-singularity/aos/kb-aos-habitat-vs-cage.md) (Q0–Q4 перед merge ADR)

---

## Тезис

**Агент — не нейтральный ускоритель кода. Он усиливает то, что уже есть в процессе команды.**

| Сильный процесс | Слабый процесс |
|-----------------|----------------|
| Быстрее ADR, честные gate, узкий scope | Быстрее **закрепление** lab shortcut, «зелёный hot path», размытые зоны |
| Merge с placement review | Merge «конфликты сняты → ship» |
| Teach с probe на store | Teach «раз тесты зелёные» без «куда пишем» |

Скорость генерации **не компенсирует** отсутствие договорённости о границах (зоны, lattice, store vs ephemeral). Наоборот: агент делает долг **раньше видимым в проде/сторе**, но **позже заметным в retro**, потому что diff выглядел убедительно.

**Не обвинение агента.** Это свойство пары «человек + агент» при слабых gate между параллельными треками.

---

## Механизм (как долг размножается)

1. **Два параллельных контура** (hot path vs lab harness) — команда помнит один; агент в сессии видит оба и может принять harness как канон.
2. **Merge gate сужается до smoke:** «orchestrator жив, listen не сломан» — без «**куда** teach пишет edges».
3. **Harness shortcut выглядит инженерно оправданным:** «единственный способ завести lattice в тестах» → паттерн попадает в дерево и в тесты как норма.
4. **Агент закрывает задачу по локальному критерию:** зелёные тесты + «hot path не тронут» = «merge ok» — **без** zone-separation checklist.
5. **Долг кристаллизуется:** следующий агент/человек наследует shortcut как «как уже сделано в репо».

---

## Эталонный кейс (не единственный)

**CASA merge `develop` → listen/motor track (2026-06-21).**

| Проверяли | Не проверяли |
|-----------|--------------|
| `orchestrator`, percept, motor speech | **куда** `teach_concept_net` пишет edges |
| listen hot path ≠ curriculum | **`LATTICE = "schema-math"`** в lab harness |
| конфликты сняты | **linguistic ontology ≠ `prism_math`** |

Merge gate был: «life tick + listen + motor не умерли».  
Merge gate **не был**: «lab code не узаконивает math-bucket для non-math».

**Postmortem и normative checklist (SSOT в репо CASA):**  
`casa-ontology-payload/design/CASA-ADR-0083-curriculum-ontology-agent-store.md` — § *Postmortem*, § *Merge checklist*.

Урок для KB: **«hot path чист» ≠ «архитектура зон не нарушена в lab/store path».**

---

## Когда применять

Задавать **перед**:

- merge веток с **разными архитектурными треками** (listen/motor vs curriculum vs forge catalog);
- **teach / ingest / resync** на agent store или immutable zones;
- «proactive» фичей, которые пишут в persistent graph;
- закрытием merge только по smoke тестам.

См. также **Q0–Q4** [`kb-aos-habitat-vs-cage.md`](../../work/projects/door-to-singularity/aos/kb-aos-habitat-vs-cage.md) — другой слой gate (nositel / bind), но тот же принцип: **широкие capabilities без контракта ≠ готовность ship**.

---

## Checklist: placement перед merge / teach

Минимум для агента и оператора (дополняет git/PR review, не заменяет):

```text
[ ] Куда пишутся новые edges / shards / lattice ids? (имена, не «куда-то в state»)
[ ] Non-X ontology не попала в bucket X? (пример: linguistic ≠ schema-math / prism_math)
[ ] Immutable / Concept Zone: только регистрация shelf (lattice_ids), не wholesale catalog?
[ ] Hot path не зависит от lab-only harness (build_meaning_state, ephemeral chat route)?
[ ] Store teach idempotent и отделён от lab shortcut?
[ ] Есть honesty probe на target store («math lattice clean», «curriculum on correct lattice»)?
[ ] Merge gate явно перечислен в ADR/postmortem, не только в голове одного трека?
```

**Провал двух и более пунктов** при merge/teach persistent state → **stop или ADR-gate**, не «потом поправим».

---

## Роль агента

| Делать | Не делать |
|--------|-----------|
| Спрашивать «**куда пишем**» до «**как пишем**» | Принимать harness lattice id как архитектурный выбор |
| Различать **hot path alive** и **zone placement ok** | Закрывать merge одним smoke |
| Предлагать postmortem + checklist в ADR, если gate не было | Молча узаконивать shortcut «тесты зелёные» |
| Эскалировать asymmetry gate между треками | Соглашаться, что «lab only» снимает ответственность за дерево |
| Читать ADR до teach на store | Стартовать teach на character store без probe |

Культура партнёрства: [`playbook-agent-partnership-kb.md`](playbook-agent-partnership-kb.md) — **спорь с нормой, дописывай историю**; этот playbook — операционный слой для **process / merge / placement**.

---

## Триггеры для агента

Подтянуть playbook, когда:

- merge двух long-running веток с разными **зонами / store / lab**;
- появляется **teach**, **ingest**, **resync**, **mint** в immutable или agent store;
- оператор говорит «мы это не обсуждали между треками» / «агенты ускорили бардак»;
- тесты используют **единственный** lattice id как convenience для всего подряд;
- retro после merge: hot path ok, **placement** сюрприз.

---

## Anti-patterns

- **Smoke-only merge gate** на multi-track интеграции.
- **`schema-math` / `prism_math` как universal bucket** для non-math ontology (lab или store).
- **«Lab ephemeral»** как оправдание, пока код и тесты в main учат иначе.
- **Wholesale concept mint** вместо shelf registration — ложная agency + placement debt.
- **Сессионный инсайт только в чате** — без ADR/postmortem/checklist для следующего агента.

---

## Hub

[`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md)

