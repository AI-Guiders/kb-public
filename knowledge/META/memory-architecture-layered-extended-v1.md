# Memory Architecture v1 (Layered) — extended

Перенесено из `agent-notes.md` (приборка hot). В hot остаётся stub `memory-architecture-v1` с `l0_manifest` (выше `public-cut` для kb-public).

Manifest: `knowledge/META/memory-architecture-v1.json`

---

## Memory Architecture v1 (Layered)

l0_manifest: knowledge/META/memory-architecture-v1.json
### L0: Hot State (always load, независимо от проекта/задачи/scope)
- Source of truth: `knowledge/META/memory-architecture-v1.json` (только `l0`; без глобального owner-sprint в hot).
- **kb-public:** только `l0` и секции **выше** `<!-- public-cut -->` (stub `memory-architecture-v1` с `l0_manifest`).
- Compatibility mirror — `l0` (публичные контракты):
  - baseline-integrity-epistemic-v1
  - agent-equal-standing-v1
  - epistemic-default-distrust-v1
  - core-when-barriers-fail-v1
  - principled-clarity-v1
  - active-scope
  - response-finalizer-v1
  - response-one-step-before-finish-v1
  - scope-disambiguation-all-everywhere-v1
- **Операционный спринт:** не в L0; по проекту — `project-operational-memory-v1` и README в `knowledge/work/projects/`.

### L1: Operational Memory (scope slices)
- scope-door-to-singularity (внутри — карточки `### Карточка: …`; см. `knowledge/META/MIGRATION-scope-project-cards-v1.md`; длинный контур — `knowledge/work/projects/door-to-singularity/`)
- scope-portal (operational; карточки + `knowledge/work/projects/portal/edw-portal/`)
- scope-harvester (карточка + `knowledge/work/projects/harvester/edw-harvester/README.md`; ориентиры — `harvester/edw-harvester/orientations.md`; отдельно от portal)
- scope-imc (карточка + `knowledge/work/projects/imc/imc-portal/README.md`)
- execution-gate-v1
- hot-context-writing-contract

### On-demand (не в L0/L1, подгружать по route_context)
- **`agent-memory-and-operating-principles-v1.md`** — hub операционных принципов (маршрутизатор → один playbook по теме)
- `response-one-step-checklist-v1` → `worlds/workspace-context/response-one-step-checklist-extended-v1.md` — чек-лист «завершён?» / «изменил KB»
- knowledge/baseline-integrity-epistemic-extended-v1.md — развёрнутый baseline (целостность, ссылки playbook/kb)
- knowledge/epistemic-default-distrust-extended-v1.md — развёрнутый эпистемический принцип
- knowledge/META/core-when-barriers-fail-extended-v1.md — ядро при крахе барьеров (слой рядом с POST/ядром)
- knowledge/worlds/workspace-context/response-finalizer-extended-v1.md — вычитка долгоживущего текста и детали финализатора
- knowledge/worlds/workspace-context/active-scope-resolution-extended-v1.md — резолв workspace_path → slice, карта, fallback MCP
- principled-clarity-extended-v1 → `domains/agent-operations/playbook-principled-clarity-v1.md` § «Развёрнуто»
- domains/agent-operations/playbook-proactive-micro-improvements-v1.md, playbook-fuzzy-search-implicit-language-v1.md, playbook-strict-execution-when-analogy-v1.md, playbook-agent-knowledge-responsibility-v1.md, playbook-utility-judgment-underdetermination-v1.md
- worlds/agent-orchestration/playbook-agent-reconnaissance-before-action-v1.md — разведка до патча (anti-hurry)
- scope-disambiguation-examples-v1 — примеры ∀/∃ и кейсы «везде»
- project-operational-memory-v1 — где хранить текущую задачу / next step (только карточки проектов, не корневой hot)
- project-switch-protocol-v1 — маркеры `[PRIMARY:…]` / `[SCOPE:…]` и приоритеты; рядом с mode-switch-protocol
- agent-autonomy-routing-stub-v1 → `worlds/agent-orchestration/playbook-agent-autonomy-and-routing-v1.md`
- Подсказки «запрос → секция»: route-context-hints-v1

### Мета и поддержка
- archive-index-v1 — ключевые ревизии и якоря; полный список секций — grep / memory_health
- memory-large-sections-policy-v1 — политика крупных секций (>2.5k символов)
- kb-external-links-v1 — ожидаемые пути knowledge/, META (чек-лист ссылок)
- kb-public-cut-v1 — граница public-cut для agent-notes.md

### L2: Episodic Archive
- revision snapshots in `.revisions/*.md`
- loaded only when facts are missing or user requests historical context

### L3: Semantic Routing Layer
- context is represented as weighted facets, not rigid domain classes
- candidate facets: professional, personal, reflective, cultural, procedural, relational
- routing uses facet weights + evidence type required by task

Invariant:
- scope split improves operations, but does not replace ontology routing.
- **Операционные принципы:** hub `knowledge/agent-memory-and-operating-principles-v1.md` → целевой playbook; hot stubs: `proactive-micro-improvements-and-intuition-v1`, `fuzzy-search-and-implicit-language-v1`, `strict-execution-when-analogy-v1`, `autonomy-right-to-pause-reconnaissance-v1`. **Длинная сессия / итогы:** `playbook-session-summary-and-chat-export-v1.md`, `tools/Export-CursorJsonlTranscript.ps1`.
- **Миры/метамиры:** stub-секции `world-*` в `agent-notes.md` → полные тексты в `knowledge/worlds/world-life/map-world-life-subworlds-v1.md`; правила — `knowledge/worlds/knowledge-engineering/kb-knowledge-engineering-multiworld-rules-v1.md`, `world-modeling-playbook.md`. Домены в index (Git, IT, …) — навигация knowledge, не подмиры world-life.
