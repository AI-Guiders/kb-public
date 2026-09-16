# ADR 020: KB language contours — English open perimeter, Russian operator interior

**Status:** Accepted (2026-08-28)  
**Tags:** #adr #kb #i18n #language #kb-public #federation  
**Related:** [001](001-kb-public-publishing-pipeline.md), [011](011-aiguiders-org-collaborative-kb-repo.md), [019](019-writing-canon-layers-and-guiders-style.md) (mirror → CDP-ADR-0207)

**Operator context (non-normative):** [`../personal/operator-notes/note-language-contours-operator-context-2026-08-28.ru.md`](../personal/operator-notes/note-language-contours-operator-context-2026-08-28.ru.md)

---

## Context

The KB and federation repos today mix **Russian and English** without an explicit policy:

| Area | Typical language today |
|------|------------------------|
| NuGet monorepos, product ADRs (`guiders-ui-platform`, …) | English |
| `knowledge/worlds/`, playbooks | Often English |
| `knowledge/work/`, operator research | Often Russian |
| `knowledge/personal/`, `*.ru.md` | Russian |
| **kb-public** MkDocs | Russian **default** locale + English branch; synced `knowledge/` is **mixed** |

Full product i18n (paired translations, sync pipelines) is **out of scope** — high cost, low leverage for a small federation. Outreach (GitHub Issues, ADR citations, Uncle Bob / Karpathy-class peers) requires a **predictable lingua franca**.

The maintainer is **fluent in English** but operates in a **Russian daily environment**; English-for-everything imposes **extra cognitive load** when drafting. Policy must **not** pretend that tension does not exist.

---

## Decision

### 1. Three language contours (not “translate everything”)

| Contour | Paths / artifacts | Language | Published? |
|---------|-------------------|----------|------------|
| **A — Open perimeter** | GitHub README, product ADRs, NuGet API names, `operationId`, public issues, kb-public **default** reading path | **English** | Yes |
| **B — Work interior** | `knowledge/work/`, research notes, project cards, internal runbooks | **Russian or English** | No (`public-kb.ignore`) |
| **C — Personal** | `knowledge/personal/`, `*.ru.md`, dialogue archives | **Russian** (or operator choice) | Never |

**Rule:** files without a language suffix on contour **A** are **English**. Suffix **`.ru.md`** = Russian-only; **must not** appear in contour A or kb-public builds.

### 2. No dual-maintenance i18n

- We **do not** maintain `foo.md` + `foo.ru.md` pairs for the same canonical doc.
- **Migrate on touch:** when a contour B doc is cited externally or copied to A, add or rewrite an **English** version (or extract EN summary + link).
- Agents may **draft English from Russian** operator input; operator reviews meaning, not every comma.

### 3. kb-public

- **Default locale:** English (`mkdocs.yml` `default: true` on `en`).
- Russian onboarding may remain as **secondary** locale; no requirement to keep RU nav in lockstep with every EN change.
- Synced `knowledge/` for public slice: prefer **English** for new/edited files that ship in the slice; mixed legacy files are **technical debt**, not blockers.

### 4. Code and identifiers

- Public identifiers (`TestId`, `operationId`, `handler_id`, package names, ADR slugs): **English**.
- User-facing UI strings: per **planet** product law; federation Core does not mandate UI i18n in v1.

### 5. Operator affordances (cognitive load)

- **Contour B/C in Russian is allowed and expected** for speed and precision of thought.
- **Contour A** may be produced via agent-assisted English draft; deadline pressure does not require the operator to “think in English” for internal notes.
- Switching chat language (RU ↔ EN) is operational, not a policy violation.
- Policy targets **artifact placement**, not **operator brain language**.

### 6. Relation to writing canon (CDP-ADR-0207)

- **CDP-ADR-0207** (`guiders-style/{lang}/`) governs **prose style in code repos** per language.
- **This ADR** governs **which contour** uses which language in KB and open federation surfaces.
- Orthogonal: English ADR in `guiders-ui-platform` + Russian scratch in `work/` is valid.

---

## Non-goals

- Machine-translating the entire KB.
- Forcing the operator to stop writing Russian in `work/` or `personal/`.
- Locale-aware UI platform (resx / gettext) as a federation gate in v1.
- Declaring English superiority; this is **interoperability**, not identity.

---

## Consequences

- New product ADRs and GitHub-facing docs: **English**.
- Research that may be linked from Issues (e.g. UI IR platform): **English primary** in `work/` or EN excerpt + RU deep note.
- kb-public site default language flips to **English** (implementation: `kb-public` repo `mkdocs.yml`).
- Router / supplement: optional one-line pointer to this ADR.

---

## Implementation (ordered)

1. `kb-public`: set MkDocs i18n default locale to `en`.
2. Link this ADR from `knowledge/README.md` (public section) and `PUBLISHING.md` one sentence.
3. On next touch of heavily mixed public files (`00-entry-kb.md`, …): EN rewrite or EN stub at top.
4. Agent rule (operator prefs / project card): public draft → English unless explicitly `personal/` or `*.ru.md`.

---

## Review gate

- [ ] New file on contour A: English body (or explicitly marked translation target)
- [ ] No new `*.ru.md` outside `personal/` without `work/` path and no public citation
- [ ] Product repo PR: README/ADR English
- [ ] kb-public PR: default locale EN after step 1

