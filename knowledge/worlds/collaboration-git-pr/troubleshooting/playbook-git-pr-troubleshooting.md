---
type: Playbook
title: 'Playbook: Git / PR — troubleshooting'
description: '> **Контур:** A · kb-public'
tags: [collaboration-git-pr, living, playbook, worlds]
world: collaboration
subworld: git-pr
---
# Playbook: Git / PR — troubleshooting


> **Контур:** A · kb-public  
> **Когда:** commit rejected (identity), submodule pointer, whitespace-only diff noise  
> **Workflow:** [`../playbook-git-workflow.md`](../playbook-git-workflow.md)

---

## Симптом → действие

| Симптом | Действие |
|---------|----------|
| `Author identity unknown` / empty ident | [`../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting.md`](../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting.md) § Git identity |
| `modified: submodule` без своих правок | Bump указателя подмодуля в родителе (`git add path`) |
| Сгенерированный `.g.cs` «changed» но совпадает с HEAD | `git restore` файла; не `assume-unchanged` без нужды |
| Много EOL/BOM-only в preflight | `git_preflight` → `git_preflight_fix_safe` (renormalize) |

---

## Как дополнять

Product-specific git (monorepo layout) — `work/projects/…` README § Git.

