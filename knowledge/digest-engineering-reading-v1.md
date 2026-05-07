# Engineering Reading Digest v1

**Legacy.** Каноническая база знаний — `kb-engineering-evidence-v1.md` (записи по темам). Этот файл сохранён как архив выписок по батчам.

## Purpose
Accumulated distilled notes from completed reading with direct applicability to .NET engineering work.

## Entry Template
- Source:
- Date:
- Fact:
- Heuristic:
- First adoption task:
- Success criterion:
- Confidence:

## Batch 01 (Completed): Platform Baseline

### Entry 01
- Source: Microsoft Learn - What's new in C# 14 (`https://learn.microsoft.com/dotnet/csharp/whats-new/csharp-14`)
- Date: 2026-02-25
- Fact: C# 14 introduces extension members, null-conditional assignment, field-backed properties, enhanced span conversions, and partial constructors/events.
- Heuristic: treat language features as selective leverage; adopt only where they reduce complexity or runtime overhead in active code.
- First adoption task: evaluate `field`-backed property and null-conditional assignment opportunities in actively edited domain models/view models.
- Success criterion: reduced boilerplate without added ambiguity in code review.
- Confidence: medium

### Entry 02
- Source: Microsoft Learn - C# language versioning (`https://learn.microsoft.com/dotnet/csharp/language-reference/language-versioning`)
- Date: 2026-02-25
- Fact: C# 14 is supported on .NET 10+; compiler defaults are TFM-aligned; using newer-than-TFM language combinations is unsupported.
- Heuristic: keep language policy deterministic and framework-compatible to avoid machine-specific breakage.
- First adoption task: verify solution-wide TFM and LangVersion policy in shared build config.
- Success criterion: no unsupported language/runtime combinations across projects.
- Confidence: high

### Entry 03
- Source: Microsoft Learn - What's new in .NET 10 (`https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/overview`)
- Date: 2026-02-25
- Fact: .NET 10 (LTS) includes runtime, SDK, testing platform, and libraries improvements relevant to performance and delivery workflows.
- Heuristic: upgrade decisions should be driven by measurable gains (build/test/debug/latency), not by novelty.
- First adoption task: define a small before/after benchmark set for representative workloads.
- Success criterion: evidence-backed upgrade value on local project metrics.
- Confidence: medium

### Entry 04
- Source: Microsoft Learn - Unit testing best practices for .NET (`https://learn.microsoft.com/dotnet/core/testing/unit-testing-best-practices`)
- Date: 2026-02-25
- Fact: resilient tests are fast, isolated, repeatable, and readable; avoid infrastructure in unit tests; prefer AAA and one Act per test.
- Heuristic: test quality is constrained more by design and readability than by raw coverage percentage.
- First adoption task: enforce naming/AAA/one-Act conventions in newly added tests and refactor flaky patterns.
- Success criterion: lower flaky test rate and faster root-cause detection in CI/local runs.
- Confidence: high

## Queue (Next Sources)
- C# in Depth (Skeet) - language semantics and hidden sharp edges.
- Pro .NET Memory Management (Kokosa) - GC and allocation strategy.
- xUnit Test Patterns (Meszaros) - test smell catalog and remediation.
- Working Effectively with Legacy Code (Feathers) - seam-first recovery strategy.
- Designing Data-Intensive Applications (Kleppmann) - data-system tradeoffs.

## Batch 02 (Completed): Test and Diagnostics Foundations

### Entry 05
- Source: Microsoft Learn - Integration tests in ASP.NET Core (`https://learn.microsoft.com/aspnet/core/test/integration-tests?view=aspnetcore-10.0`)
- Date: 2026-02-25
- Fact: integration tests should cover critical infrastructure boundaries (DB/files/network/request pipeline), while broad permutation coverage remains in unit tests for speed.
- Heuristic: reserve integration tests for high-risk seams and use `WebApplicationFactory` + `TestServer` as the standard host pattern.
- First adoption task: define a minimal integration suite for critical HTTP flows, persistence boundary, and auth boundary.
- Success criterion: critical path regressions are caught without major slowdown in feedback cycle.
- Confidence: high

### Entry 06
- Source: Microsoft Learn - .NET diagnostic tools overview (`https://learn.microsoft.com/dotnet/core/diagnostics/tools-overview`)
- Date: 2026-02-25
- Fact: first-line diagnosis should start with counters/stacks/traces (`dotnet-counters`, `dotnet-stack`, `dotnet-trace`) before deep dump analysis.
- Heuristic: use staged diagnostics escalation (health signals -> trace -> dump) to reduce time-to-root-cause.
- First adoption task: create a lightweight diagnostics runbook mapping common symptoms to first tool choice.
- Success criterion: lower mean time to identify root cause in CPU/memory/thread incidents.
- Confidence: high

### Entry 07
- Source: Microsoft Learn - Testing with `dotnet test` (`https://learn.microsoft.com/dotnet/core/testing/unit-testing-with-dotnet-test`)
- Date: 2026-02-25
- Fact: .NET 10 introduces Microsoft.Testing.Platform mode for `dotnet test`; mixed VSTest/MTP usage is discouraged.
- Heuristic: keep one consistent test runner model solution-wide to avoid silent option mismatches and unsupported configurations.
- First adoption task: decide and document single runner mode for active solutions (`global.json` + shared props policy).
- Success criterion: deterministic local/CI test behavior without mode-dependent surprises.
- Confidence: medium

### Entry 08
- Source: xUnit docs via Context7 (`/xunit/xunit.net`) - shared context and fixtures guidance
- Date: 2026-02-25
- Fact: xUnit creates a new test class instance per test; shared setup should use fixtures (`IClassFixture`, `ICollectionFixture`, assembly fixtures) deliberately.
- Heuristic: default to isolated tests and introduce shared fixtures only for expensive immutable context.
- First adoption task: audit existing test classes for hidden shared mutable state and migrate to explicit fixture patterns where needed.
- Success criterion: reduced flakiness and clearer test lifecycle semantics.
- Confidence: high

