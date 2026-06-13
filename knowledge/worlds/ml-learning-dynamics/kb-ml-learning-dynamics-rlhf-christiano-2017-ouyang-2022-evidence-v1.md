# Evidence: RLHF — Christiano et al. (2017) + Ouyang et al. (2022, InstructGPT)

## Provenance
- source_refs:
  - christiano2017: Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. *NeurIPS 30*. arXiv:1706.03741. https://arxiv.org/abs/1706.03741
  - ouyang2022: Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 35*. arXiv:2203.02155. https://arxiv.org/abs/2203.02155
  - text_consulted: **full** обоих PDF (web fetch 2026-05-31)
- created_at: 2026-05-31
- updated_at: 2026-05-31
- extraction_note: Кластер из двух работ: принцип (preference-based reward) + масштаб на LLM (SFT→RM→PPO).

## Metadata
- card_id: kb-ml-learning-dynamics-rlhf-christiano-2017-ouyang-2022-evidence-v1
- world: ml.learning-dynamics
- layer: knowledge
- tags: [paper-evidence, rlhf, christiano-2017, ouyang-2022, instructgpt, preference-learning, reward-model, alignment, richer-than-scalar]
- status: active

## Epistemic Linkage
- epistemic_basis: две primary peer-reviewed работы + эксперименты
- evidence_type: ML алгоритм + RL/LLM эксперименты
- confidence: **high** для «preference/feedback signal эффективнее голого скаляра-лосса для intent-alignment»
- read_depth: **full**
- transfer_boundary: ML → CASA **allow-with-check** (ричер feedback и critic/value; PPO-машинерия не переносится буквально на NCA)
- falsification_trigger: на задаче CASA richer feedback (почему/предпочтение) не превосходит плотный скаляр при равном бюджете разметки

## Core Unit
- context: как сообщить агенту сложную цель, когда reward трудно задать руками / next-token мисалайнен.
- signal: **человеческие предпочтения** (пары траекторий / ранжирование выводов) несут больше, чем скалярный лосс.
- action: обучить **reward model** на предпочтениях, потом оптимизировать политику по нему (Christiano: RL; Ouyang: SFT→RM→PPO).
- outcome: Christiano — сложные Atari/MuJoCo задачи решены при feedback <1% взаимодействий; Ouyang — 1.3B InstructGPT предпочитаемее 175B GPT-3.
- lesson: ричер-than-scalar обратная связь + модель ценности/предпочтения дешёво выравнивает поведение под intent.

## Fundamentals

### K-тезисы
| # | Тезис |
|---|--------|
| **K1** | Christiano 2017: учим reward function из парных человеческих предпочтений между сегментами траекторий; reward обучается **одновременно** с политикой. |
| **K2** | Feedback дёшев: <1% взаимодействий; ±час человеческого времени учит новые поведения без доступа к true reward. |
| **K3** | Ouyang 2022 (InstructGPT): пайплайн **SFT → Reward Model на ранжированиях → PPO** против RM. |
| **K4** | Результат: выводы 1.3B InstructGPT предпочтительнее 175B GPT-3 (100× меньше параметров); выше truthfulness, ниже токсичность. |
| **K5** | Общий принцип: «предскажи следующий токен» мисалайнен с «следуй намерению»; выравнивание требует сигнала о предпочтении, а не только имитации. |
| **K6** | «Alignment tax» минимизируем (PPO-ptx) — можно выравнивать без большой регрессии на базовых NLP-задачах. |

### Ограничения
- PPO/RM — тяжёлая машинерия, не переносится на NCA буквально; для CASA берём идею richer-feedback/value, не алгоритм.
- reward hacking / переоптимизация RM — известные риски.

## Operationalization (CASA hypothesis only)
- first_adoption_task: critic даёт **почему/предпочтение** (richer-than-scalar) → rule episode + value-тег (ADR-0010 `lattice_value`); active ask при surprise (`lattice_predict`→CEN clarify).
- validation_check: richer feedback vs плотный скаляр на rule-uptake / held-out understanding при равном бюджете разметки.
- success_criterion: меньше teacher-вмешательств на тот же uptake (ср. <1% feedback у Christiano).
- rollback_or_mitigation: следить за reward-hacking value-тега (ограничения).

## Lifecycle
- supersedes: —
- superseded_by: —

*Версия: v1.0 · 2026-05-31 — full text (arXiv:1706.03741 + arXiv:2203.02155)*