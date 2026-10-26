---
type: Note
title: dsh-plugin-primary-hints — подсказки маркеров [PRIMARY:]/[SCOPE:]
description: '**Статус:** прототип работает (2026-09-20) · **Место:** `D:\dsh-plugin-primary-hints` (установлен в профиль web: bundles + link)'
language: ru
sections: [toml-path-fix]
---
# dsh-plugin-primary-hints — подсказки маркеров [PRIMARY:]/[SCOPE:]

**Статус:** прототип работает (2026-09-20) · **Место:** `D:\dsh-plugin-primary-hints` (установлен в профиль web: bundles + link)
**Назначение:** при вводе `[` в composer GUI — нативное меню (режимы PRIMARY/SCOPE/HUMAN/WORK → проекты/подпроекты → вставка канона `[PRIMARY:<id>]`).

## Архитектура

- **Host half** (`lib/index.js`): маршрут `/primary-hints` — живой индекс из **типизированных реестров KB** (таблицы `project-ids-quickref.md` + `subprojects-catalog.md`; markdown pipe-tables, НЕ regex по карточкам). Парсится свежим на каждый запрос. `AGENT_NOTES_CANON_PATH` может указывать на корень KB или `knowledge/` — резолвится.
- **Client half** (`lib/client.js`): регистрирует `registerTriggerChar('[', detectBracket)` + `inputTriggers.registerSource({ trigger: '[', name: 'primary-hints', ... })` — нативный пикер, вставка через pipeline (`{ text }` outcome → Lexical-safe).

## ПАТЧ ЯДРА (форк AI-Guiders/deepseek-harness, НЕ ЗАКОММИЧЕН!)

`packages/client/ui-input-trigger` — рефактор: `TriggerChar = string` (был `'/' | '@'`), per-char детекторы (`detectAt`, `detectSlash`, `combineDetectors`), `registerTriggerChar()` в сервисе, controller через `roster.detectors()`. Файлы: `src/types.ts`, `src/core/contract.ts`, `src/core/detect.ts`, `src/client/service.ts`, `src/client/controller.ts` + пересобран `lib/`. Upstream (deepseek-ai master, npm alpha.2) — тот же хардкод, т.е. это локальная доработка форка.

## Проверка

- Headless E2E: `node D:\dsh-plugin-primary-hints\test-gui.mjs` (минт cookie из `~/.dsh/.credentials.yaml`, playwright 1.61.1 в pnpm-store чекаута, chromium-1243) — меню, фильтр, вставка — зелёные.
- Индекс: 83 записи (quickref ~45 + каталог ~38); `guiders-federation` FED, `code-center-v1` FED/CC — добавлены в `subprojects-catalog.md`.

## Правило (важное)

Подсказки показывают ТОЛЬКО то, что есть в типизированных реестрах (quickref + каталог). Новый трек = запись в реестр, и он появится в подсказках. Group-проекты вне каталога (bogdb, witdb) не показываются.

## Слои KB (обновление)

- Индекс учитывает **personal** (`D:\Experiments\agent-notes` → quickref + subprojects-catalog) и **group** (клоны `ai-guiders/kb` → `aiguiders-open/door-to-singularity/project-ids-quickref-v1.md` + карточки с типовыми полями `**project-id:**`).
- Путь group — **конфиг плагина** в `~/.dsh/profiles/web/cordis.patch.yml` (`- id: dsh-plugin-primary-hints config: { groupKbPath: ... }`), не env. Хост читает `apply(ctx, config)`.
- Group-специфичные проекты (dash-spec-studio, dba-studio, hybrid-codebase-index и др.) в реестрах отсутствуют — источником служат их карточки (типовой формат). `guiders-declarative-stack` и `solutions-registry` — без README, в индекс не попадают.
- ⚠️ **Найдено:** `D:\agent-notes-mcp\agent-notes-mcp.toml` — `[[knowledge.read_only]] id=group path="D:/Experiments/PersonalCursorFolder/Financial/software/open/group-kb"` — путь УСТАРЕЛ (реальный: `D:\Experiments\Personal Cursor Folder\open\group-kb`). MCP group-слой, вероятно, не резолвится — требует правки оператором.
- Баг-фикс: ленивый `+?` в regex project-id давал однобуквенные мусорные id — заменён на greedy/backtick-first + plain fallback.

<!-- section:toml-path-fix -->
- ⚠️→✅ **Путь group в TOML был битым:** `agent-notes-mcp.toml` указывал `D:/Experiments/PersonalCursorFolder/Financial/software/open/group-kb`, но `Financial\software\open` не существует (там только IncomeCascade/OpenFigiClient/TInvestMcp). `PersonalCursorFolder` — junction на `Personal Cursor Folder` (без пробела резолвится). Исправлено на `D:/Experiments/PersonalCursorFolder/open/group-kb` (и comment для group-kb-clone). Тот же битый паттерн `Financial\software\open\python-debug-mcp` был в `~/.dsh/profiles/web/cordis.patch.yml` (cwd/PYTHONPATH) и в KB-копии — исправлены на `...\open\python-debug-mcp`; python-debug MCP-тулы не загружались из-за этого.
<!-- /section:toml-path-fix -->

## Форк (2026-09-20): закоммичено и запушено

- `58a0b977a2` — feat(client-ui-input-trigger): data-driven trigger-char registry (src + тесты, 6 файлов).
- `b30ae1a616` — refactor(client-ui-conversation): widen trigger char types to string (11 файлов; хардкод `'/' | '@'` в типах редактора/декораций/лексикона → string).
- Гейты: lint staged ✓, typecheck ✓ (tsc -b tsconfig.client.json), vitest ui-input-trigger+ui-conversation 563/563 ✓. `lib/` не коммитится (gitignore) — пересобирается `pnpm --filter @deepseek-ai/dsh-client-ui-input-trigger bundle`.