## Batch 03 (Completed): Async and Web Reliability

### Entry 09
- Source: Microsoft Learn - ASP.NET Core Best Practices (`https://learn.microsoft.com/aspnet/core/fundamentals/best-practices?view=aspnetcore-10.0`)
- Date: 2026-02-25
- Fact: reliability and throughput depend on async end-to-end paths, avoiding sync-over-async, reducing LOH pressure, and keeping hot paths minimal.
- Heuristic: treat thread-pool starvation and allocation spikes as first-class regressions, not incidental performance noise.
- First adoption task: create a concise checklist for controller/middleware reviews (async I/O, pagination, HttpClientFactory, no captured HttpContext in background tasks).
- Success criterion: fewer starvation-related incidents and lower p95 latency variance.
- Confidence: high

### Entry 10
- Source: Microsoft Learn - Asynchronous programming scenarios (`https://learn.microsoft.com/dotnet/csharp/asynchronous-programming/async-scenarios`)
- Date: 2026-02-25
- Fact: choose async strategy by workload type (I/O-bound vs CPU-bound), use `Task.WhenAll/WhenAny`, avoid blocking waits (`Wait/Result`), and force immediate LINQ task materialization (`ToArray/ToList`).
- Heuristic: async correctness is mostly about preserving non-blocking flow and explicit concurrency boundaries.
- First adoption task: audit existing async code for blocking calls and deferred LINQ task pitfalls.
- Success criterion: no deadlock-prone patterns in newly touched modules.
- Confidence: high

### Entry 11
- Source: Microsoft Learn - EventCounters tutorial (`https://learn.microsoft.com/dotnet/core/diagnostics/event-counter-perf`)
- Date: 2026-02-25
- Fact: low-overhead operational telemetry can be established with `EventSource/EventCounter` plus `dotnet-counters monitor/collect`.
- Heuristic: instrument first, optimize second; track trend over time instead of single-point snapshots.
- First adoption task: define a minimal counter set for active services (`requests/sec`, request latency metric, `cpu-usage`) and capture baseline traces.
- Success criterion: at least one reproducible before/after performance baseline per optimization cycle.
- Confidence: medium

## Batch 04 (Completed): Platform Evolution and Data Layer

### Entry 12
- Source: Microsoft Learn - What's new in .NET 10 runtime (`https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/runtime`)
- Date: 2026-02-25
- Fact: .NET 10 runtime improves JIT codegen/inlining/devirtualization, broadens stack allocation scenarios, and reduces abstraction overhead in common patterns.
- Heuristic: performance work should prioritize shape-friendly code that the JIT can optimize (tight loops, predictable allocations, clear call paths).
- First adoption task: identify one hot path and test whether minor code-shape changes produce measurable JIT wins in Release mode.
- Success criterion: observable CPU or latency improvement with no semantic regression.
- Confidence: medium

### Entry 13
- Source: Microsoft Learn - What's new in ASP.NET Core 10 (`https://learn.microsoft.com/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0`)
- Date: 2026-02-25
- Fact: ASP.NET Core 10 introduces meaningful behavior changes (for example, streaming defaults in some client paths) and template/runtime-level UX/security updates.
- Heuristic: release upgrades require explicit audit of behavioral defaults, not only API compilation success.
- First adoption task: create upgrade checklist item for runtime behavior deltas impacting networking/streaming/security-sensitive flows.
- Success criterion: no unexpected post-upgrade runtime behavior in critical scenarios.
- Confidence: medium

### Entry 14
- Source: Microsoft Learn - What's new in EF Core 10 (`https://learn.microsoft.com/ef/core/what-is-new/ef-core-10.0/whatsnew`)
- Date: 2026-02-25
- Fact: EF Core 10 adds major capabilities (JSON/vector support, named filters, richer translation controls, improved bulk update ergonomics) and updates SQL generation strategies.
- Heuristic: treat ORM upgrades as query-planning events; verify generated SQL and plan behavior on representative workloads.
- First adoption task: select 2-3 high-impact queries and compare generated SQL/plans before and after EF10 adoption.
- Success criterion: neutral or improved query stability and performance under production-like data shapes.
- Confidence: medium

### Entry 15
- Source: Microsoft Learn - Microsoft.Testing.Platform intro (`https://learn.microsoft.com/dotnet/core/testing/microsoft-testing-platform-intro`)
- Date: 2026-02-25
- Fact: MTP emphasizes deterministic, hostable, low-dependency test execution and aligns with .NET 10 `dotnet test` evolution.
- Heuristic: prefer one deterministic test execution model per repo to avoid mode split and inconsistent tooling behavior.
- First adoption task: define repository-wide test runner stance and codify it in `global.json` + shared test project policy.
- Success criterion: identical local and CI test semantics for the same commit.
- Confidence: high

### Entry 16
- Source: Microsoft Learn - C# language versioning + C# 14 (`https://learn.microsoft.com/dotnet/csharp/language-reference/language-versioning`, `https://learn.microsoft.com/dotnet/csharp/whats-new/csharp-14`)
- Date: 2026-02-25
- Fact: C# 14 support is bound to .NET 10+ targets; mismatched language/runtime combinations are unsupported and risk subtle failures.
- Heuristic: pin language-policy by TFM and avoid machine-dependent compiler behavior for shared codebases.
- First adoption task: validate that active projects target `.NET 10` where C# 14 features are expected, and enforce explicit fallback for older targets.
- Success criterion: no unsupported language-version combinations in build matrix.
- Confidence: high

### Entry 17
- Source: Microsoft Learn - Testing with `dotnet test` in .NET 10 (`https://learn.microsoft.com/dotnet/core/testing/unit-testing-with-dotnet-test`)
- Date: 2026-02-25
- Fact: .NET 10 differentiates VSTest mode and MTP mode with concrete migration steps; mixed assumptions can silently ignore options.
- Heuristic: command-line compatibility must be treated as contract and verified in CI scripts after runner migration.
- First adoption task: add CI smoke command set that validates expected test runner options and exit behavior.
- Success criterion: no silently ignored critical test arguments in CI.
- Confidence: medium

