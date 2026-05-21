<!-- markdownlint-disable MD032 -->

# Psychology Foundations Playbook v1

## Purpose

Base layer for psychological models that frequently appear in human decision loops, communication failures, and deep-pattern behavior.

Scope of this playbook:
- foundational schools (Freud, Jung, Adler, Berne, Fromm, Horney, Klein, Bowlby, Frankl);
- model boundaries (where each school helps and where it overreaches);
- operational transfer into dialogue and support design.

## Epistemic Contract

- Distinguish `historical-theory value` from `modern empirical support`.
- Label claims as:
  - `fact` (well-established historical attribution or robust evidence),
  - `inference` (model-based interpretation),
  - `hypothesis` (working assumption needing validation).
- For any clinical-strength claim, require primary source or modern review before operationalization.

## Canonical Baseline (Layer 0)

- **Freud** (psychoanalysis): unconscious conflict, defense mechanisms, structural model (`id/ego/superego`).
- **Jung** (analytic psychology): archetypes, collective unconscious, individuation.
- **Adler** (individual psychology): inferiority feelings, compensation, striving, social interest.
- **Berne** (transactional analysis): Parent-Adult-Child ego states, transaction patterns.
- **Fromm** (humanistic psychoanalysis): social character, freedom-anxiety, conformity/authoritarian escape routes.
- **Horney**: basic anxiety, interpersonal coping orientations, critique of orthodox Freudian assumptions.
- **Klein**: object relations, early internal object dynamics, depressive/paranoid-schizoid positions.
- **Bowlby**: attachment system and internal working models.
- **Frankl**: logotherapy, meaning orientation under suffering and constraint.

## Router: When To Use Which Lens

- Use `Freud/Jung/Klein` for **symbolic and deep-pattern interpretation** (high risk of over-interpretation; require caution).
- Use `Adler/Berne` for **interaction dynamics and practical relational patterns**.
- Use `Bowlby/Horney` for **attachment anxiety and relational safety design**.
- Use `Fromm/Frankl` for **value, meaning, freedom, and social pressure conflicts**.

## Do-Not-Overreach Rules

- Do not turn a single school into a universal explanatory engine.
- Do not infer pathology from one dialogue fragment.
- Do not treat metaphoric frameworks as empirical proof.
- Do not export culture-bound interpretation between countries without local validation.

## Operational Use in This Workspace

- Primary target: improve conflict diagnosis and communication routing in mixed human/agent dialogues.
- Secondary target: support world separation (`culture.global`, `culture.country-specific`, `psychology.*`) without model leakage.
- Integration points:
  - `matrix-culture-routing-v1.md`
  - `matrix-do-not-transfer-v1.md`
  - `templates/template-knowledge-card-v1.md`

## Quality Gates For New Psychology Cards

- Must include `transfer_boundary`.
- Must include `falsification_trigger`.
- Must include at least one caution statement against overgeneralization.
- Must specify whether the claim is historical, empirical, or interpretive.

## Validation Snapshot v1 (Modern Evidence Layer)

- **Psychodynamic psychotherapy**: umbrella/meta evidence supports effectiveness for several common disorders; condition-specific strength remains uneven.
- **Attachment framework**: broad longitudinal and meta-analytic support for moderate stability and predictive utility (probabilistic, not deterministic).
- **Transactional analysis**: growing evidence base with positive effects in reviews; heterogeneity and quality variation require cautious operational use.
- **Meaning-centered interventions / logotherapy-derived methods**: supportive effects in specific contexts (notably oncology/palliative settings), generalization limits remain.
- **Object-relations constructs**: strong conceptual influence and measurement work, but therapeutic-effect evidence is less consolidated than broader psychodynamic outcomes.

Operational rule:
- router-level policy promotion requires at least one modern review class source and explicit uncertainty note.

## Cross-Cultural Validation Snapshot v1

- **Culturally adapted interventions**: meta-analytic evidence indicates adapted protocols often outperform non-adapted delivery in relevant populations.
- **Multicultural practice guidance**: APA-style intersectional/context-aware principles are useful as operational guardrails for clinician/research communication.
- **Structured cultural assessment**: DSM-5 Cultural Formulation Interview (CFI) shows feasibility and clinical utility in multi-country settings.
- **Global implementation caution**: WHO mhGAP implementation literature highlights recurrent culture/context mismatch risks when local adaptation is weak.

Cross-cultural operational rule:
- any transfer from `psychology.*` to policy/action in diverse populations must pass:
  1) local context check,
  2) language/meaning check,
  3) power/ethics check,
  4) fallback to neutral safe framing when uncertainty remains.

## Domain Definition Of Done (Psych Foundations)

Psych foundations domain is considered "done v1" when:
- classical baseline exists in structured playbook form;
- modern validation snapshot exists with confidence and caveats;
- cross-cultural transfer limits are mapped to culture matrices;
- at least two large card batches exist (baseline + validation);
- index and routing links are synchronized in canonical notes.

## Open Questions

- Which classical constructs are most robust under modern replication standards?
- How to calibrate narrative-rich models (Jung/Fromm/Frankl) against measurable outcomes?
- What minimum evidence threshold is needed before promoting a psychology card to router-level policy?

<!-- markdownlint-enable MD032 -->
