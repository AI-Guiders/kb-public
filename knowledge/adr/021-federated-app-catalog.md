# ADR 021: Federated App Catalog — open trust, unified operator journey

**Status:** Accepted (draft charter, 2026-08-28)  
**Tags:** #adr #federation #distribution #desktop #trust  
**Related:** [020](020-kb-language-contours.md), friction-book [ch.24](https://github.com/AI-Guiders/friction-book/blob/main/src/24-invisible-desktop-production.en.md), [ch.25](https://github.com/AI-Guiders/friction-book/blob/main/src/25-federated-app-catalog.en.md)  
**Project:** `federated-app-catalog` (`FAC`) · protocol sub-track: `guiders-platform/platform-app-catalog-v1` (`GPLAT/APPCAT`)

---

## Context

Application distribution is fragmented (winget, flatpak, snap, direct downloads, game launchers, mobile-only feature parity). Mobile app stores provide a **unified journey** (search, trust, install, update) but centralize policy and metrics. Desktop production work is **invisible** to product narratives optimized for pocket engagement.

Users and operators already build **meta-launchers** (e.g. Playnite, GOG Galaxy) — evidence of demand for one journey across many sources. F-Droid and regional stores prove demand for **freedom of upstream** without a single gatekeeper.

We need an **open, federated** model with the **same operator journey** a good store provides — without pretending one OS or one vendor owns the funnel.

---

## Decision

### 1. Federated App Catalog (FAC) as a federation concern

Establish **Federated App Catalog** as a cross-cutting track:

- **Charter & narrative:** `federated-app-catalog` project in KB
- **Protocol packages (future):** `AIGuiders.Platform.Catalog.*` under `guiders-platform/platform-app-catalog-v1`
- **Not** a monolithic store binary; **not** a replacement for winget/apt — **adapters** on existing legs

### 2. Layered contract (v0.1)

| Layer | Responsibility |
|-------|----------------|
| **Package manifest** | Stable `package_id`, version, publisher, capabilities, per-platform artifacts + hashes |
| **Trust graph** | Signing keys, policy pack attestations, revoke/block (federated) |
| **Federated index** | Instance exposes catalog; upstream mirror/cherry-pick; search aggregates with source badge |
| **Install adapters** | Pluggable legs: winget, flatpak, snap, direct signed, enterprise channel |
| **Unified shell** | Operator UI: search → trust badge → permissions → install → update history |

Same **meaning** (install this package safely), different **physical** install per planet — analogous to GUIP FunctionalSpec → PhysicalImplementation.

### 3. Design principles

1. **Federation over monopoly** — many upstreams; operator chooses policy packs
2. **Unified journey over fragmented CLI** — one shell; legs stay pluggable
3. **Desktop-class first** — hours-in-seat, review, multi-surface PAN; phone = triage, not sole hub
4. **Trust as service** — explicit capabilities and policy tags (F-Droid anti-features as minimum inspiration)
5. **Verify, don’t accuse** — install delta visible; IOP-friendly for agent-assisted installs later

### 4. Non-goals (v0.1)

- Replacing OS package managers
- Single billing rail / 30% store tax
- Full GPlay feature parity (family, refunds) in v1
- Mandating one binary format

---

## Consequences

- Positive complement to friction-book ch.24 (invisible desktop): **actionable** distribution vision
- `agent-forge`, `agent-nuget-pm`, `open-agent-registry` remain **siblings** — different artifact classes
- Implementation starts with **schema + static index mock** before any store UI

---

## Implementation plan (v0.1)

1. ✅ Charter + ADR + friction ch.25
2. Package manifest JSON Schema draft (markdown + example)
3. Static federated index (two mock instances)
4. Windows prototype: winget leg + minimal shell
5. Policy pack format draft

---

## References

- Operator charter (RU): `knowledge/work/projects/door-to-singularity/federated-app-catalog/research/note-federated-app-catalog-charter.md`
- Project card: `…/federated-app-catalog/README.md`