## Batch 05 (Completed): Perf Diagnostics and Query Efficiency

### Entry 18
- Source: Microsoft Learn - Debug high CPU usage (`https://learn.microsoft.com/dotnet/core/diagnostics/debug-highcpu`)
- Date: 2026-02-25
- Fact: high-CPU investigation is most effective with staged workflow: verify counters, capture trace, inspect call stacks/hot methods.
- Heuristic: always separate symptom confirmation (`dotnet-counters`) from causal analysis (`dotnet-trace` + stack/call-tree tools).
- First adoption task: standardize a high-CPU playbook for active services with fixed capture duration and artifact naming.
- Success criterion: repeatable hotspot identification in one diagnostic cycle.
- Confidence: high

### Entry 19
- Source: Microsoft Learn - Debug a memory leak (`https://learn.microsoft.com/dotnet/core/diagnostics/debug-memory-leak`)
- Date: 2026-02-25
- Fact: leak diagnosis requires both growth confirmation over time and heap root analysis from dumps, not only working-set observation.
- Heuristic: use object-root chains (`gcroot`) to find ownership leaks rather than guessing from type counts alone.
- First adoption task: add memory-leak checklist (baseline -> load -> counters -> dump -> root analysis).
- Success criterion: identified retaining owner for major leaked object classes.
- Confidence: high

### Entry 20
- Source: Microsoft Learn - Debug ThreadPool starvation (`https://learn.microsoft.com/dotnet/core/diagnostics/debug-threadpool-starvation`)
- Date: 2026-02-25
- Fact: starvation is strongly indicated by sustained thread count growth with low CPU saturation and blocking stacks on ThreadPool workers.
- Heuristic: treat sync-over-async (`.Result/.Wait`) as critical risk in request paths and enforce async end-to-end.
- First adoption task: run static/targeted audit for blocking waits in request handlers and service hot paths.
- Success criterion: no blocking wait pattern in newly changed high-traffic paths.
- Confidence: high

### Entry 21
- Source: Microsoft Learn - dotnet-trace utility (`https://learn.microsoft.com/dotnet/core/diagnostics/dotnet-trace`)
- Date: 2026-02-25
- Fact: `dotnet-trace` provides cross-platform EventPipe-based traces with tunable providers/profiles and controlled duration for production-safe capture.
- Heuristic: keep trace collection scope narrow (providers + duration) to reduce noise and dropped events.
- First adoption task: define default trace presets for CPU, contention, and GC investigations.
- Success criterion: actionable traces with low event-loss and clear analysis target.
- Confidence: medium

### Entry 22
- Source: Microsoft Learn - Unit testing code coverage (`https://learn.microsoft.com/dotnet/core/testing/unit-testing-code-coverage`)
- Date: 2026-02-25
- Fact: coverage metrics are useful as feedback signals but not as standalone quality proxy; tooling should feed branch-level insight into review workflow.
- Heuristic: optimize for meaningful test behavior coverage, not maximal percentage.
- First adoption task: publish baseline coverage report generation path (`coverlet` + report generator) for CI/local parity.
- Success criterion: stable and readable coverage artifacts per test run.
- Confidence: medium

### Entry 23
- Source: Microsoft Learn - EF Core efficient querying (`https://learn.microsoft.com/ef/core/performance/efficient-querying`)
- Date: 2026-02-25
- Fact: major EF perf wins come from indexing alignment, selective projection, controlled result size, eager/split loading strategy, and tracking-mode choice.
- Heuristic: query performance is primarily data-shape and SQL-plan driven; ORM API choices should be evaluated by generated SQL and execution plans.
- First adoption task: audit top read queries for over-projection, missing pagination, and unnecessary tracking.
- Success criterion: reduced query latency and allocation for selected hot queries.
- Confidence: high

## Batch 06 (Completed): Architecture and Testing Methodology

### Entry 24
- Source: Refactoring.Guru - Code Smells (`https://refactoring.guru/refactoring/smells`)
- Date: 2026-02-25
- Fact: smell taxonomy (bloaters, couplers, dispensables, change preventers, OOP abusers) provides a practical lens for refactoring prioritization.
- Heuristic: classify before changing; choose refactoring moves by smell class rather than ad-hoc stylistic edits.
- First adoption task: add lightweight PR-review smell tags (`duplicate code`, `long method`, `feature envy`, `shotgun surgery`) for changed files.
- Success criterion: recurring refactoring decisions become faster and more consistent.
- Confidence: medium

### Entry 25
- Source: Refactoring.Guru - Design Patterns Catalog (`https://refactoring.guru/design-patterns/catalog`)
- Date: 2026-02-25
- Fact: pattern selection remains most effective when mapped to change pressure (creation flexibility, composition constraints, behavior variability).
- Heuristic: treat patterns as response to concrete forces, not as architecture defaults.
- First adoption task: for each new abstraction, require one-sentence force statement before introducing a pattern.
- Success criterion: lower accidental complexity from unnecessary abstractions.
- Confidence: medium

### Entry 26
- Source: Martin Fowler - Patterns of Enterprise Application Architecture catalog (`https://martinfowler.com/eaaCatalog/`)
- Date: 2026-02-25
- Fact: enterprise systems benefit from explicit pattern choices around domain logic, mapping, transactional boundaries, and integration seams.
- Heuristic: make data-access and domain-boundary patterns explicit in architecture docs to avoid hidden coupling drift.
- First adoption task: map current persistence strategy to EAA vocabulary (`Repository`, `Unit of Work`, `Data Mapper`) and document intent.
- Success criterion: clearer architectural communication and fewer contradictory implementations.
- Confidence: high

