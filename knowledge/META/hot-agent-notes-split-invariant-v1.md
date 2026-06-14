# Hot split invariant v1

**Статус:** active  
**Дата:** 2026-05-16

## Правило

`agent-notes.md` — **индекс + L0**, не склад тел.

1. **L0** — только контракты выше `<!-- public-cut -->`; список в `memory-architecture-v1.json` (`l0`).
2. **Тело > ~2.5k символов** или **кластер ≥5 связанных секций** — перенос в `knowledge/` (worlds / work/projects / META), в hot — **stub** с тем же `section_id`.
3. **Оперативка проекта** — `knowledge/work/projects/<scope>/<project-id>/`, не глобальный sprint в каноне.
4. **Пути к диску** — `knowledge/work/local/`, не в hot и не в kb-public.
5. **Один `section_id`** — одна секция в `agent-notes.md` (дубликаты перетирают друг друга в MCP).

## Corpus-файлы (тела секций, снимок 2026-05-16)

Имена по контракту `rename-plan.md` (`map-` / `playbook-` / `digest-`), не `agent-notes-*-hot-sections`.

| Файл | Секции |
|------|--------|
| `worlds/world-life/map-world-life-subworlds-v1.md` | `world-*` |
| `worlds/world-life/playbook-world-life-modeling-toolchain-v1.md` | modeling, N-Why, ontology |
| `worlds/systems-it/digest-systems-it-reference-corpus-v1.md` | `it-*` |
| `worlds/knowledge-engineering/playbook-epistemic-methods-and-calibration-v1.md` | epistemic, calibration, hpmor |
| `worlds/knowledge-engineering/playbook-kb-canonical-publication-v1.md` | kb-canonical, trust roadmap |
| `domains/agent-operations/playbook-*.md` | project/mode switch, multi-agent write, integrity |
| `worlds/agent-orchestration/playbook-agent-orchestration-operations-v1.md` | acceleration, auto-rotation |
| `META/memory-architecture-layered-extended-v1.md` | L0–L3 описание |
| `worlds/workspace-context/*-extended-v1.md` | response checklist (и др.) |

Политика: секция `memory-large-sections-policy-v1` в `agent-notes.md`.

