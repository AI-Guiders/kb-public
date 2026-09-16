**Tags:** #llm-native-card #definition #epistemic-scene #blast-radius

# Blast Radius

- id: blast-radius
- kind: definition
- modes: feature, act
- informal: Насколько широко уйдёт мутация (файлы/символы/проекты) и что ещё неизвестно по краю.
- formal.measure: size of typed impact set + unknown fringe
- formal.classes: compatible | needs-update | unsafe
- gate_step: unknown_impact shrinks each planning step; impact typed before write
- gate_done: blast set known and accepted (no silent unsafe)
- llm_cue: Is blast radius known before write? If not — do not promote the mutation.
- related: debug-radius, verification-contract, stage-result, delta-radius-gate
- sources: work/projects/door-to-singularity/cascade-ide/kb-cide-sdm-decision-making-research.md, worlds/_llm-native-packs/note-pack-layers.md

