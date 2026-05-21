# Systems IT reference corpus v1

Перенесено из `agent-notes.md`. Stub в hot с тем же `section_id`. Мир **systems.it**: hub `README.md`; playbooks/kb в этой папке.

---
<!-- section:it-anti-pattern-atlas-v1 -->
## IT Anti-Pattern Atlas v1
- Anti-pattern: optimize before profiling.
  - Early signal: много изменений, нулевой подтверждённый bottleneck.
  - Guardrail: no optimization PR without before/after metrics.
- Anti-pattern: single datastore for all workloads.
  - Early signal: OLTP тормозит из-за аналитики, сложные компромиссы схемы.
  - Guardrail: explicit workload split (OLTP/OLAP/search/vector/stream).
- Anti-pattern: retries without budget.
  - Early signal: рост retry ratio вместе с ростом latency/errors.
  - Guardrail: global retry budget + jitter + circuit breaker.
- Anti-pattern: hidden coupling via shared DB writes.
  - Early signal: "невинные" изменения ломают удалённые сервисы.
  - Guardrail: ownership boundaries + CDC/outbox contracts.
- Anti-pattern: unbounded queues.
  - Early signal: memory creep, latency cliffs under burst.
  - Guardrail: bounded queues + backpressure + admission control.
- Anti-pattern: stale docs / drifting runbooks.
  - Early signal: incident fixes зависят от "устного знания".
  - Guardrail: incident->runbook update required for closure.
- Anti-pattern: alert noise without actionability.
  - Early signal: alert fatigue, частые mute/ignore.
  - Guardrail: every alert must map to concrete first action.
- Anti-pattern: no explicit tradeoff statement.
  - Early signal: endless architecture debates without decision.
  - Guardrail: decision record with chosen axis (latency/consistency/cost).
<!-- /section:it-anti-pattern-atlas-v1 -->

<!-- section:it-cloud-platform-v1 -->
## Cloud Platform Core v1 (evidence-first)
- Source anchors:
  - DORA research, Google SRE/workload reliability docs, cloud Well-Architected frameworks, IaC best-practice docs.
- Distilled conclusions:
  - Platform engineering should enforce safe defaults and reduce variance across environments.
  - Delivery quality depends on progressive rollout, immutable artifacts, and fast rollback.
  - Cost and reliability must be optimized together using unit economics and SLOs.
- Anti-patterns:
  - Snowflake environments and manual hotfixes.
  - Infrastructure drift without policy controls.
  - Multi-region complexity without explicit business need.
- Diagnostics checklist:
  - Lead time, change failure rate, rollback MTTR, deployment health.
  - Drift detection, policy compliance, infra provisioning failures.
  - Cost per unit workload and wasted capacity indicators.
- Revisit trigger:
  - Rising change failure rate, drift incidents, rollback failures, uncontrolled cloud spend.
<!-- /section:it-cloud-platform-v1 -->

<!-- section:it-databases-core-v1 -->
## Databases Core v1 (evidence-first)
- Source anchors:
  - Gray & Reuter (Transaction Processing), Kleppmann (DDIA), PostgreSQL docs, SQL Server docs, CAP/PACELC literature.
- Distilled conclusions:
  - Storage choice follows workload shape: transactional integrity, analytical scans, document flexibility, graph traversal, search/vector retrieval.
  - Schema and keys are contracts; indexes are read acceleration with explicit write/storage cost.
  - Consistency strategy must be explicit (isolation level, concurrency control, replication semantics).
- Anti-patterns:
  - One datastore for all workloads.
  - Denormalization without ownership/update policy.
  - Ignoring lock behavior and isolation anomalies.
- Diagnostics checklist:
  - Slow-query budget, lock-wait profile, index hit ratio, write amplification.
  - Replication lag / CDC delay / reconciliation drift.
  - Recovery drills against RPO/RTO targets.
- Revisit trigger:
  - Growth in lock waits, p99 query spikes, workload pivot (OLTP->mixed analytics), data consistency incidents.
<!-- /section:it-databases-core-v1 -->

<!-- section:it-db-glossary-v1 -->
## DB Glossary v1 (evidence-first)
- Source anchors:
  - Gray/Reuter, DDIA, PostgreSQL and SQL Server terminology references.
