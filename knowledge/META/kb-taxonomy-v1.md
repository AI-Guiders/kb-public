# KB taxonomy v1 (канонический описатель)

**Статус:** Accepted · 2026-05-11 (v1 таксономии под [ADR 009](../adr/009-kb-entry-structure-and-pre-open-onboarding.md)). Примеры миров: **cognition.human-perception**, **aviation.human-factors**, **psychology.models**, **medicine.evidence**, **hci.ux-dx**, **software.engineering-evidence**, **software.automation-scripting**, **collaboration.git-pr**, **systems.it**, **knowledge.engineering**, **ops** (host / network / observability / reliability), **agent.orchestration**, **workspace.context**, **information.management**, **evidence.humanities-shelf** — каталоги под `worlds/<…>/`; **полный список** — [`worlds/README.md`](../worlds/README.md). Роутеры — в корне `knowledge/`.  
**Не путать с роутером:** машинный контракт загрузки остаётся в `index-knowledge-router-v1.md` и supplement; этот файл — **человеческая карта корней** и соглашений «куда класть новое».

---

## Зачем один файл

Имена папок `worlds/`, `domains/`, `templates/` сами по себе не объясняют смысл. Здесь зафиксированы определения, отличия от `work/`, `META/`, корневых `playbook-*` / `kb-*`, и куда смотреть первым делом: **`../00-entry-kb-v1.md`**.

---

## Определения

| Корень | Назначение |
|--------|------------|
| **`worlds/`** | Крупные контексты («вселенные»): продуктовые стеки, исследовательские миры, длинные дуги. Примеры: `worlds/cognition-human-perception/` (статус, playbooks и kb этого мира внутри папки); `worlds/arts-music/` (мир **arts.music**); `worlds/software-engineering-evidence/` (**software.engineering-evidence**); `worlds/software-automation-scripting/` (**software.automation-scripting**). Не смешивать со **scope** в `active_scope` / `work/projects/<scope>/` — это оперативные карточки workspace, не мир KB. |
| **`domains/`** | Сквозные темы (безопасность, инструменты, процессы, …) — по мере появления контента; v1 может быть пустым кроме README. **Имя корзины не финально** — см. **`domains/README.md`**. |
| **`templates/`** | Реюзабельные **шаблоны** (каркасы карточек, чеклисты). Экземпляры после копирования живут в согласованном месте (часто `work/projects/...`), не редактируются как «живые» внутри `templates/`. |
| **`work/`** | Оперативный слой: карточки проектов, локальные runbook’и, то, что **не** входит в kb-public (`public-kb.ignore`). |
| **`META/`** | Well-known спеки, integrity, provenance; корень доверия. |
| **`adr/`** | ADR оглавление и записи решений. |
| **Корень `knowledge/*.md`** | Легаси и намеренно плоские артефакты (роутер, playbooks, kb-*): **не обязаны** немигрировать в корзины; миграция — инкрементально с обновлением ссылок и роутера ([009](../adr/009-kb-entry-structure-and-pre-open-onboarding.md) §9–10). |

---

## Роутеры vs «indexes»

Файлы `index-knowledge-router-*.md` пока остаются в **корне** `knowledge/` (легаси-путь). Отдельная папка **`routers/`** — только если явно перенесём роутер и обновим все вызовы MCP/примеры ([009](../adr/009-kb-entry-structure-and-pre-open-onboarding.md) §11–13). Папку **`indexes/`** не вводим как синоним роутера; при необходимости позже — только под человеческие каталоги (ToC).

---

## Полнотекст (опционально)

Локальный FTS по Markdown **не** часть канона в Git: опциональный MCP **Hybrid Codebase Index**, артефакты под `.hybrid-codebase-index/` вне коммитов. Политика: [ADR 010](../adr/010-kb-markdown-fts-index-boundary.md); пошагово: `work/projects/door-to-singularity/agent-notes-kb/kb-hci-optional-fts-runbook-v1.md`.

---

## Таблица «корень → роль» (снимок v1)

| Путь | Роль |
|------|------|
| `SHOWCASE.md` | Быстрый обзор без full load |
| `00-entry-kb-v1.md` | Тонкий вход: ссылки по осям |
| `index-knowledge-router-v1.md` | Машинный маршрутизатор |
| `META/integrity-core.md` | Корень доверия |
| `work/` | Оперативка, не kb-public |
| `personal/` | Личный контур, не kb-public |
| `worlds/`, `domains/`, `templates/` | Корзины по этому файлу |

---

## Правило для нового материала

1. Если это **карточка проекта / трек** — `work/projects/<scope>/…` ([003](../adr/003-multi-project-scope-and-project-cards.md)).  
2. Если это **мир / длинный контур** — по мере зрелости `worlds/<slug>/…`.  
3. Если это **сквозная тема** — `domains/<slug>/…` когда появится согласованный slug.  
4. Если это **шаблон** — `templates/` и ссылка отсюда в таблицу ниже при стабилизации имени.

**Шаблоны (v1):** **`templates/template-knowledge-card-v1.md`** — каноническая карточка KB (в т.ч. evidence-слой `kb-*-evidence-v1`); **`templates/template-domain-note-v1.md`** — минимальный каркас заметки под домен.
