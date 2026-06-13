# Evidence: Sentance & Waite (2021) — PRIMM programming pedagogy

## Provenance

- source_refs:
  - primary: Sentance, S., & Waite, J. (2021). Teachers' perspectives on PRIMM: A structured approach to teaching programming in school. In Proceedings of the 16th Workshop on Primary and Secondary Computing Education (WiPSCE '21). ACM.
  - doi: [10.1145/3481312.3481315](https://doi.org/10.1145/3481312.3481315)
  - framework_site: [PRIMM portal](https://primmportal.com/)
  - earlier: Sentance, S., & Csizmadia, A. (2017). Computing in the curriculum: Challenges and strategies from a teacher education perspective. *WiPSCE 2017*.
- created_at: 2026-06-06
- extraction_note: **read_depth: partial (extended)** — PRIMM portal + WiPSCE proceedings abstract; teacher survey themes.

## Metadata

- card_id: kb-pedagogy-informatics-sentance-primm-2021-evidence-v1
- world: pedagogy.informatics
- status: active

## Epistemic linkage

- confidence: **high** for PRIMM as widely adopted UK/international K-12 programming structure; **medium** for causal achievement effect sizes (mostly practice + teacher report)
- transfer_boundary: block/text languages in school CS; not university CS1 MOOC evidence
- falsification_trigger: controlled studies show PRIMM ≈ code-first on transfer debugging tasks

---

## Fundamentals

**Thesis:** **PRIMM** structures novice programming lessons to reduce cognitive overload and build **code reading** before authorship:

| Phase | Learner activity |
|-------|------------------|
| **P**redict | What will this program do? |
| **R**un | Execute and observe |
| **I**nvestigate | Trace, modify small parts |
| **M**odify | Change behavior purposefully |
| **M**ake | Create new program using pattern |

**Rationale (CLT-aligned):** novices who start with blank IDE face **goal-free problem overload**; reading/modifying worked programs scaffolds schema formation (links Sweller worked-examples strand).

**Sentance & Waite (2021) teacher findings (themes):**

- PRIMM gives **lesson rhythm** and shared vocabulary across department
- **Investigate** phase most valued for debugging habit formation
- Challenges: pacing for fast/slow pairs; transition from blocks to text

## Extracted knowledge (K)

| # | Тезис |
|---|--------|
| K1 | Code reading is not optional precursor to coding — assess predict/trace before make |
| K2 | Modify before Make prevents copy-paste without comprehension |
| K3 | PRIMM pairs with K12CS practices (debugging, abstraction) without jumping to AP exam pace |
| K4 | Unplugged + plugged PRIMM variants exist for primary bands |
| K5 | von Neumann informatics gate: no `Make` project without documented Predict–Run–Investigate on starter |

## Operationalization (informatics v1)

- **Tag:** `cs.primm.phase` ∈ {predict, run, investigate, modify, make}
- **Artifact:** starter program + prediction worksheet + modification diff
- **Deny:** «open project» week 1 with no structured reading phase

## Related cards

- [`kb-pedagogy-informatics-k12cs-2016-evidence-v1.md`](kb-pedagogy-informatics-k12cs-2016-evidence-v1.md)

*Версия: v1.0 · 2026-06-06 · read_depth: partial (extended)*