### Entry 27
- Source: Martin Fowler - The Practical Test Pyramid (`https://martinfowler.com/articles/practical-test-pyramid.html`)
- Date: 2026-02-25
- Fact: effective test portfolios prioritize many fast low-level tests, fewer integration tests, and very limited end-to-end tests.
- Heuristic: optimize for feedback speed and maintainability; avoid test-suite shape drift toward slow end-to-end-heavy layers.
- First adoption task: categorize existing tests by pyramid layer and identify overrepresented expensive layers.
- Success criterion: reduced end-to-end dependence and faster median CI cycle.
- Confidence: high

### Entry 28
- Source: Martin Fowler - CQRS (`https://martinfowler.com/bliki/CQRS.html`)
- Date: 2026-02-25
- Fact: CQRS is situational; it can help in complex/high-scale bounded contexts but often introduces harmful complexity when applied broadly.
- Heuristic: apply CQRS only where read/write model divergence is proven by domain or scaling constraints.
- First adoption task: introduce architecture decision check requiring explicit bounded-context and complexity tradeoff when proposing CQRS.
- Success criterion: fewer premature split-model designs with weak justification.
- Confidence: high

### Entry 29
- Source: Twelve-Factor App (`https://12factor.net/`)
- Date: 2026-02-25
- Fact: deployment resilience and portability improve with strict config separation, stateless processes, and dev/prod parity discipline.
- Heuristic: delivery robustness should be encoded into runtime/process contracts, not left to operator convention.
- First adoption task: evaluate active services against 12-factor checklist and log highest-risk gaps.
- Success criterion: reduced environment-specific failures across local/stage/prod.
- Confidence: medium

## Batch 07 (Completed): Data and Resilience Infrastructure

### Entry 30
- Source: PostgreSQL docs - Index introduction (`https://www.postgresql.org/docs/current/indexes-intro.html`)
- Date: 2026-02-25
- Fact: index value comes from selectivity and planner statistics; indexing adds write overhead and must be justified by query workload.
- Heuristic: treat every index as a read/write tradeoff decision with maintenance cost.
- First adoption task: inventory frequently used indexes and remove low-value prefixes/duplicates.
- Success criterion: stable or improved query latency with no unnecessary index maintenance burden.
- Confidence: high

### Entry 31
- Source: PostgreSQL docs - Using EXPLAIN (`https://www.postgresql.org/docs/current/using-explain.html`)
- Date: 2026-02-25
- Fact: plan analysis requires comparing estimates vs actuals (`EXPLAIN ANALYZE`) and understanding join/scan node composition.
- Heuristic: SQL tuning should begin with plan literacy, not blind query rewrites.
- First adoption task: introduce plan-review template for critical queries (node type, row estimate error, dominant cost).
- Success criterion: faster root-cause isolation for slow query incidents.
- Confidence: high

### Entry 32
- Source: SQLite docs - Query planner (`https://sqlite.org/queryplanner.html`)
- Date: 2026-02-25
- Fact: multi-column and covering indexes materially reduce lookup/sort cost; index order strongly shapes planner effectiveness.
- Heuristic: index design must mirror real filter and ordering patterns.
- First adoption task: validate that mobile/embedded query patterns align with left-prefix and covering-index opportunities.
- Success criterion: lower scan/sort overhead in representative SQLite workloads.
- Confidence: medium

### Entry 33
- Source: Redis docs - Diagnosing latency (`https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency/`)
- Date: 2026-02-25
- Fact: Redis latency spikes often originate from environment/OS constraints (intrinsic latency, THP, fork, swap, slow commands), not Redis core command cost alone.
- Heuristic: troubleshoot from infrastructure baseline upward before optimizing command-level logic.
- First adoption task: create Redis latency checklist (intrinsic latency, slowlog, THP, fork time, swap, AOF/fsync profile).
- Success criterion: quicker discrimination between infra-induced and workload-induced latency.
- Confidence: high

### Entry 34
- Source: Azure Architecture Center - CQRS pattern (`https://learn.microsoft.com/azure/architecture/patterns/cqrs`)
- Date: 2026-02-25
- Fact: CQRS can improve scalability and boundary clarity but introduces synchronization and eventual-consistency complexity.
- Heuristic: adopt CQRS only with clear asymmetry in read/write requirements or explicit bounded-context complexity.
- First adoption task: require ADR section for consistency model and synchronization strategy in CQRS proposals.
- Success criterion: fewer architecture reversals caused by underestimated complexity.
- Confidence: high

### Entry 35
- Source: Azure Architecture Center - Retry pattern (`https://learn.microsoft.com/azure/architecture/patterns/retry`)
- Date: 2026-02-25
- Fact: robust retries depend on transient-fault classification, backoff strategy, idempotency guarantees, and bounded attempts.
- Heuristic: retries are reliability controls, not universal error handling.
- First adoption task: define per-dependency retry profiles (attempts, backoff, timeout, circuit-breaker interplay).
- Success criterion: fewer cascading failures and reduced tail-latency amplification under partial outages.
- Confidence: high

## Batch 08 (Completed): Agile Architecture and Fault Isolation

### Entry 36
- Source: Microsoft Learn - Architectural principles (`https://learn.microsoft.com/dotnet/architecture/modern-web-apps-azure/architectural-principles`)
- Date: 2026-02-25
- Fact: maintainable systems consistently rely on separation of concerns, encapsulation, dependency inversion, explicit dependencies, and bounded contexts.
- Heuristic: architecture quality improves when dependencies point toward abstractions and domain logic remains isolated from infrastructure/UI.
- First adoption task: add architecture review checklist for new modules (SoC, DIP, explicit dependencies, bounded context boundary).
- Success criterion: fewer cross-layer leaks and easier testability of business logic.
- Confidence: high

### Entry 37
- Source: Microsoft Learn - Domain model validations (`https://learn.microsoft.com/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-model-layer-validations`)
- Date: 2026-02-25
- Fact: aggregate/domain invariants must be enforced in domain behavior, not delegated only to UI binding or persistence metadata.
- Heuristic: domain entities should be invalid-state resistant by construction and mutation methods.
- First adoption task: review aggregate roots for invariant enforcement in constructors/mutators and close annotation-only validation gaps.
- Success criterion: invalid domain state cannot be persisted through normal code paths.
- Confidence: high

