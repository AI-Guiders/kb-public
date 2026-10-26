---
type: Index
title: '`templates/worlds/` — триада мира и hub'
description: 'Экземпляры в **`knowledge/worlds/<slug>/`**. Порядок загрузки (роутер): **status → playbook → kb**. При симптомах/инцидентах: **`troubleshooting/`** — [`template-world-troubleshooting-readme.md`](template-world-troubleshooting-readme.md); индекс — [`../../META/index-troubleshooting.md`](../../META/index-troubleshooting.md).'
tags: [readme, templates]
language: ru
world: README.md
---
# `templates/worlds/` — триада мира и hub


Экземпляры в **`knowledge/worlds/<slug>/`**. Порядок загрузки (роутер): **status → playbook → kb**. При симптомах/инцидентах: **`troubleshooting/`** — [`template-world-troubleshooting-readme.md`](template-world-troubleshooting-readme.md); индекс — [`../../META/index-troubleshooting.md`](../../META/index-troubleshooting.md).

| Шаблон | Имя экземпляра |
|--------|----------------|
| `template-world-readme.md` | `worlds/<slug>/README.md` |
| `template-status.md` | `status-<domain>.md` |
| `template-playbook.md` | `playbook-<topic>.md` |
| `template-playbook-operational.md` | `playbook-<topic>-operational.md` |
| `template-kb-fundamentals.md` | `kb-<topic>-fundamentals.md` |
| `template-kb-chapter-map.md` | `kb-<source>-chapter-map.md` |

Evidence-карточки книг/источников: [`../cards/template-kb-evidence.md`](../cards/template-kb-evidence.md).  
Transfer matrix: [`../matrices/template-transfer-matrix.md`](../matrices/template-transfer-matrix.md).

**Перед коммитом (обязательно):** экземпляр **любого** `worlds/<slug>/` попадает в **kb-public** — пройти [`playbook-kb-world-public-authoring.md`](../worlds/knowledge-engineering/playbook-kb-world-public-authoring.md) (без scope, `work/`, внутренних брендов, машинных путей). Правило на все миры, не только knowledge.engineering. Operational clone/диск — только в `work/projects/`.

Верхний индекс: [`../README.md`](../README.md).

