# Playbook: .NET Roslyn / MCP — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** CSxxxx, warning не уходит, code action не применяется, ошибка только в `dotnet build`, rename/find usages  
> **Протокол агента:** [`../playbook-csharp-roslyn-mcp-diagnostics-v1.md`](../playbook-csharp-roslyn-mcp-diagnostics-v1.md)  
> **Глубина refactor/debug:** [`../dotnet-roslyn-debug-playbook.md`](../dotnet-roslyn-debug-playbook.md)

---

## Симптом → действие

| Симптом | Действие |
|---------|----------|
| Ошибка в **новом** `.cs`, агент «закончил» | `roslyn_get_diagnostics` по **каждому** новому/затронутому файлу + solution; не только ReadLints |
| Ошибка видна только в **build** | Повторить Roslyn по всем затронутым `.cs`; MSBuild — дополнение, не замена |
| Warning «неиспользуемое» | `get_code_actions` → `apply_code_action` / `fix_all_scope: document` |
| Rename не тот symbol | Позиция на **идентификаторе**, не на типе в сигнатуре (`find_usages`) |
| Extract method на один токен | Передать `end_line`/`end_column` диапазона выделения |
| MCP roslyn «Error» после kill dbg | `debug_stop`, не taskkill netcoredbg снаружи — см. tooling playbook |
| PDB locked при rebuild | `debug_stop` перед сборкой цели |

---

## Чеклист завершения задачи (C#)

1. `roslyn_get_diagnostics` (solution + `file_path` per changed `.cs`).
2. Fix errors via code actions; повтор diagnostics.
3. `dotnet build` — дополнительно.

---

## Ложные гипотезы

| Гипотеза | Почему |
|----------|--------|
| Ручной патч вместо code action | Пока MCP доступен — сначала Roslyn |
| Один файл в diagnostics достаточен | Ошибка часто в соседнем partial/файле |

---

## Связанные

- Сборка: [`../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md`](../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md)
- Структура кода: [`../../software-authoring/troubleshooting/`](../../software-authoring/troubleshooting/)
