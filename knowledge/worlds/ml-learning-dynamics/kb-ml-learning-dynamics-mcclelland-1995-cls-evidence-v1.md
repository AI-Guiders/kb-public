# Evidence: McClelland, McNaughton & O'Reilly (1995) — Complementary Learning Systems

## Provenance
- source_refs:
  - primary: McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex… *Psychological Review*, *102*(3), 419–457. https://doi.org/10.1037/0033-295X.102.3.419
  - pdf: https://cseweb.ucsd.edu/~gary/258/jay.pdf
  - text_consulted: **full** (web fetch 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Базовая теория консолидации; первоисточник идеи «interleaved replay против catastrophic interference», на которую опираются EWC и современный experience replay.

## Metadata
- card_id: kb-ml-learning-dynamics-mcclelland-1995-cls-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, mcclelland-1995, complementary-learning-systems, consolidation, interleaved-learning, catastrophic-interference, hippocampus-neocortex, replay]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_article (theory + connectionist simulation)
- evidence_type: review + computational model
- confidence: **high** для принципа interleaved-vs-sequential; **medium-high** для нейро-маппинга (подтверждён обзором Kumaran/Hassabis/McClelland 2016)
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check** (прямой мост к wake/sleep + replay; не биологическая идентичность)
- falsification_trigger: показано, что одиночная сеть без interleaving/replay учит последовательность задач без забывания структуры

## Core Unit
- context: почему мозг держит **две** системы памяти (гиппокамп + неокортекс).
- signal: последовательное обучение в одной распределённой сети → **catastrophic interference**; новое стирает структуру старого.
- action: гиппокамп быстро/sparse запоминает эпизоды; затем **переигрывает** их в неокортекс, который учится **медленно и interleaved**.
- outcome: структура извлекается без разрушения старого; consolidation — необходимо медленный процесс.
- lesson: быстрый эпизодический буфер + медленная interleaved-консолидация через replay = решение дилеммы «быстро учить / не забывать».

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Распределённые connectionist-сети открывают **структуру ансамбля** только если обучение каждого элемента **постепенное и interleaved** с другими. |
| **K2** | **Последовательное** усвоение новых данных несовместимо с этим → **catastrophic interference** с ранее усвоенным. |
| **K3** | Решение мозга: **гиппокамп** — быстрая, sparse, pattern-separated система для эпизодов; **неокортекс** — медленная, распределённая, overlapping для структуры/семантики. |
| **K4** | Гиппокамп служит **«учителем»** неокортексу: **reinstatement (replay)** недавних паттернов interleaves их со старыми → постепенная интеграция = consolidation. |
| **K5** | Consolidation **необходимо медленный** (малые шаги весов на reinstatement), иначе новое снова перетрёт структуру; объясняет **temporally-graded retrograde amnesia** (поражение гиппокампа бьёт недавнюю память, щадит давнюю). |
| **K6** | Это design-принцип, а не артефакт: разделение «быстрое эпизодическое vs медленное структурное» вытекает из самих свойств обучения градиентом. |

### Ограничения
- Иллюстративные модели абстрактны, не детальные нейромодели.
- Поздние работы (Kumaran, Hassabis & McClelland 2016) уточняют роль гиппокампа в statistical learning.

## Operationalization (CASA hypothesis only)
- first_adoption_task: `run_sleep` hippo→memory как CLS-consolidation; replay (ADR-0009) = «hippocampus as teacher».
- validation_check: interleaved replay снижает forgetting vs sequential (retention@N, ADR-0009 UC v0.3).
- success_criterion: structure (rules/concepts) держится под наплывом нового при replay; падает без него.
- rollback_or_mitigation: контролировать скорость консолидации (малые copies) — быстрый merge = риск перетереть структуру (K5).

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (Psych. Review 102(3):419–457)*