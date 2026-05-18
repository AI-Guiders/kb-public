# `templates/work/` — операционный слой (`work/`)

Экземпляры живут в **`knowledge/work/projects/`** (не в kb-public). Шаблоны **публикуются** в kb-public как каркасы.

**Норма work-слоя:** общие каркасы — здесь (`templates/work/`, `templates/meta/`, …); **только для одного `project-id`** (runbook-скелет, capture, релизный чеклист) — опционально **`work/projects/<scope>/<project-id>/templates/`**. Канон процедуры: `worlds/workspace-context/playbook-multi-project-context-v1.md` §6c п.5.

| Файл | Куда копировать |
|------|-----------------|
| `template-project-card-v1.md` | `work/projects/<scope>/<project-id>/README.md` |
| `template-checklist-new-track-v1.md` | вставка в хаб scope или отдельный чеклист |

Протокол scope: `worlds/workspace-context/playbook-multi-project-context-v1.md` §6c.  
Соглашение полей: `work/projects/README.md`.

Верхний индекс: [`../README.md`](../README.md).