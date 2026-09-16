**Tags:** #agent-operations #domains #living #playbook

﻿# Playbook — next-task handoff (substance, not just id)

**Status:** Active (automated in TaskKnowledge Core/MCP **0.3.1**)  
**Date:** 2026-07-18  
**Контур:** agent-operations · TaskKnowledge / AFPM trajectory  
**Связь:** ADR 0001 D6 (`process_get`); `route_next`; epic `ecosystem-one-click` / task `eco-next-handoff-substance`

## Проблема

Агент: «A done → готов к B». Называет `task_id` / короткое title. Оператор **не видит**, что такое B (to_be, criterion), пока сам не `read_card`.

## Решение (не дисциплина)

**Автоматизировать в `route_next`:** каждый элемент `next[]` несёт handoff substance из карточки:

- `taskId`, `title`, `status`
- `toBe`, `criterion` (и `asIs`)
- `blockedBy`

Агент **цитирует** поля из tool result; не держит B в голове и не просит оператора угадывать.

```text
Done: <task_id> — <evidence>
Next: <taskId> — <title>
  to_be: <from next[].toBe>
  criterion: <from next[].criterion>
```

Bare id без toBe/criterion = anti-pattern **и** признак старого MCP (&lt; 0.3.1).

## Где

| Слой | Что |
|------|-----|
| **Core `TaskCardSummary`** | поля `ToBe`, `AsIs`, `Criterion` |
| **MCP `route_next` / `tasks`** | сериализация тех же полей |
| **man route_next** | документирует handoff OUTPUT |

## Не делать

- Не полагаться на «агент сам вспомнит прочитать карточку».
- Не раздувать ответ дампом всей md-карточки.
- Не CLAUDE.md как замена route_next.

## Criterion

`route_next` на ready-задаче с заполненным substance возвращает непустые `toBe` и `criterion` без отдельного `read_card`.

