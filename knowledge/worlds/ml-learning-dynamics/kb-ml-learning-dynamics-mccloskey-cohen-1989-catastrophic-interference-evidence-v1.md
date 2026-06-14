# Evidence: McCloskey & Cohen (1989) — Catastrophic interference in connectionist networks

## Provenance
- source_refs:
  - primary: McCloskey, M., & Cohen, N. J. (1989). Catastrophic interference in connectionist networks: The sequential learning problem. *The Psychology of Learning and Motivation*, *24*, 109–165. https://doi.org/10.1016/S0079-7421(08)60536-8
  - pdf: https://www.andywills.info/hbab/mccloskeycohen.pdf
  - text_consulted: **full** (web fetch 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Оригинал термина «catastrophic interference»; основа, на которую отвечают CLS (McClelland 1995), pseudorehearsal (Robins 1995), EWC (Kirkpatrick 2017).

## Metadata
- card_id: kb-ml-learning-dynamics-mccloskey-cohen-1989-catastrophic-interference-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, mccloskey-cohen-1989, catastrophic-interference, sequential-learning, distributed-representations, forgetting]
- status: active

## Epistemic Linkage
- epistemic_basis: primary_peer_reviewed_chapter + эксперименты
- evidence_type: connectionist simulation
- confidence: **high** для феномена; поздние работы уточняют условия/степень (French 1999; CLS)
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check** (мотивирует необходимость replay/protection; сам субстрат CASA — NCA, не backprop-MLP)
- falsification_trigger: на сопоставимой архитектуре sequential-обучение **не** разрушает старое (напр. разрежённые/локальные представления)

## Core Unit
- context: будут ли распределённые сети учиться **последовательно** (как люди), а не concurrent.
- signal: обучили сеть на «ones» фактах сложения, потом на «twos» — после одного прохода по «twos» сеть **уже не отвечает** на «ones».
- action: назвали явление **catastrophic interference**; показали его и на AB–AC paired-associate.
- outcome: интерференция катастрофична и качественно хуже человеческой retroactive interference.
- lesson: любое обучение, меняющее веса «старого», рискует его стереть → sequential learning требует явной защиты/replay.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Распределённые представления дают content-addressable memory и авто-генерализацию, **но** цена — перекрытие весов между элементами. |
| **K2** | Эксперимент 1 (арифметика): последовательное обучение «ones»→«twos» стирает «ones» почти полностью уже после первых trial'ов; даже общие факты (2+1,1+2) ломаются. |
| **K3** | Эксперимент 2 (AB–AC retroactive interference): сеть теряет AB при обучении AC намного сильнее, чем люди. |
| **K4** | Причина фундаментальна: **хотя бы некоторая интерференция** неизбежна, когда новое меняет веса «старого»; чем больше нового — тем сильнее разрушение. |
| **K5** | Граница: «catastrophic» показано для **конкретных** backprop-сетей; авторы явно не утверждают универсальности степени. |

### Ограничения
- Эпоха 1989: малые MLP; степень зависит от архитектуры/представления (sparse → меньше).

## Operationalization (CASA hypothesis only)
- first_adoption_task: мотивация для `bench_retention_v0` — воспроизвести интерференцию на CASA-субстрате как baseline.
- validation_check: sequential ingest без replay показывает forgetting gap > 0.
- success_criterion: replay (ADR-0009) / EWC (Kirkpatrick) заметно сокращают этот gap.
- rollback_or_mitigation: не предполагать ту же степень для NCA — измерять (K5).

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (PLM 24:109–165)*
