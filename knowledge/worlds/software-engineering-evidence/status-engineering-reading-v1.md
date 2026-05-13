# Engineering Reading Domain Status v1

## Scope

Evidence-based reading system for .NET/C# engineering decisions (language, runtime, testing, architecture, data, operations, compilers, F#, OS environments).

## Completion State

Status: **Done v1 (Foundation Layer)**

Primary artifact: **`kb-engineering-evidence-v1.md`** — база знаний по темам (evidence, не список книг). Map — справочник источников; digest — архив/legacy.

Completed artifacts:

- `kb-engineering-evidence-v1.md`
- `kb-mcconnell-code-complete-2-chapter-map-v1.md` (карта глав *Code Complete* 2nd ed., evidence-протокол, локальный source в карточке)
- `map-engineering-reading-v1.md`
- `digest-engineering-reading-v1.md` (legacy; выписки перенесены в kb)
- `status-engineering-reading-v1.md`

## Definition of Done Check

- Version baseline (C# 14 / .NET 10+) fixed: done.
- Multi-track literature map with ingestion contract: done.
- Digest has multi-batch distilled entries with adoption tasks/confidence: done.
- Track H (Windows/Linux) includes explicit applied examples: done.
- Index synchronization: done.

## Active Guardrails

- Read for transfer, not for volume.
- Promote only techniques with measurable workflow impact.
- Keep confidence proportional to repeated practical usage.
- Separate stable fundamentals from fast-changing platform guidance.

## Remaining Backlog (Out of v1 Closure)

- Continue Phase C expansion (cloud/platform engineering, architecture economics, large-scale diagnostics).
- Periodic freshness pass for high-volatility official docs.

### Legacy / compatibility bridge (.NET Framework → .NET)

- For legacy .NET Framework topics (1.0–4.x history, CLR 2.0/3.5 vs CLR 4.0, supported combinations, migration decisions) **не открывать новый домен**: использовать тонкий мостовой слой поверх этого фонда:
  - `worlds/software-dotnet-desktop/kb-dotnet-fundamentals-v1.md` — конспект по линиям .NET, TFMs, моделям приложений и границам .NET↔native;
  - блок `.NET Framework history and compatibility (1.0 → 4.x)` внутри `kb-engineering-evidence-v1.md` — факты/эвиденция по истории/совместимости;
  - `worlds/software-dotnet-desktop/kb-dotnet-playbooks-v1.md` — короткие playbook’и (выбор TFM/версии, оценка миграции с .NET Framework, базовый диагностический цикл).
- Глубинные диагностические/отладочные дорожки остаются в существующих playbook’ах (`worlds/software-dotnet-desktop/dotnet-roslyn-debug-playbook.md`, `tooling-debug-playbook.md`, `worlds/software-dotnet-desktop/frontend-dotnet-playbook.md`) и считаются продолжением этого же домена.

## Next sources to ingest (Queue)

При следующем чтении — кандидаты для выписок в `kb-engineering-evidence-v1.md` (по темам, формат: Fact, Heuristic, First adoption task, Success criterion, Confidence, Source). Приоритет по map и потребности проекта.

- C# in Depth (Skeet) — семантика языка, скрытые острые края.
- Pro .NET Memory Management (Kokosa) — GC и стратегии аллокаций.
- xUnit Test Patterns (Meszaros) — каталог тестовых запахов и ремедиация.
- Working Effectively with Legacy Code (Feathers) — восстановление через швы (seam-first).
- Designing Data-Intensive Applications (Kleppmann) — tradeoffs данных и систем.

## Alias Window

Closed. Legacy aliases were retired after semantic-primary stabilization.

## Next Domain Handoff

Engineering-reading foundation closed at v1.  
Next step: move to remaining pending technical domain, then run naming/index cleanup.
