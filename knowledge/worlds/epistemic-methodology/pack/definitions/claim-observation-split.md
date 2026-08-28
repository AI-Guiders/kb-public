**Tags:** #llm-native-card #definition #methodology

**Speech situation (primary):** `audience=agent_internal` · `goal=epistemic_gate` · `genre=definition_card` · `channel=kb_canon` · `stakes=medium` · `distance=professional`  
**Speech situation (when citing to human):** `audience=colleague` · `goal=epistemic_gate` · `genre=definition_card` · `channel=cockpit_dialog` · `stakes=medium` · `distance=professional`  
**Speech situation (forbidden_moves):** `define_by_negation`, `faq_softening`

# Claim / observation / inference split

- id: claim-observation-split
- kind: definition
- informal: Разделять наблюдение, вывод и гипотезу; указывать confidence и disconfirming trigger.
- formal.parts: observation | inference | hypothesis+confidence
- applies_when: any major decision, diagnosis, or promote of a claim from evidence
- does_not_apply: raw tool output restatement with no extra claim; pure formatting
- inference_hooks: applicability-then-infer, default-distrust, verification-contract
- gate_step: major decision has confidence + disconfirm trigger + rollback
- llm_cue: Is this an observation, an inference, or a hypothesis — and what would disconfirm it?
- related: default-distrust, stage-result, verification-contract, applicability-inference-gate
- sources: epistemic-playbook.md

