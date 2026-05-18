# Playbook: чистая установка стека знаний (ANM + kb-public → personal)

**Статус:** active · v1.1 · 2026-05-19  
**Назначение:** протокол для **нового пользователя** и **агента** (agent-notes-mcp + публичный срез kb-public → личный канон chmod **u**).

**Поставка kb-public:** этот playbook + **`templates/newcomer/`** (см. `templates/README.md`).

**Триггеры:** «чистая установка», «первый раз», «настроить agent-notes», «скачал kb-public», «завести personal», «clean setup».

**Не путать:** поднять **свою организацию** (`{ORG_SLUG}/kb` + kb-public) — [`playbook-org-kb-white-label-v1.md`](playbook-org-kb-white-label-v1.md). Здесь — **участник**, который читает **чужой или свой** public slice и ведёт **personal**.

---

## Модель chmod ugo

| chmod | Слой | MCP |
|-------|------|-----|
| **u** | personal (primary) | без `knowledge_root_id` |
| **g** | group (`{ORG_SLUG}/kb`) | `knowledge_root_id=group` |
| **o** | kb-public | `knowledge_root_id=public` |

---

## Фаза 0 — машина

.NET SDK, Git, Cursor; пути без пробелов — желательно.

---

## Фаза 1 — agent-notes-mcp (ANM)

1. Собрать MCP из репозитория **agent-notes-mcp** (upstream open source, MIT) — `dotnet publish`.
2. TOML: пример в репо ANM или **`templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml`** (подставить **свои** пути).
3. Cursor `mcp.json`: `"args": ["--config", "<path-to-toml>"]`.

До personal: `primary = "public"` (путь к **вашему** clone kb-public).

---

## Фаза 2 — personal

1. Репозиторий personal kanon (`agent-notes` или свой fork) — минимум `knowledge/work/local/` + `agent-notes.md`.
2. TOML: `primary = "personal"`, roots personal + public (пути к **вашим** клонам).
3. Шаблоны: **`templates/newcomer/`** → см. `templates/newcomer/README.md`.
4. Перезапуск MCP.

---

## Фаза 3 — `work/local/` в personal

| Экземпляр | Шаблон |
|-----------|--------|
| `work/local/workspace-scope-map-v1.md` | `templates/newcomer/template-clean-setup-workspace-scope-map-v1.md` |
| `work/local/knowledge-roots-index-v1.md` | `templates/newcomer/template-clean-setup-knowledge-roots-index-v1.md` |
| hot-секции | `templates/newcomer/template-clean-setup-hot-*.md` |

Каталог `work/` в **kb-public нет** — шаблоны лежат в `knowledge/templates/newcomer/`.

---

## Фаза 4 — group (опционально, участник существующей org)

Если команда уже ведёт **`{ORG_SLUG}/kb`** (private):

1. Доступ к clone group + строка в TOML: `[[knowledge.read_only]]` id = `group`.
2. Заполнить `knowledge-roots-index-v1.md` (какие файлы только в group).
3. Hot: `template-clean-setup-hot-knowledge-roots-routing-v1.md`.
4. Smoke: `read_knowledge_file` + `group/smoke-test-v1.md` + `knowledge_root_id=group`.

**Основатель org** (создание `{ORG_SLUG}/kb`, seed, public push) — **не** эта фаза; см. [`playbook-org-kb-white-label-v1.md`](playbook-org-kb-white-label-v1.md).

---

## Фаза 5 — готово

MCP, primary=personal, scope-map, при необходимости public/group read-only.

---

## Поведение агента

1. Playbook + `templates/newcomer/README.md`.
2. Опрос → только оставшиеся фазы.
3. **Не** подставлять в инструкции чужой org slug (например из примеров в исторических ADR) — спросить `{ORG_SLUG}` или пути пользователя.
4. `memory_health` + `route_context`.

---

## Связанные документы

- `templates/README.md`, `map-kb-three-contours-v1.md`, `playbook-org-kb-white-label-v1.md`, `adr/016-*`