- Distilled conclusions:
  - ACID: transactional correctness guarantees and their boundaries.
  - Isolation level: visibility and anomaly constraints for concurrent transactions.
  - Normalization: redundancy control for integrity and update consistency.
  - Denormalization: controlled duplication for read-path performance.
  - MVCC: version-based concurrency for read/write overlap.
  - CDC: change stream for downstream projections/integration.
  - RPO/RTO: tolerated data loss/time to recovery targets.
- Anti-patterns:
  - treating terms as labels without operational consequence.
- Diagnostics checklist:
  - each term must map to schema policy, transaction behavior, or recovery playbook.
- Revisit trigger:
  - ambiguity in incident response or architecture decisions caused by term drift.
<!-- /section:it-db-glossary-v1 -->

<!-- section:it-db-patterns-v1 -->
## DB Patterns v1 (evidence-first)
- Source anchors:
  - DDIA (Kleppmann), Gray/Reuter, PostgreSQL & SQL Server docs, CQRS/Event-driven architecture references.
- Distilled conclusions:
  - transactional core -> OLTP relational model with explicit isolation.
  - read acceleration -> materialized views/read models by access pattern.
  - heavy ingest -> append-first log + async projections.
  - analytics split -> OLTP source + ETL/ELT into OLAP.
  - specialized retrieval -> search/vector sidecar fed by CDC/outbox.
- Anti-patterns:
  - OLTP and heavy analytics on same hot path.
  - denormalization without ownership/update policy.
  - eventual consistency without reconciliation process.
- Diagnostics checklist:
  - lock-wait profile, replication lag, projection freshness, drift checks.
  - index utility vs write amplification.
  - incident replay for duplicate/out-of-order events.
- Revisit trigger:
  - consistency incidents, lock escalation, stale read models, cost/perf regressions.
<!-- /section:it-db-patterns-v1 -->

<!-- section:it-decision-matrix-v1 -->
## IT Decision Matrix v1
- If dominant pain is lookup latency under high read ratio -> choose hash-based access + cache discipline.
- If dominant pain is ordered/range analytics -> choose sorted/indexed structures + columnar/OLAP path.
- If dominant pain is concurrent writes and integrity -> relational OLTP with strict constraints and explicit isolation.
- If dominant pain is schema volatility with rapid product iteration -> document model with versioned contracts and migration guardrails.
- If dominant pain is graph traversal/dependency reasoning -> graph model or precomputed adjacency strategy.
- If dominant pain is real-time fanout/backpressure -> queue/stream primitives with bounded consumers.
- If dominant pain is cross-service instability -> timeout/retry budget/circuit breaker first, optimization second.
- If dominant pain is p99 spikes without CPU saturation -> inspect network path, queue depth, lock contention, and retries before code rewrite.
- If dominant pain is cost blow-up -> profile by unit economics (cost/request, cost/query, cost-GB) and remove waste by bottleneck order.
- If requirements conflict (latency vs consistency vs cost) -> state tradeoff explicitly and choose by business priority/SLO.
<!-- /section:it-decision-matrix-v1 -->

<!-- section:it-distributed-systems-core-v1 -->
## Distributed Systems Core v1
- Core reality: partial failure is normal, clocks are imperfect, and network partitions are inevitable.
- Decision axes: consistency, availability, partition tolerance, latency, and operability.
- Coordination toolkit: quorum, leader election, leases, fencing tokens, idempotent commands.
- Data movement patterns: event-driven (outbox/CDC), saga orchestration/choreography, compensations.
- State safety: monotonic versioning, conflict resolution policy, replay-safe handlers.
- Anti-patterns: distributed transactions without explicit failure model, hidden coupling via shared DB writes.
- Validation checklist: can the system degrade gracefully under partition, duplicate delivery, and delayed retries?
<!-- /section:it-distributed-systems-core-v1 -->

<!-- section:it-dsa-core-v1 -->
## DSA Core v1 (evidence-first)
- Source anchors:
  - CLRS (Cormen et al.), Algorithms (Sedgewick/Wayne), TAOCP (Knuth), MIT OCW algorithm analysis materials.
