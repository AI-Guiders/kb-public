---
type: Note
title: Migration map — KB prose → LLM-native definitions
description: Не полный каталог 442 файлов. Priority seeds (2026-07-20).
tags: [worlds, llm-ready, map]
world: _llm
subworld: native-packs
---
# Migration map — KB prose → LLM-native definitions


Не полный каталог 442 файлов. Priority seeds (2026-07-20).

| Source (KB) | Pack | Definition ids (seed) → `definitions/<id>.md` |
|-------------|------|------------------------|
| `software-authoring/code-writing-principles.md` | software-authoring | `solid-as-orienting`, `composition-over-inheritance`, `dry`, `kiss`, `csharp-async-no-sync-over-async`, `httpclient-reuse`, traps pass A (0.5.0): `csharp-dispose-using`, `csharp-ienumerable-multipass`, `csharp-culture-invariant-vs-current`, `csharp-logging-no-secrets`, `csharp-no-unsync-mutable-static`, `csharp-valuetask-semantics`, `csharp-async-void-ui-only`, `csharp-configureawait-library-vs-app`, `csharp-aot-trimming-constraints`, `csharp-nuget-vulnerable-check`; plus agent gap `csharp-di-no-scoped-from-singleton`; async neighbor (0.5.1): `csharp-cancellationtoken-propagate` |
| `software-authoring/kb-ooad-fundamentals.md` | software-authoring | `ooa`, `ood`, `noun-verb-analysis`, `grasp-information-expert`, `grasp-high-cohesion`, `solid-after-grasp` |
| `personal/…dev-books…` + [Refactoring.Guru](https://refactoring.guru/) | software-authoring | `what-is-design-pattern`, `pattern-vs-algorithm`, `mc-pattern-first`, `gof-singleton`, `gof-factory-method`, `gof-strategy`, `gof-observer`, `smell-long-method`, `smell-feature-envy` (pilot 2026-07-21; not full catalog) |
| `software-authoring/playbook-ooad-agent-operational.md` | software-authoring | (process) `ooad-agent-pass` |
| `software-dotnet-csharp/kb-dotnet-fundamentals.md` | software-dotnet-csharp | `net-framework-vs-net`, `tfm`, `dotnet-cli-as-ssot` |
| `software-dotnet-csharp/kb-dotnet-playbooks.md` | software-dotnet-csharp | procedures (0.4.0): `dotnet-choose-tfm`, `dotnet-plan-framework-migrate`, `dotnet-perf-diag-cycle` |
| `math-numerics-pde/kb-math-pde-fundamentals.md` | math-numerics-pde | `pde-elliptic`, `pde-parabolic`, `pde-hyperbolic`, `pde-well-posedness`, `bc-dirichlet`, `bc-neumann` |
| `pedagogy-physics/kb-pedagogy-physics-fundamentals.md` | pedagogy-physics | `phys-modeling-conceptual-change`, `phys-p1-phenomenon`, `phys-p2-representations`, `phys-p3-model-refinement`, `phys-p4-quantitative` |
| `domains/agent-operations` + CDP design | epistemic-scene | `debug-radius`, `hypothesis-space-h`, `delta-radius-gate`, `stage-result`, `verification-contract`, `blast-radius`, `core-when-barriers-fail` |
| L0 hot epistemic contracts | epistemic-methodology | `integrity-baseline`, `default-distrust`, `principled-clarity`, `equal-standing`, `claim-observation-split` |
| CDP consumer thin | agent-operations-cdp | `migrate-one-then-batch` + `mc-mass-migrate-script-first` + procedure `migrate-one-then-batch` (0.4.0; skill facet) |
| `software-engineering-evidence/*` | (later) | evidence digests → `related` only in v0 |
| `ml-learning-dynamics/*` | (later) | curriculum / catastrophic interference — pack after CDP dogfood |
| `collaboration-git-pr/*`, `hci-ux-dx/*`, … | (later) | inventory by route_context hits |

## Next passes (suggested order)

1. Dogfood CDP pack (`agent-operations-cdp`) in `cdp_session` — pack+procedure ready; SessionPlane facet fallback in CdpMcp 0.5.8 (needs MCP restart to deploy).
2. ~~Expand SOLID~~ + GoF pilot (singleton/factory/strategy/observer) — done 0.4.0; more GoF only on hit rate.
2b. ~~Pass A C# traps~~ — done 0.5.0–0.5.1 (+ CT propagate, DI captive).
2c. ~~DOTNET-01..03 → procedures~~ — `software-dotnet-csharp` 0.4.0.
3. ~~Trap cards from `code-writing-principles`~~ — folded into 2b.
4. `software-javascript`, `software-php-laravel` — language packs from existing worlds.
5. `pedagogy-mathematics`, `pedagogy-chemistry` — same sparse pattern as physics.
6. `ml-learning-dynamics` — learning theory for “how to teach networks”.

