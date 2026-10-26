---
type: Note
title: 'WORK: CDP-ADR-0218 — unified recall facade (`recall_knowledge`) + G1 UX'
description: '**Status:** done · shipped 2026-09-12 (`4740608` guiders-core, `85ee3dd` cdp-mcp, `587193c` agent-notes; habitat `0.5.764+85ee3dd`)'
---
# WORK: CDP-ADR-0218 — unified recall facade (`recall_knowledge`) + G1 UX

**Status:** done · shipped 2026-09-12 (`4740608` guiders-core, `85ee3dd` cdp-mcp, `587193c` agent-notes; habitat `0.5.764+85ee3dd`)  
**Parent:** CDP-ADR-0210 (v0+v1 shipped)  
**SSOT ADR (create on ship):** `cdp-mcp/docs/adr/CDP-ADR-0218-knowledge-recall-facade-g1-ux.md`

---

## Контекст

CDP-ADR-0210 v0+v1 **shipped** (federated `knowledge_tags mode=search`, optional workspace, scope-first rank).

Проблема осталась **G1 cognitive**: агенты вызывают `memory_session_search_agent_notes` для corpus-тем → 0 hits выглядит как «нет данных», не «wrong layer».

**Цель UoW:** один фасад «найди в KB» + мелкие UX-фиксы affordance/empty.

**Не цель:** v2 pre-write gate, F# `Recall` contract, rename breaking MCP tools, external HCI FTS.

---

## Решение (ADR-0218)

Новый tool **`recall_knowledge`** — единая точка входа для агентов.

Старые tools **остаются** (power users / ACL reads), но descriptions + citizen + affordances ведут на facade.

### MCP surface

| Tool | Facet | MCP name |
|------|-------|----------|
| `recall_knowledge` | **world only** (Find+Kb primary) | `memory_world_recall_knowledge` |

**Args:**

| Arg | Required | Default | Notes |
|-----|----------|---------|-------|
| `query` | yes | — | free text или tag-like |
| `layer` | no | `auto` | `auto` \| `corpus` \| `hot` |
| `limit` | no | 15 | 1–50 |
| `active_scope` | no | — | corpus rank boost (0210) |
| `primary_project_id` | no | — | corpus rank boost |
| `scope_only` | no | false | corpus filter |
| `workspace_path` | no | — | только hot layer |

**Description (первая строка обязательна):**

`Unified KB recall — auto picks corpus (tags/search) then hot notes. Prefer this over search_agent_notes / bare knowledge_tags.`

### `layer=auto` pipeline (deterministic, no LLM)

```text
1. corpus tag resolve  (mode=resolve, query)
   → if known && hits → return (layers_used: ["corpus","resolve"])

2. corpus tag lookup   (mode=lookup, query)
   → if total > 0 → return (layers_used: ["corpus","lookup"])

3. corpus substring    (mode=search, query)
   → if total > 0 → return (layers_used: ["corpus","search"])

4. hot grep            (search_agent_notes on agent-notes.md)
   → return whatever (layers_used includes "hot" if step 4 ran)

layer=corpus → steps 1–3 only
layer=hot    → step 4 only
```

**Unified JSON shape** (новый, не passthrough сырого child JSON):

```json
{
  "tool": "recall_knowledge",
  "query": "ai-incidents",
  "layer_requested": "auto",
  "layers_used": ["corpus", "lookup"],
  "total": 12,
  "hits": [
    {
      "layer": "corpus",
      "kind": "lookup",
      "path": "personal/ai-incidents/README.md",
      "line": null,
      "preview": "...",
      "scope_boost": 0
    }
  ],
  "hot": { "total_matches": 0, "returned_matches": 0, "matches": [] }
}
```

- `hits[]` — merged ranked list (corpus first; hot hits appended with `layer:"hot"`, `kind:"grep"`, `line`, `text`).
- Если corpus дал результат — **hot всё равно не вызывать** в `auto` (экономия; hot только когда corpus пуст).
- Поле `hot` — только если hot layer выполнялся или `layer=hot`.

### G1 UX без facade (в том же UoW, малый diff)

1. **`NotesStorage.Search`**: при `total_matches=0` добавить:
   - `layer: "hot"`, `searched: "agent-notes.md"`
   - `hint`: corpus topics not in hot notes
   - `try_next`: `{ tool: "memory_world_recall_knowledge", query: "<same>" }`

2. **`Wave1AffordanceSeed`**: `search_agent_notes` objects → **Session only** (убрать `Kb`).
   Добавить `recall_knowledge` на **MemoryWorld**, Find+Kb, cost 1, phase RecallThroughPlan.

