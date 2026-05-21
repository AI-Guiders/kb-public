# ADR 012: Multi-canon resolution (личный + org) и workspace-конфиг MCP

**Статус:** Proposed  
**Дата:** 2026-05-15  
**Источник в истории:** один Cursor-workspace (`PersonalCursorFolder`) и много кодовых проектов; появление org-kb ([011](011-aiguiders-org-collaborative-kb-repo-v1.md)); риск дублировать org-знания в личном каноне через `knowledge/organization/`; обсуждение расширения agent-notes-mcp.  
**Supersedes:** —  
**Extended by:** [013](013-agent-notes-mcp-local-settings-toml-v1.md) (схема TOML, слияние, вывод env)  
**Связано:** [003](003-multi-project-scope-and-project-cards.md), [008](008-workspace-scope-map-hot-mcp-and-public-cut.md), [011](011-aiguiders-org-collaborative-kb-repo-v1.md), [001](001-kb-public-publishing-pipeline.md)

---

## Контекст

### 1. Один workspace — много проектов

Держатель канона часто открывает **один** корневой workspace (monorepo / umbrella), а `active_scope` и карта путей выбирают **кодовый** контекст ([003](003-multi-project-scope-and-project-cards.md), [008](008-workspace-scope-map-hot-mcp-and-public-cut.md)):

- `workspace_path` в MCP = корень **того** workspace, который передал Cursor;
- `work/local/workspace-scope-map-v1.md` (личный канон) сопоставляет **абсолютные пути** к подпроектам → `door-to-singularity` | `portal` | `harvester` | …;
- hot / `route_context` / `memory_health` читают **один** `agent-notes.md` (primary canon).

Это уже решает «сижу в одном воркспейсе — работаю с разными проектами» **без** смены KB.

### 2. Org-kb и «инфа только в орге»

Когда появится живой **`AI-Guiders/kb`** ([011](011-aiguiders-org-collaborative-kb-repo-v1.md)), часть playbook/kb будет **принята в org** раньше, чем попадёт в **личный** канон владельца (или никогда — если личное не дублирует всё org).

**Плохой обход:** завести в личном каноне `knowledge/organization/` (или `work/organization/`) и копировать туда org-файлы.

| Почему криво |
|--------------|
| Два SSOT на один текст → drift, лишние merge. |
| Смешение **коллаборативного** (org PR) и **личного** (спринт, пути, `personal/`). |
| Публикация kb-public / public-cut не про «organization/» в личном дереве. |
| Агент не отличит «устаревшая копия в личном» от «актуально в org». |

**Правильная ось:** org-kb — **отдельный git-корень**; личный канон — **primary для записи и операционки**; org — **secondary для чтения** (и явного `canon_path` в тулах).

### 3. Что MCP умеет сегодня

- **Один primary** на процесс: `AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` → `GetNotesPath`, `read_hot_context`, `route_context`, `memory_health`, запись в `agent-notes.md`.
- **`read_knowledge_file` / `write_knowledge_file` / …** — опциональный аргумент **`canon_path`** → другой корень с `knowledge/`.
- Карта workspace → scope **всегда** из primary (файл под личным каноном), не из org-kb ([008](008-workspace-scope-map-hot-mcp-and-public-cut.md)).

---

## Решение (принципы)

### P1. Роли канонов

| Роль | Репо | Запись через MCP | Hot / L0 | Карта workspace |
|------|------|------------------|----------|-----------------|
| **primary** | личный `agent-notes` | да (`upsert_*`, `append_*`, …) | да | да (только primary) |
| **secondary** (0..n) | org-kb, при необходимости kb-public | **нет** по умолчанию | **не** сливать в один hot | нет |
| **public** | kb-public | нет | только для потребителей без org | нет |

### P2. Не дублировать org в личное дерево

- **Не** вводить `knowledge/organization/` как зону копирования org-kb.
- В личном hot допустимы **тонкие указатели** (1–2 секции): где org SSOT, как клонировать, политика import — не полнотекстовые копии playbook.
- Принятие org → личный: **import workflow** (cherry-pick / скрипт / ручной merge в `knowledge/worlds/…`), осознанно, с review владельца.

### P3. Один workspace — два измерения

```text
workspace_path (Cursor)
    │
    ├─► active_scope     ← workspace-scope-map (primary / личный канон)
    │
    └─► primary canon    ← agent-notes.md + hot (личный)
            │
            └─► secondary[]  ← только чтение knowledge/ + опционально route overlay
```

### P4. Не склеивать два hot в один `read_hot_context`

Слияние L0 из личного и org в один JSON:

- размывает бюджет и `memory_health`;
- риск утечки `l0_owner` / `current-task` при ошибке конфига;
- непонятно, куда писать `upsert_agent_notes_section`.

