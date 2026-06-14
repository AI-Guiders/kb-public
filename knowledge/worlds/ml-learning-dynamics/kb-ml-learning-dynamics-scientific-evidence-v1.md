# ML learning dynamics — scientific evidence index v1

## Provenance
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: ML-половина гипотезы CASA «педагогика развития». Якоря извлечены из полных PDF (web fetch 2026-05-31), кроме Robins 1995 (abstract+secondary, paywall).

## Metadata
- card_id: kb-ml-learning-dynamics-scientific-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- status: active

## Epistemic linkage
- transfer_boundary: ML-домен → CASA-инженерия **allow-with-check** (design протокола/bench, не slap-on oracle)
- falsification_trigger: новый обзор/replication меняет тезис строки → обновить карту и read_depth

---

## Index (источник → evidence card → read_depth)

### Якоря: куррикулум / starting small
| Источник | DOI / URL | Evidence card | read_depth |
|----------|-----------|---------------|------------|
| Elman (1993) Importance of starting small | [10.1016/0010-0277(93)90058-4](https://doi.org/10.1016/0010-0277(93)90058-4) | [`...elman-1993-starting-small...`](kb-ml-learning-dynamics-elman-1993-starting-small-evidence-v1.md) | **full** |
| Bengio, Louradour, Collobert & Weston (2009) Curriculum learning | [10.1145/1553374.1553380](https://doi.org/10.1145/1553374.1553380) | [`...bengio-2009-curriculum...`](kb-ml-learning-dynamics-bengio-2009-curriculum-evidence-v1.md) | **full** |

### Якоря: забывание / консолидация / replay
| Источник | DOI / URL | Evidence card | read_depth |
|----------|-----------|---------------|------------|
| McCloskey & Cohen (1989) Catastrophic interference | [10.1016/S0079-7421(08)60536-8](https://doi.org/10.1016/S0079-7421(08)60536-8) | [`...mccloskey-cohen-1989...`](kb-ml-learning-dynamics-mccloskey-cohen-1989-catastrophic-interference-evidence-v1.md) | **full** |
| Robins (1995) Rehearsal & pseudorehearsal | [10.1080/09540099550039318](https://doi.org/10.1080/09540099550039318) | [`...robins-1995-pseudorehearsal...`](kb-ml-learning-dynamics-robins-1995-pseudorehearsal-evidence-v1.md) | abstract+secondary |
| McClelland, McNaughton & O'Reilly (1995) CLS | [10.1037/0033-295X.102.3.419](https://doi.org/10.1037/0033-295X.102.3.419) | [`...mcclelland-1995-cls...`](kb-ml-learning-dynamics-mcclelland-1995-cls-evidence-v1.md) | **full** |
| Kirkpatrick et al. (2017) EWC | [10.1073/pnas.1611835114](https://doi.org/10.1073/pnas.1611835114) | [`...kirkpatrick-2017-ewc...`](kb-ml-learning-dynamics-kirkpatrick-2017-ewc-evidence-v1.md) | **full** |

### Якоря: spacing / обратная связь
| Источник | DOI / URL | Evidence card | read_depth |
|----------|-----------|---------------|------------|
| Cepeda, Pashler, Vul, Wixted & Rohrer (2006) Distributed practice | [10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354) | [`...cepeda-2006-distributed-practice...`](kb-ml-learning-dynamics-cepeda-2006-distributed-practice-evidence-v1.md) | **full** |
| Christiano et al. (2017) RL from human preferences + Ouyang et al. (2022) InstructGPT | [arXiv 1706.03741](https://arxiv.org/abs/1706.03741) · [arXiv 2203.02155](https://arxiv.org/abs/2203.02155) | [`...rlhf-christiano-2017-ouyang-2022...`](kb-ml-learning-dynamics-rlhf-christiano-2017-ouyang-2022-evidence-v1.md) | **full** |

**Roadmap (третья волна, ещё не извлечено):** French (1999) обзор catastrophic forgetting; Ratcliff (1990); Rohde & Plaut (1999) критика starting-small; Kumaran, Hassabis & McClelland (2016) CLS-update; Ebbinghaus (1885) первоисточник spacing.

---

## Связь с CASA

Эти карты — доказательная база для `research-training-developmental-pedagogy-v1` (секция «инженерная половина») и для ADR-0009 (replay/retention) / ADR-0010 (predict/value) репозитория `casa-ontology-payload`. Сиблинг — человеческая половина [`cognition.language-acquisition`](../cognition-language-acquisition/README.md) (`deny`).

*Версия: v1.1 · 2026-05-31 — 8 якорных карт (волны 1+2)*
