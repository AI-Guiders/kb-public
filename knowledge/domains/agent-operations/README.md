# Domain: agent-operations
**Tags:** #agent-operations #domains #readme


Сквозные **операционные контракты агента** (маркеры чата, целостность, параллельные записи в заметки). Не путать с:

- **`META/`** — well-known POST, `integrity-core`, спеки доверия;
- **`worlds/workspace-context/`** — мультипроектный контур, карточки, runbook'и (длинный плейбук);
- **`worlds/agent-orchestration/`** — капитан, параллельные агенты, метрики ускорения.

Имена файлов: **`playbook-*-v1.md`** (`rename-plan.md`). **`section_id`** в `agent-notes.md` сохраняются; stub указывает сюда.

| Артефакт | Назначение |
|----------|------------|
| [map-kb-three-contours-v1.md](map-kb-three-contours-v1.md) | **Канон · group · kb-public · workspace** — плейсхолдер `{ORG_SLUG}` |
| [playbook-knowledge-stack-clean-setup-v1.md](playbook-knowledge-stack-clean-setup-v1.md) | Участник: kb-public → personal + MCP |
| [playbook-org-kb-white-label-v1.md](playbook-org-kb-white-label-v1.md) | Основатель org: `{ORG_SLUG}/kb` + kb-public |

| Playbook | `section_id` в hot |
|----------|-------------------|
| [playbook-project-switch-v1.md](playbook-project-switch-v1.md) | `project-switch-protocol-v1` |
| [playbook-mode-switch-v1.md](playbook-mode-switch-v1.md) | `mode-switch-protocol` |
| [playbook-multi-agent-write-v1.md](playbook-multi-agent-write-v1.md) | `multi-agent-write-protocol-v1` |
| [playbook-integrity-under-pressure-v1.md](playbook-integrity-under-pressure-v1.md) | `integrity-under-pressure-protocol` |
| [playbook-agent-partnership-kb-v1.md](playbook-agent-partnership-kb-v1.md) | *(см. файл — культура ADR, не промпт-роль)* |
| [playbook-review-as-conversation-v1.md](playbook-review-as-conversation-v1.md) | `review-as-conversation-v1` (L0), `review-as-conversation-extended-v1` |
| [playbook-context-pressure-checkpoint-v1.md](playbook-context-pressure-checkpoint-v1.md) | Pressure signals (L0–L2); см. [`playbook-session-summary-and-chat-export-v1.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export-v1.md) |
| [playbook-cursor-chat-threading-v1.md](playbook-cursor-chat-threading-v1.md) | Cursor: epic / spike / meta, fork vs один тред, brief; дополняет context-pressure (CIDE topics → handoff) |
| [playbook-agent-knowledge-responsibility-v1.md](playbook-agent-knowledge-responsibility-v1.md) | Ответственность за KB |
| [playbook-proactive-micro-improvements-v1.md](playbook-proactive-micro-improvements-v1.md) | `proactive-micro-improvements-and-intuition-v1` |
| [playbook-fuzzy-search-implicit-language-v1.md](playbook-fuzzy-search-implicit-language-v1.md) | `fuzzy-search-and-implicit-language-v1` |
| [playbook-utility-judgment-underdetermination-v1.md](playbook-utility-judgment-underdetermination-v1.md) | Полезность недоопределена |
| [playbook-principled-clarity-v1.md](playbook-principled-clarity-v1.md) | `principled-clarity-v1` |
| [playbook-strict-execution-when-analogy-v1.md](playbook-strict-execution-when-analogy-v1.md) | `strict-execution-when-analogy-v1` |
| [playbook-agent-process-debt-amplifier-v1.md](playbook-agent-process-debt-amplifier-v1.md) | Merge/teach/placement: агент усиливает process debt; checklist + ADR-0083 postmortem |
| [playbook-agent-data-tiers-v1.md](playbook-agent-data-tiers-v1.md) | T0–T3 data classification; local LLM vs vast; redaction; CIDE/forge continuity |
| [playbook-rf-llm-cloudru-foundation-models-v1.md](playbook-rf-llm-cloudru-foundation-models-v1.md) | РФ: Cloud.ru FM + Roo Code / CIDE; рубли без KZ/Stripe; внутр. vs внешн. модели |
| [playbook-cide-harness-parity-vs-cursor-v1.md](playbook-cide-harness-parity-vs-cursor-v1.md) | CIDE+FM vs Cursor: parity matrix, automation-first checklist |
| [playbook-kb-topic-hashtags-v1.md](playbook-kb-topic-hashtags-v1.md) | Тематические `#tags` + роль (`#ssot` / `#research`); seed registry |
| [playbook-agent-driven-context-management-v1.md](playbook-agent-driven-context-management-v1.md) | ADCM: harness signals, agent tactics; не silent compact |
| [note-lira-meeting-who-v1.md](note-lira-meeting-who-v1.md) | Голос агента: встреча «кто» vs инструмент (Лира, 2026-06) |

**Hub:** [`agent-memory-and-operating-principles-v1.md`](../../agent-memory-and-operating-principles-v1.md) — маршрутизатор, не дубль тел.

**Product (CascadeIDE):** [cascade-ide/playbook-agent-execution-environment-v1.md](../work/projects/door-to-singularity/cascade-ide/playbook-agent-execution-environment-v1.md) — AEE, verify ladder; SSOT — ADR 0148 в репо IDE. `knowledge/kb-protocols-and-entities-one-pager-v1.md`, `knowledge/kb-one-pager-structure-and-protocols-v1.md`.

