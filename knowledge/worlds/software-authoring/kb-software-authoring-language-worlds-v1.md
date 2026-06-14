# Software authoring: карта языковых миров v1

**Назначение:** разделить **языконезависимый** контур (OOA&D), **языки**, **tooling** (компилятор/семантика ≠ язык) и **UI/framework**-стеки.

**Версия:** v1.2 · 2026-05-17

---

## Слои (не смешивать)

| Слой | World tag | Что это | Когда |
|------|-----------|---------|--------|
| **1. Структура** | `software.authoring` | OOA&D, nouns/verbs, transfer matrix | god-class, switch, новая подсистема |
| **2. Язык** | `software.authoring.dotnet.csharp` | **Спецификация и idioms C#:** типы, async, nullable, record, стиль | «как написать на C#» |
| **2b. Tooling .NET** | `software.authoring.dotnet.tooling.roslyn` | **Платформа компилятора:** semantic model, analyzers, refactorings, `roslyn_*` MCP | CSxxxx, rename, code actions, symbols |
| **3. UI на C#** | `…csharp.desktop-ui.avalonia` | Avalonia, axaml, Dock | UI-фреймворк |
| **4. Web на PHP** | `…php.web.laravel` *(план)* | Laravel | ORM/routing |

**Ключевое:** Roslyn **не является** языком C#. Это API и сервисы поверх **скомпилируемого** C# (и VB в платформе Microsoft). Язык можно знать без Roslyn; Roslyn без понимания C# бесполезен.

---

## Дерево .NET (v1.2)

```
software.authoring
└── dotnet
    ├── csharp                         # язык
    │   └── desktop-ui
    │       ├── avalonia
    │       ├── wpf
    │       ├── winforms
    │       ├── maui
    │       └── silverlight            # historical
    ├── fsharp                         # язык (TBD kb)
    └── tooling
        ├── roslyn                     # компиляторная платформа, MCP
        └── build                      # dotnet build/test MCP (эвристика)
```

---

## Таблица: язык vs tooling vs UI

| World tag | Не путать с | KB (папка) |
|-----------|-------------|------------|
| `…dotnet.csharp` | Roslyn, Avalonia | `../software-dotnet-csharp/` (`kb-dotnet-fundamentals-v1.md`, `code-writing-principles-v1.md` в `software-authoring/`) |
| `…dotnet.tooling.roslyn` | язык, UI | `../software-dotnet-tooling-roslyn/` |
| `…csharp.desktop-ui.avalonia` | Roslyn, язык целиком | `../software-dotnet-avalonia/` |

**Легаси:** `software.desktop-ui` → `…desktop-ui.avalonia`.

---

## Резолв (агент)

1. **Файл `.cs`** → сначала `…dotnet.csharp` (если вопрос про синтаксис/idiom).
2. **Диагностика / refactor / symbol / MCP roslyn** → `…dotnet.tooling.roslyn` (параллельно или вместо углубления в language kb).
3. **`Avalonia` в csproj** → `…desktop-ui.avalonia` **после** csharp.
4. **OOA&D / god-class** → `software.authoring` + matrix **до** всех dotnet-слоёв.

Типичная цепочка Cascade IDE: **authoring → csharp → (roslyn при правках .cs) → avalonia (если UI) → HCI (если UX)**.

---

## Другие языки (корень)

| World tag | Папка |
|-----------|--------|
| `software.authoring.php` | `software-php-laravel/` |
| `software.authoring.javascript` | `software-javascript/` |

Аналог tooling для PHP/JS — **отдельные** миры (phpstan, eslint), не под `dotnet.tooling.roslyn`.

---

## Related

- `matrix-software-cross-domain-transfer-v1.md`
- Hub .NET (редирект): `worlds/software-dotnet-desktop/README.md` → `software-dotnet-csharp/`, `software-dotnet-tooling-roslyn/`, `software-dotnet-avalonia/`

<!-- section:objectpascal-and-legacy-stacks-v1 -->
## Object Pascal и прочие «вспомнилось» (зарезервировано)

**Язык (не .NET):** `software.authoring.objectpascal`  
Наследники Turbo Pascal → Delphi / Free Pascal (Lazarus).

| World tag (план) | Стек | Сигнал | KB |
|------------------|------|--------|-----|
| `…objectpascal.desktop-ui.vcl` | Delphi VCL | `.dfm`, `TForm`, Win32 | TBD |
| `…objectpascal.desktop-ui.fmx` | Delphi FMX | cross-platform FireMonkey | TBD |
| `…objectpascal.desktop-ui.lcl` | Lazarus LCL | `.lfm`, Free Pascal | TBD |

**Не переносить слепо из C#:** properties vs `property` с другой семантикой; `with` в Pascal ≠ C# `with`; RTTI/DFM — не Avalonia axaml.

**Связь с .NET:** только через interop/OOA&D на уровне `software.authoring` (nouns/verbs, слои) — не через `dotnet.csharp`.

**Silverlight** остаётся под `…csharp.desktop-ui.silverlight` (C#-экосистема Microsoft); Object Pascal — **отдельный корень** дерева.
<!-- /section:objectpascal-and-legacy-stacks-v1 -->

