<!-- markdownlint-disable MD022 MD032 -->

# Engineering Reading Map v1 (.NET / C#)

**Каноническая база знаний:** `kb-engineering-evidence-v1.md` — факты, эвристики и задачи внедрения по темам. Этот файл — справочник источников и опциональное углублённое чтение по трекам.

## Purpose
A practical literature map for resilient, confident, and effective .NET development.

## Version Baseline (Current)
- Language target: C# 14 and newer.
- Platform target: .NET 10 and newer.
- Compatibility rule: avoid unsupported combinations (for example, C# 14 on pre-.NET 10 targets).
- Build reliability rule: avoid `<LangVersion>latest</LangVersion>` for shared repos; prefer TFM-aligned defaults or explicit pinned versions (`14.0`, `15.0` when adopted).

## Evidence-Based Learning Protocol
- Fact: identify current gap (bug class, architecture weakness, delivery slowdown).
- Hypothesis: specify which source should reduce that gap and how.
- Check: apply one technique in a real task within 7 days.
- Decision criterion: keep only sources that measurably improve quality or speed.
- Confidence mark: tag adoption confidence (`low`, `medium`, `high`) after 2-3 uses.

## Track A: C# and .NET
- C# language docs (Microsoft Learn): modern language features and async model.
- What's new in C# 14 (Microsoft Learn): language delta map and migration implications.
- C# language versioning (Microsoft Learn): TFM-to-language compatibility and defaults.
- What's new in .NET 10 (Microsoft Learn): runtime/SDK/libraries release-level changes.
- C# in Depth (Jon Skeet): deep language semantics and tradeoffs.
- CLR via C# (Jeffrey Richter): runtime behavior, memory model, threading foundations.
- Pro .NET Memory Management (Konrad Kokosa): GC, allocations, performance diagnostics.
- .NET diagnostics docs (`dotnet-counters`, `dotnet-trace`, `dotnet-dump`): operational profiling workflow.

## Track B: Testing and Quality
- Unit testing best practices for .NET (Microsoft Learn): baseline conventions and anti-patterns.
- Integration testing in ASP.NET Core (Microsoft Learn): test host and realistic boundaries.
- xUnit official docs: framework idioms and maintainable test structure.
- xUnit Test Patterns (Gerard Meszaros): test smell taxonomy and refactoring.
- Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov): test design economics.
- Working Effectively with Legacy Code (Michael Feathers): seam-based recovery in hard codebases.
- Test-Driven Development: By Example (Kent Beck): TDD micro-loop and feedback discipline.

## Track C: Design, Architecture, Refactoring
- Code Complete, 2nd ed. (Steve McConnell): practical software *construction* (routines, defensive programming, readability, reviews, testing, debugging, integration); chapter map and evidence protocol — `kb-mcconnell-code-complete-2-chapter-map-v1.md`; local copy path in that card.
- Refactoring (Martin Fowler): catalog and safe transformation strategy.
- Refactoring.Guru: quick pattern/smell lookup with C# examples.
- Clean Architecture (Robert C. Martin): dependency boundaries and policy layering.
- Domain-Driven Design (Eric Evans) + Implementing Domain-Driven Design (Vaughn Vernon): domain modeling and strategic design.
- Patterns of Enterprise Application Architecture (Martin Fowler): enterprise pattern language.

## Track D: Algorithms, Data Structures, Databases
- Introduction to Algorithms (CLRS): formal algorithmic toolkit.
- The Algorithm Design Manual (Steven Skiena): practical algorithm selection.
- Algorithms, 4th Edition (Sedgewick/Wayne): implementation-focused DS and algorithms.
- Designing Data-Intensive Applications (Martin Kleppmann): modern data system tradeoffs.
- Database Internals (Alex Petrov): storage engines, indexing, transaction internals.
- SQL Antipatterns (Bill Karwin): schema/query pitfalls and remediation patterns.

