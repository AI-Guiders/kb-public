---
type: Note
title: ZCode harness quirks (v1)
description: 'Факты проверены на ZCode Desktop 3.x (Windows, 2026-10-23/24, логи и живые прогоны в ходе OKF-миграции ADR-026 M1–M2). При апдейте харнесса — перепроверить (freshness: operational).'
tags: [zcode, harness, mcp, cdp, agent-operations]
language: ru
verified:
  - by: human:operator
    at: 2026-10-24
world: agent
subworld: operations
---

# ZCode harness quirks (v1)

Факты проверены на ZCode Desktop 3.x (Windows, 2026-10-23/24, логи и живые прогоны в ходе OKF-миграции ADR-026 M1–M2). При апдейте харнесса — перепроверить (freshness: operational).

## 1. MCP-тулы появляются только в новой сессии

Набор MCP-инструментов фиксируется при `mcp.startup.completed` сессии; правка `~/.zcode/cli/config.json` или рестарт приложения не добавляет тула в текущий диалог — нужен новый чат. Инфраструктура при этом живёт: процессы серверов запускаются, пулы переподключаются. Проверка: логи `~/.zcode/cli/log/*.jsonl` (события `mcp.server.connected`, `mcp.startup.completed`, `toolCount`) и Settings → MCP.

## 2. Diff/changes-панель не перечитывает файлы с диска

Панель «изменённых» держит снимок на момент открытия; правка файла агентом на диске не отражается до переоткрытия. Актуальность проверять чтением файла, не панелью.

## 3. Диагностики: syntax-scope по умолчанию, project — по запросу

CDP-диагностики после содержательных правок под открытым решением запрашивать с `scope=project` (полный Roslyn; холодный первый прогон ~минута, тёплый мгновенный). Дефолтный syntax ловит только синтаксис — семантические ошибки (например, CS0246 без using) видны только на project-уровне. Поддерживаемые языки: csharp | typescript | powershell | fsharp | gdl; для xml (csproj/slnx) онлайн-диагностик нет.

## 4. Фоновые джобы CDP (wake/AutoIgnition) в ZCode не доставляются

`cdp_build` / `cdp_test` с `background=true` возвращают `job_id`, но wake по завершении в ZCode не приходит. Фоновые задачи: поллить последний результат или использовать фоновый Bash самого харнесса — его уведомления работают штатно.

## 5. MCP-конфиг ZCode — user scope; бутстрап без MCP

SSOT MCP-серверов — `~/.zcode/cli/config.json` → `mcp.servers` (user scope; schema: `command` строкой + `args[]`, `env`, `headers`, `timeoutMs`; шаблоны `{env:…}` не разворачиваются — подставлять значения; строгая схема — лишние ключи роняют сервер). Исторический источник миграции (2026-10-23) — `~/.config/opencode/opencode.jsonc`; обратная синхронизация не ведётся.

**Бутстрап памяти без MCP:** `~/.zcode/AGENTS.md` грузится инструкциями в каждой сессии независимо от состояния MCP и содержит путь к KB + правила загрузки (`read_hot_context` и др.) — это точка входа, когда тулы ещё не подключены.

---

provenance: сессия 2026-10-23/24 — анализ логов ZCode (`~/.zcode/cli/log/*.jsonl`), CDP-диагностики, миграция ADR-026 M1–M2; operator подтверждена перезапуском сессии.

