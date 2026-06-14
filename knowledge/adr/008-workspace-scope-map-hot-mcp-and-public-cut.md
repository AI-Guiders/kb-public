# ADR 008: Карта workspace → scope (hot), публичная сборка и резолв в agent-notes-mcp

**Статус:** Accepted (части A и B)  
**Дата:** 2026-05-12  
**Источник в истории:** обсуждение публикации kb-public, вынесение машинных путей из hot, паттерн «scope map отдельным файлом» (Codex).  
**Supersedes:** —  
**Extended by:** [013](013-agent-notes-mcp-local-settings-toml-v1.md) (часть C: `[workspace].scope_map` / `scope_aliases` в TOML вместо `mcp-resolve-paths-v1.json`)  
**Связано:** [003](003-multi-project-scope-and-project-cards.md), [001](001-kb-public-publishing-pipeline.md)

---

## Контекст

1. **Публикация kb-public.** `agent-notes.md` участвует в сборке **до первого** маркера `<!-- public-cut -->` ([ADR 001](001-kb-public-publishing-pipeline.md)). Пока карта `workspace_path` → `active_scope` жила в секции **`workspace-scope-map-v1`** выше cut, **локальные пути к дискам** утекали в публичное зеркало вместе с остальным hot.

2. **Стабильность сопровождения.** Редактирование карты путей в одном огромном `agent-notes.md` даёт лишние конфликты merge и смешивает **протокол** (общий) с **инсталляцией** (частная машина). Внешняя практика (в т.ч. предложения Codex): вынести карту в **отдельный локальный файл**.

3. **MCP.** `agent-notes-mcp` резолвит `active_scope` для `read_hot_context`, `route_context`, `memory_health` по цепочке: явный параметр → содержимое файла карты по пути из **`workspace_scope_map`** (диск: **`knowledge/META/mcp-resolve-paths-v1.json`** при наличии; иначе **embedded** `mcp-resolve-paths-defaults.json` в сборке AgentNotes.Core) **иначе** секции карты в распарсенном hot (`workspace-scope-map-v1`, legacy `scope-map-v1`) → опционально поле `current:` в секции `active-scope` (легаси) → встроенный fallback в коде. Алиасы scope — файл по **`scope_alias_map`** из того же контура (диск → embedded → резерв в коде).

---

## Решение — часть A (принято)

### KB (канон)

- **Первый `<!-- public-cut -->`** в `agent-notes.md` размещается **до** секции **`workspace-scope-map-v1`** и всего операционного хвоста с машинными путями (`scope-*` с дисками, полный **`project-switch-protocol-v1`** и т.д.). В kb-public остаётся компактный **L0 / baseline** без путей.
- **Жизненный цикл `scope`** (когда заводить slice, где хранить карту, публикация) описан в **`knowledge/worlds/workspace-context/playbook-multi-project-context-v1.md` §6c** и связан с [ADR 003](003-multi-project-scope-and-project-cards.md).
- **Публичная механика** для потребителей без полного hot: **`knowledge/kb-one-pager-structure-and-protocols-v1.md`**, роутер указывает на плейбук.

### agent-notes-mcp

- Резолв `active_scope`: явный аргумент → файл карты по **`workspace_scope_map`** (переопределение в **`knowledge/META/mcp-resolve-paths-v1.json`**, иначе пути из **embedded** `mcp-resolve-paths-defaults.json`) → секции hot → `active-scope` (`current:`) → fallback в коде. Алиасы — файл по **`scope_alias_map`** из того же контура.
- Документировать контракт цепочки резолва в ADR и в `docs/` MCP (см. зеркальный файл в репо `agent-notes-mcp`), чтобы правки не «ломали молча» ожидания.

---

## Решение — часть B (принято)

### Вынести карту в отдельный файл

- **Путь под канон (не в kb-public):** `knowledge/work/local/workspace-scope-map-v1.md` (см. `knowledge/work/local/README.md`).
- **MCP:** при наличии файла — читать его **в приоритете** над секциями `workspace-scope-map-v1` / `scope-map-v1` в hot; формат строк тот же (`path => scope`). Секция в hot — указатель для `compact_order_suffix` и человека.
- **Плюсы:** меньше конфликтов на `agent-notes.md`; карту можно не коммитить (gitignore) или коммитить как у автора канона.

Итог части B: реализовано в `NotesStorage.cs` + юнит-тест `MemoryHealth_UsesWorkspaceScopeMapFromWorkLocal_WhenCanonEnvSet`.

---

## Решение — часть C (принято, legacy): bootstrap путей MCP

> **Эволюция:** при **`--config`** (KB [013](013-agent-notes-mcp-local-settings-toml-v1.md)) пути к карте и алиасам — ключи **`workspace.scope_map`** / **`workspace.scope_aliases`** в TOML; META JSON **не используется**. Ниже — **исторический** контракт.

- **Файл:** `knowledge/META/mcp-resolve-paths-v1.json` — JSON с относительными путями внутри `knowledge/`: **`workspace_scope_map`**, **`scope_alias_map`**.
- **Дефолты в сборке:** embedded `mcp-resolve-paths-defaults.json` в AgentNotes.Core.

Итог части C (legacy): `McpResolvePathsDefaults` + `NotesStorage.ReadMcpResolvePathsOrDefaults`.

---

## Последствия

**Плюсы (A)**

- kb-public не содержит машинных путей из hot.
- Протоколы и карта жизненного цикла scope остаются в **versioned** `knowledge/*.md`.

**Минусы (A)**

- В публичном `agent-notes.md` нет полного `project-switch-protocol-v1`; потребители kb-public опираются на плейбук и one-pager.
- `route_context` по **публичному** срезу `agent-notes` видит укороченный hot — при работе только с kb-public без полного канона явный **`active_scope`** важнее.

**Плюсы (B), если сделать**

- Чёткое разделение «протокол / инсталляция»; проще per-machine карты.

**Минусы (B)**

- Доп. код и тесты в MCP; документация для операторов (где лежит файл).

**Плюсы (C)**

- Перенос карт в другую ветку `knowledge/` (например при таксономии `worlds/` / `domains/`) без правки и пересборки MCP — только JSON и сами файлы.

**Минусы (C)**

- Ещё один артефакт под каноном; при ошибке в JSON тихий откат к дефолтам (диагностировать по «не тем» scope).

---

## План внедрения (часть B) — выполнено

1. Имя пути и приоритет: `knowledge/work/local/workspace-scope-map-v1.md`, файл приоритетнее секций hot.
2. Реализация в `agent-notes-mcp` (`NotesStorage`), юнит-тест.
3. При изменении контракта — обновить `agent-notes-mcp/README.md`, `docs/MCP-TOOLS.md`, манифест.
4. В каноне: указатель в hot + пример файла в `work/local/`.

---

## Примечание об эволюции

Часть A закрывает утечку путей в kb-public без смены контракта MCP. Часть B — файл карты workspace с приоритетом в MCP; при его отсутствии по-прежнему используются секции **`workspace-scope-map-v1`** / **`scope-map-v1`** в полном `agent-notes.md` ниже `public-cut`. Часть C — опциональный **`knowledge/META/mcp-resolve-paths-v1.json`**: переопределение относительных путей к файлам карты и алиасов без смены кода MCP.

