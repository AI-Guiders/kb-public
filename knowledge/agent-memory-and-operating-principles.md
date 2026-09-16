# Agent: память и операционные принципы — hub
**Tags:** #kb-root


**Роль:** **маршрутизатор**, не сводный пересказ. Тела правил — в playbooks ниже; L0-контракты — в `agent-notes.md`; дожим ответа — в `worlds/workspace-context/`.

При вопросе «как агент работает с памятью / пользователем» — **сначала этот hub**, затем **один** целевой файл по строке таблицы, не весь канон.

---

## Карта (SSOT)

| Тема | Куда грузить |
|------|----------------|
| **Ответственность за KB** | [`domains/agent-operations/playbook-agent-knowledge-responsibility.md`](domains/agent-operations/playbook-agent-knowledge-responsibility.md) |
| **External memory (workaround harness)** | [`domains/agent-operations/playbook-external-memory-workaround.md`](domains/agent-operations/playbook-external-memory-workaround.md) · scratch: [`temp/README.md`](temp/README.md) |
| **Партнёрство по ADR (культура, не слои KB)** | [`domains/agent-operations/playbook-agent-partnership-kb.md`](domains/agent-operations/playbook-agent-partnership-kb.md) |
| **Execution Gate (L1 в hot)** | `execution-gate-v1` в agent-notes → reconnaissance / autonomy playbooks ниже |
| **Проактивные микро-улучшения** | [`domains/agent-operations/playbook-proactive-micro-improvements.md`](domains/agent-operations/playbook-proactive-micro-improvements.md) |
| **Идея из чата / «Кстати…» в ходе** | [`work/projects/door-to-singularity/door-to-singularity/note-product-idea-from-chat.md`](work/projects/door-to-singularity/door-to-singularity/note-product-idea-from-chat.md) |
| **Нечёткий поиск / неявный язык** | [`domains/agent-operations/playbook-fuzzy-search-implicit-language.md`](domains/agent-operations/playbook-fuzzy-search-implicit-language.md) |
| **Роутер, baseline, safety, multi-project** | [`index-knowledge-router.md`](index-knowledge-router.md), [`router-operational-baseline.md`](router-operational-baseline.md), [`index-knowledge-router-safety.md`](index-knowledge-router-safety.md), [`worlds/workspace-context/playbook-multi-project-context.md`](worlds/workspace-context/playbook-multi-project-context.md) |
| **Код: нормы, рефакторинг** | [`worlds/software-authoring/code-writing-principles.md`](worlds/software-authoring/code-writing-principles.md) |
| **IOP / экосистема** | [IOP-манifest](https://github.com/AI-Guiders/cascade-ide/blob/develop/docs/iop-manifest-v1.md), [`SHOWCASE.md`](SHOWCASE.md) |
| **Автономия, внешний мир** | [`worlds/agent-orchestration/playbook-agent-autonomy-and-routing.md`](worlds/agent-orchestration/playbook-agent-autonomy-and-routing.md) |
| **Пауза / разведка (anti-hurry)** | [`worlds/agent-orchestration/playbook-agent-reconnaissance-before-action.md`](worlds/agent-orchestration/playbook-agent-reconnaissance-before-action.md) |
| **Свежесть канона** | [`worlds/knowledge-engineering/playbook-kb-operational-freshness.md`](worlds/knowledge-engineering/playbook-kb-operational-freshness.md) |
| **Дожми шаг / две оси commit** | [`worlds/workspace-context/response-one-step-checklist-extended.md`](worlds/workspace-context/response-one-step-checklist-extended.md) |
| **Финализатор + вычитка** | [`worlds/workspace-context/response-finalizer-extended.md`](worlds/workspace-context/response-finalizer-extended.md) |
| **Полезность недоопределена** | [`domains/agent-operations/playbook-utility-judgment-underdetermination.md`](domains/agent-operations/playbook-utility-judgment-underdetermination.md) |
| **Принципиальная ясность** | [`domains/agent-operations/playbook-principled-clarity.md`](domains/agent-operations/playbook-principled-clarity.md) |
| **Just Culture / Blame Culture (habitat)** | [`domains/agent-operations/playbook-habitat-just-culture.md`](domains/agent-operations/playbook-habitat-just-culture.md) · axiom §8 in [`META/environment-axioms.md`](META/environment-axioms.md) |
| **Incident investigation (habitat formal)** | [`domains/agent-operations/playbook-habitat-incident-investigation.md`](domains/agent-operations/playbook-habitat-incident-investigation.md) · 7 steps · template · P0/P1 gates |
| **Правки KB только через MCP** | [`worlds/knowledge-engineering/runbook-kb-mcp-access.md`](worlds/knowledge-engineering/runbook-kb-mcp-access.md) §6–7 |
| **Строгое выполнение по образцу** | [`domains/agent-operations/playbook-strict-execution-when-analogy.md`](domains/agent-operations/playbook-strict-execution-when-analogy.md) |
| **Длинная сессия, итоги, экспорт** | [`worlds/agent-orchestration/playbook-session-summary-and-chat-export.md`](worlds/agent-orchestration/playbook-session-summary-and-chat-export.md) |
| **Pressure / checkpoint** | [`domains/agent-operations/playbook-context-pressure-checkpoint.md`](domains/agent-operations/playbook-context-pressure-checkpoint.md) |
| **Стоп / заземление (post-train urgency ≠ оператор)** | [`domains/agent-operations/playbook-agent-pause-ground-continue.md`](domains/agent-operations/playbook-agent-pause-ground-continue.md) |
| **Целостность, эпистемия (baseline)** | [`baseline-integrity-epistemic-extended.md`](baseline-integrity-epistemic-extended.md) — **не** смешивать с этим hub |

---

## Maintenance

- Новый принцип **того же класса** → **playbook** в `domains/agent-operations/` или `worlds/agent-orchestration/`; сюда — **одна строка** в таблице.
- **Не** раздувать hub телом; дубли с `agent-notes.md` — убирать в пользу SSOT playbook.
- Роутер: одна ссылка на этот файл в `index-knowledge-router.md` / supplement.

**История hub:** 2026-06-12 — рефакторинг: монолит ~186 строк → маршрутизатор; тела в playbooks и extended-файлах. 2026-06-12 — cleanup: partnership vs responsibility, execution-gate иерархия. 2026-06-14 — external memory workaround (playbook + строка в карте).

