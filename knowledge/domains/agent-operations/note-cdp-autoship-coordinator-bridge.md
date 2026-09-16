# KB AutoShip — FileWatcher in CdpService
**Tags:** #agent-operations #cdp #autoship #git #agent-notes #living

**Status:** shipped · 2026-09-12 (CDP-ADR-0224, cdp-mcp `0b6619a`, habitat `0.5.764+0b6619a`)  
**Provenance:** `opencodedb` session `ses_f9741bec4ffe5WuDhUhSkaRL5m` · query via `execute_sql_opencodedb`  
**Implement leaf:** [`WORK-CDP-kb-autoship-filewatcher.md`](WORK-CDP-kb-autoship-filewatcher.md)

> **Correction (2026-09-12):** ранний bridge «AutoShip = coordinator git_plan» был **ошибкой**. Настоящая идея — **background FileWatcher** на KB repo, debounced commit+push без ручного ship агентом.

---

## Одна строка

**CdpService следит за `agent-notes` (и KB roots), после debounce тишины сам делает logical commit + `git push` (multi-remote через pushurl); конфликт → SA alert, не молчаливый фейл.**

---

## Зачем

Агент пишет KB через `cdp_buffer` / `memory_*` / `cdp_forum` — каждый раз вручную `git commit && push` = лишняя канитель и забывание.

Operator (2026-09-07): «обычный гитпуш на несколько remotes» — **один** `git push`, у origin два `pushurl` (github + wissance), не два отдельных push.

---

## Почему не hook в memory_* tool

Hook на каждую запись tool → записи **мимо** pipeline (Cursor Write, forum, buffer) выпадают.

**Писатель-агностично:** `FileSystemWatcher` на корне KB видит **любые** изменения на диске.

Repo git hooks / server triggers **не заменяют**: hook срабатывает на уже сделанный commit; server — на чужой push. Нужен **watcher в сервисе**.

---

## Design v0 (из OpenCode)

1. **Watch** — `FileSystemWatcher` в CdpService на primary KB root (`agent-notes`, paths из `--config`).
2. **Debounce** — ship после **90s тишины** (не ловить полузапись / parallel lines).
3. **Sync** — `git fetch`; если `origin/main` впереди локального HEAD → **SA alert, stop** (оператор решает). Не auto-rebase/auto-merge на markdown canon.
4. **Commit** — `git add -A` + message `KB auto: <path summary>` (logical slice по changed paths).
5. **Push** — `git push origin main` (multi pushurl); reject → alert.
6. **Tests** — debounce coalesce; conflict → alert not silent fail.

---

## Non-goals

- Auto-commit product code repos (только KB / configured canon roots).
- Silent force push.
- Замена `git_plan` для code ship on handoff.

---

## Связи

- [`note-opencode-dbhub-queries.md`](note-opencode-dbhub-queries.md) — как доставать обсуждение из OpenCode
- [`playbook-cursor-coordinator-local-workers.md`](playbook-cursor-coordinator-local-workers.md) — workers **не** push KB; AutoShip сервис закрывает KB
- CDP-ADR-0219 — соседняя волна (state consolidation)

