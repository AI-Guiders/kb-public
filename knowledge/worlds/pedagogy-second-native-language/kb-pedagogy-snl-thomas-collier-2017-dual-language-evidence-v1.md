# Evidence: Thomas & Collier (2017) — dual-language schooling longitudinal outcomes

## Provenance

- source_refs:
  - primary: Thomas, W. P., & Collier, V. P. (2017). Validating the power of bilingual schooling: Thirty-two years of large-scale, longitudinal research. In *Annual Review of Applied Linguistics* (Vol. 37, pp. 203–217). Cambridge University Press.
  - doi: [10.1017/S0267190517000034](https://doi.org/10.1017/S0267190517000034)
  - open_pdf: [author chapter PDF](https://katemenken.org/wp-content/uploads/2020/12/validating_the_power_of_biling.pdf)
  - earlier: Thomas & Collier (2004). The astounding effectiveness of dual language education for all. *NABE Journal of Research and Practice*, 2(1), 1–20.
- created_at: 2026-06-06
- extraction_note: **read_depth: partial (extended)** — open chapter PDF; 32 yr / 36 districts / 7.5M records summary.

## Metadata

- card_id: kb-pedagogy-snl-thomas-collier-2017-dual-language-evidence-v1
- world: pedagogy.second-native-language
- status: active

## Epistemic linkage

- confidence: **high** for relative program rankings (dual-language > transitional > ESL-only) in US longitudinal corpus; **medium** for exact % gap closure transfer to RU/EN von Neumann without local replication
- transfer_boundary: US district data; quality implementation variance; **6+ years** both languages required for full gap closure claims
- falsification_trigger: matched long-term study shows dual-language ≈ short ESL on L2 grade-level norms

---

## Fundamentals

**Thesis:** **long-term dual-language** schooling (both L1 and L2 as media of instruction) closes achievement gaps; **short English-only or short transitional** programs close ~**half** the gap at best.

**Scale:** 32 years, 36 districts, 16 US states, >7.5M student records; individual tracking K–12.

**Program comparison (summary):**

| Program type | Gap closure (typical) | Notes |
|--------------|----------------------|--------|
| ESL content / short transitional | ~50% by end elementary | Better than sink-or-swim but plateau |
| **Dual-language (one/two-way, 50:50 or 90:10)** | **100%** gap closure possible | 5–6 years minimum both languages |
| Annual effect size (dual-language) | **0.14–0.29** NCE/year | Meaningful cumulative gain |

**Time-on-L2 answer:** ~**6 years** quality dual-language from kindergarten (≥50% instruction in each language over span) to reach grade-level L2 norms for EL starters.

**Prism model:** outcomes = interaction of background + child input + **program treatment** — weak program ≠ weak child.

## Extracted knowledge (K)

| # | Тезис |
|---|--------|
| K1 | Second-native ≠ 2 lessons/week — need **years** of L2-as-medium time |
| K2 | Two-way 90:10 fastest L2 norm gains in their data; 50:50 needs middle school continuation |
| K3 | von Neumann bilingual track: document **annual L2 %** and **6-year horizon** |
| K4 | Subtracting L1 for «more English hours» underperforms long dual-language |
| K5 | Effect sizes small annually but **cumulative** — don't abandon at year 2 |

## Operationalization (second-native v1)

- **Tag:** `snl.dual_lang.model` ∈ {one_way_90_10, two_way_50_50, …} + `snl.dual_lang.l2_pct`
- **Gate:** program review at year 5 against grade-level L2 benchmark, not year 1 oral test
- **Deny:** label «bilingual» with <30% L2 medium time and no L1 literacy parallel

*Версия: v1.0 · 2026-06-06 · read_depth: partial (extended)*
