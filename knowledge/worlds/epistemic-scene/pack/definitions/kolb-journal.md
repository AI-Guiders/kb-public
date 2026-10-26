---
type: Definition Card
title: Kolb journal (LLM-native)
description: 'Не жизнь между инференсами. Не monolith DRAFT. Паттерн как A&H — INDEX + drafts/*.md; JSONL только для pin/итога. Instance park = f(gesture): project → work/projects/…/kolb-journal; free-theme → personal/kolb. До layout — scout reuse.'
tags: [llm-native-card, definition, epistemic-scene, cdp-adr-0002, harness]
world: epistemic
subworld: scene
---

# Kolb journal (LLM-native)

- id: kolb-journal
- kind: definition
- informal: Не жизнь между инференсами. Не monolith DRAFT. Паттерн как A&H — INDEX + drafts/*.md; JSONL только для pin/итога. Instance park = f(gesture): project → work/projects/…/kolb-journal; free-theme → personal/kolb. До layout — scout reuse.
- formal.is_not: continuous existence between inferences; chat CoT substitute; monolith DRAFT; inventing sheets/ when drafts/ exists; JSONL as planning surface; one hard-coded cascade-ide park for all gestures; free-theme under synthetic work/projects
- formal.is: routed dual park reusing A&H INDEX+drafts shape + settle ledger; park_root chosen by gesture
- formal.park_path: f(gesture) — see park_by_gesture
- formal.park_by_gesture: project|task → work/projects/<scope>/<project>/scratch/kolb-journal/; free-theme|curiosity → personal/kolb/; disposable → temp/; epic continuity → scratch/checkpoint-*.handoff (sibling, not Kolb)
- formal.park_pilot_project: work/projects/door-to-singularity/cascade-ide/scratch/kolb-journal/
- formal.park_free_theme: personal/kolb/
- formal.park_index: <park_root>/INDEX.md
- formal.park_hot: <park_root>/DRAFT.md
- formal.park_drafts: <park_root>/drafts/
- formal.settle_path: <park_root>/JOURNAL.jsonl
- formal.park_ops: <park_root>/README.md
- formal.facet: memory_project (roots work/projects + personal); not memory_world; not memory_self_finding (memo/hash-gate ≠ workbook)
- formal.reuses: work/projects/door-to-singularity/agents-and-humans/INDEX.md; work/projects/door-to-singularity/agents-and-humans/drafts/; cascade-ide/scratch spike-*/checkpoint-*.handoff.md; playbook-agent-notes-section-store-hygiene.md; personal/operator-guides/personal-playbook.md
- formal.park_how: scout reuse first; choose park_root by gesture; new topic → drafts/kj-*.md + INDEX row + hot stub; pin → JOURNAL.jsonl with draft_ref; read INDEX then one draft; free-theme with ПДн stays in personal (no public promote as-is)
- formal.park_tool: memory_project_* ; not Shell; not endless append to one DRAFT
- formal.allowed_moves: sketch; cite; claim×source; contradiction hunt; scratch formalization; settle pin
- formal.why: (1) PF workbook freedom; (2) avoid agent-notes monolith; (3) reuse existing INDEX+drafts; (4) JSONL indexes pins; (5) free-theme ≠ fake project; personal hygiene for PII
- formal.care: stranger uses INDEX → draft; JOURNAL for decisions; do not put personal PII into work/projects park
- applies_when: curiosity-kolb-loop; wide planning; pinning conclusion
- does_not_apply: inventing parallel folder names; stuffing episodes into DRAFT.md; planning in JSONL; mounting free-theme under work/projects
- inference_hooks: curiosity-kolb-loop, kolb-journal-park, mutate-plan-then-act, harness-model-first
- llm_cue: Which gesture → which park_root? Named A&H drafts/INDEX — or inventing sheets/ again?
- related: kolb-loop, curiosity-drive, harness-model-first, kolb-journal-park, mutate-plan-then-act
- sources: scratch/kolb-journal/README.md, personal/kolb/README.md, agents-and-humans/drafts/README.md, CDP-ADR-0002, personal-playbook.md

