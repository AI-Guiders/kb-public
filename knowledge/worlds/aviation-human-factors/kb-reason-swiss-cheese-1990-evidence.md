# Evidence: Reason (1990) — Swiss Cheese / layered defenses

**Tags:** #aviation-human-factors #paper-evidence #reason #investigation #worlds

## Provenance

- source_refs:
  - primary: Reason, J. (1990). *Human Error*. Cambridge University Press. (Swiss cheese model developed across this work and later summaries)
  - widely cited summary: Reason, J. (2000). Human error: models and management. *BMJ*, *320*(7237), 768–770. PMC1117770
- created_at: 2026-08-30
- extraction_note: Модель широко репродуцируется в HF training; для цитат — BMJ open access + primary book.

## Metadata

- card_id: kb-reason-swiss-cheese-1990-evidence-v1
- world: aviation.human-factors
- layer: knowledge
- tags: [paper-evidence, swiss-cheese, investigation, system-safety]
- status: active

## Epistemic linkage

- epistemic_basis: synthesis_from_primary_literature
- evidence_type: academic monograph + clinical summary
- confidence: **high** для модели слоёв; **medium** при переносе в non-safety software без calibration
- transfer_boundary: метафора слоёв ≠ excuse for no individual accountability (Just Culture still applies)
- falsification_trigger: если post-incident review находит «один root cause» без org/tooling layers — investigation too shallow

## Fundamentals

### K1 — Swiss cheese

Defenses are layers with **holes** (weaknesses). Accident when holes **align** transiently — not because one layer «failed alone».

### K2 — Active vs latent failures

- **Active:** unsafe acts at sharp end (operator, pilot)  
- **Latent:** organizational decisions, tooling, training — dormant until aligned

### K3 — vs «root cause»

Single-root narrative **underfits** complex systems. Investigation should map **multiple contributing layers**.

### K4 — Implication for culture

Fix **system holes**, not only punish last actor — aligns with Just Culture and aviation investigation statutes.

## Operationalization (Guiders / SE)

| Layer hole | Federation example |
|------------|-------------------|
| Latent: policy | TP orphan policy not updated |
| Latent: tooling | nuget.org no policy API |
| Active: agent | Wrong pin in release |
| Active: human | Merged without briefing |
| Alignment | Prod symbol push failed + stale alliance + no EICAS watch |

Pain inventory + ADR = **close holes** with tracked recommendations.

## Lifecycle

- related: `kb-aviation-incident-investigation-fundamentals.md`, `matrix-aviation-investigation-to-se-transfer.md`, GUIDERS pain inventory

