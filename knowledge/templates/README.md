---
type: Index
title: '`knowledge/templates/` — шаблоны (каркасы для копирования)'
description: 'Не живые экземпляры под один workspace. Контракт корзины: **`../META/kb-taxonomy.md`**.'
tags: [readme, templates]
---
# `knowledge/templates/` — шаблоны (каркасы для копирования)


Не живые экземпляры под один workspace. Контракт корзины: **`../META/kb-taxonomy.md`**.

## Подкаталоги

| Папка | Содержимое |
|-------|------------|
| **[`cards/`](cards/README.md)** | KB-карточки, **evidence** (`kb-*-evidence-v1`), domain-заметки |
| **[`worlds/`](worlds/README.md)** | Триада мира: status, playbook, kb-fundamentals, chapter-map, hub README |
| **[`work/`](work/README.md)** | Project card, чеклист нового трека (`work/projects/`) |
| **[`matrices/`](matrices/README.md)** | Transfer / routing матрицы (`matrix-*-v1`) |
| **[`meta/`](meta/README.md)** | ADR, map, runbook, hot-секция, универсальный checklist |
| **[`newcomer/`](newcomer/README.md)** | Чистая установка: ANM + kb-public → personal (в kb-public) |

Новые шаблоны — в подкаталог по смыслу, **не** в корень `templates/`.

## Быстрый выбор

| Задача | Шаблон |
|--------|--------|
| Новый мир / домен | `worlds/template-world-readme.md` + status → playbook → kb |
| Книга / курс (оглавление) | `worlds/template-kb-chapter-map.md` |
| Evidence по источнику | `cards/template-kb-evidence.md` |
| Cross-domain routing | `matrices/template-transfer-matrix.md` |
| Трек в IDE | `work/template-project-card.md` |
| ADR | `meta/template-adr.md` |
| Схема контуров / маршрутизация | `meta/template-map.md` |
| Процедура со скриптами | `meta/template-runbook.md` |
| Секция в `agent-notes.md` | `meta/template-hot-section.md` или `newcomer/` |
| Свой org KB (CONTRIBUTING, CODEOWNERS) | `newcomer/template-org-kb-bootstrap-*` + `playbook-org-kb-white-label.md` |

## Легаси-пути (после v1.2)

Старые ссылки `templates/template-knowledge-card.md` → **`templates/cards/template-knowledge-card.md`** (или `template-kb-evidence.md` для evidence).

