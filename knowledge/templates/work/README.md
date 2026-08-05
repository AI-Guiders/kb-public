# `templates/work/` — операционный слой (`work/`)
**Tags:** #readme #templates


Экземпляры живут в **`knowledge/work/projects/`** (не в kb-public). Шаблоны **публикуются** в kb-public как каркасы.

**Норма work-слоя:** общие каркасы — здесь (`templates/work/`, `templates/meta/`, …); **только для одного `project-id`** (runbook-скелет, capture, релизный чеклист) — опционально **`work/projects/<scope>/<project-id>/templates/`**. Канон процедуры: `worlds/workspace-context/playbook-multi-project-context-v1.md` §6c п.5.

| Файл | Куда копировать |
|------|-----------------|
| `template-project-card-v1.md` | `work/projects/<scope>/<project-id>/README.md` |
| `template-checklist-new-track-v1.md` | вставка в хаб scope или отдельный чеклист |
| `template-scope-contour-map-v1.md` | `knowledge/work/org/scope-contour-map-v1.md` (экземпляр в `work/org/` → group KB; механика в kb-public) |
| `template-product-troubleshooting-v1.md` | `work/projects/<scope>/<project-id>/playbook-*-troubleshooting-v1.md` · реестр [`work/troubleshooting/README.md`](../../work/troubleshooting/README.md) |

Протокол scope: `worlds/workspace-context/playbook-multi-project-context-v1.md` §6c.  
Соглашение полей: `work/projects/README.md`.

Верхний индекс: [`../README.md`](../README.md).
| `template-taskknowledge-analytics.md` | analytics после ADR → Parts/Facts/Gaps/DAG (экземпляр в work store / scratch, не в канон как ADR) |
| `template-taskknowledge-task.md` | узел TaskKnowledge / findings task card (поля + зачем; criterion) |

EnvInvariant: [`domains/agent-operations/note-taskknowledge-flow.md`](../../domains/agent-operations/note-taskknowledge-flow.md).
| `template-taskknowledge-workspace-layout.md` | каркас `{workspace}/.task-knowledge/` |
