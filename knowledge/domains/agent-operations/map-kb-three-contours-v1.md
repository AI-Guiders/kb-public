# Map: три контура KB (канон · публичное · workspace)

**Назначение:** снять когнитивное трение «что в каком репо и куда писать». Одна страница для **агента** (диспетчер) и для **человека** (approve). Не заменяет `PUBLISHING.md`, `kb-one-pager-structure-and-protocols-v1.md`, `playbook-kb-operational-freshness-v1.md` — **сводит** их в схему действий.

**Статус:** active · v1.1 · 2026-05-19  
**Именование репозиториев:** ниже **`{ORG_SLUG}/kb`** и **`{ORG_SLUG}/kb-public`** — плейсхолдеры вашей GitHub-организации. Пример инстанса: `AI-Guiders/kb` (не обязателен для читателя kb-public).

**Поднять свой org:** [`playbook-org-kb-white-label-v1.md`](playbook-org-kb-white-label-v1.md).

---

## Контуры (не путать; group KB — между personal и public)

| # | Контур | Где физически | MCP / chmod | Кто обычно пишет |
|---|--------|---------------|-------------|------------------|
| **1** | **Канон** (user) | личный **`agent-notes`** (или fork) | primary / **u** | Держатель канона; git `main` |
| **2a** | **Group KB** | **`{ORG_SLUG}/kb`** private | `knowledge_root_id=group` / **g** | PR + **org-maintainer** review |
| **2b** | **Public KB** | **`{ORG_SLUG}/kb-public`** | `public` / **o** | **Canon-maintainer** — `build-public-kb.ps1` |
| **3** | **Workspace** | корни IDE, product repos | код, hot-зеркало | Код в product repos; знания — в **1** |

**Не четвёртый контур:** `knowledge/work/` и `knowledge/personal/` — **внутри канона (1)**; в kb-public **не попадают** по дизайну.

```text
[Workspace]     copy/sync              [Канон personal — agent-notes]
     │              work/local/maps          │  git commit + push
     └──────────────► agent-notes.md ◄───────┘
                           │ export (sanitize)
                           ▼
                    [{ORG_SLUG}/kb — group KB]
                           │ build-public-kb.ps1
                           ▼
                    [{ORG_SLUG}/kb-public]
```

---

## Куда что класть (шпаргалка)

| Содержание | Контур | Путь / действие |
|------------|--------|-----------------|
| Playbook, kb, роутер, META, worlds | **1 Канон** | `knowledge/...` в personal |
| L0, stub секций, `public-cut` | **1 Канон** | `agent-notes.md` (выше cut → может уйти в public) |
| Карточка проекта, operational | **1**, слой work | `knowledge/work/projects/...` (не в kb-public) |
| Черновик «только мне» | **1**, personal | `knowledge/personal/...` |
| C#, решение, тесты | **3 Workspace** | product repo |
| Правка знаний из чата | **1** | обновить канон; workspace-hot — зеркало |
| Показать миру обезличенную KB | **2b** | сборка из **1**, push kb-public |

---

## Sync: workspace hot ↔ канон

- **Правда** — контур **1** (git personal).
- Hot в workspace — зеркало; после правок — в канон и commit.
- Агент не считает workspace-файл каноном, если `AGENT_NOTES_CANON_PATH` указывает на клон personal.

---

## Роли: агент vs человек

| Действие | Агент | Человек |
|----------|-------|---------|
| «В каком контуре править» | ✅ по этой карте | approve |
| `build-public-kb`, push kb-public | preview | **canon-maintainer** |
| PR в group KB | подготовка diff | **org-maintainer** |

---

## Быстрые ссылки (kb-public)

| Вопрос | Файл |
|--------|------|
| Что в kb-public | `knowledge/PUBLISHING.md` |
| Слои L0–L3 | `knowledge/kb-one-pager-structure-and-protocols-v1.md` |
| Свой org с нуля | `knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md` |
| Участник: personal + MCP | `knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md` |
| Маркеры PRIMARY/SCOPE | `knowledge/domains/agent-operations/playbook-project-switch-v1.md` |

---

## Триггер для роутера / агента

«в каком репо», «куда записать», «три репозитория», «kb-public vs agent-notes», «свой org KB», «white-label», «синк заметок» → **сначала этот файл**, затем узкий playbook.