### Entry 38
- Source: Azure Architecture Center - Circuit Breaker (`https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker`)
- Date: 2026-02-25
- Fact: circuit breakers mitigate persistent or slow-recovery dependencies through closed/open/half-open state transitions and controlled probes.
- Heuristic: retries should be bounded by breaker state; fallback behavior must be explicit for degraded mode.
- First adoption task: define breaker policy per critical dependency (trip threshold, open duration, half-open probe count, fallback contract).
- Success criterion: reduced cascading failure during dependency outages.
- Confidence: high

### Entry 39
- Source: Martin Fowler - Unit Test (`https://martinfowler.com/bliki/UnitTest.html`)
- Date: 2026-02-25
- Fact: unit tests are fundamentally about fast feedback on small scopes; sociable vs solitary style is contextual, but speed and frequency are key.
- Heuristic: tune test suites for feedback cadence (compile suite and commit suite) rather than ideological purity.
- First adoption task: define runtime budget targets for local and CI test suites and classify tests by intended feedback loop.
- Success criterion: developers run tests frequently without friction and detect regressions earlier.
- Confidence: high

### Entry 40
- Source: Martin Fowler - Mocks Aren't Stubs (`https://martinfowler.com/articles/mocksArentStubs.html`)
- Date: 2026-02-25
- Fact: behavior-verification mocks and state-verification doubles serve different purposes; misuse increases coupling or obscures failures.
- Heuristic: choose doubles intentionally by collaboration risk (determinism, speed, boundary awkwardness), not by framework habit.
- First adoption task: add test review guidance distinguishing mock/stub/fake usage and expected verification mode.
- Success criterion: lower test brittleness and clearer failure diagnostics.
- Confidence: medium

### Entry 41
- Source: Martin Fowler - YAGNI (`https://martinfowler.com/bliki/Yagni.html`)
- Date: 2026-02-25
- Fact: speculative features impose build cost, delay cost, and carry cost; only malleable codebases can safely defer features.
- Heuristic: avoid presumptive abstractions unless immediate value is clear and complexity is near-zero.
- First adoption task: require explicit justification for "future-proofing" code in PRs/ADRs.
- Success criterion: reduced accidental complexity and faster delivery of current-value features.
- Confidence: high

## Batch 09 (Completed): Algorithmic Depth, Reliability, and Security Baselines

### Entry 42
- Source: Sedgewick/Wayne Algorithms, 4th edition site (`https://algs4.cs.princeton.edu/home/`)
- Date: 2026-02-25
- Fact: practical algorithm competence depends on fluency across core chapters: fundamentals, sorting, searching, graphs, strings, and context-driven applications.
- Heuristic: treat DS/A as an operational toolkit; map each production bottleneck to one or two candidate algorithm families before optimizing code.
- First adoption task: add "algorithm choice" section to performance investigations (data shape, operation complexity, memory tradeoff, expected scale).
- Success criterion: fewer ad-hoc optimizations and clearer complexity reasoning in design reviews.
- Confidence: high

### Entry 43
- Source: MIT OCW 6.006 Introduction to Algorithms (`https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/`)
- Date: 2026-02-25
- Fact: strong algorithm engineering links mathematical modeling, asymptotic analysis, and implementation constraints in one loop.
- Heuristic: validate algorithmic decisions with both proof-level complexity expectations and empirical benchmarks on realistic workloads.
- First adoption task: include one theoretical bound and one measured benchmark for each non-trivial algorithmic change.
- Success criterion: architecture decisions retain both analytical justification and runtime evidence.
- Confidence: high

### Entry 44
- Source: Use The Index, Luke (`https://use-the-index-luke.com/`)
- Date: 2026-02-25
- Fact: indexing is fundamentally a development-time concern; query shape, predicate form, and pagination strategy dominate SQL performance outcomes.
- Heuristic: design indexes from real query patterns (filter + sort + join), then verify plan behavior instead of relying on default ORM generation.
- First adoption task: capture top query patterns and align index strategy (covering/composite/partial) with execution plans.
- Success criterion: improved p95 query latency with controlled write overhead.
- Confidence: high

### Entry 45
- Source: Google SRE Book TOC (`https://sre.google/sre-book/table-of-contents/`)
- Date: 2026-02-25
- Fact: reliability at scale is a coherent practice stack (SLOs, alerting, on-call, incident response, postmortems, toil reduction, release engineering).
- Heuristic: treat reliability as a product loop, not as isolated incident handling.
- First adoption task: define minimal reliability operating model for active services (SLO, alert policy, incident template, postmortem cadence).
- Success criterion: clearer operational ownership and faster recovery cycles.
- Confidence: medium

### Entry 46
- Source: OWASP Top 10 project (`https://owasp.org/www-project-top-ten/`)
- Date: 2026-02-25
- Fact: OWASP Top 10 remains a baseline security awareness standard; current reference line points to 2025 update with structured data-driven process.
- Heuristic: secure coding baselines should be integrated into development workflow (threat review, code review, dependency and input handling checks).
- First adoption task: establish Top-10-mapped secure coding checklist for PR review and test scenarios.
- Success criterion: earlier detection of common web security risk classes before release.
- Confidence: medium

### Entry 47
- Source: Martin Fowler - Technical Debt (`https://martinfowler.com/bliki/TechnicalDebt.html`)
- Date: 2026-02-25
- Fact: debt is useful as a decision metaphor only when teams explicitly reason about interest vs principal and pay down high-interest hotspots progressively.
- Heuristic: prioritize debt repayment in high-change areas where interest compounds fastest.
- First adoption task: add technical debt annotation to backlog items with "interest signal" (change frequency, cycle delay, defect amplification).
- Success criterion: reduced delivery slowdown in frequently modified modules.
- Confidence: high