3. **ToolCatalog descriptions** — первая строка:
   - `search_agent_notes`: `HOT ONLY — grep agent-notes.md`
   - `knowledge_tags`: `CORPUS — tags/search; prefer recall_knowledge for agents`
   - `recall_knowledge`: см. выше

4. **Citizen router** (`CitizenIntentRouter.Kb.cs`):
   - aliases: `recall`, `recall_knowledge`, `find_kb` → `recall_knowledge`
   - free `query=` / `q=` без tool → **`recall_knowledge`** (не `knowledge_tags`)
   - `search` / `search_kb` / `search_corpus` → `recall_knowledge` layer=corpus (или tool + default layer in handler)
   - `search_hot` / `search_notes` → `search_agent_notes` (unchanged)
   - pulse при 0 corpus: `try recall_knowledge q=…`

5. **KB supplement** (1 строка):
   `knowledge/domains/agent-operations/index-knowledge-router-supplement.md`
   → corpus/playbook/incident → `memory_world_recall_knowledge`, never session search.

---

## Файлы (touch list)

### guiders-core

- `src/AgentNotes.Core/KnowledgeRecallFacade.cs` **(new)** — orchestration + merge JSON
- `src/AgentNotes.Core/NotesStorage.cs` — `RecallKnowledge(...)`, empty hot hint in `Search`
- `src/AgentNotes.Mcp.Hosting/ToolCatalog.cs` — register `recall_knowledge`
- `src/AgentNotes.Mcp.Hosting/ToolHandlers.cs` — dispatch + args
- `src/Cdp.Core/Wave1AffordanceSeed.cs` — affordances

### cdp-mcp

- `docs/adr/CDP-ADR-0218-knowledge-recall-facade-g1-ux.md` **(new)**
- `Backends/MemoryScopeGateway.cs` — whitelist `recall_knowledge` federated (same as `knowledge_tags`, no subdir inject)
- `CitizenIntentRouter.Kb.cs` — routing + `IsNotesTool` includes `recall_knowledge`
- `CitizenRouteHost.Kb.cs` — pulse formatter for recall JSON (top paths, layers_used)
- `CdpMcp.Tests/RecallKnowledgeFacadeTests.cs` **(new)**
- `CdpMcp.Tests/CitizenKbHostTests.cs` — update expectations for free query → recall

### agent-notes KB mirror

- `knowledge/domains/agent-operations/CDP-ADR-0218-…md` pointer → SSOT ADR
- supplement one-liner (above)

---

## Тесты (must pass)

### Unit / in-proc (`RecallKnowledgeFacadeTests`)

1. `query=ai-incidents layer=auto` → corpus hit `personal/ai-incidents/README.md`, `layers_used` contains `lookup`, hot **not** called
2. `query=PML layer=auto` → resolve `#engineering-pml`
3. `query=<unique hot-only string in agent-notes.md> layer=auto` → hot hit, `layers_used` contains `hot`
4. `layer=corpus` → never hot
5. `layer=hot` → never corpus
6. `active_scope=door-to-singularity query=cdp` → top hit under scope path

### Citizen (`CitizenKbHostTests`)

7. `@intent kb q=ai-incidents` → op `recall_knowledge`, facet world
8. `@intent kb search_hot q=foo` → `search_agent_notes`, facet session

### Regression (existing, keep green)

- `KnowledgeCorpusRecallSmokeTests` (0210)
- `MemoryScopeGatewayTests`

---

## Smoke (live CDP после deploy)

```text
memory_world_recall_knowledge query=ai-incidents
memory_world_recall_knowledge query=PML
memory_session_search_agent_notes query=ai-incidents   # 0 + hint + try_next
cdp_citizen @intent kb q=HF Swarm                      # → recall_knowledge
```

---

## Done criteria

- [x] ADR-0218 accepted + KB pointer
- [x] `memory_world_recall_knowledge` в MCP list
- [x] Все тесты green
- [x] CDP deploy + smoke 4/4
- [x] Logical commit + push (guiders-core + cdp-mcp + agent-notes mirror)

---

## Deploy

`cdp_deploy mode=rollout` → verify `cdp_health` → run smoke.

---

## Seed для implement-чата

Implement WORK CDP-ADR-0218 recall_knowledge facade per this UoW. Min diff, reuse KnowledgeTagIndex + KnowledgeCorpusRecall + NotesStorage.Search. Ship tests + deploy smoke.

