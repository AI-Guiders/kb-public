# Context pressure: сигналы и agent-initiated checkpoint (v1)

**Domain:** `agent-operations` (сквозной операционный контракт)  
**Версия:** 1 (draft / living)  
**Дата:** 2026-06-12  
**Provenance:** диалог оператор + agent (Cursor); hub agent-memory refactor 2026-06-12.

**Связь:** hub [`agent-memory-and-operating-principles-v1.md`](../../agent-memory-and-operating-principles-v1.md); сценарий export — [`playbook-session-summary-and-chat-export-v1.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export-v1.md).

---

## Одна строка

**Право агента подводить итоги работает только с детектором pressure + export-first checkpoint — не с «угадай, что тред длинный».**

---

## Проблема

В каноне уже есть **симметричное право** на итоги (§9, playbook session-summary): экспорт → резюме → согласование; не silent compaction хоста.

На практике в Cursor (и похожих IDE):

- хост **односторонне** сжимает контекст (`conversation was summarized`) без diff и без согласования;
- агент **не видит** meter заполнения контекста;
- эвристика «тред перегружен» **ненадёжна** — summary может случиться **до** предложения checkpoint агентом.

**Инвариант:** checkpoint = **named artifact + согласование**, не подмена истории пересказом платформы.

---

## Глоссарий: harness

**Harness** (обвязка, «упряжь») — среда, которая **крутит цикл** «модель ↔ tools ↔ сессия», но **не является** субстратом существования агента во времени.

| | Harness | Substrate (AOS / CASA life) |
|---|---------|------------------------------|
| **Примеры** | Pi, OpenHands, Cursor Agent loop, типичный MCP tool loop | CASA field + store, Forge IOP + provenance, P1 duck test |
| **Память** | контекстное окно, compaction по правилам хоста | field/store, WM, checkpoint с continuity |
| **Инициатива** | steer, follow-up, cron в gateway | bind partner turn, perceive → act с provenance |
| **Итог сессии** | часто silent summary | explicit checkpoint в artifact |

**Cursor сегодня** — в основном **harness**: удобный терминал + tools, но summarization без actor parity.

**CIDE / Forge / agent-notes** — шаги к **habitat**: export, issues, KB, oar: — вне контекста модели.

---

## Чего агент **не** имеет сегодня (runtime gap)

| Есть | Нет |
|------|-----|
| правило в KB «предложи итоги» | `context_used / budget` от хоста |
| functional drift (хуже recall начала треда) | visceral «пора сжать» (не применимо) |
| post-factum «был summary» | warning **до** compaction |
| jsonl на диске (ретроспектива) | continuity в **следующем** turn без artifact |

**Вывод:** инициатива §9 без **observable pressure signals** остаётся декоративной.

---

## Слои сигналов (от сильного к слабому)

### L0 — telemetry от хоста / harness (целевое)

Хост или harness отдаёт агенту (system, MCP, hook):

- `context_tokens_used`, `context_budget`, `pressure_ratio`
- `turns_since_last_checkpoint`
- `compaction_pending: false` (явный запрет silent cut без checkpoint)

**Действие при `pressure_ratio > threshold`:** агент **обязан предложить** цепочку §9 до того, как хост сожмёт.

*Cursor сегодня: L0 отсутствует.*

### L1 — структурные proxy (можно уже сейчас)

| Proxy | Порог (черновик) | Действие |
|-------|------------------|----------|
| user turns в сессии | ≥ 40–60 | предложить checkpoint |
| смена домена задачи | Forge → KB → философия | «зафиксируем open items?» |
| длинная tool-heavy цепочка | ≥ N tool calls подряд | export transcript |
| hook / rule reminder | каждые K turns | inject §9 в контекст |

Proxy **не ground truth** — но исполним без meter'а.

### L2 — functional probe (опционально)

Агент (или rule): «назови 3 решения из начала треда». Слабый recall → **флаг деградации** → предложить export, не «пересказ из головы».

### L3 — пользовательский триггер

«Подведи итоги», «что мы решили» — всегда в силе; не заменяет L0–L2.

---

## Цепочка checkpoint (канон, без изменений)

1. **Экспорт** — проверяемый файл (`Export-CursorJsonlTranscript.ps1`, CIDE `chat_export_readable`, Forge issue + anchors).
2. **Резюме** — решения, open items, next steps (кратко).
3. **Согласование** — пользователь правит; только потом считать checkpoint закрытым.
4. **Фиксация** (опционально) — KB / project card / issue по правилам канона.

**Anti-pattern:** platform summary без шагов 1–3.

---

## Связь с AOS habitat (Q2)

| Cage | Habitat |
|------|---------|
| silent summarization = tabula rasa | checkpoint переживает смену сессии |
| «помню» = пересказ хоста | «помню» = artifact + store |

Agent-initiated checkpoint при pressure — **минимальный duck test** для harness-сред (Cursor), пока нет P1 substrate.

---

## Backlog реализации

| # | Где | Что |
|---|-----|-----|
| 1 | Cursor hooks | **`.cursor/hooks/session_checkpoint_pressure.py`** — L1: ≥40 user turns → postToolUse inject §9; `preCompact` → user_message + inject queue. State: `.cursor/hooks/state/` (gitignored). |
| 2 | CIDE MCP | `session_turn_count`, `chat_export_readable` в hot path |
| 3 | agent-notes rule | явные пороги L1 в §9 или ссылка на этот doc |
| 4 | Forge | issue template «session checkpoint» с oar: actor |
| 5 | AOS P1+ | pressure → bind partner turn «пора зафиксировать» (не alert) |

---

## Чего не делать

- Не полагаться на «модель сама почувствует полный контекст».
- Не считать silent summary acceptable substitute для §9.
- Не путать **harness compaction** с **KB memory-compaction-loop** (другой контур: L0/L1/L2 репозитория).

---

## Канон

`knowledge/domains/agent-operations/playbook-context-pressure-checkpoint-v1.md`

