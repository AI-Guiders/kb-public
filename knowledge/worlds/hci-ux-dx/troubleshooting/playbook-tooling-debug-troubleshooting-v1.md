# Playbook: tooling — build, test, debug (troubleshooting v1)

> **Контур:** A · мир **hci.ux-dx** (сквозной tooling для .NET и IDE) · kb-public  
> **Канон:** этот файл; легаси-редирект: [`../../tooling-debug-playbook.md`](../../tooling-debug-playbook.md)  
> **Roslyn depth:** [`../../software-dotnet-tooling-roslyn/troubleshooting/`](../../software-dotnet-tooling-roslyn/troubleshooting/)

---

## Purpose

Build, test, diagnostics, debugging across .NET projects; кратчайший цикл обратной связи.

---

## Симптом → куда

| Симптом | Действие |
|---------|----------|
| CSxxxx / analyzer / code fix | Roslyn troubleshooting (см. ссылку выше) |
| `Author identity unknown` / empty ident | § Git identity ниже |
| Flaky test / build break / exe locked | § Build/test + Debugging workflow |
| «Тормозит» runtime .NET | [`../../software-dotnet-csharp/troubleshooting/`](../../software-dotnet-csharp/troubleshooting/) |
| Avalonia runtime-only bug | [`../../software-dotnet-avalonia/troubleshooting/`](../../software-dotnet-avalonia/troubleshooting/) |

---

## Evidence-based loop

- **Fact:** failing signal (build, test, runtime).
- **Hypothesis:** smallest corrective action.
- **Check:** focused rebuild/retest/debug.
- **Decision:** close/escalate threshold upfront.

---

## Operational baseline

- Shortest loop first: lint/diagnostics → build → test.
- Isolate scope: file → project → solution.
- Reproducible debug state (breakpoints, target, args, env).

---

## Build and test

- Build failures before optional refactors.
- Flaky tests tracked, not ignored.
- CI aligned with local where practical.

---

## Git identity triage

| Step | Command / check |
|------|-------------------|
| 1 | `git config --show-origin --get user.name` / `user.email` |
| 2 | `git var GIT_AUTHOR_IDENT` / `GIT_COMMITTER_IDENT` |
| 3 | Env: `GIT_AUTHOR_*`, `GIT_COMMITTER_*`, `EMAIL` |
| Workaround | `git -c user.name=… -c user.email=… commit …` |

Подробнее Git workflow: [`../../collaboration-git-pr/playbook-git-workflow-v1.md`](../../collaboration-git-pr/playbook-git-workflow-v1.md).

---

## Debugging workflow

1. Minimal repro.
2. Expected vs actual before deep step.
3. Verify after each step-out/continue.
4. One root-cause note at end.

**MCP dotnet-debug:** `debug_continue` / `debug_stop`; не taskkill netcoredbg.

---

## Metrics & revisit

MTTR root cause; restore pipeline time; reopen rate; documented RCA %.  
Revisit if cycle times up, repeated failure class, low-signal debug sessions.

---

## Как дополнять

Product-specific tooling — `work/projects/…`; сюда — только обобщённые паттерны.
