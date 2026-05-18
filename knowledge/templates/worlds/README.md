# `templates/worlds/` — триада мира и hub

Экземпляры в **`knowledge/worlds/<slug>/`**. Порядок загрузки (роутер): **status → playbook → kb**.

| Шаблон | Имя экземпляра |
|--------|----------------|
| `template-world-readme-v1.md` | `worlds/<slug>/README.md` |
| `template-status-v1.md` | `status-<domain>-v1.md` |
| `template-playbook-v1.md` | `playbook-<topic>-v1.md` |
| `template-playbook-operational-v1.md` | `playbook-<topic>-operational-v1.md` |
| `template-kb-fundamentals-v1.md` | `kb-<topic>-fundamentals-v1.md` |
| `template-kb-chapter-map-v1.md` | `kb-<source>-chapter-map-v1.md` |

Evidence-карточки книг/источников: [`../cards/template-kb-evidence-v1.md`](../cards/template-kb-evidence-v1.md).  
Transfer matrix: [`../matrices/template-transfer-matrix-v1.md`](../matrices/template-transfer-matrix-v1.md).

Верхний индекс: [`../README.md`](../README.md).