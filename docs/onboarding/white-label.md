# Подключить свой org KB (white-label)

**Для основателя организации:** пошаговый playbook в репозитории kb-public:

[playbook-org-kb-white-label-v1.md](../knowledge/domains/agent-operations/playbook-org-kb-white-label-v1.md)

**Шаблоны** (CONTRIBUTING, CODEOWNERS, README для `{ORG_SLUG}/kb`): [templates/newcomer](../knowledge/templates/newcomer/README.md) — файлы `template-org-kb-bootstrap-*`.

**Участник команды** (уже есть personal + доступ к group): [Onboarding за 30 минут](quick-start-30min.md) и фаза 4 в [playbook-knowledge-stack-clean-setup-v1.md](../knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md).

**Карта контуров:** [Три контура KB](three-contours.md) — плейсхолдер `{ORG_SLUG}`, не привязка к одному бренду.

*Пример инстанса:* org `AI-Guiders` — одна реализация; для своей org подставь свой slug.

## Краткий план (фазы)

| Фаза | Действие |
|------|----------|
| A | Репозитории `{ORG_SLUG}/kb-public` + `{ORG_SLUG}/kb` (private), LICENSE, CONTRIBUTING |
| B | Source canon maintainer: `public-kb.ignore`, `group-kb.ignore`, санитизация |
| C | `build-public-kb.ps1` → push public |
| D | `seed-org-kb.ps1` → push group |
| E | Участники: [чистая установка](clean-setup.md), фаза 4 |

## Роли

| Роль | Зона |
|------|------|
| **org-maintainer** | review и merge в group KB |
| **canon-maintainer** | сборки public, push kb-public |
| **участник** | personal канон + read group/public |
