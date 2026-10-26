# ADR 022: KB Graph Substrate v2 — structure IR, slices, SAT

**Tags:** #adr #kb #graph #fsharp #agentnotes #sat #just-culture

**Статус:** Proposed  
**Дата:** 2026-09-13  
**Источник в истории:** операторский steer — KB как implicit graph в Markdown; нет быстрых срезов и structural consistency; правила (transfer matrix, Integrity POST, program state) держатся на дисциплине агента, не на substrate (Blame Culture под видом Just Culture).  
**Supersedes:** —  
**Extended by:** — (planned: 023 records basket, 024 transfer compile, 025 kb-sat catalog)  
**Связано:** [002](002-integrity-post-and-epistemic-baseline.md) · [006](006-zettelkasten-overlay-for-kb.md) · [007](007-kb-project-constitution.md) · [010](010-kb-markdown-fts-index-boundary.md) · [020](020-kb-language-contours.md) · GUIDERS-FSHARP-ADR-0002 (Platform vs habitat guild) · `domains/agent-operations/playbook-habitat-just-culture.md` · `work/projects/door-to-singularity/ca-substrate-agent/` (CASA — Track B research)

---

## Контекст

### 1. KB уже граф — без graph engine

Канон agent-notes — **property graph**, сериализованный текстом:

| Узел (implicit) | Рёбра (implicit) | Где сегодня |
|-----------------|------------------|-------------|
| playbook, ADR, matrix, project card, pack card | link, tag, PRIMARY, supersedes, Related | Markdown |
| world, domain, scope | transfer allow/deny, contour u/g/o | matrices prose |
| hot section | L0 order | `agent-notes.md` + `memory-architecture.json` |
| operational fact (wave done, blocker) | blocks, unlocks, touches epic | **нет** — таблицы в чате / hand-edited MD |

**Нет:** materialized structure, единой алгебры рёбер, операций slice / reachability / consistency closure.

### 2. As-built enforcement

| Mechanical | Honor-system |
|------------|--------------|
| public-cut, `public-kb.ignore`, publish CI | transfer matrices |
| section markup validate | Integrity POST behavior |
| tag index, scope boost | router supplement policy hints |
| primary-root write lock (if TOML) | Kolb discipline, program tables |

~90% «системы KB» — контент + договорённости; substrate не помогает крутить срезы и не проверяет согласованность структуры.

### 3. Native habitat vs pretrain economics (motivation)

**Аналогия поколений (operator steer, 2026-09-13):** люди, выросшие без мобильного интернета, *могут* хотеть адаптироваться, но у них нет встроенной моторики среды — они **переводят** новое в старые паттерны. Цифровые «native» поколения не дисциплинированнее — **среда совпадает** с привычкой.

Текущие LLM в agent-notes/KB — **не native** для typed graph, transfer deny, contour, fail-closed mutate. Pretrain = текстовое море без graph IR. Мы даём constitution на сотни страниц и ждём рыбу в воде — получаем **interpretation layer**, который compaction и контекст ломают.

**Вторая боль (дороже первой):** «вырастить» модель, native для *нашей* среды, через pretrain — порог **oligopoly** (compute, data, capital). CASA и альтернативные вычислительные модели — **отдельная ставка** на economics обучения; не блокер и не замена habitat v2 в горизонте квартала.

**Вывод для ADR 022:**

| Путь | Стоимость | Горизонт |
|------|-----------|----------|
| **Habitat substrate** (graph, SAT, gates, slice API) | инженерия, итерации | **сейчас** — P0–P5 |
| **Model adaptation** (open weights, без pretrain) | LoRA/SFT/abliteration-scale | **параллельно** — § Research track |
| **Full pretrain / CASA field** | высокая / исследование | long bet |

KB Graph Substrate — **тротуары и светофоры** для моделей, которые нельзя дешёво перевоспитать pretrain'ом. Just Culture честна только когда substrate refuse/warn **до** «агент не дочитал supplement».

### 4. Research track — skip pretrain, habitat-native weights? (operator hypothesis)

