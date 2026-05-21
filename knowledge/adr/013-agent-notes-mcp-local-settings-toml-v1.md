# ADR 013: Локальные настройки agent-notes-mcp (TOML)

**Статус:** Proposed  
**Дата:** 2026-05-16  
**Supersedes:** часть C [008](008-workspace-scope-map-hot-mcp-and-public-cut.md) (`mcp-resolve-paths-v1.json` → секция **`[workspace]`** в TOML)  
**Extended by:** —  
**Связано:** [008](008-workspace-scope-map-hot-mcp-and-public-cut.md), [012](012-multi-canon-workspace-resolution-v1.md); реализация в репо **agent-notes-mcp** — `docs/adr/014-agent-notes-local-settings-toml-v1.md`; UI диагностики — `docs/adr/013-localhost-status-surface-v1.md` (MCP, **не** в kb-public как продукт IDE).

---

## Контекст

Сегодня установка MCP опирается на **env** в `mcp.json` и отдельный **`knowledge/META/mcp-resolve-paths-v1.json`** ([008](008-workspace-scope-map-hot-mcp-and-public-cut.md) часть C) — два неявных угла конфигурации.

[012](012-multi-canon-workspace-resolution-v1.md) задаёт **primary / read-only knowledge roots** (в тексте ADR 012 ещё «canon» — историческое имя). Этот ADR вводит **новый** локальный **TOML** (в **1.x его не было**) и привязывает его к мажору **agent-notes-mcp 2.0** — секции **`[knowledge]`**, **`[workspace]`**, **`[status]`**, без META JSON.

---

## Решение

### P0. Явное лучше неявного

Конфигурация MCP **не** угадывается по дереву workspace и **не** размазывается по десятку env. Один **явный** путь к TOML в `mcp.json` (как DBHub). Если путь задан и файл недоступен — **fail fast**, а не тихий откат на «как получится».

### R1. Явный путь к конфигу (как DBHub)

