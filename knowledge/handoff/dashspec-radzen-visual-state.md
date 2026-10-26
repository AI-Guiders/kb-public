---
type: Note
title: 'DashSpec: ветка feature/radzen-visual — состояние и карта знаний'
description: '**Status:** живой стейт-файл · 2026-10-25 · репо `D:\Experiments\Personal Cursor Folder\open\dash-spec`'
---
# DashSpec: ветка feature/radzen-visual — состояние и карта знаний

**Status:** живой стейт-файл · 2026-10-25 · репо `D:\Experiments\Personal Cursor Folder\open\dash-spec`
**Ветка:** `feature/radzen-visual`, голова `48cb9f3` (не запушена). Прод-контент (D:/SSCADRepo/URSA.LicenseUsage) в открытый репо не попадает.

## Сделано (коммиты по порядку)

- `40fbdc1` host-блок в host-модуле (ADR-0112 §6): `host … end host`, однотокенные ключи (`render`, `color_scheme`, `language`, `provider_default`), bootstrap fold поверх легаси configuration/presentation.
- `d57cd1f` фикс таблиц: **RadzenDataGrid v12.1.5 колонки только через `<Columns>`-шаблон** (дефолтный ChildContent не рендерится вовсе — «No records to display» при непустом payload).
- `1b085e2` квадратный heatmap (HTML/CSS-грид, `aspect-ratio:1`, колонки 2.6rem; клик → `HeatmapCellContext` ADR-0107) + маршрутизация `KindPlugins["heatmap"]=radzen`.
- `f6882c4` типизированный вход на рендер: `TablePayload{Fields[Name,Header,DashPrimitiveKind,…], Rows: DashValue[][]}`; display-строки делает present-слой (`LabelFormat.FormatObject`); дефолты отчёта едут явно на `CardRenderResult.FormatDefaults`. ADR-0079 дополнен.
- `50d0b10` тема navy+cyan: `theme-dark.css` переопределяет только шкалы `--rz-*` на `:root`, компонентные переменные каскадируют; монтируется ПОСЛЕ stock dark.css; `light` стоковый.
- `8554726` хром: левое меню `DashboardSidebar` (RadzenPanelMenu: «Отчёты» — каталог, «Разделы» — вкладки) вместо TabBar+комбобокса; drill-клики строк таблиц (source «row», первая колонка → YLabel).
- `c061e6c` тулбар-панель `dash-toolbar-radzen` + media: ≤1100px сайдбар наверх, ≤800px меню в 1 колонку.
- `29e81b8` доска: `.dash-home-column { flex:1 }` (flex-item по умолчанию сжимался до контента) + reflow строк на mid.
- `dbb2de0` **P4 ADR-0111 §7 — адаптивность вариантами плоскости** (см. ниже).
- `8fc660c` сайдбар: метки через локализатор (ADR-0077, ключи Reports/Sections/Navigation).
- `48cb9f3` ADR-0113 (PBT) принят в репо.

## P4 (ADR-0111 §7) — как устроена адаптивность

Пайплайн: спека → компакторы → **SlotPlane** (собирается раз на ревизию, `SlotPlaneBuilder`) → рендер читает и размещает.

