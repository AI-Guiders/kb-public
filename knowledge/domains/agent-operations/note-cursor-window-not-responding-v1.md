# Cursor: The window is not responding (Reopen / Close / Keep Waiting)
**Tags:** #agent-operations #cursor #harness #epsilon #continuity
**Status:** Identified · 2026-07-31
**Links:** `note-cursor-planning-connection-flake-v1.md` · VS Code `windowImpl.ts` stall path

## Identity

Это **не** диалог Windows «приложение не отвечает / Завершить задачу».

Это **Electron/VS Code/Cursor** main-process `dialog.showMessageBox`:

- message: `The window is not responding`
- detail: `You can reopen or close the window or keep waiting.`
- buttons: **Reopen** · **Close** · **Keep Waiting**

Источник: `src/vs/platform/windows/electron-main/windowImpl.ts` (WindowError unresponsive).

Отдельное нативное окно — **не** overlay над Composer → **CDT JS не кликает**.

## Response (organ)

AutoI ≥ **0.5.316**: post-fire `ConnectionWatch` → `IdeIgniteNativeDialogs.TryClickKeepWaiting()` (Win32 EnumWindows + BM_CLICK).

## Not

- Не playbook.
- Не путать с Connection Problems → Retry (DOM/CDT).
- Close/Reopen = убить ход; Keep Waiting = ε-камень «дай отвиснуть».

## §7

Оператор как афферент (увидел stall) → AutoI organ. Lived Win-Win: `META/environment-axioms-v1.md` §7.

