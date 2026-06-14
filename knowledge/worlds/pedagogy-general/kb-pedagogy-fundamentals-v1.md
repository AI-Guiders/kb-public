# Pedagogy fundamentals v1

**Мир:** `pedagogy.general`  
**Назначение:** самодостаточный опорный слой для authoring curriculum и gate-конструктов.  
**Связь:** `status-*` → `playbook-*` → **этот файл** → evidence cards.

**Версия:** v1.0 · 2026-06-06 · **status:** active

---

## Scope

- Школьные предметы: что учим, порядок, чего не делаем.
- Gate ЗУН на **held-out**, не recall § учебника.
- Out of scope: клиника SLP; human L1 acquisition spec ([`cognition.language-acquisition`](../cognition-language-acquisition/)).

---

## Fundamentals → operational

```text
Evidence (scientific-evidence index + per-paper cards)
    → Fundamentals (subject + pedagogy.general)
    → Playbook (router)
    → Authoring (lesson manifests, probes — вне kb-public)
    → Field + gate (agent KSA)
```

**Правило:** не claim pedagogical basis in product/lab без subject evidence + fundamentals + playbook в `worlds/pedagogy-*`.

---

## Цель: владение на поле

| Тракт | Цель | Не цель |
|-------|------|---------|
| RU written v1 | fluent read, ortho/punct in context, text dialogue | лингвистика; § как oracle |
| Math | compare, structures on field, vis↔symbol | ranker tweak без probe |
| STEM/humanities | construct in context | exam template without bind |

Школа = **authoring labels** (разделы учебника), не epistemic root.

---

## Цикл 1–5 (исполнитель)

| # | Шаг | Учитель | Агент |
|---|-----|---------|-------|
| 1 | Goal | stage spec | interpret / defer |
| 2 | Classify | concept_id, tract | votes on field |
| 3 | Methods | moment plan | bridges, compose |
| 4 | Synthesize | — | predict, articulate |
| 5 | Verify | probe spec | **gate ЗУН** held-out |

Fail step 5 → revise 2–3, **not** tune probe to pass.

---

## Gate = ЗУН (KSA)

| ЗУН | На поле | Probe |
|-----|---------|-------|
| Знания | confirmed concept, journal | held-out → concept |
| Умения | skill after gate | capability on store |
| Навыки | stable route | N× pass, novel context |

---

## Teacher vs field

| Учитель | Агент |
|---------|-------|
| Environment, probe criteria | Own field, honest pass/fail |
| KB orient (contrast frames) | Mastery = journal |

**Hot path anti-oracle:** external morph analyzer, paste grammar chunk, wake-time answer key.

---

## Модальности (written v1 default)

| Тракт | Status |
|-------|--------|
| Visual + text | in scope |
| Audio / orthoepy | **deferred** unless status updated |

---

## Anti-patterns

- Code/lab before evidence kb in canon
- One probe = whole subject mastery
- Jargon maturity levels outside `draft` | `active`
- Import L1 acquisition findings into school gate without [`matrix-pedagogy-cross-subject-transfer-v1.md`](matrix-pedagogy-cross-subject-transfer-v1.md)

---

## Evidence and updates

- Cross-cutting: [`kb-pedagogy-scientific-evidence-v1.md`](kb-pedagogy-scientific-evidence-v1.md)
- Synthesis: [`kb-pedagogy-evidence-global-v1.md`](kb-pedagogy-evidence-global-v1.md)
- Provenance: `META/provenance-contract-v1.md`

