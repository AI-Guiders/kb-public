# Project switch v1

Тела секции `project-switch-protocol-v1` из `agent-notes.md`. Длинный контур: `knowledge/worlds/workspace-context/playbook-multi-project-context-v1.md`.

<!-- section:project-switch-protocol-v1 -->
## Project Switch Protocol v1

**Назначение:** один **primary** `project-id` и один **scope** slice (L1) за раз в мультипроектном чате — без смешения репозиториев. Параллель **`mode-switch-protocol`** (WORK/HUMAN): не авто-угадывание, а **явные маркеры + дефолт из карты пути + переопределение**.

### Маркеры в сообщении пользователя (высший приоритет)

- **`[PRIMARY:<project-id>]`** — какой трек сейчас главный. Полный перечень id без таблицы: `knowledge/work/projects/door-to-singularity/door-to-singularity/project-ids-quickref-v1.md`; **алиасы** (например `CIDE` → `cascade-ide`, `DTS` → `door-to-singularity`) — в том же файле, секция «Алиасы → канон»; в каноне и путях после резолва — только канонический id. Каталоги и детали — `knowledge/work/projects/README.md`, таблица — `knowledge/work/projects/door-to-singularity/door-to-singularity/README.md`. Примеры: `cascade-ide`, `equation-to-ca-cuda`, `ca-substrate-agent`, `agent-first-learn`, `agent-personhood-research`, `ainet`, `open-agent-registry`, `agent-audio`, `agents-and-humans`, `income-cascade`, `roslyn-mcp`, `door-to-singularity`, `edw-portal`, `imc-portal`, …
- **`[SCOPE:<slice>]`** — какой slice операционной памяти грузить: `door-to-singularity` | `portal` | `harvester` | `imc` | `mixed`. Соответствует резолву **`active_scope`** в MCP (`read_hot_context`, `route_context`, `memory_health`). **Алиасы scope:** `DTS` (и legacy `current-projects`) → `door-to-singularity`; `PTL` → `portal`; `HRV` / `EDWH` → `harvester` — см. `project-ids-quickref-v1.md`, секция «Алиасы scope → канон».

Правило приоритета: **явный маркер в текущем сообщении** переопределяет состояние «primary/scope» для этого шага; при отсутствии маркеров — ниже.

### Дефолт без маркеров

1. **`workspace_path`** (корень workspace в Cursor) матчится по **`workspace-scope-map-v1`** → `door-to-singularity` / `portal` / `harvester` / `imc`.
2. Если путь однозначен — **primary** можно вывести из контекста задачи и карточек в `knowledge/work/projects/door-to-singularity/` / `portal/` / `imc/` (хабы README), но при **риске смешения** двух продуктов в одном сообщении — **один** уточняющий вопрос или явное «считаю primary: …, ок?».

### Эвристики (не заменяют маркеры)

- Путь к файлу в сообщении (`…/cascade-ide/…`, `…/EDW.Portal…`) → подсказка primary/scope; не менять primary «молча», если в том же треде недавно был другой явный PRIMARY.
- Полная автоматика без маркеров и без карты — **не** гарантируется; при сомнении — маркер или вопрос.

### Связь с инструментами и KB

- Длинный контур: `knowledge/worlds/workspace-context/playbook-multi-project-context-v1.md`.
- Вызов MCP: параметр **`active_scope`**, если slice должен отличаться от резолва по пути.
- **route_context** индексирует только `agent-notes.md`; playbook и карточки проектов — **`read_knowledge_file`** по путям из `knowledge/work/projects/`.
<!-- /section:project-switch-protocol-v1 -->
