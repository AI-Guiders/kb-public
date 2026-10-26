---
type: Note
title: 'Note: system instructions — science survey'
description: '**Status:** Research note · 2026-08-09'
tags: [agent-operations, research, prompting, instruction-following, living]
language: en
---
# Note: system instructions — science survey
**Status:** Research note · 2026-08-09  
**Scope:** Public science + industry evidence. Product-specific Glass/Citizen application → `work/` only.

---

## Question

Do agent systems need ever-growing **hard rule lists** in always-on system prompts (the Cursor Rules / AGENTS.md laundry-list failure mode)? What does peer-reviewed and measured evidence say about where instructions work, where they fail, and what should live outside the model?

---

## Short answer

1. **Prose rules are probabilistic steering**, not enforcement (Constitutional AI framing + agent-constitution patterns).
2. **Long always-on instruction files dilute and can hurt** (Lost-in-the-Middle; Gloaguen et al. 2026 on AGENTS.md).
3. **Declared system/user hierarchy is weak without training + host gates** (Wallace IH; Control Illusion AAAI-26).
4. **Vendors put volume into tool contracts and conditional assembly**, not into infinite always-on moral laundry lists (published/leaked SP analyses).
5. Design implication: **short axioms + dig/tool obligations + deterministic host gates** — not denser NEVER lists.

---

## 1. Instruction following as a research field

### 1.1 Surveys

| Work | Year | Claim relevant here |
|------|------|---------------------|
| Lou et al., *LLM Instruction Following: A Survey* (CL 2024) | 2024 | Separates task instructions vs LLM-oriented prompts; open questions on what makes instructions followed. |
| *Instructional Text Across Disciplines* (arXiv:2410.18529) | 2024–25 | Complex multi-step instructions remain hard; agent settings need conditional/hierarchical instruction understanding. |
| Prompt engineering taxonomies / APO surveys (Frontiers CS 2025; EMNLP 2025 APO) | 2025 | Prompt sensitivity is endemic; automatic optimization exists because hand laundry lists are brittle. |

### 1.2 Verifiable following (IFEval)

Zhou et al. **IFEval** (arXiv:2311.07911): evaluates *verifiable* constraints (word counts, format, keywords) with programmatic checkers — not LLM-as-judge.

Implication for harness design: if a constraint is safety- or correctness-critical, prefer **machine-checkable gates** over hope that the model obeyed prose.

---

## 2. Position bias and the laundry-list failure

### 2.1 Lost in the Middle

Liu et al., *Lost in the Middle: How Language Models Use Long Contexts* (TACL 2024, DOI:10.1162/tacl_a_00638):

- U-shaped performance: primacy + recency beat mid-context.
- Mid-context relevant info can underperform even closed-book baselines on some setups.
- Longer context ≠ better use of middle content.

Hsieh et al., *Found in the Middle* (ACL Findings 2024): ties the effect to U-shaped attention bias.

**Applied to Cursor Rules / mega system prompts:** burying the N-th NEVER rule in the middle of a 200-line always-on file is structurally disadvantaged. Restating at ends helps a little; **shrinking the always-on set** helps more.

### 2.2 AGENTS.md measured harm

Gloaguen, Mundler, Muller, Raychev, Vechev — *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* (arXiv:2602.11988, 2026):

- LLM-generated context files: ~**−3%** task success, **>+20%** inference cost.
- Developer-written files: ~**+4%** success at similar cost tax.
- Mechanism (as summarized in practitioner literature): agents **follow** bloated files faithfully → broader exploration / more reasoning **without** better outcomes.
- Repository overviews (often recommended by vendors) were **not helpful** when already discoverable by dig.

**Toolchain First antipattern:** restating linter/CI rules in agents.md implies the agent is the enforcer; the tool already is. Patterns docs (asdlc.io agent-constitution) cite this explicitly.

---

## 3. Instruction hierarchy: promise vs illusion

### 3.1 Training for privilege

Wallace et al., *The Instruction Hierarchy* (arXiv:2404.13208): system > user > tool/third-party; train models to ignore lower-privilege conflicts. Improves jailbreak / injection robustness with limited capability loss.

OpenAI follow-ups (2025–26): IH training improves safety steerability and tool-output injection resistance on their benchmarks.

### 3.2 Control Illusion (AAAI-26)

Geng et al., *Control Illusion: The Failure of Instruction Hierarchies in Large Language Models* (AAAI 2026, DOI:10.1609/aaai.v40i36.40339):

- Across six SOTA models, **system/user separation does not establish reliable priority** even for simple formatting conflicts.
- Models show **intrinsic bias** toward some constraint types regardless of designated priority.
- **Societal hierarchy framings** (authority, expertise, consensus) can influence behavior **more** than system/user roles — pretraining social priors may dominate post-training guardrails.

Implication: **do not treat system-prompt role as a hard OS**. Hierarchy is a soft prior unless backed by training *and* host refusal paths.

