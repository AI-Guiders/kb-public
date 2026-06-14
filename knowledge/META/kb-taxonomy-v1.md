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
| **`worlds/`** | Крупные контексты («вселенные»): продуктовые стеки, исследовательские миры, длинные дуги. Внутри мира: `status-*`, `playbook-*`, `kb-*`; **`troubleshooting/`** — симптомы и чеклисты (контур A, kb-public). Индекс: [`META/index-troubleshooting-v1.md`](index-troubleshooting-v1.md). Не смешивать со **scope** в `work/projects/<scope>/` (контур B). |
| **`domains/`** | Сквозные темы (безопасность, инструменты, процессы, …). **v1:** [`domains/agent-operations/`](../domains/agent-operations/) — операционные контракты агента (`playbook-project-switch`, `playbook-mode-switch`, multi-agent write, integrity под давлением). **Имя корзины не финально** для других slug — см. **`domains/README.md`**. |
| **`templates/`** | Реюзабельные **шаблоны** (каркасы). Подкаталоги: `cards/`, `worlds/`, `work/`, `matrices/`, `meta/`, `newcomer/` — [`templates/README.md`](../templates/README.md). Экземпляры живут в `work/projects/…`, `worlds/…`, `adr/…` и т.д., не в `templates/`. |
| **`work/`** | Оперативный слой: карточки проектов, локальные runbook’и; **весь product troubleshooting** — `work/projects/<id>/playbook-*-troubleshooting-v1.md`, реестр [`work/troubleshooting/README.md`](work/troubleshooting/README.md) (контур B, не kb-public). Сквозная диагностика стека — `worlds/<world>/troubleshooting/` (контур A). Сводка: [`META/index-troubleshooting-v1.md`](index-troubleshooting-v1.md). |
| **`temp/`** | Scratch **external WM** агента (workaround harness): не канон, не kb-public. [`temp/README.md`](../temp/README.md). |
| **`META/`** | Well-known спеки, integrity, provenance; корень доверия. |
| **`adr/`** | ADR оглавление и записи решений. |
| **Корень `knowledge/*.md`** | Легаси и намеренно плоские артефакты (роутер, playbooks, kb-*): **не обязаны** немигрировать в корзины; миграция — инкрементально с обновлением ссылок и роутера ([009](../adr/009-kb-entry-structure-and-pre-open-onboarding.md) §9–10). |

---

## Роутеры vs «indexes»

Файлы `index-knowledge-router-*.md` пока остаются в **корне** `knowledge/` (легаси-путь). Отдельная папка **`routers/`** — только если явно перенесём роутер и обновим все вызовы MCP/примеры ([009](../adr/009-kb-entry-structure-and-pre-open-onboarding.md) §11–13). Папку **`indexes/`** не вводим как синоним роутера; при необходимости позже — только под человеческие каталоги (ToC).

---

## Полнотекст (опционально)

Локальный FTS по Markdown **не** часть канона в Git: опциональный MCP **Hybrid Codebase Index**, артефакты под `.hybrid-codebase-index/` вне коммитов. Политика: [ADR 010](../adr/010-kb-markdown-fts-index-boundary.md); пошагово: `work/projects/door-to-singularity/agent-notes-kb/templates/kb-hci-optional-fts-runbook-v1.md`.

---

## Таблица «корень → роль» (снимок v1)

| Путь | Роль |
|------|------|
| `SHOWCASE.md` | Быстрый обзор без full load |
| `00-entry-kb-v1.md` | Тонкий вход: ссылки по осям |
| `index-knowledge-router-v1.md` | Машинный маршрутизатор |
| `META/integrity-core.md` | Корень доверия |
| `work/` | Оперативка, не kb-public |
| `temp/` | Scratch агента (external WM), не kb-public |
| `personal/` | Личный контур, не kb-public |
| `worlds/`, `domains/`, `templates/` | Корзины по этому файлу |

---

## Правило для нового материала

1. Если это **карточка проекта / трек** — `work/projects/<scope>/…` ([003](../adr/003-multi-project-scope-and-project-cards.md)).  
2. Если это **мир / длинный контур** — по мере зрелости `worlds/<slug>/…`.  
3. Если это **сквозная тема** — `domains/<slug>/…` когда появится согласованный slug.  
4. Если это **шаблон** — подкаталог `templates/<kind>/` (не корень `templates/`). Полный индекс — § `taxonomy-templates-v13` ниже и [`templates/README.md`](../templates/README.md).

