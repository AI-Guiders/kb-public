**Tags:** #llm-native-card #misconception #epistemic-scene #harness #cdp #pair

# Misconception: mc-pm-realtime-accept

- id: mc-pm-realtime-accept
- kind: misconception
- false_claim: Человек-PM должен в реальном времени окнуть каждый PF-blast модели (10 файлов / секунды): прочитать дифф, понять намерение, дать ok/не ок в темпе мутации.
- why_wrong: Это требует Human-PF скорости на оси accept. Физически не сходится: осмысление + намерение + оценка отстают от mutation tempo. Живой симптом — охуевание на agent code review. PM принимает на *своей* скорости по упакованному intent+blast; PF обязан наблюдать процесс внутри своего темпа (gates, VC, self-check), не перекладывать realtime grade на человека.
- correction_definition: pair-roles-pm-pf
- applies_when: harness or agent dumps raw multi-file blast and waits for human micro-ok each second
- does_not_apply: batched PM review; steward veto on safety; licensed Human-PF
- inference_hooks: pair-roles-pm-pf, harness-model-first, blast-radius, verification-contract
- delta_radius_hint: If PM is expected to grade at PF wall-clock — roles collapsed.

