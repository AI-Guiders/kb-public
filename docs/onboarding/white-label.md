# White-label: свой org KB

Любая организация: **`{ORG_SLUG}/kb`** + **`{ORG_SLUG}/kb-public`**.

**Playbook:** [playbook-org-kb-white-label-v1.md](../knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md)  
**Шаблоны:** `template-org-kb-bootstrap-*` в [newcomer](../knowledge/templates/newcomer/README.md)

## Кратко

| Фаза | Действие |
|------|----------|
| A | Репозитории public + private, LICENSE, CONTRIBUTING |
| B | Source canon maintainer: ignore-файлы, санитизация |
| C | `build-public-kb.ps1` → push public |
| D | `seed-org-kb.ps1` → push group |
| E | Участники: [clean-setup](clean-setup.md) фаза 4 |

**Документация:** этот сайт (MkDocs), не GitHub wiki.

## Роли

**org-maintainer** (review group) · **canon-maintainer** (сборки) · **участник** (personal + read group/public)