**Исключение (будущее, отдельная фаза):** явный whitelist секций org для **read-only overlay** (например только `integrity-core` / `l0_manifest` stub), только если нет в primary — **не** в scope первой реализации.

### P5. Как агент видит «только в org»

| Механизм | Когда |
|----------|--------|
| `read_knowledge_file(file_path=…, canon_path=<org>)` | точечно, уже сейчас |
| `route_context` по primary | как сейчас |
| **`route_context` + secondary** (фаза 2) | поиск по индексу/секциям org-kb, блоки с меткой `canon: org` |
| Правило в playbook / Cursor rule | «если тема org — сначала read org path …» |

---

## Workspace-конфиг (TOML по явному пути)

Семантика **primary / read-only** knowledge roots — в этом ADR ([P1–P5](#решение-принципы)); в тексте ниже ещё **«canon»** = то же (исторический термин). **Подключение:** с **agent-notes-mcp 2.0** — TOML по **`--config`** — **[013](013-agent-notes-mcp-local-settings-toml-v1.md)** (`[knowledge]`, major MCP).

### Пример (шаблон содержимого)

См. [`knowledge/work/local/agent-notes.workspace.example.toml`](../work/local/agent-notes.workspace.example.toml) — копируешь куда удобно (напр. `D:/Experiments/agent-notes-mcp.local.toml`) и указываешь путь в `args`.

### Цепочка резолва primary (целевая)

1. Аргумент тула `canon_path` (если есть).
2. TOML из **`--config`** / `AGENT_NOTES_CONFIG` — [013](013-agent-notes-mcp-local-settings-toml-v1.md).
3. `AGENT_NOTES_CANON_PATH` / `AGENT_NOTES_FILE` (legacy).
4. Fallback: `workspace_path/.cascade-ide/agent-notes.md`.

`scope_map` **всегда** из **primary** knowledge root, даже если в workspace открыт клон org-kb — отдельный профиль (редко).

---

## Альтернативы (отклонены)

| Вариант | Почему нет |
|---------|------------|
| `knowledge/organization/` в личном каноне | дублирование SSOT ([P2](#p2-не-дублировать-org-в-личное-дерево)) |
| Три MCP-сервера в Cursor без workspace-файла | работает, но не привязано к umbrella-workspace; дублирует env |
| Один hot = merge personal + org | [P4](#p4-не-склеивать-два-hot-в-один-read_hot_context) |
| Org-kb содержит `work/local` с путями владельца | запрещено политикой [011](011-aiguiders-org-collaborative-kb-repo-v1.md) |

---

## Последствия

**Плюсы**

- Monorepo + много проектов остаётся на [008](008-workspace-scope-map-hot-mcp-and-public-cut.md).
- Org--only контент доступен без копипасты в личное дерево.
- Друг / участник org: `primary = org` в **своём** workspace или только env — без личного канона.

**Минусы**

- Две фазы внедрения (спека → код в Core).
- Агент должен **знать**, что искать в secondary (playbook + опционально route overlay).

**Риски**

- Забытый `canon_path` → агент отвечает только из личного; mitigation: `route_overlay`, правила Cursor, health-check «secondary configured but unused».

---

## План внедрения

| Фаза | Содержание | Статус |
|------|------------|--------|
| **0** | Документ + example toml; правило: org не копировать в `organization/` | этот ADR |
| **1** | Ручной режим: env primary + `read_knowledge_file(canon_path=org)` | сейчас |
| **2** | Core: чтение `.cursor/agent-notes.toml`, `ResolveCanonPath(workspace)` | код |
| **3** | `route_context`: опциональный поиск по `secondary[]` с метками и лимитом chars | код |
| **4** | (опционально) read-only L0 overlay whitelist | только при сценарии |

Зависимости: [011](011-aiguiders-org-collaborative-kb-repo-v1.md) (репо `AI-Guiders/kb`) для реального secondary; до этого secondary может указывать на клон `kb-public`.

---

## Открытые вопросы

1. Имя файла: `.cursor/agent-notes.toml` vs `.cascade/agent-notes.toml` — зафиксировать одно; поддержать второе как alias?
2. Walk-up: один umbrella на весь `PersonalCursorFolder` vs per-subproject toml в `Financial/software/open/…`?
3. Нужен ли `route_overlay` по умолчанию `true`, когда `org` path существует на диске?

---

## Ссылки

- Пример workspace-конфига: `knowledge/work/local/agent-notes.workspace.example.toml`
- Runbook wiki / org: `knowledge/work/projects/door-to-singularity/ai-guiders/templates/runbook-gitlab-wiki-to-github-ai-guiders-v1.md` (контуры kb-public / handbook)
