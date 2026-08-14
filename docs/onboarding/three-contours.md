# Карта: три контура KB

**Версия:** v1.0 · **2026-05-19**

Снять трение «что в каком репо и куда писать». Одна страница для **агента** и для **человека** (approve).

**Полный текст:** [map-kb-three-contours-v1.md](../knowledge/domains/agent-operations/map-kb-three-contours-v1.md) · **Свой org:** [Подключить-свой-org-KB-white-label](white-label.md)

*Пример инстанса: `AI-Guiders` — не обязателен для читателя.*

См. также: [Протоколы-и-сущности](protocols.md) · [Память-и-KB-как-устроено](../guide/memory-and-kb.md) · [PUBLISHING.md](../knowledge/PUBLISHING.md)

---

## Контуры (не путать)

| # | Контур | Где | MCP / chmod | Кто пишет |
|---|--------|-----|-------------|-----------|
| **1** | **Канон** (личный) | репозиторий держателя (`agent-notes` / fork) | `primary` / **u** | владелец канона |
| **2a** | **Group KB** | **`{ORG_SLUG}/kb`** (private) | `knowledge_root_id=group` / **g** | PR + org-maintainer |
| **2b** | **Public KB** | **`{ORG_SLUG}/kb-public`** | read-only / **o** | canon-maintainer → `build-public-kb.ps1` |
| **3** | **Workspace** | корень IDE, product repos | код, hot-зеркало | код в product repos; знания — в **1** |

**Не четвёртый контур:** `knowledge/work/` и `knowledge/personal/` — **внутри канона (1)**; в kb-public **не попадают** по дизайну.

```text
[Workspace]  copy/sync     [Канон — personal]
     │                           │ git
     └──────► agent-notes.md ◄───┘
                    │ export (sanitize)
                    ▼
             [{ORG_SLUG}/kb — group KB]
                    │ build-public-kb.ps1
                    ▼
                [{ORG_SLUG}/kb-public]
```

---

## Куда что класть (шпаргалка)

| Содержание | Контур | Действие |
|------------|--------|----------|
| Playbook, роутер, META, worlds | **1** | `knowledge/...` в каноне |
| L0, секции hot | **1** | `agent-notes.md` (выше `<!-- public-cut -->` может уйти в публичное) |
| Карточка проекта, operational | **1**, слой work | только в **полном** каноне (не в kb-public) |
| Черновик «только мне» | **1**, personal | не публикуется |
| C#, тесты, UI | **3** | product repo |
| Правка из чата в Cursor | **1** | обновить канон; workspace-hot — зеркало |
| Показать миру обезличенную KB | **2b** | сборка из **1** → push kb-public |

---

## Sync: workspace hot ↔ канон

- **Правда** — контур **1** (git канона).
- Hot в workspace (`.cascade-ide/agent-notes.md` и т.п.) — рабочая поверхность MCP; после существенных правок — **в канон** и commit.
- Агент не считает workspace-файл каноном, если `AGENT_NOTES_CANON_PATH` указывает на клон канона.

---

## MCP: несколько корней

| Параметр | Смысл |
|----------|--------|
| `knowledge_root_id=group` | чтение из **AI-Guiders/kb** (read-only в MCP) |
| `primary` | запись только в личный/основной канон |
| `route_context` | overlay из hot + опционально preview group KB ([ADR 015](https://github.com/AI-Guiders/agent-notes-mcp/blob/main/docs/adr/015-multi-root-knowledge-roots-v1.md)) |

Подробнее: [ADR 012](../knowledge/adr/012-multi-canon-workspace-resolution-v1.md) · [Протоколы-и-сущности](protocols.md)

---

## Роли

| Действие | Агент | Человек |
|----------|-------|---------|
| «В каком контуре править» | ✅ по этой карте | approve при сомнении |
| Коммит в канон | подготовка | approve, commit |
| `build-public-kb`, push | preview, diff | **canon-maintainer** |
| Ослабление Integrity | ❌ | ❌ |

---

## Триггеры для агента

«в каком репо», «куда записать», «три репозитория», «kb-public vs agent-notes», «group KB», «синк заметок» → **сначала эта карта**, затем узкий playbook.
