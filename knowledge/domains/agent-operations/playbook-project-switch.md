# Project switch v1
**Tags:** #agent-operations #domains #living #playbook


Тела секции `project-switch-protocol-v1` из `agent-notes.md`. Длинный контур: `knowledge/worlds/workspace-context/playbook-multi-project-context.md`.

<!-- section:project-switch-protocol-v1 -->
## Project Switch Protocol v1

**Назначение:** один **primary** `project-id` и один **scope** slice (L1) за раз в мультипроектном чате — без смешения репозиториев. Параллель **`mode-switch-protocol`** (WORK/HUMAN): не авто-угадывание, а **явные маркеры + дефолт из карты пути + переопределение**.

### Маркеры в сообщении пользователя (высший приоритет)

- **`[PRIMARY:<project-id>]`** — корневой трек (репо / продукт). Полный перечень id: `knowledge/work/projects/door-to-singularity/door-to-singularity/project-ids-quickref.md`; **алиасы** (`CIDE` → `cascade-ide`, `GUIP` → `guiders-ui-platform`, …) — там же; после резолва — канонический id.
- **`[PRIMARY:<project-id>/<sub-project-id>]`** — подпроект внутри родителя (иерархия). Карточка: `…/<project-id>/subprojects/<sub-project-id>.md`. **Алиасы с обеих сторон** (`GUIP/UIR`, `CDP/BUF`, `CIDE/GLASS`); sub-project = подмножество, но для PRIMARY — полноценный трек. Таблица: `project-ids-quickref.md` § Sub-project алиасы; соглашение: `work/projects/README.md` § Sub-project.
- **`[SCOPE:<slice>]`** — slice операционной памяти: `door-to-singularity` | `portal` | `harvester` | `imc` | `mixed`. Алиасы scope: `DTS` → `door-to-singularity`; `PTL` → `portal`; … — `project-ids-quickref.md`.

Правило приоритета: **явный маркер в текущем сообщении** переопределяет состояние «primary/scope» для этого шага; при отсутствии маркеров — ниже.

### Дефолт без маркеров

1. **`workspace_path`** (корень workspace в Cursor) матчится по **`workspace-scope-map-v1`** → `door-to-singularity` / `portal` / `harvester` / `imc`.
2. Если путь однозначен — **primary** можно вывести из контекста задачи и карточек в `knowledge/work/projects/door-to-singularity/` / `portal/` / `imc/` (хабы README), но при **риске смешения** двух продуктов в одном сообщении — **один** уточняющий вопрос или явное «считаю primary: …, ок?».

### Эвристики (не заменяют маркеры)

- Путь к файлу в сообщении (`…/cascade-ide/…`, `…/EDW.Portal…`) → подсказка primary/scope; не менять primary «молча», если в том же треде недавно был другой явный PRIMARY.
- Полная автоматика без маркеров и без карты — **не** гарантируется; при сомнении — маркер или вопрос.

### Связь с инструментами и KB

- Длинный контур: `knowledge/worlds/workspace-context/playbook-multi-project-context.md`.
- Вызов MCP: параметр **`active_scope`**, если slice должен отличаться от резолва по пути.
- **route_context** индексирует только `agent-notes.md`; playbook и карточки проектов — **`read_knowledge_file`** по путям из `knowledge/work/projects/`.
<!-- /section:project-switch-protocol-v1 -->

