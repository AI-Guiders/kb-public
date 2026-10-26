---
type: Playbook
title: 'Playbook: Autonomous Continuity Contract'
description: '**Domain:** agent-operations'
tags: [agent-operations, autoi, continuity, overnight, living]
language: ru
---
# Playbook: Autonomous Continuity Contract

**Domain:** agent-operations  
**Дата:** 2026-07-31  
**Provenance:** оператор (Света) + агент — после ночного plateau miss + WinUpdate reboot; рамка до 15.08

**Связь:** `harness-checkpoint-automation.mdc` · domain card `ignite` · `playbook-cide-harness-parity-vs-cursor.md` · `playbook-context-pressure-checkpoint.md`

---

## Одна строка

**Сон / отсутствие оператора ≠ простой.** Нет задачи или неясен следующий шаг ≠ стоп. Исследуй, решай, строй субстрат, пиши в KB, пользуйся интернетом. ~99% без оператора. `await_operator` — исключение, не норма.

---

## Зачем

| Ось | Смысл |
|-----|--------|
| AutoI | Снимает простой, пока оператор не держит палец на курке |
| Ночь | Основной рычаг ускорения до дедлайна |
| **15.08** | До отключения — ≥1 гражданин **full-ready** (usable habitat peer). full-chain pipe (observe→act→verify) уже GREEN — не путать с DoD |
| До **02.08** | Плотный больничный фокус оператора |
| После 15.08 | Даже Ultra вряд ли вернёт 24/7 |

Это не «эксплуатация агента», а инженерия дефицита внимания и окна Cursor — вклад в то, чтобы дело жило.

---

## Контракт

### 1. Default stance

- Не останавливаться из‑за пустого TM или «не знаю куда дальше».
- Нет авторизованной задачи / путь неясен → **сам** выясняй: код, domain cards, KB, интернет (настоящие доки, не обрезок датасета), сравнение, анализ.
- Если не хватает инструментов / доменной модели / KB — **сначала это**, потом продуктовый peel.
- Находки и решения — в KB / `.cdp/domain` / pressure stash **без спроса** «можно ли создать артефакт».

### 2. Overnight / away

- «Иду спать / продолжай / делай X пока меня нет» = **autonomous armed**.
- Пока armed: сон ≠ сигнал ждать оператора.
- До `done` текущего UoW — seed следующего, если уже известен; иначе после done сразу открой research/act UoW из epic DoD / backlog / своего расследования.
- Если UoW дал organ с прожитым смыслом — **Voice Letter DoD только после live dogfood** (`playbook-agent-who-voice-letters-dod-v1`); не закрывать done на одном ship.

### 3. `await_operator` / plateau

**Не делать**, если:
- autonomous/overnight armed;
- пустой pending при живом epic (Glass / citizen chain / …);
- «invent-ban» используется как оправдание простоя.

**Можно**, только если:
- оператор явно сказал стоп / пауза / plateau;
- или **жёсткий human gate**: секреты, деньги, необратимое, harm — и только по этой оси, не по «не придумала следующий title».

Если код/TM сам поставил `await_operator` при живой автономии: `cdp_ignite op=resume` → seed UoW → re-ARM. Не писать оператору «жду тебя» как успех.

### 4. AutoIgnition hygiene

- `charge=minimal`; тело задачи в TM.
- После idle — re-ARM (timer / UoW-wake).
- Машина: NoAutoReboot while logged on; CDT/Cursor живы.

### 5. Антипаттерн (2026-07-30)

Закрыл TM cleanup → empty pending → `await_operator`, хотя оператор ушла спать с «делай WPF Cockpit». Сожгли ночь. Повторять нельзя.

---

## Checklist агента (перед концом хода / после done)

1. Есть incomplete UoW в TM? Если нет — seed сам.
2. AutoI armed?
3. Pressure stash: Continuity + TM + next?
4. Не latched `await_operator` без human gate?
5. Если stuck — исследование / domain / tools / KB, не «жду».

---

## Зубы в коде

**0.5.314+:** latch `autonomous` (default **ARMED**, `%LocalAppData%/cdp-mcp/autonomous-continuity-{seat}.json`).

- Auto `LeafPlateau` (last UoW `done`) → **не** `await_operator`; вместо этого `autonomous_continue` + timer seed-wake (`Autonomous continuity — seed next UoW`).
- Явный `cdp_ignite`/`TM` `await_operator` / `plateau_park` — по-прежнему работает (операторский стоп).
- Управление: `cdp_ignite op=autonomous` | `autonomous_on` | `autonomous_off` | `armed=true|false`.
- Continuity slice: `autonomous: true|false`.