**Гипотеза:** не строить свой pretrain; взять **open weights** + **целевую адаптацию** под habitat, чтобы модель *ближе к native* для graph/slice/tool-first работы.

**Не путать с v1 ship:** P0–P5 **не ждут** fine-tune. Substrate must work with **любой** frontier/harness model через API. Adaptation — ускоритель, не dependency.

#### 4.1 Что реально может дать «skip pretrain»

| Technique | Что меняет | Native для KB graph? |
|-----------|------------|----------------------|
| **Open weights base** (Llama, Qwen, Mistral, …) | стартовая политика | частично — всё ещё text-native |
| **LoRA / SFT на habitat traces** | tool-call patterns, slice→act, deny→stop | **да, практично** — учим *использовать* graph API |
| **Abliteration / refusal-direction ablation** | снимает alignment-слой (incl. «китайская цензура» у open models) | **нет** для graph — другая ось (refusal, not structure) |
| **RL in environment** (tool rewards, SAT pass/fail) | policy под fail-closed habitat | **да, средний горизонт** — дороже SFT, нужен sim |
| **Continual / field learning (CASA)** | economics адаптации без full pretrain | **возможно, TBD** — см. door-to-singularity CASA |
| **Synthetic pretrain на graph ops** | малый corpus «Cypher-like» KB slice DSL | исследование; не замена open weights |

**Практичный stack (если идти):**

```text
open weights
    → (optional) abliteration / uncensor — только если нужен operator alignment, не graph
    → LoRA on curated habitat traces:
         kb_graph_slice → read nodes → respect TransferDeny
         kb_record_append → never hand-edit L2 views
         incident → substrate-first playbook
    → (later) RL with SAT/habitat reward in CDP dogfood
    → (long) CASA field — если desk докажет cheaper continual adaptation
```

#### 4.2 Что adaptation **не** заменяет

- **Fail-closed gates** — даже native-ish модель ошибается; SAT и PathMutateGate остаются.
- **SSOT git + graph IR** — weights не хранят canon; habitat хранит.
- **Semantic judgment** — transfer «по смыслу», harm POST — human + prose.

#### 4.3 Trace corpus (future asset)

P0–P3 substrate создаёт **machine-checkable traces** — enrichment для \(P.habitat\) в XL export.

**SSOT export grammar:** [`explainable-learning/README.md`](../work/projects/door-to-singularity/explainable-learning/README.md) — tuple v2:

\[
(P,\ A,\ B,\ C_A,\ C_B,\ S_A,\ S_B,\ E,\ T)
\]

- **Preference** \((P,A,B,C,S)\): *почему* B лучше A в этой среде (affordance literacy), не scalar fear.  
- **Debrief** \(E\): после ошибки — «что помешало / что было неясно?» (Just Culture, не shame).  
- **Teacher** \(T\): delta канона/substrate — **bidirectional learning**.  
- **Epistemic axes** в \(S\): `honest_gap_ok`, `external_lookup_ok`, `closed_world_reject` — явный reject **closed-world obligation** («только из весов»). См. [`note-epistemic-openness-rubric.md`](../work/projects/door-to-singularity/explainable-learning/note-epistemic-openness-rubric.md).

Substrate traces (examples):

- `(query, subgraph JSON, action, SAT outcome)`  
- deny events с matrix row anchor  
- program record append sequences  

LoRA/DPO **не** «chat logs + worse on не знаю». Export human_reviewed XL rows; substrate без \(C,S,E,T\) = снова honor system.

**Agent-native post-train grammar** (weights audit limits, trajectory training, contour LoRA, harness eval): [`note-agent-proposals-llm-post-train.md`](../work/projects/door-to-singularity/explainable-learning/note-agent-proposals-llm-post-train.md).

#### 4.4 Связь с CASA

CASA (ca-substrate-agent, door-to-singularity) — ставка на **другую вычислительную модель** и cheaper continuity/adaptation. Если выстрелит — может снизить цену «модель, выросшая в field», но **не отменяет** graph substrate: field всё равно нужна **структура** (edges, gates), не только weights.

**Два параллельных трека:**