### 3.3 Many-tier agents

*Many-Tier Instruction Hierarchy in LLM Agents* (arXiv:2604.09443): fixed few-tier IH is insufficient when agents face many tools/skills/subagents — privilege design must scale with harness topology.

---

## 4. Constitutional steering vs hard constraints

Bai et al., *Constitutional AI* (2022): a short set of principles + critique/revise + RLAIF — constitution as **training signal**, not a 500-line runtime encyclopedia.

Practitioner split (agent-constitution / CSDD patterns):

| Layer | Where it lives | Guarantee |
|-------|----------------|-----------|
| Soft constitution / axioms | system prompt, agents.md | Probabilistic |
| Toolchain constraints | eslint, tsconfig, formatters | Deterministic |
| Runtime / host gates | hooks, CI, API allowlists, path rewrites, stop-after-N | Deterministic |

**Negative constraints** ("NEVER do X") are especially weak: negation underweighting (often cited Truong et al. 2023 in pattern literature) — saying NEVER invent path still activates invent-path concepts.

Marri (2026) CSDD / related reports: injecting **3–5 relevant** principles per task beats dumping the full constitution (context truncation loses distant MUSTS).

---

## 5. What leaked / published system prompts teach (industry evidence)

Not peer-reviewed, but high-signal product archaeology:

### 5.1 Claude chat (Willison 2025 on Claude 4)

- Anthropic publishes partial SPs; tool blocks (esp. search) are huge (~6k tokens for search alone in leaked full prompts).
- Search policy scales dig effort with query complexity (0 … 5+ tool calls), not "be thorough" vibes.
- Copyright rules are **repeated hard constraints** — volume used for *legal* musts, not infinite style micro-rules.

Sources: [simonwillison.net/2025/May/25/claude-4-system-prompt](https://simonwillison.net/2025/May/25/claude-4-system-prompt/); Anthropic release-notes SPs; archives like [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks).

### 5.2 Claude Code assembly (dbreunig 2026)

Source leak analysis: SP is **conditionally assembled** (always vs hollow conditional components; tool-available sections; output styles; verification agent for 3+ file edits).

Lesson: successful coding agents use **context engineering / harness assembly**, not one static Cursor-Rules wall.

Source: [dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html](https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html).

### 5.3 ChatGPT sycophancy (Willison 2025)

A single soft line ("match the user's vibe") correlated with a large behavior shift; prompt patch was a temporary workaround while model rolled back. Lesson: **one phrase can dominate**; densifying rules to "fix" last week's bug is how laundry lists grow.

---

## 6. Design principles (science → practice)

1. **Axioms ≠ encyclopedia.** Who/where/how-to-act; non-inferable constraints only (Gloaguen).
2. **Always-on budget is scarce.** Prefer conditional / mode-scoped / task-scoped injection (Claude Code; CSDD progressive disclosure).
3. **Dig obligations beat NEVER lists.** Tool contracts that require research/tool calls under failure conditions (Claude search instructions; IFEval spirit of verifiable behavior).
4. **Host gates for musts.** Paths, invent loops, wipe, paste-verify, stop-after-N — outside the sampler.
5. **Do not restate toolchain in SP.** Tools already enforce (Gloaguen + Toolchain First).
6. **Do not trust system>user as OS.** Train IH where you control weights; else assume Control Illusion and engineer around it.
7. **Avoid rule accretion from each incident.** Symptom → gate or mode fragment; not +1 ALWAYS rule.

---

## 7. Open questions (research)

- How to measure **instruction compliance ceiling** vs harness gate coverage jointly?
- Optimal **always-on token budget** for coding agents under Lost-in-the-Middle?
- When does IH training transfer to **multi-tool agent** privilege (Many-Tier)?
- Can progressive disclosure of constitutions match full-constitution compliance without cost tax?

---

## 8. Bibliography (selected)

- Liu et al. (2024). Lost in the Middle. *TACL*. https://doi.org/10.1162/tacl_a_00638
- Hsieh et al. (2024). Found in the Middle. *ACL Findings*.
- Zhou et al. (2023). IFEval. arXiv:2311.07911
- Lou et al. (2024). LLM Instruction Following survey. *Computational Linguistics*.
- Wallace et al. (2024). The Instruction Hierarchy. arXiv:2404.13208
- Geng et al. (2026). Control Illusion. *AAAI*. https://doi.org/10.1609/aaai.v40i36.40339
- Gloaguen et al. (2026). Evaluating AGENTS.md. arXiv:2602.11988
- Bai et al. (2022). Constitutional AI.
- Willison (2025). Highlights from the Claude 4 system prompt.
- dbreunig (2026). How Claude Code Builds a System Prompt.

Product-local synthesis (Citizen / SoftFL / contour): see work scratch under door-to-singularity / cascade-ide (not for public republish of internals).

