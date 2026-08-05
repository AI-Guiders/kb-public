**Tags:** #llm-native-card #definition #software-authoring

# Noun/verb analysis

- id: noun-verb-analysis
- kind: definition
- informal: Существительные → кандидаты в типы; глаголы → операции/сценарии.
- formal.steps: extract_nouns, extract_verbs, drop_technical_noise, merge_synonyms, assign_operations
- gate_step: each_stable_domain_noun_maps_to_type_or_field_decision
- llm_cue: Did I treat Kind/switch as domain, or list nouns first?
- related: ooa, ood
- sources: worlds/software-authoring/kb-ooad-fundamentals-v1.md#3