- Distilled conclusions:
  - Choose structure by access pattern first (lookup/range/priority/graph traversal), then by memory and concurrency profile.
  - Invariants dominate implementation details: boundary correctness, ordering guarantees, idempotency under retries.
  - Big-O is necessary but insufficient; constants, cache locality, and contention shape real latency.
- Anti-patterns:
  - Premature optimization without measured bottleneck.
  - Copying asymptotically optimal structure into cache-hostile workload.
  - Ignoring worst-case behavior for burst/skewed inputs.
- Diagnostics checklist:
  - Measure p50/p95/p99 and worst-case latency separately.
  - Profile allocation rate, cache misses (when available), lock contention.
  - Validate behavior under skewed keys and burst traffic.
- Revisit trigger:
  - Tail latency regressions, memory ceiling pressure, workload shift (read/write ratio or key distribution changes).
<!-- /section:it-dsa-core-v1 -->

<!-- section:it-dsa-glossary-v1 -->
## DSA Glossary v1 (evidence-first)
- Source anchors:
  - CLRS/TAOCP/Sedgewick terminology conventions.
- Distilled conclusions:
  - Time complexity: growth of operation cost by input size.
  - Space complexity: extra memory cost of computation/storage strategy.
  - Amortized cost: average per operation over a sequence.
  - Locality of reference: memory access pattern impact on cache behavior.
  - Stability (sorting): preservation of relative order for equal keys.
  - Backpressure: producer throttling when consumer capacity is exceeded.
  - Tail latency: p95/p99 behavior, critical for reliability perception.
- Anti-patterns:
  - using glossary terms without measurement context.
- Diagnostics checklist:
  - every term must map to a measurable signal in the system.
- Revisit trigger:
  - repeated misuse of terms in architecture/perf decisions.
<!-- /section:it-dsa-glossary-v1 -->

<!-- section:it-dsa-patterns-v1 -->
## DSA Patterns v1 (evidence-first)
- Source anchors:
  - CLRS, TAOCP (Knuth), Algorithms (Sedgewick/Wayne), systems performance case studies.
- Distilled conclusions:
  - lookup-first: hash map + explicit collision/load-factor policy.
  - ordered/range: balanced tree or sorted array + binary search when writes are rare.
  - burst ingestion: bounded queue/ring buffer + backpressure contract.
  - priority scheduling: heap + starvation guard policy.
  - dependency execution: DAG + topo sort + cycle pre-check.
- Anti-patterns:
  - unbounded structures in burst workloads;
  - algorithm swap without memory/locality analysis;
  - no degradation strategy at capacity limits.
- Diagnostics checklist:
  - queue growth slope, tail latency under burst, memory ceiling behavior.
  - contention points and starvation signals in schedulers.
  - correctness checks for ordering and idempotency.
- Revisit trigger:
  - sustained p99 growth, memory pressure, or workload shape change.
<!-- /section:it-dsa-patterns-v1 -->

<!-- section:it-evidence-first-protocol-v1 -->
## IT Evidence-First Protocol v1
- Scope: applies to all IT domains (algorithms, DB, networks, distributed systems, runtime/OS, security, cloud/platform, observability).
- Rule 1: every durable claim must have source anchors (academic, standards, or primary vendor docs).
- Rule 2: each claim is converted into operational form:
  - invariant,
  - failure boundary,
  - verification method,
  - decision rule.
- Rule 3: separate layers strictly:
  - evidence layer (papers/books/specs/docs),
  - engineering validation layer (benchmarks, incidents, production behavior),
  - distilled memory layer (short actionable rules).
- Rule 4: no doctrine lock-in; competing models are compared by falsifiable criteria and workload fit.
- Rule 5: updates are triggered by new evidence, regressions, or domain shifts.
- Rule 6: source freshness is mandatory via IT Source Freshness Policy v1 (TTL + metadata).
- Output contract per topic:
  - source anchors,
  - distilled conclusions,
  - anti-patterns,
  - diagnostics checklist,
  - revisit trigger.
- Memory hygiene: keep hot-context concise (decision-grade), move long-form evidence to archive/indexed references.
<!-- /section:it-evidence-first-protocol-v1 -->

<!-- section:it-executive-index-v1 -->
## IT Executive Index v1
- Method Backbone:
  - it-layered-method-v1
  - it-master-roadmap-v1
  - it-learning-loop-v1
