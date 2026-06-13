# `templates/worlds/` — триада мира и hub

Экземпляры в **`knowledge/worlds/<slug>/`**. Порядок загрузки (роутер): **status → playbook → kb**. При симптомах/инцидентах: **`troubleshooting/`** — [`template-world-troubleshooting-readme-v1.md`](template-world-troubleshooting-readme-v1.md); индекс — [`../../META/index-troubleshooting-v1.md`](../../META/index-troubleshooting-v1.md).

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

**Перед коммитом (обязательно):** экземпляр **любого** `worlds/<slug>/` попадает в **kb-public** — пройти [`playbook-kb-world-public-authoring-v1.md`](../worlds/knowledge-engineering/playbook-kb-world-public-authoring-v1.md) (без scope, `work/`, внутренних брендов, машинных путей). Правило на все миры, не только knowledge.engineering. Operational clone/диск — только в `work/projects/`.

Верхний индекс: [`../README.md`](../README.md).