- Модель: `Slot.Placement: PlacementVariants {Wide; Mid; Narrow}` (F# `SlotPlane.fs`) + `ViewportClass` (Wide=0|Mid=1|Narrow=2) — на будущее.
- Деривация: `PlacementVariantsPlanning.For(placement, wideColumns)` — wide = как объявлено; mid = `MidColumns = wide/2`, спан масштабируется пропорционально (`ScaleSpan`, клампы), row/col = 0 (авто-флоу dense); narrow = span 1, авто. `ForFixedMid` — для хром-ряда (max-content apply-колонка ADR-0061 не переносится): mid = wide.
- Проекция: `PlacementGridCss` емитит **только custom properties** — слоты `--gc/--gr`, `--gc-mid/--gr-mid`, `--gc-narrow/--gr-narrow`; контейнеры `--tracks/--tracks-mid/--tracks-narrow` (интерьеры `--card-tracks*`). Финальные `grid-column/grid-row` разрешают **стили стеков** медиа-запросами (wide >1200 > mid >768 > narrow; 480-блок снесён — narrow поглощает). CSS в `cards.css`/`filters.css` SelfMade (грузятся в обоих стеках), `chrome.css` Radzen — только хром сайдбара/тулбара.
- `[style*="span N"]`-хак снесён. `PlacementSlot` больше не принимает `GridColumns`.
- Тесты: `PlacementVariantsPlanningTests` — 4 свойства FsCheck + регрессионные примеры; **FsCheck 3.6.0, CPM (`Directory.Packages.props`)** — `FsCheck.FSharp` как отдельного пакета НЕ существует (F#-API внутри основного FsCheck). Из C# `==` на F#-записях — ссылочное равенство, сравнивать `.Equals`.

## Radzen v12 gotchas (накопленное)

Колонки DataGrid только через `<Columns>`; `DataGridRowMouseEventArgs<TItem>` для RowClick; `RadzenPanelMenuItem` — Click/Selected/Expanded/Icon; `DisplayResolutionHost` — static; Chart/Gantt ChildContent живут. Клики по rz-меню из браузера: надёжнее `evaluate` + `element.click()`; координаты меню плывут при сворачивании групп.

## Хост/среда

- Прогон на проде: `src/DashSpec.Host/dash-spec.local.host.ds` (gitignored) — `render = radzen|selfmade` (флип + рестарт), каталог `D:/SSCADRepo/URSA.LicenseUsage/docs/dashspec/catalogs/sscad-prod.ds`.
- Хост стартовать с **CWD = `src/DashSpec.Host`** (иначе relative `../../samples/demo/demo.ds` не решается): `./bin/Debug/net10.0/DashSpec.Host.exe --urls http://localhost:5295`.
- Перед rebuild убивать `DashSpec.Host.exe` (держит DLL); полный `dotnet build` не идёт, пока хост жив — собирать по проектам или `--no-build` для тестов, читающих исходники (архитектурные).
- Архитектурные тесты (ADR-0077 гейт) не пробегают молча, если хост держит лок — инлайн-кириллица в razore запрещена; вчера это проскочило в `8554726`, починено в `8fc660c`.
- Известный не-мой баг хоста: `CatalogUsageService.RecordSelection` — UNIQUE constraint при повторном выборе той же записи за день (upsert не работает: `HitCount++` не сохраняется?); ловится как non-fatal warning.

## Осталось (приоритет оператора)

0) Карточный тулбар с viz-state тогглами (ShowLegend/ShowDigits не существуют; `VizStateCardId` — заготовка ключа): viz-state store → Radzen-тогглы в карточном хроме → потребители (Chart legend, heatmap labels, таблицы) → собрать весь карточный тулбар в одну строку.
1) Плагин `Filter.Radzen` (RadzenDatePicker/DropDown; фильтр-виджеты — вертикальные плагины ADR-0060, Filter.Builtins не трогать).
2) KPI-ветка `number` в RadzenCardViz (её нет — KPI показывает «Нет данных»; прод использует 11 KPI).
3) Полировка графиков из ChartPresentation; финальные скриншоты vs референс. Даты в XLSX текстом — follow-up (numFmt).
4) `ViewportClass` пока не читается рендером (варианты выбирает чистый CSS) — перспектива: per-class погрешности/пограничные классы, если чистого CSS не хватит.

[[dsh]] · практики оператора: сначала изучай потом действуй, стоп-машины, «скрестить не портировать», прод-контент не в открытый репо, тест на прод-конфиге, «не надо хаков — разберись как всё работает».
## Per-stack монтирование (2026-10-25, `24869ac`)

ADR-0112 §4/§5 доведены: App.razor монтирует head/scripts стека **только в его режиме** (`@if (IsRadzenStack) … else <SelfMade…/>`). Radzen-стек несёт свой полный набор поверхности: `wwwroot/css/parts/` (копия проекции плоскости) + `chrome.css` с `@import` parts; **`tokens.css` Radzen читает плоские токены из `--rz-*`** (`--surface: var(--rz-base-800)` и т.д.) — тема красит, словарь общий, плоские имена нужны гостям-плагинам (их css использует --surface/--border/--text/--muted/--surface-2/--accent).

Flatpickr + `dashspec-datepicker.js` переехали к владельцу — **Filter.Builtins** (`lib/flatpickr`, `js/`, `FilterBuiltinsHead` css + новый `FilterBuiltinsScripts` после Routes): виджеты дат — плагинные в обоих стеках. Из SelfMade либа удалена. Chartjs остался SelfMade-only (radzen Chart/Table/Scalar/Gantt → Radzen; Matrix → canvas-гость).

Проверено в обоих режимах (radzen: selfmade-ассетов 0, flatpickr-календарь открывается, body = `--rz-base-background-color`; selfmade: свой css+chartjs, radzen-хрома нет). Порядок каскада: в radzen parts теперь ПОСЛЕ theme-dark (раньше app.css был до) — на вид ничего не изменилось, но при конфликте правил выигрывает part, помнить при отладке.

Флип режима: `src/DashSpec.Host/dash-spec.local.host.ds` → `render = radzen|selfmade` + рестарт хоста (файл вернул на `radzen`).