## Batch 10 (Completed): Platform Reliability and Delivery Operations

### Entry 48
- Source: Azure Well-Architected - Reliability checklist (`https://learn.microsoft.com/power-platform/well-architected/reliability/checklist#checklist`)
- Date: 2026-02-25
- Fact: reliability can be operationalized as a concrete control loop: flow criticality, failure-mode analysis, target metrics, resiliency tests, BCDR, and monitoring strategy.
- Heuristic: treat reliability as a checklist-backed engineering discipline, not an ad-hoc incident reaction.
- First adoption task: run RE:01-RE:08 checklist against one active service and record gaps as prioritized backlog items.
- Success criterion: visible reduction of unknown failure modes and clearer recovery playbooks.
- Confidence: high

### Entry 49
- Source: Azure Well-Architected - Operational Excellence checklist (`https://learn.microsoft.com/azure/well-architected/operational-excellence/checklist#checklist`)
- Date: 2026-02-25
- Fact: stable delivery quality is driven by standardized development practices, IaC, automated supply chain, observability, and structured incident management.
- Heuristic: optimize process reliability through explicit standards and automation-first execution.
- First adoption task: introduce OE checklist review for pipeline/tooling decisions (OE:01..OE:08).
- Success criterion: fewer release surprises and faster incident triage under change.
- Confidence: high

### Entry 50
- Source: .NET observability with OpenTelemetry (`https://learn.microsoft.com/dotnet/core/diagnostics/observability-with-otel`)
- Date: 2026-02-25
- Fact: .NET observability architecture is natively aligned around ILogger + Meter + ActivitySource, with OTel SDK used for collection/export and vendor-neutral telemetry flow.
- Heuristic: instrument once using platform APIs and keep backend choice decoupled through OTel exporters/protocols.
- First adoption task: standardize application instrumentation baseline (logs/metrics/traces) for all new services.
- Success criterion: consistent cross-service diagnostics with minimal vendor lock-in.
- Confidence: high

### Entry 51
- Source: ASP.NET Core health checks (`https://learn.microsoft.com/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-10.0`)
- Date: 2026-02-25
- Fact: liveness/readiness separation, dependency probes, and orchestrator-integrated endpoints are core to reliable service operation.
- Heuristic: health endpoints should represent operational truth (startup readiness, dependency health, degraded behavior) rather than a single binary ping.
- First adoption task: define `/healthz` + readiness endpoint policy and dependency probe tags for active APIs.
- Success criterion: fewer false-positive restarts and more accurate traffic routing during partial failures.
- Confidence: high

### Entry 52
- Source: GitHub Actions and .NET (`https://learn.microsoft.com/dotnet/devops/github-actions-overview`) + build/test quickstart (`https://learn.microsoft.com/dotnet/devops/dotnet-test-github-action`)
- Date: 2026-02-25
- Fact: repeatable CI in .NET should center on workflow files with setup-dotnet + restore/build/test stages and explicit secret handling.
- Heuristic: pipeline quality depends on deterministic workflow composition, not just successful ad-hoc command runs.
- First adoption task: validate each .NET repo has a minimal build+test workflow with pinned SDK strategy and status badge.
- Success criterion: reliable CI signal for every PR and lower integration regressions.
- Confidence: high

### Entry 53
- Source: Platform Engineering planning guidance (DORA metrics mention) (`https://learn.microsoft.com/platform-engineering/plan#measure-success-and-proving-value`)
- Date: 2026-02-25
- Fact: delivery improvement should be measured with outcome metrics such as lead time, deployment frequency, change fail rate, and time to restore service.
- Heuristic: use DORA-like metrics as feedback on engineering system health, not as isolated team scorekeeping.
- First adoption task: define baseline collection for 4 delivery metrics across at least one primary product stream.
- Success criterion: measurable trend visibility for delivery reliability and recovery performance.
- Confidence: medium

## Batch 11 (Completed): Compiler Foundations (Dragon Book Layer)

### Entry 54
- Source: Dragon Book overview (`https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools`)
- Date: 2026-02-25
- Fact: Dragon Book remains the canonical reference for the full compiler chain: lexical analysis, parsing, semantic analysis, intermediate representation, optimization, and code generation.
- Heuristic: treat compiler construction as a pipeline with explicit contracts between stages, not as a monolithic parser task.
- First adoption task: maintain a stage-by-stage architecture template for any language tooling project (tokens -> AST -> typed AST -> IR -> optimized IR -> target code).
- Success criterion: easier debugging and replacement of individual compiler stages without global rewrites.
- Confidence: medium

### Entry 55
- Source: Dragon Book companion site (`https://suif.stanford.edu/dragonbook/`)
- Date: 2026-02-25
- Fact: companion resources (errata, appendix source code, course links like Stanford CS143/MIT 6.035) are essential for grounding textbook theory in implementable artifacts.
- Heuristic: pair foundational texts with verified companion artifacts to avoid conceptual drift and outdated interpretations.
- First adoption task: create a compiler-study checklist that requires "theory chapter + companion artifact + runnable micro-implementation".
- Success criterion: reduced gap between conceptual understanding and executable implementation.
- Confidence: high

### Entry 56
- Source: LLVM Kaleidoscope tutorial (`https://llvm.org/docs/tutorial/`)
- Date: 2026-02-25
- Fact: modern compiler workflows are effectively IR-first; early transition to LLVM IR enables optimization/JIT/object generation with reusable backend infrastructure.
- Heuristic: when building DSL/tooling, minimize custom backend work by targeting a mature IR ecosystem as early as possible.
- First adoption task: prototype one minimal expression language that emits LLVM IR before adding advanced syntax.
- Success criterion: working end-to-end prototype with measurable compile/execute loop and extensible backend path.
- Confidence: high

