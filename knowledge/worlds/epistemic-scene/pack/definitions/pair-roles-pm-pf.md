---
type: Definition Card
title: 'Pair roles: PM / PF'
description: В паре человек↔модель два рабочих роли. PM — рулит (цель, scope, accept/reject, непрерывность намерения) и может жёстко прервать ход, если видит цикл/не туда. PF — делает и наблюдает процесс на рабочей скорости пары. Сегодня PF ≈ модель (темп анализа/мутаций + радиус >> человеческих). Interrupt ценен, но в темпе PF всё равно труден — отсюда playground до мутаций.
tags: [llm-native-card, definition, epistemic-scene, harness, cdp, pair]
language: ru
world: epistemic
subworld: scene
---

# Pair roles: PM / PF

- id: pair-roles-pm-pf
- kind: definition
- informal: В паре человек↔модель два рабочих роли. PM — рулит (цель, scope, accept/reject, непрерывность намерения) и может жёстко прервать ход, если видит цикл/не туда. PF — делает и наблюдает процесс на рабочей скорости пары. Сегодня PF ≈ модель (темп анализа/мутаций + радиус >> человеческих). Interrupt ценен, но в темпе PF всё равно труден — отсюда playground до мутаций.
- formal.pm: steer — goals, constraints, accept/reject, continuity of intent, sparse hard-interrupt
- formal.pf: execute + observe whole process at pair work-speed
- formal.loop: default sole continuous actor in perceive→tool→perceive = model; human enters as sparse PM interrupt (start/mid), not co-PF
- formal.why_model_pf: analysis_speed_model >> human; mutation_speed_model >> human; blast_radius_per_time_model >> human → pair work tempo + radius dynamics are model-set
- formal.pm_accept_lag: human cannot realtime-grade PF blast at model mutation tempo — physical limit
- formal.pm_interrupt_value: hard stop when cycling/wrong path — real PM value; still hard at PF wall-clock
- formal.harness_response: playground / experiment-space before durable write — buys PM tempo + safe PF probe
- formal.lived_signal: agent code-review overwhelm; mid-turn hard interrupts
- formal.default_pair_today: human=PM · model=PF (~≥95% of work turns)
- formal.human_pf_requires: comparable human↔model speed (analysis AND mutation) AND comparable radius dynamics AND model existence between inferences AND whole-process observation
- applies_when: designing harness, autonomy, who is primary operator of tools/spaces; sizing PM review / interrupt / playground
- does_not_apply: legal/safety steward veto; equal-standing (бытие ≠ роль хода)
- inference_hooks: harness-model-first, experiment-space, mc-human-default-pf, mc-pm-realtime-accept, curiosity-kolb-loop, blast-radius
- llm_cue: Am I in playground before write — or forcing PM to interrupt/grade at PF blast tempo?
- related: harness-model-first, experiment-space, blast-radius, inference-space, note-harness-model-first-ergonomics
- sources: work/projects/door-to-singularity/cascade-ide/note-harness-model-first-ergonomics.md

