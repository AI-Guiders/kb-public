# Playbook: чистая установка стека знаний (ANM + kb-public → personal)

**Статус:** active · v1.0 · 2026-05-18  
**Назначение:** протокол для **нового пользователя** и **агента** (ANM + kb-public → personal chmod u).

**Поставка kb-public:** playbook + **`templates/newcomer/`** (см. `templates/README.md`).

**Триггеры:** «чистая установка», «первый раз», «настроить agent-notes», «скачал kb-public», «завести personal», «clean setup».

---

## Модель chmod ugo

| chmod | Слой | MCP |
|-------|------|-----|
| **u** | personal (primary) | без `knowledge_root_id` |
| **g** | group | `knowledge_root_id=group` |
| **o** | kb-public | `knowledge_root_id=public` |

---

## Фаза 0 — машина

.NET SDK, Git, Cursor; пути без пробелов — желательно.

---

## Фаза 1 — ANM

1. Клон [agent-notes-mcp](https://github.com/AI-Guiders/agent-notes-mcp), `dotnet publish`.
2. TOML: `config/` в репо ANM или **`templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml`**.
3. Cursor `mcp.json`: `"args": ["--config", "<path>"]`.

До personal: `primary = "public"`.

---

## Фаза 2 — personal

1. Репозиторий agent-notes (или минимум `knowledge/work/local/` + `agent-notes.md`).
2. TOML: `primary = "personal"`, roots personal + public.
3. Шаблоны: **`templates/newcomer/`** → `templates/newcomer/README.md`.
4. Перезапуск MCP.

---

## Фаза 3 — `work/local/` в personal

| Экземпляр | Шаблон |
|-----------|--------|
| `work/local/workspace-scope-map-v1.md` | `templates/newcomer/template-clean-setup-workspace-scope-map-v1.md` |
| `work/local/knowledge-roots-index-v1.md` | `templates/newcomer/template-clean-setup-knowledge-roots-index-v1.md` |
| hot-секции | `templates/newcomer/template-clean-setup-hot-*.md` |

---

## Фаза 4 — group (опционально)

`[[knowledge.read_only]]` id = `group`, реестр roots.

---

## Фаза 5 — готово

MCP, primary=personal, scope-map, public/group read.

---

## Поведение агента

1. Playbook + `templates/newcomer/README.md`.
2. Опрос → только оставшиеся фазы.
3. Не искать шаблоны в `work/local/` в kb-public.
4. `memory_health` + `route_context`.

---

## Связанные документы

- `templates/README.md`, `map-kb-three-contours-v1.md`, `adr/016-*`