### Entry 57
- Source: Crafting Interpreters contents (`https://craftinginterpreters.com/contents.html`)
- Date: 2026-02-25
- Fact: language engineering competence requires both interpreter path (tree-walk clarity) and VM path (bytecode/runtime performance and GC realities).
- Heuristic: sequence learning and implementation in two passes: semantic clarity first, runtime efficiency second.
- First adoption task: for new language experiments, implement interpreter baseline before introducing bytecode/VM optimizations.
- Success criterion: faster correctness convergence and fewer premature performance abstractions.
- Confidence: high

### Entry 58
- Source: Dragon Book + LLVM + Crafting Interpreters synthesis
- Date: 2026-02-25
- Fact: the strongest practical model is a three-layer lens: formal compiler theory (Dragon), industrial IR/toolchain integration (LLVM), and runtime ergonomics (Crafting Interpreters).
- Heuristic: evaluate design decisions by asking three questions: is it formally sound, is it toolchain-compatible, and is it runtime-maintainable?
- First adoption task: introduce this 3-lens review as a mandatory section in language-tooling ADRs.
- Success criterion: fewer dead-end architecture choices in parser/IR/runtime evolution.
- Confidence: medium

### Entry 59
- Source: Dragon Book learning adoption note
- Date: 2026-02-25
- Fact: Dragon Book is foundational but dense; retention improves when each chapter is converted into one executable artifact and one "error-class map".
- Heuristic: convert each studied compiler topic into "buildable toy + failure taxonomy" rather than passive notes.
- First adoption task: start chapter-to-artifact backlog (lexer DFA, precedence parser, type checker, SSA transform, local optimizer, codegen pass).
- Success criterion: ability to answer design questions with concrete prototypes instead of abstract recollection.
- Confidence: high

## Batch 12 (Completed): F# for Production .NET and C# Interop

### Entry 60
- Source: F# style guide (`https://learn.microsoft.com/dotnet/fsharp/style-guide/`) + coding conventions (`https://learn.microsoft.com/dotnet/fsharp/style-guide/conventions`)
- Date: 2026-02-25
- Fact: large-scale F# remains maintainable when code is organized with explicit namespace/module boundaries, restrained point-free style, and interoperability-aware API shape.
- Heuristic: optimize for readability/tooling/debuggability first; compactness is valuable only when it preserves clarity.
- First adoption task: define team-level F# conventions (namespace-first organization, RequireQualifiedAccess policy, public API naming and argument labels).
- Success criterion: reduced onboarding/debug friction for mixed-skill teams.
- Confidence: high

## Batch 13 (Completed): Windows/Linux Environment Foundations

### Entry 65
- Source: Operating System Concepts (Silberschatz/Galvin/Gagne)
- Date: 2026-03-01
- Fact: core OS guarantees are built around process isolation, virtual memory, scheduling policy, and explicit synchronization contracts; most production failures map to one of these boundaries.
- Heuristic: classify environment incidents by boundary first (process/memory/scheduler/IO/sync) before selecting tools.
- First adoption task: add boundary tag to every OS-related incident note in active projects.
- Success criterion: faster root-cause triage and fewer tool-selection detours.
- Confidence: medium

### Entry 66
- Source: Modern Operating Systems (Tanenbaum/Bos)
- Date: 2026-03-01
- Fact: different OS families optimize different tradeoffs (throughput, fairness, latency, isolation), so observed behavior can differ even with identical app code.
- Heuristic: treat cross-platform divergence as expected architectural variance, not as random anomaly.
- First adoption task: extend troubleshooting checklists with explicit OS-tradeoff questions (latency vs throughput vs isolation).
- Success criterion: fewer "mystery" discrepancies between Windows and Linux runs.
- Confidence: medium

### Entry 67
- Source: The Linux Programming Interface (Kerrisk)
- Date: 2026-03-01
- Fact: Linux runtime reliability depends on correct assumptions about file descriptors, signals, process groups, and resource limits.
- Heuristic: verify descriptor/signal/limit state early in Linux incidents before deep app-level debugging.
- First adoption task: add a standard Linux incident probe set (process tree, open files, limits, signal behavior).
- Success criterion: reduced time-to-first-valid-cause in Linux production incidents.
- Confidence: medium

### Entry 68
- Source: Advanced Programming in the UNIX Environment (Stevens/Rago)
- Date: 2026-03-01
- Fact: robust process supervision and IPC behavior require explicit lifecycle contracts; implicit assumptions around forks/exec/waits often cause unstable orchestration.
- Heuristic: model service startup/shutdown and child-process ownership explicitly in ops-sensitive components.
- First adoption task: audit one worker/service path for lifecycle ownership and shutdown correctness.
- Success criterion: deterministic stop/restart behavior with no orphaned subprocesses.
- Confidence: medium

### Entry 69
- Source: Windows Internals (Russinovich et al.)
- Date: 2026-03-01
- Fact: Windows behavior in services/security/performance incidents is strongly shaped by token/ACL/session mechanics and kernel object semantics.
- Heuristic: in Windows incidents, verify account/token/ACL context before application logic assumptions.
- First adoption task: add a Windows service-context checklist (identity, ACL, policy, startup account permissions).
- Success criterion: fewer false diagnoses caused by hidden security-context mismatch.
- Confidence: medium

### Entry 70
- Source: UNIX and Linux System Administration Handbook (Nemeth et al.)
- Date: 2026-03-01
- Fact: environment reliability is maintained by explicit operational contracts (service definitions, logging routes, backup/recovery routines, change discipline), not by ad-hoc admin actions.
- Heuristic: promote "ops as documented contract" for all recurring environment procedures.
- First adoption task: convert one recurring environment fix into a repeatable runbook entry with validation criteria.
- Success criterion: same issue resolved consistently by different operators/agents.
- Confidence: high