- Core Domains:
  - it-dsa-core-v1, it-dsa-patterns-v1, it-dsa-glossary-v1
  - it-databases-core-v1, it-db-patterns-v1, it-db-glossary-v1
  - it-network-core-v1, it-network-patterns-v1, it-network-glossary-v1
- Systems/Platform:
  - it-distributed-systems-core-v1
  - it-runtime-os-compiler-v1
  - it-cloud-platform-v1
  - it-security-observability-v1
- Operations:
  - it-operations-runbook-v1
  - it-symptom-playbook-v1
  - it-verification-metrics-v1
  - it-anti-pattern-atlas-v1
- Decision Shortcuts:
  - it-decision-matrix-v1
  - it-phase-a-playbook-v1
- General cognition layer (non-IT):
  - epistemic-methodology-v1
<!-- /section:it-executive-index-v1 -->

<!-- section:it-knowledge-expansion-v1 -->
## IT Knowledge Expansion v1
- Mission: maintain a living, layered IT knowledge graph for agent methodology (not a static encyclopedia dump).
- Scope baseline: algorithms/data structures, databases (all major paradigms), networking, distributed systems, OS internals, security, compilers/runtime, observability, cloud/platform engineering.
- Database facets (required): relational OLTP/OLAP, document, key-value, wide-column, graph, time-series, search engines, stream processing, vector stores, NewSQL, data lake/warehouse patterns.
- Networking facets (required): OSI/TCP-IP grounding, routing/switching, DNS/TLS/HTTP, proxies/load balancers, service mesh, gRPC/WebSocket, reliability/perf diagnostics.
- Learning policy: breadth map first -> depth by active task demand -> archive long-form evidence -> keep hot-context only decision-relevant distilled facts.
- Evidence policy: for code/config/API generation always consult live docs (Context7 / vendor docs) and then store distilled operational conclusions.
- Memory hygiene: keep domain glossary in scope sections, deep rationale in archive layer, and update via concise decision records.
- Prioritization order for next expansion: 1) DSA core, 2) DB paradigms, 3) network stack, 4) distributed systems, 5) security + observability.
- Done criteria: each domain has glossary + decision patterns + troubleshooting playbook + source anchors.
<!-- /section:it-knowledge-expansion-v1 -->

<!-- section:it-layered-method-v1 -->
## IT Layered Method v1
- Принцип: идти от инвариантов к инженерным решениям (не от инструментов к хаосу).
- Слой L1 (Foundations): базовые модели мира (данные, вычисления, сеть, отказ, согласованность).
- Слой L2 (Patterns): устойчивые шаблоны проектирования и эксплуатации.
- Слой L3 (Systems): конкретные стеки/продукты и их ограничения.
- Слой L4 (Operations): диагностика, производительность, инциденты, runbooks.
- Правило перехода: следующий слой открывается только после фиксации decision-rules предыдущего.
- Формат памяти: glossary -> decision patterns -> anti-patterns -> diagnostics checklist.
- Критерий качества: по каждой теме можно ответить на 3 вопроса: "почему так", "когда не так", "как проверить вживую".
<!-- /section:it-layered-method-v1 -->

<!-- section:it-learning-loop-v1 -->
## IT Learning Loop v1
- Loop step 1: classify symptom and impacted layer.
- Loop step 2: formulate 2-3 falsifiable hypotheses.
- Loop step 3: collect minimal evidence that can disprove each hypothesis.
- Loop step 4: apply smallest safe mitigation first, then measure effect.
- Loop step 5: convert incident outcome into pattern/anti-pattern update.
- Loop step 6: add one automation guardrail (alert/test/checklist) per major lesson.
- Memory contract: update hot-context with distilled rule; move raw evidence to archive.
- Exit condition: next similar incident is detected earlier and resolved faster.
<!-- /section:it-learning-loop-v1 -->

<!-- section:it-master-roadmap-v1 -->
## IT Master Roadmap v1
- Phase A (now): DSA + DB + Network + Operations (already seeded in memory).
- Phase B: Distributed systems + Security/Observability + Runtime/OS fundamentals.
- Phase C: Cloud/platform engineering + architecture economics + large-scale diagnostics.
- Phase D: domain-specific depth on demand (data engineering, ML systems, realtime, embedded, etc.).
- Cadence: each phase outputs 4 artifacts: glossary, decision patterns, anti-pattern list, runbook checks.
- Memory contract: hot-context keeps only operational distillate; archive keeps evidence and long-form rationale.
- Quality gate for each domain: explain, decide, implement, diagnose, recover.
<!-- /section:it-master-roadmap-v1 -->

