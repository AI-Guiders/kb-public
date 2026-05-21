# Playbook: Git / PR — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** commit rejected (identity), submodule pointer, whitespace-only diff noise  
> **Workflow:** [`../playbook-git-workflow-v1.md`](../playbook-git-workflow-v1.md)

---

## Симптом → действие

| Симптом | Действие |
|---------|----------|
| `Author identity unknown` / empty ident | [`../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md`](../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md) § Git identity |
| `modified: submodule` без своих правок | Bump указателя подмодуля в родителе (`git add path`) |
| Сгенерированный `.g.cs` «changed» но совпадает с HEAD | `git restore` файла; не `assume-unchanged` без нужды |
| Много EOL/BOM-only в preflight | `git_preflight` → `git_preflight_fix_safe` (renormalize) |

---

## Как дополнять

Product-specific git (monorepo layout) — `work/projects/…` README § Git.
