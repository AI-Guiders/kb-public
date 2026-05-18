# `knowledge/templates/` — шаблоны (каркасы для копирования)

Не живые экземпляры под один workspace. Контракт корзины: **`../META/kb-taxonomy-v1.md`**.

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
| Новый мир / домен | `worlds/template-world-readme-v1.md` + status → playbook → kb |
| Книга / курс (оглавление) | `worlds/template-kb-chapter-map-v1.md` |
| Evidence по источнику | `cards/template-kb-evidence-v1.md` |
| Cross-domain routing | `matrices/template-transfer-matrix-v1.md` |
| Трек в IDE | `work/template-project-card-v1.md` |
| ADR | `meta/template-adr-v1.md` |
| Схема контуров / маршрутизация | `meta/template-map-v1.md` |
| Процедура со скриптами | `meta/template-runbook-v1.md` |
| Секция в `agent-notes.md` | `meta/template-hot-section-v1.md` или `newcomer/` |
| Свой org KB (CONTRIBUTING, CODEOWNERS) | `newcomer/template-org-kb-bootstrap-*` + `playbook-org-kb-white-label-v1.md` |

## Легаси-пути (после v1.2)

Старые ссылки `templates/template-knowledge-card-v1.md` → **`templates/cards/template-knowledge-card-v1.md`** (или `template-kb-evidence-v1.md` для evidence).