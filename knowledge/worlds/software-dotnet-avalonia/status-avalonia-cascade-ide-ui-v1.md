# Avalonia UI (desktop .NET) — domain status v1

## Scope

Desktop UI на **Avalonia** с **Dock** (панели/документы): XAML + MVVM, темы Fluent + кастомные JSON, AvaloniaEdit, Markdown и др. Домен **software.authoring.dotnet.csharp.desktop-ui.avalonia**; HCI — `../hci-ux-dx/`.  
**Product troubleshooting** (layout именованного IDE, user settings) — **только** [`work/troubleshooting/README.md`](../../work/troubleshooting/README.md), не этот status.

## Reference stack (пример: проверять csproj целевого приложения)

Версии зафиксированы в `CascadeIDE.csproj` (проверять при обновлении KB):

- `Avalonia` / `Avalonia.Desktop` / `Avalonia.Themes.Fluent` / `Avalonia.Fonts.Inter` / `Avalonia.Skia` — **12.0.x** (проверять `CascadeIDE.csproj`)
- `Dock.Avalonia`, `Dock.Model.Avalonia`, `Dock.Model.Mvvm`, `Dock.Avalonia.Themes.Fluent` — **12.0.x**
- `AIGuiders.AvaloniaEdit`, `AvaloniaEdit.TextMate` — **12.0.x** (fork, см. csproj)
- `Markdown.Avalonia` / прочие пакеты — версии в `CascadeIDE.csproj`
- `CommunityToolkit.Mvvm` — **8.x**
- TFM приложения: **net10.0**, `AvaloniaUseCompiledBindingsByDefault` — **true**

Исходники правды по макету приложения: `Views/MainWindow.axaml`, `Views/DocumentsDockView.axaml`, темы `Themes/*.json`, включение Dock Fluent в `App.axaml`.

## Completion state

Status: **Done v1** (фундамент + операционный playbook + индекс маршрутизации).

Artifacts:

- `status-avalonia-cascade-ide-ui-v1.md` (этот файл)
- `playbook-avalonia-dock-ui-v1.md`
- `kb-avalonia-ui-dock-fundamentals-v1.md`

См. также (литература, не имплементация): `../hci-ux-dx/kb-ide-dx-literature-evidence-v1.md` (DX/IDE, Osmani/Smalltalk/Boxer), `../hci-ux-dx/kb-ui-ux-literature-evidence-v1.md` (Norman/Nielsen/Shneiderman/Krug).

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

<!-- section:cross-link-software-transfer-matrix -->
## Cross-link: software transfer matrix

При **структурном** UI-рефакторинге (Skia `switch`, рост ViewModel, новый overview) — не только Avalonia playbook: **`../software-authoring/matrix-software-cross-domain-transfer-v1.md`**. При чисто биндинге/теме/Dock — остаёмся в `playbook-avalonia-dock-ui-v1.md`.
<!-- /section:cross-link-software-transfer-matrix -->

<!-- section:world-tag-v1 -->
**World tag (KE):** `software.authoring.dotnet.csharp.desktop-ui.avalonia`  
**Язык:** `software.authoring.dotnet.csharp` — idioms, `code-writing-principles-v1.md`.  
**Tooling:** `software.authoring.dotnet.tooling.roslyn` — диагностики/MCP, **отдельно** от языка.  
**Легаси:** `software.desktop-ui`.
<!-- /section:world-tag-v1 -->
