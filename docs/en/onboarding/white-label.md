# Connect your org KB (white-label)

**For org founders:** step-by-step playbook in kb-public:

[playbook-org-kb-white-label-v1.md](../knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md)

**Templates** (CONTRIBUTING, CODEOWNERS, README for `{ORG_SLUG}/kb`): [templates/newcomer](../knowledge/templates/newcomer/README.md) — `template-org-kb-bootstrap-*`.

**Team member** (already has personal + group access): [30-minute onboarding](quick-start-30min.md) and phase 4 in [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md).

**Contour map:** [Three contours](three-contours.md) — `{ORG_SLUG}` placeholder, not tied to one brand.

*Example instance:* org `AI-Guiders`; use your slug for your org.

## Short plan (phases)

| Phase | Action |
|-------|--------|
| A | Repos `{ORG_SLUG}/kb-public` + `{ORG_SLUG}/kb` (private), LICENSE, CONTRIBUTING |
| B | Source canon maintainer: `public-kb.ignore`, `group-kb.ignore`, sanitization |
| C | `build-public-kb.ps1` → push public |
| D | `seed-org-kb.ps1` → push group |
| E | Members: [clean setup](clean-setup.md), phase 4 |

## Roles

| Role | Scope |
|------|-------|
| **org-maintainer** | review/merge group KB |
| **canon-maintainer** | public builds, push kb-public |
| **member** | personal canon + read group/public |