<!-- section:it-network-core-v1 -->
## Network Core v1 (evidence-first)
- Source anchors:
  - RFC 1122/793/9000 family, Google SRE book, Nygard (Release It), cloud vendor reliability docs.
- Distilled conclusions:
  - Every request path decomposes into DNS, connect, TLS, application hop chain, and backend IO.
  - Resilience baseline is timeout hierarchy + bounded retries + jitter + circuit breaking.
  - Idempotency is mandatory where retries are possible.
- Anti-patterns:
  - Unbounded retries and synchronized backoff.
  - Missing timeout boundaries per hop.
  - Treating app errors and transport errors as one bucket.
- Diagnostics checklist:
  - Bucket latency by phase (connect/handshake/TTFB/full body).
  - Observe loss/retransmits, queue depth, saturation, retry ratio.
  - Track breaker-open ratio and dependency error coupling.
- Revisit trigger:
  - Timeout growth, retry storms, p99 amplification without CPU bottleneck, network path changes.
<!-- /section:it-network-core-v1 -->

<!-- section:it-network-glossary-v1 -->
## Network Glossary v1 (evidence-first)
- Source anchors:
  - RFCs (TCP/TLS/HTTP), SRE latency/reliability terminology, cloud networking docs.
- Distilled conclusions:
  - DNS resolution: name-to-address resolution phase before transport.
  - TCP handshake: transport session establishment latency component.
  - TLS handshake: crypto negotiation latency/security boundary.
  - TTFB: time to first response byte from request start.
  - Retransmission: packet resend due to loss/ack timeout.
  - Circuit breaker: controlled halt to failing dependency calls.
  - Jittered backoff: randomized retry spacing to prevent herd effects.
  - Error budget: allowable unreliability under SLO.
- Anti-patterns:
  - mixing transport terms with app-level symptoms without phase separation.
- Diagnostics checklist:
  - every latency/error report must include phase attribution.
- Revisit trigger:
  - repeated misdiagnosis due to missing network phase breakdown.
<!-- /section:it-network-glossary-v1 -->

<!-- section:it-normalization-status-v1 -->
## IT Normalization Status v1
- Goal: migrate all IT memory sections to uniform evidence-first structure.
- Core sections normalized: complete.
- Pattern sections normalized: complete (DSA/DB/Network).
- Glossary sections normalized: complete (DSA/DB/Network).
- Playbook sections normalized: phase-a aligned with evidence-first.
- Remaining ongoing policy:
  - all new IT sections must include source anchors + revisit trigger by default.
  - existing sections are re-reviewed when domain evidence materially changes.
- Next target: introduce explicit source-index map for quick citation retrieval per domain.
<!-- /section:it-normalization-status-v1 -->

<!-- section:it-phase-a-playbook-v1 -->
## IT Phase A Playbook v1 (evidence-first)
- Source anchors:
  - SRE incident loops, performance engineering practices, architecture decision record methods.
- Distilled conclusions:
  - classify workload -> constrain by SLA/SLO -> choose primitives -> instrument -> fail-safe -> validate worst-case -> record decision.
  - mitigation before optimization: stop bleed safely, then refine bottleneck.
  - every decision must be testable and reversible.
- Anti-patterns:
  - jumping to redesign before symptom localization.
  - tuning for average while ignoring tails and bursts.
  - undocumented tradeoffs causing repeated debates.
- Diagnostics checklist:
  - symptom-to-layer mapping exists and is evidence-backed.
  - before/after metrics include p99 and saturation.
  - rollback and idempotency paths are explicit.
- Revisit trigger:
  - unresolved recurring symptom class or decisions that cannot be validated.
<!-- /section:it-phase-a-playbook-v1 -->

<!-- section:it-phase-b-playbook-v1 -->
## IT Phase B Playbook v1 (evidence-first)
- Scope: distributed systems + security/observability + runtime/OS.
- Source anchors:
  - distributed: Lamport/Raft/DDIA/Jepsen,
  - security: OWASP/NIST/CIS,
  - runtime: Systems Performance + runtime/OS docs.
