# KB: Situation Awareness Measurement in Dynamic Systems v1

## Provenance (происхождение)
- source_refs:
  - https://www.routledge.com/Situation-Awareness-Analysis-and-Measurement/Endsley-Garland/p/book/9780805821345 (book metadata + table of contents)
  - https://maritimesafetyinnovationlab.org/wp-content/uploads/2018/11/Endsley-Theory-of-Situational-Awareness.pdf (chapter text: "Theoretical Underpinnings of Situation Awareness: A Critical Review", 2000)
  - https://web.cs.wpi.edu/~gogo/courses/cs525H_2010f/papers/SAGATvSART_HFES1998.pdf (comparative paper: SAGAT vs SART, HFES 1998)
  - https://journals.sagepub.com/doi/10.1518/001872095779049499 (canonical article record: "Measurement of Situation Awareness in Dynamic Systems", Human Factors, 1995; abstract/metadata only in this pass due access limit)
- created_at: 2026-04-15
- updated_at: 2026-04-15
- author: codex

## Metadata
- card_id: KB-SA-DYNAMIC-MEASUREMENT-2026-04-15
- world: hci.situational-awareness.measurement
- layer: world
- tags: situation-awareness, endsley, sagat, sart, workload, human-factors, dynamic-systems, aviation
- status: active

## Epistemic Linkage
- epistemic_basis: fact + inference
- evidence_type: book metadata + chapter text + conference paper + journal record
- confidence: high (for method taxonomy and core claims), medium (for chapter-level details not independently verified against publisher PDF in this pass)
- uncertainty:
  - full publisher text of the 1995 Human Factors article is paywalled in this pass;
  - one open-source chapter copy is an uploaded mirror and may differ in formatting from official print.
- falsification_trigger:
  - direct full-text check of the 1995 article or 2000 edited volume reveals contradictions with method descriptions below.
- transfer_boundary:
  - SA measures are domain- and goal-dependent; methods must be adapted via task analysis before transfer to another domain.

## Core Unit
- context:
  - In dynamic systems (aviation, ATC, control rooms, medicine), performance metrics alone are often too sparse or ambiguous to evaluate interface and automation quality.
- signal:
  - SA is modeled as three levels (perception, comprehension, projection), and measurement approaches differ in what they actually capture.
- action:
  - Use an explicit SA measurement battery rather than a single metric:
    - objective query-based methods (SAGAT),
    - subjective self-rating methods (SART),
    - observer/post-hoc/performance and other complementary methods.
  - Keep SA and workload as separate constructs during evaluation.
  - Treat SA as multi-dimensional; avoid collapsing all probes into one scalar score.
- outcome:
  - Better diagnosticity for design decisions (what improved, what degraded, where attention shifted).
  - Detection of hidden trade-offs (for example: one display improves some SA elements while degrading others).
- lesson:
  - "More data != more information." The core measure of merit is how well the design bridges the information gap under operational constraints.

## Operationalization
- first_adoption_task:
  - For any cockpit/monitoring UI change, define SA requirements by scenario and map probes to L1/L2/L3 before running eval.
- validation_check:
  - Confirm that:
    1) probes align with task-relevant SA requirements,
    2) metric collection does not materially distort operator behavior,
    3) SA, workload, and performance are reported separately.
- success_criterion:
  - Candidate design shows improved SA on critical probes without unacceptable regressions in other probes, workload, or task outcomes.
- rollback_or_mitigation:
  - If SA gains are local but global SA degrades, revert design or add compensating cues (salience, grouping, attention guidance, projection support).

## Measurement Notes (practical)
- SAGAT (objective, freeze-probe):
  - strength: direct, objective snapshot of operator SA; high diagnosticity;
  - limits: simulation freeze requirement; scenario/query engineering cost.
- SART (subjective self-rating):
  - strength: easy deployment, useful operator-perceived SA signal;
  - limits: can correlate with confidence/workload/perceived performance rather than veridical SA.
- Evidence from Endsley-line comparisons (HFES 1998):
  - SAGAT and SART can diverge and may not correlate directly;
  - both can be useful, but they are not interchangeable.

## Canonical Decision Rules (for KB consumers)
- Do not use a single SA score as release gate for dynamic-system UI.
- Always pair SA metrics with workload and performance.
- Prefer scenario-realistic measurement contexts over abstract lab-only tasks when making operational design decisions.
- Use SA requirements analysis first; only then author probes and choose methods.

## Lifecycle
- supersedes: none
- superseded_by: none
- deprecation_reason: n/a