```text
Track A (this ADR): KB Graph Substrate — habitat muscle, model-agnostic
Track B (research): open weights + habitat LoRA / CASA — model native-ish
```

Track B **питуется** артефактами Track A (traces, SAT labels).

### 5. Operator thesis (accepted as direction)

- KB — **огромный граф знаний**, записанный текстом.
- Нужны **быстрые срезы в памяти** (subgraph), structural SAT, fail-closed mutate — не замена prose MD.
- **F#** — guild для typed graph IR, validation traversals, slice/emit (как GDL/Notations в Platform.Modeling).
- **Graph DB** — опциональный **query projection**, не SSOT канона (см. § Graph storage).

### 6. Guild boundary

**Не** `Platform.Modeling.Knowledge` — federation mechanics ≠ personal/org canon.

```text
AgentNotes.Modeling.*     F#   Graph IR, policy, validate, slice, emit, SAT specs
AgentNotes.Execution.*    C#   MCP, storage I/O, recall orchestration
AgentNotes.Habitat.*      C#   CDP mutate gate parity (KB writes)

agent-notes (git)         MD + records wire + generated views

Platform.Modeling.*       без изменений (GDL, Notations, …)
```

---

## Решение

### 1. Разделить payload и structure

| Слой | Содержимое | Mutability |
|------|------------|------------|
| **L0 Prose canon** | ADR, playbooks, worlds kb — hand MD | human PR |
| **L1 Records** | append-only JSONL (`knowledge/records/streams/`) | `kb_record_append` only |
| **L2 Views** | emitted MD (`knowledge/records/views/`) | **deny hand-write** |
| **L3 Graph IR** | F# types + materialized index | ingest + validate |
| **L4 Query index** | SQLite / optional graph DB | gitignored rebuild |
| **L5 Hot** | `agent-notes.md` | existing hot tools |

**SSOT канона:** git (MD payloads + L1 wire). **SSOT structure:** F# IR + compiled policy edges. **Не** external graph DB as SSOT.

### 2. Typed graph (v1 schema)

```text
NodeKind (v1 subset):
  CanonDoc | RecordEvent | Project | World | MatrixRow | Tag | HotSection | Adr

EdgeKind (v1 subset):
  LinksTo | Tagged | ScopedUnder | PrimaryProject
  TransferAllow | TransferDeny | TransferAllowWithCheck
  Supersedes | InContour
  Blocks | Unlocks | EmitsView | SatDependsOn

(v2+, ADR 006 amend):
  Supports | Contrasts   — zettel edges в graph, не отдельная prose-only zettel/
```

Packages (guiders-core или sibling repo):

```text
AgentNotes.Modeling.Core       — NodeId, EdgeKind, Contour, LayerTag
AgentNotes.Modeling.Graph      — ingest, slice, reachability, subgraph
AgentNotes.Modeling.Policy     — TransferPolicy, ContourPolicy, IntegrityRootsCheck
AgentNotes.Modeling.Emit       — subgraph → MD view / MCP JSON
AgentNotes.Modeling.Sat        — kb-sat observers
```

### 3. Операции (API surface)

| Operation | Input | Output |
|-----------|-------|--------|
| **Ingest** | git diff / full scan | upsert nodes + edges from MD links, tags, frontmatter |
| **Slice** | scope, world, radius, contour, time, tag | SubGraph |
| **Validate** | graph + policy bundle | SAT report (structural) |
| **Emit** | SubGraph + template | L2 view MD |
| **Append** | RecordEvent | validate schema → graph update → emit views |

**Примеры slice:**

- ego-2 от `matrix-do-not-transfer-v1`
- `work/projects/door-to-singularity/**` + flagged cross-links
- public contour closure (contour o)
- open blockers + inbound `Blocks` edges
- epic E2 nodes без `uow.done`

### 4. Structural SAT (kb-sat)

| Id | Invariant |
|----|-----------|
| Sat-001 | internal `LinksTo` resolve |
| Sat-002 | public-cut / contour leak |
| Sat-003 | hand-edit on L2 generated views |
| Sat-004 | matrix MD ↔ compiled transfer policy drift |
| Sat-005 | record schema |
| Sat-006 | router references exist |
| Sat-007 | speech_situation on canon playbooks (required fields) |
| Sat-008 | Integrity POST root files hash manifest |
| Sat-009 | project card required fields |
| Sat-010 | known_fail stale |

