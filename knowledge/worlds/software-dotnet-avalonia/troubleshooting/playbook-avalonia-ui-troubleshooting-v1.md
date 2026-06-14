# Playbook: Avalonia UI — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** нет подсветки, сломалось после апгрейда пакетов, jank списка, красный биндинг, Dock не сохраняет layout  
> **Операции:** `../playbook-avalonia-dock-ui-v1.md` · **неявный симптом:** [`../../software-authoring/troubleshooting/`](../../software-authoring/troubleshooting/)

---

## Симптом → действие

| Симптом | Сначала проверить | Частая причина |
|---------|-------------------|----------------|
| **Нет подсветки** в редакторе | Bundle TextMate на диске/в ресурсах; `Content`/`EmbeddedResource`; расширение файла vs регистрация grammar; лог старта редактора | Не скопирован bundle / неверный grammar id |
| **Сломалось после апгрейда** Avalonia/AvaloniaEdit | Матрица версий **Avalonia** ↔ **AvaloniaEdit.TextMate**; release notes | Дрейф версий редактора |
| **Красный биндинг / null в runtime** | `dotnet build`; DevTools (runtime); путь DataContext | Ошибка только в run, не в design-time |
| **Dock / вкладки** странное поведение | Factory, layout persistence, версия Dock.* | VM не синхронизирован с Dock.Model |
| **Список лагает при скролле** | Виртуализация (`VirtualizingStackPanel`); тяжёлый `DataTemplate` | Сотни элементов без virtualize |
| **Markdown/контрол** обрезан | Scroll, MaxHeight, стили темы | Наследование шрифтов |
| **exe locked при build** | Процесс приложения / netcoredbg | См. [`../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md`](../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md) |

---

## Чеклист (короткий)

1. `dotnet build -c Release` после существенных AXAML-правок.
2. Smoke редактора: открытие файла, поиск, перенос строки, смена темы, ввод в большом файле.
3. При новом языке в TextMate — один grammar + один smoke-файл, не смешивать с редизайном окна.

---

## Что НЕ причина

| Ложная гипотеза | Почему |
|-----------------|--------|
| «Нужен WPF designer» | В Avalonia цикл AXAML → build → run; DevTools в dev |
| Версия major сама по себе | Сверить `PackageReference` Avalonia* в **csproj целевого приложения** и release notes пакетов |

---

## Связанные

- C# / Roslyn: [`../../software-dotnet-tooling-roslyn/troubleshooting/`](../../software-dotnet-tooling-roslyn/troubleshooting/)
- Сборка/тест: [`../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md`](../../hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md)
- Карточка инцидента: `templates/cards/template-knowledge-card-v1.md`

---

## Как дополнять

Строка в таблицу; детали API — в `kb-avalonia-ui-dock-fundamentals`, не дублировать факты.

