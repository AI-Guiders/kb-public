# Avalonia UI / CascadeIDE — domain status v1

## Scope

Desktop UI на **Avalonia** с **Dock** (панели/документы), типичный стек **CascadeIDE**: XAML + MVVM, темы Fluent + кастомные JSON, встроенный редактор (AvaloniaEdit), дополнительные контролы (Markdown и др.). Домен **software.desktop-ui** в связке с **engineering**; продуктовые правила интерфейса — см. HCI (`playbook-hci-core-v1`, `ui-ux-playbook`).

## Reference stack (эталон репо CascadeIDE)

Версии зафиксированы в `CascadeIDE.csproj` (проверять при обновлении KB):

- `Avalonia` / `Avalonia.Desktop` / `Avalonia.Themes.Fluent` / `Avalonia.Fonts.Inter` — **11.3.x**
- `Dock.Avalonia`, `Dock.Model.Avalonia`, `Dock.Model.Mvvm`, `Dock.Avalonia.Themes.Fluent` — **11.3.11.x** (patch может отличаться от Avalonia — нормально, следить за совместимостью)
- `Avalonia.AvaloniaEdit`, `AvaloniaEdit.TextMate` — **11.0.x**
- `Markdown.Avalonia` — **11.0.x**
- `CommunityToolkit.Mvvm` — **8.x**
- TFM приложения: **net10.0**, `AvaloniaUseCompiledBindingsByDefault` — **true**

Исходники правды по макету приложения: `Views/MainWindow.axaml`, `Views/DocumentsDockView.axaml`, темы `Themes/*.json`, включение Dock Fluent в `App.axaml`.

## Completion state

Status: **Done v1** (фундамент + операционный playbook + индекс маршрутизации).

Artifacts:

- `status-avalonia-cascade-ide-ui-v1.md` (этот файл)
- `playbook-avalonia-dock-ui-v1.md`
- `kb-avalonia-ui-dock-fundamentals-v1.md`

См. также (литература, не имплементация): `kb-ide-dx-literature-evidence-v1.md` (DX/IDE, Osmani/Smalltalk/Boxer), `kb-ui-ux-literature-evidence-v1.md` (Norman/Nielsen/Shneiderman/Krug).

## Definition of done check

- Зафиксированы модель стека, версии и границы ответственности Dock vs встроенный `DockPanel`.
- Описан порядок **status → playbook → kb** и связь с `frontend-dotnet-playbook` / HCI.
- Router index содержит `router-avalonia-ui` и строку в Domain Entry Map.

## Active guardrails

- Не смешивать API **разных мажоров** Avalonia; при апгрейде пакетов сверять release notes Dock и AvaloniaEdit.
- Док-панели (**Dock.Model**) и простая разбивка (**`DockPanel`**) — разные уровни; не «чинить» докинг правками только `Grid` без проверки модели.
- Дизайн-задачи: сначала HCI/UX контракт, затем выбор контролов и измерение (сборка + визуальная проверка).

## Revisit triggers

- Смена мажорной версии Avalonia или Dock.
- Повторяющиеся регрессии биндингов, тем или layout после рефакторинга.
- Новый крупный UI-паттерн в CascadeIDE (новая зона докинга, отдельное окно инструментов) — дополнить fundamentals/playbook.

## Provenance

- source_refs: `CascadeIDE.csproj` (PackageReference, PropertyGroup), структура Views; дата синхронизации: 2026-03-20
- layer: meta / domain-status
- epistemic_basis: fact (версии из csproj); confidence: high для версий на дату обновления