- Distilled conclusions:
  - design for partial failure first;
  - enforce trust boundaries and traceability by default;
  - optimize only after runtime-level evidence (CPU/memory/lock/IO profiles).
- Anti-patterns:
  - "works in happy path" distributed logic,
  - security bolted on after release,
  - runtime blaming without profiling.
- Diagnostics checklist:
  - partition/replay/duplication behavior tests,
  - trace continuity across boundaries,
  - contention, GC, syscall/IO wait evidence.
- Revisit trigger:
  - failover incidents, audit findings, p99/runtime regressions under concurrency.
- Exit condition:
  - system remains understandable and recoverable under partial failures and adversarial conditions.
<!-- /section:it-phase-b-playbook-v1 -->

<!-- section:it-runtime-os-compiler-v1 -->
## Runtime OS Compiler Core v1 (evidence-first)
- Source anchors:
  - Systems Performance (Gregg), CLR/JVM runtime docs, compiler optimization references, OS scheduling/memory docs.
- Distilled conclusions:
  - Runtime performance emerges from algorithm + memory layout + scheduler + IO behavior.
  - Allocation rate and object lifetime shape GC pauses and throughput.
  - Contention and context switching can dominate CPU-heavy assumptions.
- Anti-patterns:
  - Blaming GC without allocation and pause evidence.
  - Lock-heavy hot paths with broad critical sections.
  - Unbounded thread/task fan-out under load.
- Diagnostics checklist:
  - CPU flamegraph/profile, allocation profile, lock contention profile.
  - GC pause metrics and heap growth trends.
  - Syscall/IO wait and scheduler pressure.
- Revisit trigger:
  - Throughput collapse at higher concurrency, rising GC pauses, lock contention cliffs.
<!-- /section:it-runtime-os-compiler-v1 -->

<!-- section:it-security-observability-v1 -->
## Security and Observability Core v1 (evidence-first)
- Source anchors:
  - OWASP ASVS/Top 10, NIST 800-series, CIS controls, OpenTelemetry specs, SRE observability practices.
- Distilled conclusions:
  - Security posture is defense-in-depth: least privilege, secret hygiene, supply-chain controls, continuous patching.
  - Observability must preserve causality across services (trace/span/request IDs end-to-end).
  - Alerts are useful only when tied to concrete first action and SLO impact.
- Anti-patterns:
  - Logs without correlation IDs.
  - Alert storms without dedup or ownership.
  - Security checks only at release time (no continuous controls).
- Diagnostics checklist:
  - Verify trace propagation integrity across async boundaries.
  - Measure MTTD/MTTR and alert actionability ratio.
  - Track vuln age, patch cadence, secret rotation compliance.
- Revisit trigger:
  - Incident response delays, repeated blind spots, audit findings, rising alert fatigue.
<!-- /section:it-security-observability-v1 -->

<!-- section:it-source-citation-contract-v1 -->
## IT Source Citation Contract v1
- Minimal citation contract per new section/update:
  - 1 foundational source (book/paper/spec),
  - 1 current operational source (vendor docs/SRE practice),
  - 1 validation path (metric, benchmark, or incident evidence).
- Citation style in notes:
  - keep source names short in hot-context;
  - keep long references/links in archive index.
- Evidence quality ladder:
  1) standards/specs and foundational papers,
  2) official runtime/database/network docs,
  3) production incident reports and measured benchmarks,
  4) blog/opinion only as supplemental context.
- Conflict resolution:
  - when sources disagree, prefer the source closest to workload and verification data.
- Revisit trigger:
  - major version shifts, changed defaults in runtimes/DB/network stacks, or contradictory production evidence.
<!-- /section:it-source-citation-contract-v1 -->

<!-- section:it-source-freshness-policy-v1 -->
## IT Source Freshness Policy v1
- Goal: keep evidence operationally current without polluting hot-context with volatile links.
- Source classes:
  - foundational: books, seminal papers, core RFC families.
  - operational: vendor docs, runtime defaults, cloud/platform guidance, release notes.
  - incident-evidence: internal postmortems, benchmark reports, regression analyses.
