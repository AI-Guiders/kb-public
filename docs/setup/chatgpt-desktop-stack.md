## Стек для ChatGPT Desktop (Windows)

### 1. Состав стека

- **ChatGPT Desktop** — официальное десктопное приложение ChatGPT.
- **kb-public** — локальный клон публичного канона знаний.
- **agent-notes-mcp** — MCP‑сервер для долговременных заметок и работы с каноном.
- **webcam-mcp** — MCP‑сервер для захвата камеры/экрана/аудио и анализа.
- **git-mcp** — MCP‑сервер для git status/diff/log/commit/push.
- **Git for Windows** — системный git (для git-mcp и работы с репами).

Все MCP‑серверы поставляются как self-contained .NET 10 win‑x64, у конечного пользователя .NET SDK не требуется.

### 2. Требования

- Windows 10/11 (x64).
- Доступ к нашему GitLab.
- Учётка в GitLab.
- Установленный **Git for Windows** (git в PATH).

### 3. Установка ChatGPT Desktop

1. Скачать последнюю версию ChatGPT Desktop с официального сайта OpenAI.
2. Установить с настройками по умолчанию.
3. Авторизоваться, проверить, что приложение стартует без ошибок.

### 4. Структура директорий

Рекомендуемая структура:

- `D:\ChatGPT\tools\agent-notes-mcp\`
- `D:\ChatGPT\tools\webcam-mcp\`
- `D:\ChatGPT\tools\git-mcp\`
- `D:\ChatGPT\kb-public\`

Создать базовые папки:

```powershell
mkdir D:\ChatGPT
mkdir D:\ChatGPT\tools
```

### 5. Установка kb-public

```powershell
cd D:\ChatGPT
git clone http://193.124.113.7/Krawler/kb-public.git kb-public
```

Итого канон: `D:\ChatGPT\kb-public`.

Рекомендуется переменная окружения:

- `AGENT_NOTES_CANON_PATH = D:\ChatGPT\kb-public`

После изменения переменных окружения перезапустить ChatGPT Desktop.

### 6. Установка agent-notes-mcp

1. Войти в GitLab → проект `agent-notes-mcp` → **Releases**.
2. Скачать архив для **win-x64**.
3. Распаковать в `D:\ChatGPT\tools\agent-notes-mcp\`.
4. Проверить наличие `D:\ChatGPT\tools\agent-notes-mcp\AgentNotesMcp.exe`.

(Опционально)

```powershell
New-Item -ItemType Junction -Path "D:\agent-notes-mcp" -Target "D:\ChatGPT\tools\agent-notes-mcp"
```

### 7. Установка webcam-mcp

1. GitLab → `webcam-mcp` → **Releases** → архив **win-x64**.
2. Распаковать в `D:\ChatGPT\tools\webcam-mcp\`.
3. Проверить `D:\ChatGPT\tools\webcam-mcp\WebcamMcp.exe`.

(Опционально)

```powershell
New-Item -ItemType Junction -Path "D:\webcam-mcp" -Target "D:\ChatGPT\tools\webcam-mcp"
```

### 8. Установка git-mcp

1. Убедиться, что `git --version` работает в PowerShell.
2. GitLab → `git-mcp` → **Releases** → архив **win-x64**.
3. Распаковать в `D:\ChatGPT\tools\git-mcp\`.
4. Проверить `D:\ChatGPT\tools\git-mcp\GitMcp.exe`.

(Опционально)

```powershell
New-Item -ItemType Junction -Path "D:\git-mcp" -Target "D:\ChatGPT\tools\git-mcp"
```

### 9. Подключение к ChatGPT Desktop

Механика привязки MCP к ChatGPT Desktop может меняться, поэтому здесь фиксируются только команды/пути.

Для каждого сервера:

- **agent-notes-mcp**
  - Command: `D:\ChatGPT\tools\agent-notes-mcp\AgentNotesMcp.exe`
  - Args: `[]`
- **webcam-mcp**
  - Command: `D:\ChatGPT\tools\webcam-mcp\WebcamMcp.exe`
  - Args: `[]`
- **git-mcp**
  - Command: `D:\ChatGPT\tools\git-mcp\GitMcp.exe`
  - Args: `[]`

Дальше:

- либо добавить их как локальные MCP‑серверы в настройках ChatGPT Desktop (если UI это поддерживает),
- либо через внешний профиль (например mcp.run), если ChatGPT Desktop работает через него.

Актуальный способ см. в документации ChatGPT Desktop по MCP + во внутренних регламентах.

### 10. Быстрый smoke‑test

После подключения MCP в ChatGPT Desktop:

- **agent-notes-mcp** — попросить вызвать `memory_health` для текущего workspace.
- **webcam-mcp** — запросить `capture_webcam_frame` и проверить, что в workspace появился кадр.
- **git-mcp** — запросить `git_status` для любого локального репозитория и сверить с выводом git в консоли.

При проблемах проверить:

- корректность путей к `.exe`,
- блокировки антивирусом,
- корректность `AGENT_NOTES_CANON_PATH`,
- наличие git в `PATH` для git-mcp.
