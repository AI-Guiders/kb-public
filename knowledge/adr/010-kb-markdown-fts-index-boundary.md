# ADR 010: Полнотекстовый индекс по Markdown KB — границы и опциональный внешний MCP

**Статус:** Proposed  
**Дата:** 2026-05-12  
**Источник в истории:** запрос на поиск по канону «как в CIDE» (SQLite FTS5 ± vec); риск смешения **ANKB** (канон, роутер, MCP чтения) с **отдельным инструментом индексации** без явного решения.  
**Supersedes:** —  
**Extended by:** —  
**Связано:** [009](009-kb-entry-structure-and-pre-open-onboarding.md) (вход и таксономия «перед открытием»), [001](001-kb-public-publishing-pipeline.md) (kb-public, границы контуров), [004](004-router-supplement-and-l1-pool.md) (роутер KB). Технический референс стека FTS+vec в продуктовом контуре CascadeIDE — **вне KB-канона:** [ADR 0105](https://github.com/KarataevDmitry/cascade-ide/blob/main/docs/adr/0105-hybrid-codebase-index-for-csharp-web.md) (*Accepted · Implemented*).

---

## Контекст

1. **KB (agent-notes)** уже имеет **семантическую навигацию**: `index-knowledge-router-v1.md`, supplement, `route_context`, `read_knowledge_file`, L0 в `agent-notes.md`. Это **источник истины** по тому, *что* и в каком порядке читать, а не полнотекстовый поиск по всему дереву.

2. **Полнотекстовый индекс** (FTS по чанкам Markdown) полезен как **дополнение**: «где встречается формулировка», быстрый топ‑N перед точечным чтением. Он **не обязан** быть частью **agent-notes-mcp** и не обязан дублировать роутер.

3. В экосистеме уже есть **отдельный MCP** «Hybrid Codebase Index» (HCI): локальный SQLite FTS5, опционально vec, отдельный процесс ([описание в репозитории HCI](https://github.com/KarataevDmitry/hybrid-codebase-index), формальное решение — ADR 0105 в CascadeIDE). Путаница возникает, если считать HCI **частью ANKB** без явной границы.

4. **Публикация kb-public** ([001](001-kb-public-publishing-pipeline.md)) и **личный / work-слой** остаются политикой содержимого; индекс **не меняет** правила «что в архив», но при индексации локального полного клона нужно явно решать, индексировать ли `knowledge/work/**` и `knowledge/personal/**` (по умолчанию для «публично-ориентированного» поиска — **нет**).

---

## Решение

1. **Индекс по Markdown KB — опциональное расширение** потребителя среды (IDE, агент с несколькими MCP), а не обязательный компонент канона. **Канон и MCP чтения KB** остаются самодостаточными без индекса.

2. **Рекомендуемая реализация v1 (без кода в agent-notes-core):** использовать **внешний** MCP HCI с `workspace_path` = корень клона канона; сужение области — через профиль **`<repo>/.hybrid-codebase-index/settings.toml`** (например только `*.md`, исключение сегментов пути `personal`, `work`, `.revisions`, `dist`). Пошаговый runbook для канона — в карточке **agent-notes-kb** под `knowledge/work/` ([`kb-hci-optional-fts-runbook-v1.md`](../work/projects/door-to-singularity/agent-notes-kb/templates/kb-hci-optional-fts-runbook-v1.md)); пример `settings.toml` дублируется там (приложение А) и в репозитории HCI (`examples/settings.agent-notes-kb.toml`) для удобства сборки MCP. Содержимое runbook **не** в kb-public.

3. **Не делаем в рамках этого ADR** (явные non-goals, пока не принят отдельный ADR):
   - встраивание SQLite / sqlite-vec **внутрь** `AgentNotes.Core` / `agent-notes-mcp` как обязательную зависимость;
   - замена `route_context` / индекса роутера результатами FTS;
   - требование «каждый потребитель KB обязан поднять HCI».

4. **Связь с [009](009-kb-entry-structure-and-pre-open-onboarding.md):** entry, таксономия и «с чего начать» остаются **человеко-ориентированным** слоем; FTS — **машинный вспомогательный** слой. В файле таксономии (когда появится) можно одной строкой указать: «полнотекст — опционально, см. ADR 010».

5. **Артефакты индекса** (каталог `.hybrid-codebase-index/` с SQLite) **не являются** частью канона: их держим **вне git** (`.gitignore` в корне репо канона) либо локально без коммита.

---

## Последствия

**Плюсы**

- Ясная граница: ANKB ≠ HCI; меньше архитектурных недопониманий в чатах и в onboarding.
- Можно включать FTS там, где есть Cursor/MCP и диск, не трогая релизы agent-notes-mcp.
- Сохраняется единый технический референс по FTS/vec (ADR 0105) без дублирования спеки в KB.

**Минусы / риски**

- Два «мира правды» для автора: runbook в `work/.../agent-notes-kb`, пример настроек и README MCP — в HCI; смягчается одной строкой в таксономии ([009](009-kb-entry-structure-and-pre-open-onboarding.md)) при необходимости.
- Без дисциплины `.gitignore` легко случайно закоммитить SQLite.

---

## План внедрения (минимальный)

1. Принять ADR (смена статуса на Accepted) или оставить Proposed до первой реальной инструкции в карточке проекта.
2. В корне **agent-notes** (или зеркала): `.gitignore` → `.hybrid-codebase-index/` (отдельный коммит «chore», не смешивать с контентом KB).
3. В карточке **agent-notes-kb** уже есть ссылка на runbook и ADR 010; при желании — одна строка в таксономии ([009](009-kb-entry-structure-and-pre-open-onboarding.md)).
4. Если позже решат **встроенный** индекс в MCP — новый ADR с мотивацией, рисками и миграцией; этот ADR не запрещает, но **не** требует встраивания.
