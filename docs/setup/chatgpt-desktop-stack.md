## Cursor: локальный MCP-стек (Windows)

!!! warning "ChatGPT Desktop — не stdio"
    **ChatGPT Desktop не подключает** локальные MCP через `command` + `args` и `.exe`, как Cursor. В ChatGPT коннекторы работают по **публичному HTTPS URL** (Settings → Connectors → Create), см. [Connect from ChatGPT](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt).  
    **agent-notes-mcp** сегодня — только **stdio** (`AgentNotesMcp.exe` + `--config`). Прямой перенос инструкции Cursor в ChatGPT **не работает**. Удалённый HTTP/SSE endpoint — [бэклог upstream](https://github.com/AI-Guiders/agent-notes-mcp) (см. §2).

Исторический URL страницы (`…/chatgpt-desktop-stack/`) — с wiki про ChatGPT; актуальное содержание ниже — **установка для Cursor**.

Полный онбординг (personal + group): [Чистая установка](../onboarding/clean-setup.md), playbook [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md), шаблон TOML [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml).

### 1. ChatGPT Desktop — что возможно сейчас

| Хост | Транспорт MCP | agent-notes-mcp |
|------|----------------|-----------------|
| **Cursor**, VS Code + MCP | Локальный **stdio** (`mcp.json`: `command`, `args`) | ✅ см. §5–7 |
| **Cascade IDE** | In-proc MCP в IDE | ✅ отдельная интеграция, [документация cascade-ide](https://ai-guiders.github.io/cascade-ide/) |
| **ChatGPT Desktop** | **HTTPS** коннектор → URL вида `https://…/mcp` | ❌ нет готового публичного endpoint; только stdio-бинарник |

Если нужен именно ChatGPT:

1. Нужен **свой** MCP-сервер, доступный по HTTPS (или туннель ngrok/Cloudflare Tunnel к такому серверу) — не к `AgentNotesMcp.exe` напрямую.
2. В ChatGPT: **Settings → Connectors → Create** — указать **Connector URL**, не путь к exe.
3. Для agent-notes/kb-public в ChatGPT пока разумнее **читать сайт** [kb-public](https://ai-guiders.github.io/kb-public/) или подключать **Cursor** с тем же каноном на диске.

Разработка remote-слоя для agent-notes-mcp (безопасный URL, read-only контур) — открытый бэклог; следить за [agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp).

### 2. Состав стека (Cursor)

| Компонент | Назначение |
|-----------|------------|
| **kb-public** | Публичный срез KB ([GitHub](https://github.com/AI-Guiders/kb-public)) |
| **agent-notes-mcp** | Память, hot-context, `knowledge/` ([релизы](https://github.com/AI-Guiders/agent-notes-mcp/releases)) |
| **git-mcp** | Git ([AI-Guiders/git-mcp](https://github.com/AI-Guiders/git-mcp)) |
| **webcam-capture-mcp** / **webcam-analysis-mcp** | Опционально ([open stack](https://ai-guiders.github.io/)) |
| **Git for Windows** | Для git-mcp и клонов |

MCP-серверы — self-contained **.NET 10 win-x64**; SDK не нужен.

### 3. Требования

- Windows 10/11 (x64).
- **Cursor** (или другой хост с **stdio MCP**).
- **Git for Windows** (`git` в PATH).
- Клоны и релизы с **GitHub**.

### 4. Каталоги (пример)

```text
D:\agent-stack\
  kb-public\
  agent-notes-mcp\       ← AgentNotesMcp.exe + agent-notes-mcp.toml
  tools\git-mcp\
```

```powershell
New-Item -ItemType Directory -Path D:\agent-stack\tools -Force
cd D:\agent-stack
git clone https://github.com/AI-Guiders/kb-public.git kb-public
```

### 5. agent-notes-mcp (бинарник)

1. [Releases](https://github.com/AI-Guiders/agent-notes-mcp/releases) → **win-x64**.
2. Распаковать в `D:\agent-stack\agent-notes-mcp\`.
3. Проверить `AgentNotesMcp.exe`.

Сборка из исходников: `dotnet publish`; `publish-and-deploy.ps1` копирует пример TOML рядом с exe.

### 6. Конфиг (TOML, обязательно)

Файл вне git, например `D:\agent-stack\agent-notes-mcp\agent-notes-mcp.toml`. Без **`--config`** процесс завершится с ошибкой. Переменная **`AGENT_NOTES_CANON_PATH`** в MCP 2.x **не используется**.

**Только kb-public:**

```toml
version = 1

[knowledge]
primary = "public"

[knowledge.roots]
public = "D:/agent-stack/kb-public"

[workspace]
default_scope = "mixed"
```

**+ личный канон** — [шаблон](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml), [чистая установка](../onboarding/clean-setup.md).

| Секция | Смысл |
|--------|--------|
| `[knowledge]` / `[knowledge.roots]` | Корень с `knowledge/` и `agent-notes.md` |
| `[workspace]` | Scope-map в личном каноне |
| `[status]` | Опционально localhost status |

Подробнее: [ADR 014](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/014-agent-notes-local-settings-toml-v1.md), [MCP-TOOLS](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/MCP-TOOLS.md).

### 7. Cursor — `mcp.json`

**`%USERPROFILE%\.cursor\mcp.json`:**

```json
{
  "mcpServers": {
    "agent-notes": {
      "command": "D:\\agent-stack\\agent-notes-mcp\\AgentNotesMcp.exe",
      "args": ["--config", "D:/agent-stack/agent-notes-mcp/agent-notes-mcp.toml"],
      "env": {}
    }
  }
}
```

Альтернатива: env **`AGENT_NOTES_CONFIG`** = путь к тому же TOML.

После правок — перезапустить Cursor.

Опционально в том же файле — **git-mcp**, **webcam-*** (только `command`, без `--config`):

```json
"git": {
  "command": "D:\\agent-stack\\tools\\git-mcp\\GitMcp.exe",
  "args": [],
  "env": {}
}
```

### 8. Smoke-test (Cursor)

1. **`memory_health`** — `workspace_path` = каталог локального проекта.
2. **`read_knowledge_file`** — `file_path`: `SHOWCASE.md`.
3. **`route_context`** — запрос «чистая установка kb».

### 9. Если не работает

| Симптом | Проверить |
|---------|-----------|
| MCP сразу падает | Файл `--config`, валидный TOML (`version = 1`) |
| «Нет knowledge» | `[knowledge.roots]` → клон с каталогом **`knowledge/`** |
| Пытались подключить exe в ChatGPT | ChatGPT не stdio; нужен HTTPS MCP или используй Cursor |
| Старые гайды с `AGENT_NOTES_CANON_PATH` | TOML + `--config` |