## Track E: Delivery and Engineering Methodology
- Accelerate (Forsgren/Humble/Kim): evidence-backed delivery metrics.
- Team Topologies (Skelton/Pais): socio-technical architecture for flow.
- The Pragmatic Programmer (Hunt/Thomas): robust engineering habits.
- Release It! (Michael Nygard): production stability and failure containment.

## Track F: Language Engineering and Compilers
- Compilers: Principles, Techniques, and Tools (Aho/Lam/Sethi/Ullman, Dragon Book): canonical compiler pipeline and optimization foundations.
- Dragon Book companion site (Stanford): errata, source appendix, course links for practical reinforcement.
- LLVM Kaleidoscope tutorial: modern IR-first implementation path from lexer/parser to JIT/object code.
- Crafting Interpreters (Nystrom): end-to-end interpreter/VM construction with emphasis on language ergonomics and runtime tradeoffs.

## Track G: F# and Mixed-Language .NET Architecture
- F# style guide and coding conventions (Microsoft Learn): maintainability principles for large codebases.
- F# component design guidelines (Microsoft Learn): API ergonomics and compatibility for C# consumers.
- Async vs task expressions (Microsoft Learn): choosing concurrency model by interoperability boundaries.
- Type providers (Microsoft Learn + FSharp.Data docs): schema-first integration with external data.
- .NET language strategy for F# (Microsoft Learn): long-term interoperability and ecosystem positioning.

## Track H: Windows/Linux Systems and Runtime Environments
- Operating System Concepts (Silberschatz/Galvin/Gagne): process, memory, scheduling, file systems, synchronization foundations.
- Modern Operating Systems (Tanenbaum/Bos): comparative OS architecture and tradeoff reasoning.
- The Linux Programming Interface (Kerrisk): Linux process/IPC/filesystem/networking behavior in production detail.
- Advanced Programming in the UNIX Environment (Stevens/Rago): Unix process model and systems interfaces.
- UNIX and Linux System Administration Handbook (Nemeth et al.): practical service/network/storage/ops patterns.
- Windows Internals (Russinovich et al.): Windows kernel/process/memory/I/O/security internals.
- Microsoft Learn (Windows + .NET diagnostics): service/runtime troubleshooting on Windows hosts.
- Linux man-pages/systemd/kernel docs: service control, limits, and low-level operational contracts.

### Track H: Application Examples (Requested)
- **Windows foundation example:** correlate a latency spike to thread-pool starvation using EventCounters + ETW/EventPipe trace, then validate with blocking-stack analysis.
- **Linux foundation example:** correlate service instability to cgroup limits (`memory.max`, CPU quota) + `systemd` restart policy, then validate via journald and `/proc` pressure signals.

## Execution Cadence
- Weekly rhythm:
  - 1 deep source (book chapter or long guide),
  - 1 operational source (docs/tutorial),
  - 1 applied experiment in active code.
- Monthly output:
  - 1 playbook delta,
  - 1 anti-pattern note,
  - 1 validated engineering checklist update.

## Ingestion Contract
- Every completed source gets a knowledge entry in `kb-engineering-evidence-v1.md` (по темам, не по батчам).
- Entry format:
  - source and date,
  - key facts,
  - applicable heuristics,
  - first practical adoption task,
  - confidence mark after 2-3 usages.
- Batch size rule (fast mode): process 6-10 sources per pass before reporting status.
- Priority order:
  1. Official platform/runtime/testing docs (high volatility).
  2. Core engineering books (low volatility, high leverage).
  3. Supplemental references and pattern catalogs.

## Validation Metrics
- Fewer escaped defects in changed areas.
- Reduced lead time for similar tasks.
- Lower mean time to debug root cause.
- More stable p95/p99 for critical flows.
- Lower review churn (fewer repeated comments).

## Do Not Overfit
- Do not optimize for volume read.
- Prefer repeatable technique transfer over abstract coverage.
- Archive sources that do not survive real project constraints.

<!-- markdownlint-enable MD022 MD032 -->

