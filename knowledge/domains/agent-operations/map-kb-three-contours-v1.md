# Map: три контура KB (канон · публичное · workspace)

**Назначение:** снять когнитивное трение «что в каком репо и куда писать». Одна страница для **агента** (диспетчер) и для **человека** (approve). Не заменяет `PUBLISHING.md`, `kb-one-pager-structure-and-protocols-v1.md`, `playbook-kb-operational-freshness-v1.md` — **сводит** их в схему действий.

**Статус:** active · v1.0 · 2026-05-16  
**Идея KBMC (PWA):** отложена; пока достаточно этой карты + агент по протоколам ниже. Карточка: `knowledge/work/projects/door-to-singularity/kb-management-center/README.md`.

---

## Три контура (не путать)

| # | Контур | Где физически | Источник правды | Кто обычно пишет |
|---|--------|---------------|-----------------|------------------|
| **1** | **Канон KB** | Репозиторий **agent-notes** (`knowledge/`, корневой `agent-notes.md`, `scripts/`) | **Git `main` канона** | Человек approve; агент готовит diff/коммит **по запросу** |
| **2** | **Публичный срез** | Зеркало **kb-public** / org-kb (артефакт сборки) | Вывод `build-public-kb.ps1` из канона | Только **после** сборки и явного push; агент — preview/diff, не «тихий» push |
| **3** | **Workspace** | PersonalCursorFolder (и др. корни IDE) | Код продуктов, `.cascade-ide/agent-notes.md`, локальные карты | Код — в product repos; hot-зеркало — **копия** канона (см. §Sync) |

**Не четвёртый контур:** `knowledge/work/` и `knowledge/personal/` — **внутри канона (1)**, в kb-public **не попадают** по дизайну.

```text
[Workspace]     copy/sync (команда)     [Канон agent-notes]
     │                                    │
     │  MCP read/write hot               │  git commit + push
     └──────────────► agent-notes.md ◄───┘
                           │
                    build-public-kb.ps1
                           ▼
                    [kb-public / org mirror]
```

---

## Куда что класть (шпаргалка)

| Содержание | Контур | Путь / действие |
|------------|--------|-----------------|
| Playbook, kb, роутер, META, worlds | **1 Канон** | `knowledge/...` в agent-notes |
| L0, stub секций, `public-cut` | **1 Канон** | `agent-notes.md` (выше cut = может уйти в публичное) |
| Карточка проекта, пути к диску, operational спринт | **1 Канон**, слой work | `knowledge/work/projects/<scope>/...` |
| Черновик «только мне» | **1 Канон**, personal | `knowledge/personal/...` (не в kb-public) |
| C#, решение, тесты | **3 Workspace** | product repo (cascade-ide, …) |
| Правка знаний из чата в Cursor | **1** (не только 3) | обновить канон; workspace-hot — зеркало |
| Показать миру обезличенную KB | **2** | собрать из **1**, push kb-public |

**Правило смешивания:** не переносить `work/` и пути workspace в текст, который должен быть **выше `public-cut`**, без ревью.

---

## Sync: workspace hot ↔ канон

- **Правда** — всегда **контур 1** (git agent-notes).
- **`.cascade-ide/agent-notes.md`** (или копия в workspace) — рабочая поверхность MCP в IDE; после существенных правок — **скопировать в канон** и `git commit` + `push` (напоминание часто в operational-памяти трека `agent-notes-kb`).
- Агент **не считает** workspace-файл каноном, если `AGENT_NOTES_CANON_PATH` указывает на клон agent-notes.

---

## Устарело / перепроверить (без отдельного UI)

| Шаг | Кто | Что |
|-----|-----|-----|
| 1 | Агент | Открыть `playbook-kb-operational-freshness-v1.md` по триггеру «устарело / Проверено / deprecated» |
| 2 | Агент | Доменный `status-*` § Maintenance Policy → только нужные файлы из §5 реестра |
| 3 | Агент | Отчёт: список кандидатов + источник правды + **предлагаемая** правка |
| 4 | Человек | Approve → коммит в **контур 1**; при необходимости сборка **контур 2** |

Опционально позже: скрипт `stale-scan` (отчёт в markdown/JSON) — тот же смысл, что дашборд KBMC.

---

## Роли: агент-диспетчер vs человек

| Действие | Агент | Человек |
|----------|-------|---------|
| Навигация «в каком контуре править» | ✅ по этой карте | approve при сомнении |
| `read_knowledge_file` / `route_context` | ✅ | — |
| Правка `knowledge/` и коммит в канон | подготовка | **approve**, commit |
| `build-public-kb`, push kb-public | preview, diff, команды | **approve** push |
| Решение «публикуем / не публикуем» строку | предложение | **финал** |
| Ослабление Integrity / POST | ❌ | ❌ |

Маркеры чата: `playbook-project-switch-v1.md`, `playbook-mode-switch-v1.md` — какой **scope** и режим WORK/HUMAN.

---

## Быстрые ссылки

| Вопрос | Файл |
|--------|------|
| Что в kb-public, public-cut | `knowledge/PUBLISHING.md` |
| Слои L0–L3, обзор | `knowledge/kb-one-pager-structure-and-protocols-v1.md` |
| Свежесть любого kb | `knowledge/worlds/knowledge-engineering/playbook-kb-operational-freshness-v1.md` |
| Сопровождение репо канона | `knowledge/work/projects/door-to-singularity/agent-notes-kb/README.md` |
| Пуш kb-public (ops) | `knowledge/work/projects/door-to-singularity/agent-notes-kb/publishing-ops-internal-v1.md` |
| Маркеры PRIMARY/SCOPE | `knowledge/domains/agent-operations/playbook-project-switch-v1.md` |

---

## Триггер для роутера / агента

Фразы пользователя: «в каком репо», «куда записать», «три репозитория», «kb-public vs agent-notes», «забыл куда класть», «синк заметок» → **сначала этот файл**, затем узкий playbook по задаче.
