# Evidence: Cooper et al. (2024) — 3D learning vs active learning (video segments)

## Provenance

- source_refs:
  - primary: Cooper, M. M., Stowe, R. L., Underwood, S. M., & Klymkowsky, M. W. (2024). Exploring the impact of three-dimensional learning on student performance in a general chemistry course. *PLOS ONE*, 19(1), e0295887.
  - doi: [10.1371/journal.pone.0295887](https://doi.org/10.1371/journal.pone.0295887)
  - open_pdf: [PLOS ONE full text](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0295887&type=printable)
- created_at: 2026-06-06
- updated_at: 2026-06-06
- extraction_note: **read_depth: full** — full PLOS text; segment-level chi² on 417 video segments (Gen Chem I).

## Metadata

- card_id: kb-pedagogy-biology-cooper-2024-3d-evidence-v1
- world: pedagogy.biology
- status: active

## Epistemic linkage

- confidence: **high** for 3DL ⊃ active-learning classification and segment-level performance pattern in this course design
- transfer_boundary: general chemistry video segments; not a classroom RCT meta-analysis; biology world uses for **3D/NRC alignment** operationalization
- falsification_trigger: replication with non-video delivery fails to show 3DL > active-only advantage

---

## Fundamentals

**Thesis:** segments coded as **three-dimensional learning (3DL)** — integrating disciplinary core ideas, crosscutting concepts, and science/engineering practices (NRC Framework) — outperform segments coded as **active learning only** on post-segment quiz performance.

**Design:** 417 instructional video segments from a transformed Gen Chem I course; each segment classified post hoc as 3DL, active-only, or passive. Students (n = 1,547) answered one quiz item per segment viewed.

**Key results (Table 2, chi²):**

| Comparison | χ² | p | Interpretation |
|------------|-----|---|----------------|
| 3DL vs active-only | 15.84 | < .001 | 3DL segments associated with higher correct rates |
| 3DL vs passive | 28.47 | < .001 | Strong advantage over passive |
| Active-only vs passive | 2.89 | .089 | Active alone did not reliably beat passive |

**Effect framing:** authors cite Freeman et al. (2014) active-learning meta (g ≈ 0.47 STEM) but show **active structure necessary, not sufficient** — **3D integration** adds measurable value on fine-grained outcomes.

## Extracted knowledge (K)

| # | Тезис |
|---|--------|
| K1 | 3DL = DCIs + CCCs + SEPs together; active engagement without 3D framing underperforms |
| K2 | Segment-level quiz design enables large-N classification without new RCT infrastructure |
| K3 | Passive segments remain in corpus; transformation is partial, not binary flip |
| K4 | Performance outcome is **immediate post-segment recall/application**, not long-term retention meta |
| K5 | Supports von Neumann gate: label «active lab» insufficient — require explicit 3D tag on phenomenon + practice + crosscutting link |

## Operationalization (biology / science v1)

- **Authoring tag:** `bio.3dl.segment` with `{dci, ccc, sep}` triple; deny `bio.active.only` as sole gate pass
- **Gate item:** one phenomenon explanation tying practice (e.g. model/data) to core idea + one crosscutting concept
- **Anti-pattern:** hands-on activity without disciplinary idea anchor → classify as active-only, not 3DL

## Related cards

- [`kb-pedagogy-biology-nrc-2012-framework-evidence-v1.md`](kb-pedagogy-biology-nrc-2012-framework-evidence-v1.md) — 3D definition source
- Chemistry POGIL card — complementary inquiry structure, different evidence base

*Версия: v1.1 · 2026-06-06 · read_depth: full*
