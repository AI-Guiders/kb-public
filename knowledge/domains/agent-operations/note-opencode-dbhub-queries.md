# OpenCode session store × DBHub
**Tags:** #agent-operations #opencode #dbhub #sqlite #living

**Config:** `C:/CursorDBHubConfig/config.toml` → source `opencodedb`  
**DB path:** `C:/Users/dkara/.local/share/opencode/opencode.db`

---

## Одна строка

**Transcripts OpenCode — через DBHub `opencodedb`, таблицы `message` + `part`. Не `session_message` (пустая).**

---

## MCP tools

| Tool | Назначение |
|------|------------|
| `execute_sql_opencodedb` | произвольный SELECT |
| `search_objects_opencodedb` | schema / tables |
| `search_opencode_text` | prose search по substring (custom tool) |

После правки `config.toml` — remount **сам**: del/add секции `dbhub` в `~/.cursor/mcp.json` → smoke tool call. Канон: `note-cursor-mcp-remount.md`.

---

## Schema (live 2026-09)

```text
session(id, ...)
message(id, session_id, data JSON { role: user|assistant })
part(message_id, session_id, time_created, data JSON { type: text|tool|reasoning, text?, tool?, ... })
session_message — legacy, 0 rows — не использовать
```

Export: `agent-notes/tools/Export-OpencodeTranscript.ps1` (`-SessionID ses_...`).

---

## Примеры SQL

**Prose search (KB AutoShip):**

```sql
SELECT m.session_id,
       datetime(p.time_created / 1000.0, 'unixepoch') AS ts_utc,
       substr(json_extract(p.data, '$.text'), 1, 2000) AS text
FROM part p
JOIN message m ON m.id = p.message_id
WHERE json_extract(p.data, '$.type') = 'text'
  AND lower(json_extract(p.data, '$.text')) LIKE '%kb autoship%'
ORDER BY p.time_created DESC
LIMIT 5;
```

**Session message count:**

```sql
SELECT session_id, COUNT(*) AS parts
FROM part
GROUP BY session_id
ORDER BY parts DESC
LIMIT 10;
```

---

## Anti-pattern

- Node one-off scripts на `opencode.db` когда DBHub жив.
- `session_message` — пусто.
- `opencodedb` MCP namespace в dbhub ≠ отдельная установка; уже в config.

