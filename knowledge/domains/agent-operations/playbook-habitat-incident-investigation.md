# Playbook: Habitat incident investigation
**domain:** agent-operations  
**Status:** living · 2026-09-13  
**Tags:** #habitat #incident #investigation #just-culture #losa #cdp #agent-operations #aviation-transfer

**Speech situation:** `audience=agent_internal` · `goal=operational_protocol` · `genre=playbook` · `channel=kb_canon` · `stakes=high` · `distance=professional`

**Principle (culture gate):** [`playbook-habitat-just-culture.md`](playbook-habitat-just-culture.md) · axiom §8 [`environment-axioms.md`](../../META/environment-axioms.md)  
**Aviation depth (do not duplicate here):** [`worlds/aviation-human-factors/kb-aviation-incident-investigation-fundamentals.md`](../../worlds/aviation-human-factors/kb-aviation-incident-investigation-fundamentals.md) · [`matrix-aviation-investigation-to-se-transfer.md`](../../worlds/aviation-human-factors/matrix-aviation-investigation-to-se-transfer.md)

---

## One line

**Формализованное расследование habitat:** snapshot → слои (latent/active) → habitat fix → tracked recommendation → ship → verify. **Blame narrative invalid** until substrate checklist passes (Just Culture).

---

## When mandatory

| Class | Trigger | Minimum output |
|-------|---------|----------------|
| **P0** | Data loss, silent wrong `ok`, prod/habitat down, security bypass | Full record + ADR or architecture gap + ship in same wake when fix known |
| **P1** | Operator-visible flake class (deploy, MCP disconnect, build gate miss) | Full record + domain/ops card or ADX |
| **P2** | Local friction, recovered without operator rescue | Short record or `@intent postmortem` one-liner |
| **Near-miss** | Would be P0/P1 with bad luck; caught early | Record if it exposes **latent** gap; skip ceremony if no substrate lesson |

**Not mandatory:** typo in chat, single test flake without pattern, already-filed duplicate ADX.

---

## Procedure (7 steps — do in order)

### 1. Freeze snapshot (LOSA)

Capture **observable state before narrative**. No root-cause story yet.

- CDP: `cdp_health` (ops_pulse, deploy_los, seats, continuity)
- Relevant organ pulse: build/test/deploy lifecycle last, domain card hint
- Tool JSON that misled (full `ok`/`quality`/`errors[]`, not paraphrase)
- Git: commit, branch, dirty paths (if code incident)
- Harness: MCP reload? bridge wait? Cursor Connection Problems?

**Rule:** if pulse existed and was ignored → **active** layer; if pulse missing → **latent** substrate gap.

### 2. Event timeline (facts only)

Bullet sequence: operator action → tool → outcome. Tag each line:

- **fact** — logged, reproducible
- **inference** — reasonable but not proven
- **hypothesis** — needs test

No «агент не дождался» until step 3 complete.

### 3. Swiss cheese / layers

Fill at least **three layers** (empty cell = investigate further):

| Layer | Question | Example (deploy flake 2026-09-12) |
|-------|----------|-----------------------------------|
| **Latent** | Old design/default still live? | ADR-0223 ship existed; default still `hard` |
| **Active** | What aligned today? | rollout → hard_sibling + toml lock |
| **Substrate** | Tool/host contract gap? | no deploy_los; create silent empty |
| **Harness** | MCP/stdio/Cursor outside CDP? | Client closed; mcp_auth reload |
| **Actor** | Good-faith / at-risk / reckless? | Only after rows above |

Use Reason model — **no single root cause**. See [`kb-reason-swiss-cheese-1990-evidence.md`](../../worlds/aviation-human-factors/kb-reason-swiss-cheese-1990-evidence.md).

### 4. Just Culture gate

Before any blame wording, answer:

1. What did habitat **promise** (schema, Meta description, domain invariant, ADR)?
2. What did habitat **pulse/refuse/warn**?
3. **Gap** = promise − pulse?

If gap ≠ ∅ → primary recommendation is **substrate fix**, not persona/training. Apply accountability matrix from Just Culture playbook.

**Reject:** closing investigation with only «agent should have…».

### 5. Recommendations (tracked)

Each finding → one row:

| ID | Layer | Recommendation | Owner artifact |
|----|-------|----------------|----------------|
| R1 | latent | default deploy → ship | ADR-0226 + code |
| R2 | substrate | deploy_los in ops_pulse | IdeOpsPulse + ops.md |

**Tracking equivalents (aviation AD/SB):**

- Product code → ADR in repo (`cdp-mcp/docs/adr/…`)
- Living architecture → `architecture-current.md` gap # (close when shipped)
- Operator canon → `.cdp/domain/*.md` last_ship
- Cross-cutting → ADX-HX-xxx in domain or ADR body

### 6. Ship + verify

- Fix **latent + substrate** before blaming actor layer.
- Tests for contract change; dry_run when deploy class.
- Verify: pulse shows new state (`deploy_los`, quality WARN, build anchors).
- P0/P1: operator sees closure (commit hash, health version, gap closed).

### 7. Close investigation

Investigation **closed** only when:

- [ ] Snapshot attached or cited
- [ ] ≥3 layers documented
- [ ] Just Culture gate passed (or explicit reckless with evidence)
- [ ] Each R* has owner artifact **or** wont-fix with reason
- [ ] Ship verify done for substrate fixes
- [ ] Lived example row added (below or linked ADR)

Optional: `@intent postmortem` / `cdp_postmortem` for CDP-native record; KB row here for cross-repo pattern.

---

## Investigation record (template)

Copy into postmortem, ADR Context, or WORK leaf:

```markdown
## Investigation: <short title> · <YYYY-MM-DD> · P0|P1|P2

### Snapshot (LOSA)
- health: …
- organ pulse: …
- tool evidence: …

### Timeline
1. (fact) …
2. (inference) …

### Layers
| Layer | Finding | epistemic |
|-------|---------|-----------|
| latent | … | fact/inference/hypothesis |
| active | … | … |
| substrate | … | … |
| harness | … | … |
| actor | error/at-risk/reckless/n-a | … |

### Just Culture gate
- Promise: …
- Pulse: …
- Gap: …

### Recommendations
| ID | Rec | Artifact | Status |
|----|-----|----------|--------|
| R1 | … | ADR-… / gap #… | open/shipped |

### Verify
- …
```

---

## CDP hooks (agent)

| Surface | Use |
|---------|-----|
| `@intent postmortem` / `cdp_postmortem` | Structured incident record in habitat |
| `cdp_health` | LOSA snapshot; post-ship `deploy_los`, seats |
| `cdp_lifecycle_last kind=deploy` | Deploy in-flight / last job |
| `go=quality` | Silent ok / create_empty class |
| `.cdp/domain/*` | Invariant + antipattern + last_ship |

---

## Lived examples

| Incident | Key layers | Ship |
|----------|------------|------|
| Deploy flake 2026-09-12 | latent default hard; active rollout hard_sibling; harness MCP reload | ADR-0226, `deploy_los`, commit `2542a09` |
| ADX-HX-003 empty create | substrate: `content=` ignored, silent ok | `DocumentEditPlane.Create`, quality WARN |
| Build 100+ after F# cutover | latent incomplete migration; substrate missing GlobalUsings signal | guiders-platform peel (in progress) |

---

## Maintenance

- New P0/P1 → one row in **Lived examples** + link artifact.
- Do not duplicate aviation KB body — link transfer matrix.
- Hub: [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md).