**Ориентир:** [DBHub](https://github.com/bytebase/dbhub) — в `mcp.json` передаётся **`--config`** с абсолютным путём к TOML; процесс **не ищет** конфиг сам по дереву workspace.

| Свойство | Значение |
|----------|----------|
| **Формат файла** | **TOML** (комментарии, таблицы) |
| **Где лежит файл** | **любой** путь на диске (как `C:/CursorDBHubConfig/config.toml` у DBHub); не обязан называться `.cursor/agent-notes.toml` |
| **Как указать** | аргумент CLI **`--config`** `<path>` в `args` сервера `agent-notes` в Cursor |
| **В git** | локальный файл с путями — обычно **вне** репо или в gitignore; шаблон — `knowledge/work/local/agent-notes.workspace.example.toml` |

**Пример `mcp.json` (как dbhub):**

```json
"agent-notes": {
  "command": "D:\\agent-notes-mcp\\AgentNotesMcp.exe",
  "args": [
    "--config",
    "D:/Experiments/agent-notes-mcp.local.toml"
  ],
  "env": {}
}
```

**Опционально (одна env, если хост не умеет args):** `AGENT_NOTES_CONFIG` = тот же путь. Приоритет в **2.0:** **`--config`** > `AGENT_NOTES_CONFIG` > fail (R4).

**Walk-up** (автопоиск `.cursor/agent-notes.toml` по каталогам) — **не** в v1: отклонён как неявный SSOT. Новая установка: только `--config` (или `AGENT_NOTES_CONFIG` в тестах).

**Путь в `--config`:** предпочтительно **абсолютный** (как у DBHub в `mcp.json`), чтобы не зависеть от cwd процесса Cursor.

### R2. Слияние настроек

**MCP 2.0** (есть `--config`):

| Уровень | Источник |
|---------|----------|
| 0 | embedded `agent-notes-mcp.defaults.toml` в **AgentNotes.Core** |
| 1 | пользовательский TOML по **`--config`** / `AGENT_NOTES_CONFIG` |

Файл **обязан** существовать и парситься → иначе **fail fast**. `AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` в **2.0 не читаем**.

**MCP 1.x** (TOML **нет**): как сегодня — env, META JSON, fallback `{workspace}/.cascade-ide/agent-notes.md`.

### R3. Схема локального TOML (первая редакция)

Два разных «версии» **не путать**:

| Что | Номер | Смысл |
|-----|-------|--------|
| **agent-notes-mcp** (exe / NuGet) | **2.0.0** | semver **major** продукта (R7) |
| поле **`version`** в TOML | **1** | **первая** схема этого файла; в 1.x поля не было, «TOML v2» не существует |

Когда позже изменим раскладку секций TOML — поднимем только **`version`** в файле (напр. `2`), не обязательно вместе с MCP 3.0.

Опционально в v1 схемы: `version = 1` в example; loader принимает отсутствие поля как `1` до появления второй схемы.

Черновик с `[canon]` в ранних правках ADR **не** публикуем.

#### Терминология: до 2.0 и после 2.0

| Смысл | MCP **1.x** (сейчас) | MCP **2.0** (целевое) |
|-------|----------------------|------------------------|
| главный корень KB | primary canon, `AGENT_NOTES_CANON_PATH` | `[knowledge].primary`, без env в `mcp.json` |
| доп. корень read-only | secondary canon | `[[knowledge.read_only]]` |
| аргумент тула | `canon_path` | **`knowledge_path`** (breaking rename) |
| резолв в коде | `ResolveCanonPath` | `ResolveKnowledgeRoot` (или эквивалент; внутреннее имя) |

В ADR 012 в prose ещё **«canon»** — историческое имя той же сущности; для **2.0** в публичном API MCP переходим на **knowledge** (как каталог `knowledge/` в репо).

**Правила именования:**

- **Секции** — по **роли** (`knowledge`, `workspace`, `status`), не по механизму резолва в коде.
- **Ключи** — короткие **существительные**; без `mcp_`, без копирования имён JSON/C#.
- `scope_map` / `scope_aliases` — пути **относительно корня primary** (`[knowledge].primary`), не относительно пути к `.toml`.

| Секция | Зачем |
|--------|--------|
| **`[knowledge]`** | какой корень KB главный (запись, hot, карта workspace) |
| **`[knowledge.roots]`** | именованные пути к репозиториям agent-notes / org-kb |
| **`[[knowledge.read_only]]`** | доп. корни только для чтения ([012](012-multi-canon-workspace-resolution-v1.md)) |
| **`[workspace]`** | scope: дефолт, карта `путь → slice`, алиасы |
| **`[status]`** | localhost AgentNotesStatus (MCP ADR 013) |
| **`[status.preview]`** | опционально: workspace для превью |
| **`[routing]`** *(фаза 2)* | overlay org в `route_context` |

```toml
version = 1

# --- Корни knowledge base (ADR 012) ---
[knowledge]
primary = "personal"          # ключ из [knowledge.roots] или абсолютный путь

[knowledge.roots]
personal = "D:/Experiments/agent-notes"
# org = "D:/clones/AI-Guiders/kb"

[[knowledge.read_only]]
id = "org"
path = "D:/clones/AI-Guiders/kb"

# --- Workspace → scope (файлы в primary knowledge root, см. 008) ---
[workspace]
default_scope = "door-to-singularity"
scope_map = "work/local/workspace-scope-map-v1.md"
scope_aliases = "work/local/scope-alias-map-v1.md"

[status]
enabled = false
port = 17341
bind = "127.0.0.1"

# [status.preview]
# workspace = "D:/Experiments/PersonalCursorFolder"
```

**Минимум:** `[knowledge.roots].personal` + `[knowledge].primary = "personal"` (или `primary` = абсолютный путь без `roots`).

#### `[[knowledge.read_only]]` в релизе **2.0.0**

Смысл — [012](012-multi-canon-workspace-resolution-v1.md): org-kb и прочие корни **без записи** через MCP; primary остаётся личным `agent-notes`.

| Что | **2.0.0** |
|-----|-----------|
| Секция в схеме TOML, парсинг → `LocalSettings.ReadOnlyKnowledgeRoots` | **да** (AgentNotes.Core) |
| Тулы `read_knowledge_file` / `write_*` / `list_knowledge_files` с выбором read-only по `id` | **нет** |
| Запрет `write_*` при `knowledge_path` на read-only root | **нет** |
| AgentNotesStatus: блок «read-only roots» | **нет** (после [013](013-localhost-status-surface-v1.md) localhost) |

Пока multi-KB не включён — **`[[knowledge.read_only]]` можно не указывать**; достаточно primary. Временный обход org: явный **`knowledge_path`** в вызове тула на абсолютный путь org-kb (как в 1.x с `canon_path`).

**Фаза после 2.0:** резолв по `knowledge_root_id` / префиксу; read-only только для read/list; `[routing]` для `route_context` (см. таблицу секций выше).

**Маппинг путей workspace** (бывший META JSON → поля TOML):

| TOML `[workspace]` | `mcp-resolve-paths-v1.json` |
|--------------------|------------------------------|
| `workspace.scope_map` | `workspace_scope_map` |
| `workspace.scope_aliases` | `scope_alias_map` |
| `workspace.default_scope` | *(hot / параметр тула)* |

### R4. Env и `mcp.json` (1.x → 2.0)

| Релиз | Поведение |
|-------|-----------|
| **1.x** | `AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` в `env`; META JSON для путей scope |
| **2.0** | установка: **`args: ["--config", "...toml"]`**, `env: {}` (как dbhub); **`AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` не документируем** и не читаем в happy-path |
| **2.0, переход** | один минор 1.x с stderr-warning «upgrade to 2.0 + --config» — **опционально**; не обязательно длинный overlap |

Отдельные env на флаги (`AGENT_NOTES_STATUS_*`, …) **не** вводим. Для тестов: `AGENT_NOTES_CONFIG` + fixture TOML.

### R7. Мажорный релиз **agent-notes-mcp 2.0**

Пакет изменений из этого ADR + localhost status — **один semver major** (`2.0.0`), не серия миноров «по кусочку без сюрпризов».

**Breaking (миграция с 1.x):**

| Область | Было | Стало |
|---------|------|--------|
| Установка | `env`: `AGENT_NOTES_CANON_PATH` | **`--config`** + **новый** локальный TOML |
| Пути scope | `knowledge/META/mcp-resolve-paths-v1.json` | **`[workspace]`** в TOML |
| Tools | параметр **`canon_path`** | **`knowledge_path`** (обновить Cursor rules / playbook) |
| Описания tools | «канон» | knowledge root / KB |
| Локальный конфиг | **отсутствует** | TOML по явному пути; без `--config` — **exit** с инструкцией |

**Не breaking для KB-репозиториев:** файлы `knowledge/`, hot, карты в `work/local/` — те же пути; меняется только **как MCP их находит**.

**Версионирование:** только **MCP `2.0.0`** в README / CHANGELOG / AgentNotesStatus; поле `version` в TOML — **`1`** (схема файла), не «2».

**1.x:** maintenance только критичные фиксы; новые фичи (TOML, status) — только в ветке **2.0**.

### R5. Секция `[workspace]` вместо `mcp-resolve-paths-v1.json`

| Источник | Роль |
|----------|------|
| embedded defaults → `[workspace]` | дефолтные `scope_map` / `scope_aliases` |
| `--config` TOML | переопределение |

| Фаза | Действие |
|------|----------|
| **До кода** | JSON в META как сейчас ([008](008-workspace-scope-map-hot-mcp-and-public-cut.md)) |
| **После Tomlyn** | читать `[workspace]`; при отсутствии секции — embedded defaults, затем legacy JSON |
| **Стабилизация** | удалить META JSON из primary KB |

Markdown-файлы карты и алиасов **остаются** в **primary** knowledge root.

### R6. Runtime-артефакты (не конфиг)

Процесс MCP может писать под workspace (в `.gitignore`):

| Файл | Назначение |
|------|------------|
| `.cascade-ide/agent-notes-status.runtime.json` | pid, port, url, `config_source` (для AgentNotesStatus) |

Формат runtime — **JSON** (генерирует код, не редактирует человек).

---

## Цепочка резолва primary knowledge root

**MCP 2.0:** (1) аргумент тула **`knowledge_path`** → (2) **`[knowledge]`** из TOML по **`--config`**.

**MCP 1.x:** `canon_path` → `AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` → `workspace_path/.cascade-ide/agent-notes.md` (TOML не участвует).

`scope_map` / `scope_aliases` — из **`[workspace]`**; файлы — в **primary** root из `[knowledge].primary`.

---

## Последствия

**Плюсы:** один файл, один путь в `mcp.json` — как DBHub; без зоопарка env; AgentNotesStatus показывает `config_path` из `--config`.

**Минусы:** путь в `mcp.json` нужно обновить при смене машины (как у DBHub — отдельный локальный config).

**Риски:** миграция `mcp.json` и правил с `canon_path` → чеклист в CHANGELOG 2.0; mitigation: example toml + один абзац в README.

---

## Решения (бывшие открытые вопросы)

| Вопрос | Решение |
|--------|---------|
| Fail fast vs fallback при битом `--config` | **Fail fast**, если путь явно задан |
| Walk-up | **Нет** в v1 |
| Имя флага | **`--config`** (alias `--config-file` допустим в коде) |

---

## План внедрения (к релизу **2.0.0**)

| Фаза | Содержание |
|------|------------|
| **0** | ADR (KB + MCP mirror), example TOML, CHANGELOG draft 2.0 |
| **1** | Core: Tomlyn, `--config`, `[knowledge]` + `[workspace]`; убрать META JSON из резолва |
| **2** | AgentNotesStatus + `[status]` |
| **3** | Публичный API + приборка Core/MCP (`ResolveCanonPath` → `ResolveKnowledgeRoot`, убрать `McpResolvePaths*`, дубликаты `.cs`); см. MCP ADR 014 «Техдолг»; удалить META JSON из KB |
| **4** | **Релиз `2.0.0`**: без legacy env в supported path; README/migration; тег NuGet/exe при публикации |

