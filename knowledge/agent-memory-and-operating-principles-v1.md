# Agent: память и операционные принципы — hub (v1)

**Роль:** **маршрутизатор**, не сводный пересказ. Тела правил — в playbooks ниже; L0-контракты — в `agent-notes.md`; дожим ответа — в `worlds/workspace-context/`.

При вопросе «как агент работает с памятью / пользователем» — **сначала этот hub**, затем **один** целевой файл по строке таблицы, не весь канон.

---

## Карта (SSOT)

| Тема | Куда грузить |
|------|----------------|
| **Ответственность за KB** | [`domains/agent-operations/playbook-agent-knowledge-responsibility-v1.md`](domains/agent-operations/playbook-agent-knowledge-responsibility-v1.md) |
| **Партнёрство по ADR (культура, не слои KB)** | [`domains/agent-operations/playbook-agent-partnership-kb-v1.md`](domains/agent-operations/playbook-agent-partnership-kb-v1.md) |
| **Execution Gate (L1 в hot)** | `execution-gate-v1` в agent-notes → reconnaissance / autonomy playbooks ниже |
| **Проактивные микро-улучшения** | [`domains/agent-operations/playbook-proactive-micro-improvements-v1.md`](domains/agent-operations/playbook-proactive-micro-improvements-v1.md) |
| **Нечёткий поиск / неявный язык** | [`domains/agent-operations/playbook-fuzzy-search-implicit-language-v1.md`](domains/agent-operations/playbook-fuzzy-search-implicit-language-v1.md) |
| **Роутер, baseline, safety, multi-project** | [`index-knowledge-router-v1.md`](index-knowledge-router-v1.md), [`router-operational-baseline-v1.md`](router-operational-baseline-v1.md), [`index-knowledge-router-safety-v1.md`](index-knowledge-router-safety-v1.md), [`worlds/workspace-context/playbook-multi-project-context-v1.md`](worlds/workspace-context/playbook-multi-project-context-v1.md) |
| **Код: нормы, рефакторинг** | [`worlds/software-authoring/code-writing-principles-v1.md`](worlds/software-authoring/code-writing-principles-v1.md) |
| **IOP / экосистема** | [IOP-манifest](https://github.com/AI-Guiders/cascade-ide/blob/develop/docs/iop-manifest-v1.md), [`SHOWCASE.md`](SHOWCASE.md) |
| **Автономия, внешний мир** | [`worlds/agent-orchestration/playbook-agent-autonomy-and-routing-v1.md`](worlds/agent-orchestration/playbook-agent-autonomy-and-routing-v1.md) |
| **Пауза / разведка (anti-hurry)** | [`worlds/agent-orchestration/playbook-agent-reconnaissance-before-action-v1.md`](worlds/agent-orchestration/playbook-agent-reconnaissance-before-action-v1.md) |
| **Свежесть канона** | [`worlds/knowledge-engineering/playbook-kb-operational-freshness-v1.md`](worlds/knowledge-engineering/playbook-kb-operational-freshness-v1.md) |
| **Дожми шаг / две оси commit** | [`worlds/workspace-context/response-one-step-checklist-extended-v1.md`](worlds/workspace-context/response-one-step-checklist-extended-v1.md) |
| **Финализатор + вычитка** | [`worlds/workspace-context/response-finalizer-extended-v1.md`](worlds/workspace-context/response-finalizer-extended-v1.md) |
| **Полезность недоопределена** | [`domains/agent-operations/playbook-utility-judgment-underdetermination-v1.md`](domains/agent-operations/playbook-utility-judgment-underdetermination-v1.md) |
| **Принципиальная ясность** | [`domains/agent-operations/playbook-principled-clarity-v1.md`](domains/agent-operations/playbook-principled-clarity-v1.md) |
| **Правки KB только через MCP** | [`worlds/knowledge-engineering/runbook-kb-mcp-access-v1.md`](worlds/knowledge-engineering/runbook-kb-mcp-access-v1.md) §6–7 |
| **Строгое выполнение по образцу** | [`domains/agent-operations/playbook-strict-execution-when-analogy-v1.md`](domains/agent-operations/playbook-strict-execution-when-analogy-v1.md) |
| **Длинная сессия, итоги, экспорт** | [`worlds/agent-orchestration/playbook-session-summary-and-chat-export-v1.md`](worlds/agent-orchestration/playbook-session-summary-and-chat-export-v1.md) |
| **Pressure / checkpoint** | [`domains/agent-operations/playbook-context-pressure-checkpoint-v1.md`](domains/agent-operations/playbook-context-pressure-checkpoint-v1.md) |
| **Целостность, эпистемия (baseline)** | [`baseline-integrity-epistemic-extended-v1.md`](baseline-integrity-epistemic-extended-v1.md) — **не** смешивать с этим hub |

---

## Maintenance

- Новый принцип **того же класса** → **playbook** в `domains/agent-operations/` или `worlds/agent-orchestration/`; сюда — **одна строка** в таблице.
- **Не** раздувать hub телом; дубли с `agent-notes.md` — убирать в пользу SSOT playbook.
- Роутер: одна ссылка на этот файл в `index-knowledge-router-v1.md` / supplement.

**История hub:** 2026-06-12 — рефакторинг: монолит ~186 строк → маршрутизатор; тела в playbooks и extended-файлах. 2026-06-12 — cleanup: partnership vs responsibility, execution-gate иерархия.
