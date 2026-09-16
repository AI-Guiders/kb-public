# CASE / software workbench — reading map v1
**Tags:** #software-case-workbench #map #worlds #case #reading

**Назначение:** маршрут чтения — фундамент CASE-волны, соседи (KBSA, IPSE), уроки провала, что читать перед продуктовыми решениями Guiders.

**Порядок:** Track A (определения) → B (классика) → C (провалы) → D (современные кузены) → E (наш перенос).

---

## Track A — Определения и обзоры

| Источник | Зачем |
|----------|--------|
| Wikipedia — *Computer-aided software engineering* | Быстрый словарь upper/lower/I-CASE |
| Sommerville — *Software Engineering* (главы про design methods, legacy editions) | Учебный контекст волны 90s |
| IEEE *Software* обзоры CASE era (1990s) | Тон индустрии до agile |

---

## Track B — Классические работы (must-know)

| Работа | Год | Суть |
|--------|-----|------|
| **Kruchten** — *The 4+1 View Model of Architecture* | 1995 | Multi-view: logical, development, process, physical + scenarios |
| **Finkelstein & al.** — ICASE / framework papers | 1980s–90s | Интегрированная среда как продуктовая мечта |
| **Taylor et al.** — *Foundations for the Arcadia Environment Architecture* | 1988 | Process + OMS + tools — родитель IPSE-линии |
| **Brown & McDermid** — *Learning From IPSE's Mistakes* | 1992 | Framework tax; toolsets beat mega-environment |
| **Rumbaugh / Booch / Jacobson** → **UML** (OMG) | 1997+ | Унификация нотации; не унификация truth |
| **OMG MDA Guide** | 2003 | PIM/PSM — CASE 2.0; критически |
| **Green et al.** — KBSA report | 1983 | Assistant + repository (ветвь A historiography) |

---

## Track C — Почему спало (обязательно)

| Тема | Где искать |
|------|------------|
| Model–code drift | Postmortems agile transition; practitioner blogs; *Facts and Fallacies of Software Engineering* (Glass) |
| Ceremony / BDUF backlash | Agile Manifesto; Fowler on design dead |
| Rationale capture tax | Moran & Carroll — *Design Rationale*; gIBIS/Compendium adoption studies |
| Repository vs git | IPSE mistakes; Rose DB anecdotes |

**Локальный digest:** [`note-cognitive-se-environments-historiography.md`](../../../work/projects/door-to-singularity/cascade-ide/note-cognitive-se-environments-historiography.md)

---

## Track D — Современные кузены (ориентир, не канон)

| Полка | Примеры | Что взять | Чего нет |
|-------|---------|-----------|----------|
| **ALM** | Jira+links, Azure DevOps, Polarion | Traceability habit | Live estate graph |
| **EA tools** | Sparx EA, ArchiMate | Portfolio view | Daily dev pair |
| **Agentic IDE** | Cursor, Copilot | Speed | Decision environment |
| **ADE** | Intent-centric orchestration | Goal→worktrees | Epistemic model |
| **Code graph** | Sourcegraph-class, dep tools | Structure query | Briefing before release |

---

## Track E — Перенос в Guiders

После Track B–C читать:

- [`matrix-case-to-guiders-transfer.md`](matrix-case-to-guiders-transfer.md)
- Platform [ADR-0023](https://github.com/AI-Guiders/guiders-platform/blob/main/docs/adr/GUIDERS-ADR-0023-case-workbench-heritage.md)
- [PLATFORM-FLEET-THESIS](https://github.com/AI-Guiders/guiders-platform/blob/main/docs/PLATFORM-FLEET-THESIS.md) §3.1, §6

---

## Ingestion protocol

На каждый источник: одна **операционная** выжимка → строка в matrix transfer; не копировать главы в KB.

## Progress marker (v1)

- Track A: baseline stub.
- Track B: **Kruchten + Brown + MDA evidence cards** ✅
- Track C: linked to historiography + Brown card.
- Track D: shelf map only.
- Track E: matrix v1 written.

