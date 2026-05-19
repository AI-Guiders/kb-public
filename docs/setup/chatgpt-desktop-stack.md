## Стек агента: Cursor и ChatGPT Desktop (Windows)

Страница для **локального stdio MCP** на Windows. С **agent-notes-mcp 2.x** обязателен файл **TOML** и аргумент **`--config`** в настройках хоста; переменная **`AGENT_NOTES_CANON_PATH`** больше не используется.

Полный онбординг (personal + group): [Чистая установка](../onboarding/clean-setup.md), playbook [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md), шаблон TOML [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml).

### 1. Состав стека

| Компонент | Назначение |
|-----------|------------|
| **kb-public** | Публичный срез KB (клон с GitHub) |
| **agent-notes-mcp** | Память, hot-context, `knowledge/` ([релизы](https://github.com/AI-Guiders/agent-notes-mcp/releases)) |
| **git-mcp** | Git status/diff/commit ([AI-Guiders/git-mcp](https://github.com/AI-Guiders/git-mcp)) |
| **webcam-capture-mcp** / **webcam-analysis-mcp** | Кадры/экран/аудио и анализ (опционально; [open stack](https://ai-guiders.github.io/)) |
| **Git for Windows** | Для git-mcp и клонов |

Серверы MCP — self-contained **.NET 10 win-x64**; SDK на машине пользователя не нужен.

### 2. Требования

- Windows 10/11 (x64).
- **Git for Windows** (`git` в PATH).
- **Cursor** и/или **ChatGPT Desktop** с поддержкой **локальных** MCP (stdio: `command` + `args`).
- Доступ в интернет для клонов с **GitHub** (релизы и `kb-public`).

!!! note "ChatGPT и удалённый MCP"
    В части сценариев ChatGPT подключает MCP только по **HTTPS URL** (коннекторы), без локального `.exe`. Тогда stdio-стек ниже — для **Cursor**; для ChatGPT смотри [документацию OpenAI по MCP](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt). Удалённый endpoint для agent-notes-mcp — в бэклоге upstream.

### 3. Каталоги (пример)

```text
D:\agent-stack\
  kb-public\              ← git clone
  agent-notes-mcp\        ← AgentNotesMcp.exe + agent-notes-mcp.toml
  agent-notes-mcp.toml    ← тот же файл (рядом с exe — удобно)
  tools\git-mcp\
  tools\webcam-capture-mcp\
```

```powershell
New-Item -ItemType Directory -Path D:\agent-stack\tools -Force
```

### 4. kb-public

```powershell
cd D:\agent-stack
git clone https://github.com/AI-Guiders/kb-public.git kb-public
```

Корень среза: `D:\agent-stack\kb-public` (внутри есть `knowledge/` и урезанный `agent-notes.md`).

### 5. agent-notes-mcp (бинарник)

1. [Releases](https://github.com/AI-Guiders/agent-notes-mcp/releases) → архив **win-x64**.
2. Распаковать в `D:\agent-stack\agent-notes-mcp\`.
3. Проверить: `D:\agent-stack\agent-notes-mcp\AgentNotesMcp.exe`.

Сборка из исходников: [AI-Guiders/agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp) — `dotnet publish`; скрипт `publish-and-deploy.ps1` копирует пример TOML рядом с exe.

### 6. Конфиг agent-notes-mcp (TOML, обязательно)

Файл **вне git** (например `D:\agent-stack\agent-notes-mcp\agent-notes-mcp.toml`). Без **`--config`** процесс завершится с ошибкой.

**Только kb-public** (участник без личного канона):

```toml
# agent-notes-mcp 2.x — schema version = 1
version = 1

[knowledge]
primary = "public"

[knowledge.roots]
public = "D:/agent-stack/kb-public"

[workspace]
default_scope = "mixed"
```

**kb-public + личный канон** (после [чистой установки](../onboarding/clean-setup.md)) — см. шаблон [template-clean-setup-agent-notes-mcp-toml-v1.toml](../knowledge/templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml): `primary = "personal"`, корни `personal` и `public`, при необходимости `[[knowledge.read_only]]` для group.

Секции TOML:

| Секция | Смысл |
|--------|--------|
| `[knowledge]` / `[knowledge.roots]` | Где лежит `knowledge/` и `agent-notes.md` (primary root) |
| `[workspace]` | `default_scope`, пути к `scope_map` / `scope_aliases` в **личном** каноне |
| `[status]` | Опционально: localhost status (порт, preview) — см. ADR в [agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp/tree/main/docs/adr) |

Пути в TOML — **прямые слэши** `D:/...` или экранированные `\\` в JSON; для `mcp.json` удобнее forward slashes.

Подробнее: [ADR 014 (локальный TOML)](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/014-agent-notes-local-settings-toml-v1.md), [MCP-TOOLS](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/MCP-TOOLS.md).

### 7. Подключение в Cursor (`mcp.json`)

Файл: **`%USERPROFILE%\.cursor\mcp.json`** (или настройки MCP в IDE). Фрагмент для **agent-notes**:

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

Альтернатива пути к TOML: env **`AGENT_NOTES_CONFIG`** (если хост не передаёт `args`).

После правок — **перезапустить Cursor** (и дождаться перезапуска MCP-процесса).

### 8. Подключение в ChatGPT Desktop

Если в настройках доступны **локальные MCP-серверы** (stdio), используй **те же** `command` и `args`, что в §7 — в том числе **`--config`** с абсолютным путём к TOML.

Пример полей UI (имена могут отличаться):

| Поле | Значение |
|------|----------|
| Command | `D:\agent-stack\agent-notes-mcp\AgentNotesMcp.exe` |
| Args | `["--config", "D:/agent-stack/agent-notes-mcp/agent-notes-mcp.toml"]` |

Не оставляй `args: []` — это конфигурация **до MCP 2.0**.

### 9. Опциональные MCP

У каждого — свой `command` в `mcp.json`, **без** `--config` (если сервер не требует):

| Сервер | Пример command |
|--------|----------------|
| **git-mcp** | `D:\agent-stack\tools\git-mcp\GitMcp.exe` |
| **webcam-capture-mcp** | `...\WebcamCaptureMcp.exe` |
| **webcam-analysis-mcp** | `...\WebcamAnalysisMcp.exe` |

Релизы — репозитории [AI-Guiders](https://github.com/AI-Guiders) / open stack на [лендинге](https://ai-guiders.github.io/).

### 10. Smoke-test

В Cursor или ChatGPT (с подключённым agent-notes):

1. **`memory_health`** с `workspace_path` = каталог любого локального проекта (например `D:/projects/my-app`).
2. **`read_knowledge_file`** — `file_path`: `SHOWCASE.md` (корень из TOML `public`).
3. **`route_context`** — запрос вроде «чистая установка kb»; в ответе должны быть ссылки на playbook из kb-public.

Для **git-mcp**: `git_status` с `workspace_path` репозитория — сверить с `git status` в терминале.

### 11. Если не работает

| Симптом | Проверить |
|---------|-----------|
| MCP сразу падает | Есть ли файл из `--config`; валидный TOML (`version = 1`) |
| «Нет knowledge» | Путь в `[knowledge.roots]` ведёт в клон с каталогом **`knowledge/`** |
| Пустой hot / scope | Для полной карты workspace нужен **личный** канон и `work/local/` (см. [clean-setup](../onboarding/clean-setup.md)) |
| Старые инструкции с `AGENT_NOTES_CANON_PATH` | Заменить на TOML + `--config` |
| Антивирус | Исключение для каталога с `.exe` |
