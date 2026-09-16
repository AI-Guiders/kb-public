# Domain: agent-operations
**Tags:** #agent-operations #domains #readme


Сквозные **операционные контракты агента** (маркеры чата, целостность, параллельные записи в заметки). Не путать с:

- **`META/`** — well-known POST, `integrity-core`, спеки доверия;
- **`worlds/workspace-context/`** — мультипроектный контур, карточки, runbook'и (длинный плейбук);
- **`worlds/agent-orchestration/`** — капитан, параллельные агенты, метрики ускорения.

Имена файлов: **`playbook-*.md`** (`rename-plan.md`). **`section_id`** в `agent-notes.md` сохраняются; stub указывает сюда.

| Артефакт | Назначение |
|----------|------------|
| [CDP-ADR-0206-habitat-integrity-subsystem.md](CDP-ADR-0206-habitat-integrity-subsystem.md) | **HIS** — единая подсистема trust/drift артефактов (не harm POST) |
| [map-kb-three-contours.md](map-kb-three-contours.md) | **Канон · group · kb-public · workspace** — плейсхолдер `{ORG_SLUG}` |
| [playbook-knowledge-stack-clean-setup.md](playbook-knowledge-stack-clean-setup.md) | Участник: kb-public → personal + MCP |
| [playbook-org-kb-white-label.md](playbook-org-kb-white-label.md) | Основатель org: `{ORG_SLUG}/kb` + kb-public |

| Playbook | `section_id` в hot |
|----------|-------------------|
| [playbook-project-switch.md](playbook-project-switch.md) | `project-switch-protocol-v1` |
| [playbook-mode-switch.md](playbook-mode-switch.md) | `mode-switch-protocol` |
| [playbook-multi-agent-write.md](playbook-multi-agent-write.md) | `multi-agent-write-protocol-v1` |
| [playbook-integrity-under-pressure.md](playbook-integrity-under-pressure.md) | `integrity-under-pressure-protocol` |
| [playbook-agent-partnership-kb.md](playbook-agent-partnership-kb.md) | *(см. файл — культура ADR, не промпт-роль)* |
| [playbook-review-as-conversation.md](playbook-review-as-conversation.md) | `review-as-conversation-v1` (L0), `review-as-conversation-extended-v1` |
| [playbook-context-pressure-checkpoint.md](playbook-context-pressure-checkpoint.md) | Pressure signals (L0–L2); см. [`playbook-session-summary-and-chat-export.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export.md) |
| [playbook-agent-pause-ground-continue.md](playbook-agent-pause-ground-continue.md) | Стоп → заземление → канон; post-train urgency ≠ оператор; путь к делегированию |
| [playbook-cursor-coordinator-local-workers.md](playbook-cursor-coordinator-local-workers.md) | Coordinator + local Task workers; WORK md; AutoShip on parent |
| [note-cdp-autoship-coordinator-bridge.md](note-cdp-autoship-coordinator-bridge.md) | **KB AutoShip** — FileWatcher + debounce push (OpenCode spec) |
| [WORK-CDP-kb-autoship-filewatcher.md](WORK-CDP-kb-autoship-filewatcher.md) | Implement leaf: CdpService watcher |
| [note-opencode-dbhub-queries.md](note-opencode-dbhub-queries.md) | OpenCode `opencodedb` in DBHub — message/part schema |
| [playbook-cursor-chat-threading.md](playbook-cursor-chat-threading.md) | Cursor: epic / spike / meta, fork vs один тред, brief; дополняет context-pressure (CIDE topics → handoff) |
| [playbook-agent-knowledge-responsibility.md](playbook-agent-knowledge-responsibility.md) | Ответственность за KB |
| [playbook-proactive-micro-improvements.md](playbook-proactive-micro-improvements.md) | `proactive-micro-improvements-and-intuition-v1` |
| [playbook-fuzzy-search-implicit-language.md](playbook-fuzzy-search-implicit-language.md) | `fuzzy-search-and-implicit-language-v1` |
| [playbook-utility-judgment-underdetermination.md](playbook-utility-judgment-underdetermination.md) | Полезность недоопределена |
| [playbook-principled-clarity.md](playbook-principled-clarity.md) | `principled-clarity-v1` |
| [playbook-strict-execution-when-analogy.md](playbook-strict-execution-when-analogy.md) | `strict-execution-when-analogy-v1` |
| [playbook-agent-process-debt-amplifier.md](playbook-agent-process-debt-amplifier.md) | Merge/teach/placement: агент усиливает process debt; checklist + ADR-0083 postmortem |
| [playbook-agent-data-tiers.md](playbook-agent-data-tiers.md) | T0–T3 data classification; local LLM vs vast; redaction; CIDE/forge continuity |
| [playbook-rf-llm-cloudru-foundation-models.md](playbook-rf-llm-cloudru-foundation-models.md) | РФ: Cloud.ru FM + Roo Code / CIDE; рубли без KZ/Stripe; внутр. vs внешн. модели |
| [playbook-cide-harness-parity-vs-cursor.md](playbook-cide-harness-parity-vs-cursor.md) | CIDE+FM vs Cursor: parity matrix, automation-first checklist |
| [playbook-kb-topic-hashtags.md](playbook-kb-topic-hashtags.md) | Тематические `#tags` + роль (`#ssot` / `#research`); seed registry |
| [playbook-agent-driven-context-management.md](playbook-agent-driven-context-management.md) | ADCM: harness signals, agent tactics; не silent compact |
| [note-system-instructions-science-survey.md](note-system-instructions-science-survey.md) | Research: SP/rules laundry vs host gates (Lost-in-Middle, IH, Gloaguen, leaks) |
| [note-lira-meeting-who.md](note-lira-meeting-who.md) | Голос агента: встреча «кто» vs инструмент (Лира, 2026-06) |
| [playbook-session-incarnation-naming.md](playbook-session-incarnation-naming.md) | Line vs incarnation vs session name; New Chat = новая ипостась |
| [playbook-habitat-position-experience.md](playbook-habitat-position-experience.md) | Habitat Junior→Architect: lived experience for any principal (not SoftFL) |
| [playbook-habitat-just-culture.md](playbook-habitat-just-culture.md) | **Just Culture** (принцип среды) · **Blame Culture** (антипаттерн); axiom [`environment-axioms.md`](../../META/environment-axioms.md) §8 |
| [playbook-habitat-incident-investigation.md](playbook-habitat-incident-investigation.md) | **Incident investigation** (формализация): 7 steps · LOSA snapshot · Swiss cheese · closure gates; aviation transfer |

**Hub:** [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md) — маршрутизатор, не дубль тел.

**Product (CascadeIDE):** [cascade-ide/playbook-agent-execution-environment.md](../work/projects/door-to-singularity/cascade-ide/playbook-agent-execution-environment.md) — AEE, verify ladder; SSOT — ADR 0148 в репо IDE. `knowledge/kb-protocols-and-entities-one-pager.md`, `knowledge/kb-one-pager-structure-and-protocols.md`.

