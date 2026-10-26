---
type: Note
title: Cursor MCP remount (agent-operated)
description: '**Anti-pattern (устарело):** «перезагрузи MCP в Cursor» / Settings → Reload — **не** просить оператора.'
tags: [agent-operations, cursor, mcp, living]
language: ru
---
# Cursor MCP remount (agent-operated)

**Anti-pattern (устарело):** «перезагрузи MCP в Cursor» / Settings → Reload — **не** просить оператора.

---

## Одна строка

**Remount MCP делает агент сам** через правку `~/.cursor/mcp.json`; smoke одним tool call.

---

## Del/add (универсально, предпочтительно)

1. Прочитать `C:\Users\<user>\.cursor\mcp.json`.
2. Вырезать блок `"<server>": { ... }` целиком → сохранить.
3. Вставить **тот же** блок обратно → сохранить.

Cursor видит «сервер исчез / появился» и поднимает процесс заново. Работает для **любого** MCP (`dbhub`, `cdp`, `forge`, …). Без nudge-env, без UI.

После remount — один smoke tool call (например `search_objects_*` / `cdp_health`).

---

## Когда что

| Ситуация | Действие агента |
|----------|-----------------|
| Правка `config.toml` dbhub, stale tools | del/add секции `dbhub` |
| Deploy CDP / promote bridge | `cdp_deploy` уже bump'ит `CDP_RELOAD_NUDGE`; иначе del/add `cdp` / `cdp-debug` |
| Любая правка `command`/`args`/`env` в mcp.json | remount уже случился — smoke, не проси Reload |
| `Not connected` после KillRunning | del/add нужного сервера; если zombie — `Recover-CdpSeatRemount.ps1` (CDP) |

---

## Запрет

- Не писать оператору «Reload MCP» / «Settings → MCP» как шаг handoff.
- Не дублировать del/add инструкцию в каждой domain-note — ссылка сюда.

---

## Связь

- DBHub config: `note-opencode-dbhub-queries.md`
- CDP deploy nudge: `CdpReloadNudge.ps1` / `cdp_deploy`
- QRH: `cdp-mcp/.cdp/domain/teeth.md` § remount

**v1 · 2026-09-12**