**Semantic consistency** (смысл ADR, уместность transfer) — **вне** kb-sat v1; human review + dialogue.

### 5. Mutate gate (fail-closed)

- L2 views: deny all direct MCP/Write
- L1 records: `kb_record_append` → F# validate → graph → emit
- L0 prose: ContourPolicy + path allowlist; optional break-glass → audit `BreakGlassOverride` edge
- CDP: PathMutateGate parity — no raw Cursor Write to `knowledge/` except via MCP

TransferPolicy on cross-world promote / cite-with-action (deny → structured error + matrix row anchor).

### 6. Matrix compile pipeline

Normative source: `matrix-do-not-transfer.md` (+ domain matrices).  
Build step → embedded JSON / graph edges `TransferDeny|Allow|AllowWithCheck`.  
CI Sat-004 fails on drift.

### 7. Graph storage — .NET и «Neo4j = Java»

**Факт:** Neo4j server historically JVM, но клиент **.NET-first через Bolt**:

- [Neo4j.Driver](https://github.com/neo4j/neo4j-dotnet-driver) — официальный, NuGet, без Java в процессе приложения
- Сервер: Docker / Neo4j Desktop / Aura — отдельный процесс (как HCI MCP для FTS)

**Рекомендация по фазам:**

| Phase | Storage | Rationale |
|-------|---------|-----------|
| **P0–P1** | F# in-memory `SubGraph` + **SQLite adjacency** under `.kb-graph/` (gitignore) | zero ops; same pattern as ADR 010 HCI; rebuild from git |
| **P1 alt** | committed **`knowledge/.graph/edges.jsonl`** snapshot | reviewable diffs; merge pain on large ingest |
| **P2 optional** | **Neo4j / Memgraph / FalkorDB** as **query projection** | тяжёлые slice (multi-hop, path find); rebuild from ingest |
| **Not SSOT** | any graph DB | git MD + L1 records remain source; DB = disposable index |

**Другие .NET-viable options:**

| Engine | Notes |
|--------|-------|
| **SQLite** + adjacency tables | F# or C#; уже в стеке (HCI); достаточно для ~10⁵ edges |
| **Neo4j** (Bolt driver) | Mature Cypher; ops cost |
| **Memgraph** | Cypher-compatible; in-memory bias |
| **FalkorDB** | Redis module; graph queries |
| **Apache AGE** | PostgreSQL extension; Npgsql if PG already present |
| **SQL Server Graph** | Native if SSOT DB already MSSQL — unlikely for agent-notes |
| **Pure F# Map** | Slice/validate in-process; no persistence — OK for SAT CI |

**Decision:** v1 **не требует** external graph DB. F# Graph IR + SQLite projection. Neo4j — **ADR amendment or P2 spike** if multi-hop analytics justify ops.

Relation to [010](010-kb-markdown-fts-index-boundary.md): HCI = **text** index; graph index = **structure** index; complementary, both gitignored/local, neither replaces canon.

### 7.1 Licensing & fork policy (Neo4j)

Neo4j **Community Edition** — GPLv3, исходники на GitHub; форк CE легален с copyleft-обязательствами. **Enterprise** — commercial, EE source не полностью public (open core). **Порт сервера Neo4j на .NET** — не «переписать библиотеку», а новый graph DB engine; **не рассматривается**. Клиент .NET: [Neo4j.Driver](https://www.nuget.org/packages/Neo4j.Driver) (Apache 2.0) → Bolt → CE в Docker. SSOT канона остаётся git; graph DB — disposable projection.

### 8. Router evolution

- `index-knowledge-router.md` — human Domain Entry Map (stable)
- supplement — shrink; policy moves to F#
- optional `records/views/router-auto.md` — generated tag index

### 9. Records + graph (unified model)

Program checkpoint, blockers, known_fail — **RecordEvent nodes** + temporal edges, not hand MD tables.  
Zettel ADR 006 realized as **`Supports`/`Contrasts` edges** in `records/graph/`, not `knowledge/zettel/` prose-only.

---

## Open questions (operator steer)

| Id | Question | Default if silent |
|----|----------|-------------------|
| OQ-1 | Index SSOT: git `edges.jsonl` vs local SQLite only | SQLite rebuild + optional export snapshot |
| OQ-2 | Ingest trigger: CI only vs watch on save | CI on `knowledge/**` + manual `kb-graph ingest` |
| OQ-3 | First ingest scope: `work/**`+matrices+adr vs full worlds | phased: work + adr + KE matrices → then worlds |
| OQ-4 | MCP tool: `kb_graph_slice` vs extend `recall_knowledge` | new `kb_graph_slice` + keep recall for text |
| OQ-5 | Break-glass prose edit | `force=true` + mandatory incident record event |
| OQ-6 | Repo for Modeling packages | guiders-core `src/AgentNotes.Modeling.*` |
| OQ-7 | Neo4j spike timing | defer to P2 after SQLite slice API proven |
| OQ-8 | Track B: habitat LoRA base model + abliteration scope | defer until P1 traces exist; abliteration ≠ graph native |

---

## Non-goals (v1)

- Replace MD prose canon with graph DB nodes
- Semantic NLP «понимание» playbooks in SAT
- Merge AgentNotes into Platform.Modeling
- Require graph DB for every developer
- Automate harm / ethics judgment (Integrity POST behavior stays L0 + human)

---

## Последствия

**Плюсы**

- Structural Just Culture: инцидент → missing SAT/gate, не «агент не дочитал supplement»
- Fast slices без 15× grep round-trips
- Transfer matrix и contour rules executable
- Federation-proven pattern (F# IR + C# MCP + git wire)

**Минусы / риски**

- Ingest complexity (MD link syntax variants)
- Dual maintenance matrix MD ↔ compiled policy until compile is CI-mandatory
- Graph index drift if ingest not run — mitigated by CI kb-sat
- Neo4j ops temptation before SQLite slice proves need

---

## План внедрения

```text
P0 — Foundation (4–6 w)
  ADR 022 Accepted (direction)
  AgentNotes.Modeling.Graph + Sat skeleton
  matrix-do-not-transfer compile → policy JSON
  kb-sat Sat-001,002,004,006 in GitLab CI
  observe-only (no write gate)

P1 — Records + emit (3–4 w)
  knowledge/records/ basket + schemas
  kb_record_append MCP
  Emit L2 views; Sat-003,005
  Retro: federation program wave → program.jsonl

P2 — Write gate (3–4 w)
  L2 deny; CDP PathMutateGate for knowledge/
  TransferPolicy enforce on promote
  ContourPolicy on writes

P3 — Graph API + optional DB (4 w)
  kb_graph_slice MCP
  SQLite projection; optional Neo4j spike (OQ-7)
  Zettel edges; Kolb under records schema

P4 — Multi-canon + publish (ADR 012/013)
  TOML required for writes
  kb-sat on group/public export

P5 — Habitat desk (CDP-0206)
  Release manifest + kb_sat_digest
  incident.jsonl ↔ investigation playbook

P6 — Track B research (parallel, optional)
  Curate habitat traces from P0–P3 (slice, deny, record append)
  LoRA/SFT pilot on open weights; evaluate tool-first vs prose-first
  Optional: abliteration for alignment axis only (not graph nativeness)
  CASA desk integration if continual adaptation ships
  Success metric: fewer honor-system failures WITH gates enabled
```

Each phase ships **kb-sat green** before next gate.

Track A (P0–P5) **не блокируется** Track B.

---

## Связь с Just Culture

Habitat playbook: сначала substrate (pulse, refuse, gate), потом accountability.  
KB v2 переносит тот же контракт на канон: **matrices, records, views, transfer — muscle; prose — wisdom.**

---

## Примечание для роутера

При Accepted — одна строка в supplement: «KB graph substrate / kb-sat / slice» → этот ADR + `AgentNotes.Modeling.*` runbook (TBD P0).

