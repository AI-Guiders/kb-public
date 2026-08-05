**Tags:** #llm-native-card #definition #methodology

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

