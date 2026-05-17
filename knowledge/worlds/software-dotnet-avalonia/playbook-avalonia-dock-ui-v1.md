# Avalonia + Dock UI — operational playbook v1

## Purpose

Операционный контракт для агента и разработчика: от **дизайн-задачи** до **проверенной** правки в Avalonia/Dock (как в CascadeIDE). Фундаментальные понятия — `kb-avalonia-ui-dock-fundamentals-v1.md`. Версии и статус домена — `status-avalonia-cascade-ide-ui-v1.md`.

## Scope

- AXAML, стили, ресурсы, биндинги (compiled)
- Dock.Model + Dock.Avalonia (`DockControl`, фабрика, документы)
- Локальная компоновка (`Grid`, `DockPanel`, `Flyout`, scroll)
- Смежные пакеты: AvaloniaEdit, Markdown.Avalonia (smoke-уровень)
- Согласование с HCI: `../hci-ux-dx/playbook-hci-core-v1`, `../hci-ux-dx/ui-ux-playbook`

## Retrieval order (обязательный)

1. `status-avalonia-cascade-ide-ui-v1.md` — актуальные версии и guardrails.
2. Этот playbook — шаги и чек-листы.
3. `kb-avalonia-ui-dock-fundamentals-v1.md` — углубление по спорному месту.
4. При «застрял на API» — `playbook-learn-basics-when-stuck-v1` + официальная дока / Context7, затем фиксация вывода в KB при повторяемости.

## Evidence-based working format

- **Fact:** что видит пользователь / что в логе / точный текст ошибки XAML или биндинга.
- **Hypothesis:** минимальное объяснение (layout, DataContext, ресурс, модель Dock).
- **Check:** smallest change + `dotnet build` + ручная проверка сценария.
- **Decision criterion:** зелёная сборка + отсутствие ошибок биндинга в типичном потоке.
- **Confidence mark:** отдельно уверенность в API версии (сверка с csproj).

## Contract A — новый UI-блок по макету

1. **Зафиксировать режим:** какой `DataContext` / под-VM; видимость (`IsVisible`, режимы приложения).
2. **Иерархия по HCI:** один главный фокус; вторичное — progressive disclosure (flyout, сворачивание).
3. **Выбрать контейнер:** `Grid` vs `StackPanel` vs `UniformGrid`; где нужен `ScrollViewer` и `MaxHeight`.
4. **Ресурсы:** новые цвета → ключ темы (`DynamicResource`); не хардкодить без причины.
5. **Стили:** один «блок-секция» классом; избегать конфликтующих `Classes`.
6. **Сборка + прогон сценария** (открыть экран, сменить тему если релевантно).

## Contract B — правка Dock (документы / панели)

1. Найти: `DockControl`, `IFactory`, `IDock` / `IDockable`, где собирается `RootDock` и список документов.
2. Проверить: обновляется ли коллекция `VisibleDockables` / активный документ при смене состояния VM.
3. Не путать с локальным `DockPanel` внутри чата/панели — это не модель Dock.
4. После изменений: открытие/закрытие документа, переключение вкладки, нет ли «пустого» layout.

## Contract C — биндинги и compiled bindings

1. Убедиться в `x:DataType` на корне шаблона / контрола где требуется.
2. Ошибка «cannot find property» → несовпадение типа `DataContext` или опечатка в пути.
3. Для вложенных контекстов: явный `DataContext=` на границе; не полагаться на неявное наследование через шаблоны без проверки.

## Contract D — темы и Power/режимы

1. Режимы UI (Focus/Balanced/Power и т.д.) — свойства VM; XAML только отражает.
2. Специальные палитры (например power-theme) — не дублировать логику в двух JSON без необходимости; документировать ключи в репо (`docs/ux` при наличии).

## Contract E — обновление зависимостей

1. Сверить версии: Avalonia, Dock.*, AvaloniaEdit — матрица совместимости в release notes.
2. Smoke: старт приложения, док, редактор, чат-панель, смена темы.
3. Обновить `status-avalonia-cascade-ide-ui-v1.md` и при необходимости секцию версий в fundamentals.

## Contract F — TextMate / подсветка / новый язык в редакторе

1. Найти в коде точку **регистрации TextMate** и список путей к **grammar bundle** (не гадать пути из KB).
2. Проверить **наличие файлов** bundle после сборки (выходной каталог / ресурсы) и соответствие **расширения файла** ожидаемым правилам.
3. При сбое после обновления пакетов — сначала **совместимость AvaloniaEdit + AvaloniaEdit.TextMate**, затем правки `.tmLanguage` / scope.
4. Зафиксировать smoke: открытие эталонного файла языка + переключение темы приложения + отсутствие повторяющихся ошибок в логе редактора.
5. Повторяемый инцидент — карточка по `templates/template-knowledge-card-v1.md` с путём к коду инициализации и именем grammar.

## Integration with other playbooks

- **C# диагностика / рефакторинг:** `../software-dotnet-tooling-roslyn/dotnet-roslyn-debug-playbook.md`
- **Сборка/тест/отладка общая:** `../../tooling-debug-playbook.md`
- **DX-поток и среда (не только UI):** `../hci-ux-dx/de-dx-playbook.md`
- **Общий .NET frontend:** `frontend-dotnet-playbook.md`
- **HCI / продуктовый UX:** `../hci-ux-dx/playbook-hci-core-v1.md`, `../hci-ux-dx/ui-ux-playbook.md`, `../hci-ux-dx/kb-hci-usability-and-dialog-rules-v1.md`

## Metrics

- Время от постановки UI-задачи до зелёной сборки.
- Число итераций «угадывания» XAML до первого успешного build.
- Повторяемость регрессий на одном и том же экране.

## Revisit triggers

- Повторяющиеся ошибки одного класса (flyout, dock active document, theme key missing).
- Крупный редизайн главного окна или замена dock-пакета.

Версия: v1. 2026-03-20.