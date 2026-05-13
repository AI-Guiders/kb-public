# Active scope — резолв slice и карта workspace (развёрнуто, v1)

**Назначение:** полный текст указателя `active-scope`, ранее в секции `active-scope` в `agent-notes.md`. В hot — одна строка-контракт + ссылки.

## Active scope (указатель)

Резолв slice в MCP: аргумент **`active_scope`** → **`knowledge/work/local/workspace-scope-map-v1.md`** (если есть под корнем канона) **или** секция **`workspace-scope-map-v1`** в hot (самый длинный префикс к `workspace_path`) → при отсутствии совпадений — встроенный fallback в **`agent-notes-mcp`** (`ResolveScope`). Полный протокол: **`knowledge/worlds/workspace-context/playbook-multi-project-context-v1.md`** §6c.

Не поддерживать здесь ручной **`current:`** как источник правды: при необходимости легаси-оверрайд всё ещё возможен одной строкой вида `current: <scope-id>`, но предпочтительны карта (файл или секция) и явный параметр вызова.