### Entry 61
- Source: F# component design guidelines (`https://learn.microsoft.com/dotnet/fsharp/style-guide/component-design-guidelines`)
- Date: 2026-02-25
- Fact: for cross-language APIs, F# internals can be idiomatic while public boundaries should feel natural to C# (.NET method shape, stable DTO types, avoid exposing curried signatures and opaque unions directly).
- Heuristic: design .NET-facing contracts in C#-friendly form and keep F# expressiveness behind the boundary.
- First adoption task: adopt "interop boundary" rule: public contracts verified from C# usage examples before acceptance.
- Success criterion: predictable consumption from C# with fewer adapter layers.
- Confidence: high

### Entry 62
- Source: Async programming in F# (`https://learn.microsoft.com/dotnet/fsharp/tutorials/async`) + async expressions (`https://learn.microsoft.com/dotnet/fsharp/language-reference/async-expressions`) + task expressions (`https://learn.microsoft.com/dotnet/fsharp/language-reference/task-expressions`)
- Date: 2026-02-25
- Fact: F# async workflows are compositional and concise; task expressions are preferred at heavy .NET Task interop boundaries and can directly await Task/ValueTask/Async.
- Heuristic: default to `async` for internal orchestration, use `task` at API edges where C#/.NET task semantics are the primary contract.
- First adoption task: codify async policy in architecture docs (internal async model vs external task model, conversion points via AwaitTask/StartAsTask).
- Success criterion: fewer async interop bugs and clearer cancellation/await behavior.
- Confidence: high

### Entry 63
- Source: Type providers overview (`https://learn.microsoft.com/dotnet/fsharp/tutorials/type-providers/`) + FSharp.Data docs via Context7 (`/fsprojects/fsharp.data`)
- Date: 2026-02-25
- Fact: type providers enable schema-driven, strongly typed integration for external structured data; this is highly aligned with portal/IM ingestion layers.
- Heuristic: use type providers for exploratory or adapter layers where schema fidelity is critical; isolate provider usage behind stable domain transformations.
- First adoption task: pilot one ingestion adapter (e.g., CSV/XML/JSON) using FSharp.Data type provider mapped to canonical domain records.
- Success criterion: lower runtime parsing failures and faster evolution with schema changes.
- Confidence: medium

### Entry 64
- Source: .NET language strategy - F# (`https://learn.microsoft.com/dotnet/fundamentals/languages#f`)
- Date: 2026-02-25
- Fact: Microsoft positions F# as robust, performant, and interoperable with C# in mixed-language solutions, with active community/compiler evolution.
- Heuristic: for complex domain transformation and validation pipelines, F# + C# hybrid architecture is a strategic fit, not an edge-case compromise.
- First adoption task: define language ownership map per service layer (F# for domain transformation/validation passes, C# for mainstream host/API/UI integration).
- Success criterion: better leverage of each language without architectural fragmentation.
- Confidence: high

## Batch 14 (Completed): IT Phase C - Cloud, Economics, and Scale Diagnostics

### Entry 71
- Source: DORA 2024 report (`https://dora.dev/research/2024/dora-report/`)
- Date: 2026-03-01
- Fact: delivery performance and reliability should be evaluated together (throughput + stability), with evolving interpretation of restoration/rework dimensions.
- Heuristic: avoid single-metric optimization; make release decisions on a balanced reliability-speed profile.
- First adoption task: add DORA-style dashboard slice to active delivery stream reviews.
- Success criterion: fewer conflicting decisions between speed and stability goals.
- Confidence: medium

### Entry 72
- Source: FinOps Framework overview + unit economics (`https://learn.microsoft.com/en-us/cloud-computing/finops/framework/finops-framework`, `https://www.finops.org/framework/capabilities/unit-economics/`)
- Date: 2026-03-01
- Fact: cloud governance matures when spend is mapped to business units and operated as continuous collaboration loop.
- Heuristic: architecture economics should be tracked per business capability, not only as aggregate infrastructure cost.
- First adoption task: define one unit-economics metric for a critical capability and publish ownership.
- Success criterion: cost changes become interpretable in business terms.
- Confidence: high

### Entry 73
- Source: Google SRE workbook - eliminating toil + alerting on SLOs (`https://sre.google/workbook/eliminating-toil/`, `https://sre.google/workbook/alerting-on-slos/`)
- Date: 2026-03-01
- Fact: sustainable reliability requires toil budgeting and burn-rate-based SLO alerting rather than ad-hoc threshold paging.
- Heuristic: protect engineering capacity by converting repetitive operational load into automation backlog.
- First adoption task: classify top repetitive ops tickets and create first automation candidates.
- Success criterion: measurable reduction in repetitive manual incidents.
- Confidence: high

### Entry 74
- Source: AWS Well-Architected Cost Optimization principles (`https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost-dp.html`)
- Date: 2026-03-01
- Fact: cost optimization is design-time discipline (consumption model, attribution, efficiency measurement), not post-hoc trimming.
- Heuristic: require cost impact notes in architecture options before implementation.
- First adoption task: include cost design principles section in ADR template.
- Success criterion: fewer expensive architecture reversals.
- Confidence: high

### Entry 75
- Source: Kubernetes SLI metrics + disruption budgets (`https://kubernetes.io/docs/reference/instrumentation/slis/`, `https://v1-32.docs.kubernetes.io/docs/tasks/run-application/configure-pdb`)
- Date: 2026-03-01
- Fact: platform reliability is enforceable through measurable control points (component SLIs, disruption budgets).
- Heuristic: separate platform-level objectives from application-level objectives to avoid blurred accountability.
- First adoption task: document one workload disruption budget with expected availability impact.
- Success criterion: fewer avoidable outages during maintenance/rollouts.
- Confidence: medium

### Entry 76
- Source: OpenTelemetry metrics SDK spec (`https://opentelemetry.io/docs/specs/otel/metrics/sdk`)
- Date: 2026-03-01
- Fact: observability quality and cost are strongly influenced by cardinality controls and view-level aggregation choices.
- Heuristic: design telemetry with signal budget constraints from day one.
- First adoption task: define forbidden high-cardinality metric attributes for default instrumentation.
- Success criterion: stable telemetry cost with preserved incident diagnosability.
- Confidence: medium