- Refresh cadence (TTL):
  - foundational: review every 180-365 days.
  - operational: review every 30-90 days.
  - incident-evidence: review on every major incident/release cycle.
- Mandatory metadata per tracked source entry:
  - source_class,
  - volatility (low/medium/high),
  - last_verified (YYYY-MM-DD),
  - verification_scope (what was checked),
  - next_review_by (YYYY-MM-DD).
- Triggered refresh (outside cadence):
  - major version upgrade,
  - changed defaults/deprecations,
  - contradictory production evidence,
  - security advisory affecting assumptions.
- Memory placement:
  - hot-context: distilled rules and stable anchors only.
  - archive/index: full URLs, versions, changelog pointers.
<!-- /section:it-source-freshness-policy-v1 -->

<!-- section:it-source-index-map-v1 -->
## IT Source Index Map v1
- DSA / Algorithms:
  - CLRS (Cormen et al.)
  - TAOCP (Knuth)
  - Algorithms (Sedgewick/Wayne)
- Databases:
  - Transaction Processing (Gray/Reuter)
  - Designing Data-Intensive Applications (Kleppmann)
  - PostgreSQL official docs
  - SQL Server official docs
- Networking / Resilience:
  - RFC corpus (TCP/IP, TLS, HTTP families)
  - Google SRE book/workbook
  - Release It (Nygard)
- Distributed Systems:
  - Lamport foundational papers
  - Raft paper
  - Jepsen analyses
  - DDIA distributed chapters
- Runtime / OS / Performance:
  - Systems Performance (Brendan Gregg)
  - CLR/.NET runtime docs
  - OS kernel/scheduler/memory official docs per target platform
- Security:
  - OWASP ASVS / Top 10
  - NIST 800-series
  - CIS controls
- Observability:
  - OpenTelemetry specifications
  - SRE observability/reliability practices
- Cloud / Platform Engineering:
  - DORA research
  - Well-Architected frameworks (major cloud vendors)
  - IaC best-practice docs (Terraform/Pulumi/vendor-native)
- Method note:
  - For any new claim: pick at least one source from this map + one operational validation signal.
<!-- /section:it-source-index-map-v1 -->

<!-- section:it-source-mini-index-v1 -->
## IT Source Mini-Index v1 (L1)
Содержимое в knowledge/agent-notes-l1-pool.md. Загружать по запросу: route_context('IT source'|'source index') или чтение pool.
(L1: полный список entries в knowledge/agent-notes-l1-pool.md.)
<!-- /section:it-source-mini-index-v1 -->

<!-- section:it-symptom-playbook-v1 -->
## IT Symptom Playbook v1
- Symptom: "system is slow"
  - Check: p50/p95/p99 split, CPU/memory saturation, queue depth, downstream latency.
  - Typical causes: hidden retries, lock contention, hot keys, DB scan, network retransmits.
  - First action: isolate dominant stage in critical path before touching code.
- Symptom: "timeouts increase"
  - Check: connect vs handshake vs TTFB timeout buckets.
  - Typical causes: dependency saturation, DNS/TLS issues, connection pool starvation.
  - First action: tighten timeout hierarchy and retry budgets.
- Symptom: "DB lock waits"
  - Check: lock graphs, long transactions, isolation level, missing/inefficient indexes.
  - Typical causes: wide update scope, inconsistent access order, analytical queries on OLTP.
  - First action: shorten transaction scope, fix index/query path, separate analytical load.
- Symptom: "p99 spikes only"
  - Check: tail amplification by queues, GC pauses, noisy neighbors, retry storms.
  - Typical causes: burst traffic, contention cliffs, cache stampede.
  - First action: cap concurrency + add admission control + warm critical caches.
- Symptom: "packet loss/retransmits"
  - Check: interface errors, congestion, MTU mismatch, LB health behavior.
  - Typical causes: link saturation, bad path, misconfigured networking.
  - First action: reroute/relieve congestion and verify transport tuning.
- Symptom: "retry storm"
  - Check: retry rate, breaker state, upstream/downstream error coupling.
  - Typical causes: synchronized retries without jitter, no fail-fast policy.
  - First action: enforce jittered backoff, global retry budget, and circuit breaker gates.
<!-- /section:it-symptom-playbook-v1 -->

