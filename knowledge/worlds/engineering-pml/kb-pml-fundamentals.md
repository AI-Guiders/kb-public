---
type: KB
title: 'KB fundamentals: AVEVA PML (PML1 & PML2) v1'
description: '**Назначение:** самодостаточный опорный слой — агент не обязан каждый раз открывать полный AVEVA Software Customization Reference.'
tags: [engineering-pml, kb, worlds]
world: engineering
subworld: pml
---
# KB fundamentals: AVEVA PML (PML1 & PML2) v1


**Назначение:** самодостаточный опорный слой — агент не обязан каждый раз открывать полный AVEVA Software Customization Reference.

**Мир:** `engineering.pml`  
**Связь:** `status-engineering-pml.md` → `playbook-pml.md` → **этот файл** → `kb-pml-runtime-fundamentals.md` → `kb-pml-evidence.md`

---

## Scope

- Programmable Macro Language (PML) в AVEVA E3D / PDMS / Engineering
- Две ко-существующие линии: **PML1** и **PML2**
- Файлы `pmllib`, пользовательские объекты, формы, функции
- **Не** полный перечень системных объектов AVEVA

---

## 1) Три механизма кастомизации (контур)

| Механизм | Роль |
|----------|------|
| **PML1** | Команды PDMS/E3D, макросы, **PML1 expressions** (rules, reports, аргументы команд) |
| **PML2** | Объекты, типизированные переменные, **формы и меню** (GUI AppWare) |
| **PML addins** | Подключение .NET (отдельный контур; см. `engineering.cad`) |

Официально: PML2 **не заменил** PML1; оба используются вместе ([Software Customization Reference](https://docs.aveva.com/bundle/e3d-design-ue/page/962719.html)).

---

## 2) PML1 — fundamentals

### Стиль

- Командный синтаксис PDMS (граф команд), макросы с `IF` / `DO` / `BREAK` / `SKIP`
- Пример выражения PML1: `VAR !length ( 2 + 3 )` — результат в контексте **STRING**
- Команда `VAR` **всегда** создаёт строковую семантику; числа и булевы через `VAR` остаются текстом до явного приведения

### Где PML1 обязателен

- **Аргументы PDMS-команд**, когда выражение передаётся в команду (нужен `$` для подстановки переменной в строку команды)
- **PML1 expressions package** — rules, report templates, Standard Attribute Query ([тот же Reference](https://docs.aveva.com/bundle/e3d-design-ue/page/962719.html))
- Смешение: в одном макросе могут быть и PML1 `VAR`, и PML2 `!z = !x + !y` — ошибки «incompatible types (REAL=STRING)» типичны при смешении

### Иерархия БД (не путать с ООП)

- В учебных материалах PDMS встречается «PML 1 hierarchy» — это **иерархия элементов модели** (SITE/ZONE/…), не наследование классов PML

---

## 3) PML2 — fundamentals

### Назначение

- Написан **для GUI**: формы (`.pmlfrm`), меню, callback-методы, gadget-атрибуты через **methods**, не старые команды ([Forms loading](https://docs.aveva.com/bundle/e3d-design-ue/page/1026915.html))
- Большинство старых PML1-макросов **продолжают работать** в среде PML2

### Переменные как объекты

| Префикс | Область | Жизненный цикл |
|---------|---------|----------------|
| `!!name` | Глобальная | Сессия; глобалы из `pmllib` подхватываются при rebuild index (старт продукта) |
| `!name` | Локальная | Тело функции / метода / макроса |

- Имена: буква + буквы/цифры, до 64 Unicode-символов (+ префикс `!`/`!!`)
- **Точка в имени переменной запрещена** — `.` разделяет объект и метод (`!item.Type`, `!!form.gadget`)
- Создание с типом: `!x = 42` → REAL; `!!flag = TRUE` → BOOLEAN; `!s = |text|` → STRING

### Типы объектов (уровни)

1. **Built-in** — STRING, REAL, BOOLEAN, ARRAY, …
2. **System-defined** — POSITION, DBREF, FORM, FILE, …
3. **User-defined** — `define object MYTYPE` в `.pmlobj`

### Пользовательский объект (канонический шаблон)

```pml
define object FACTORY
  member .Name is STRING
  member .Workers is REAL
endobject

define method .FullDesc() is STRING
  return !this.Name & ' ' & string(!this.Workers)
endmethod

!plant = object FACTORY()
!plant.Name = |Main|
```

- Экземпляр: `object TYPENAME()`
- Методы: `define method .Name(…)` — **перегрузка** по сигнатуре; аргумент `ANY` слабее конкретного типа ([Overloading with ANY](https://docs.aveva.com/bundle/engineering/page/1026702.html))
- **Конструктор по умолчанию** — метод с тем же именем, что тип объекта, без аргументов: `define method .Life()`

### Наследование — **нет**

PML2 описывается как «почти ООП» с явным ограничением:

> **Main deficiency is that it lacks inheritance.**

Источники: PDMS PML Manual (раздел 12.1 Difference between PML1 and PML2); AVEVA PML Basics training PDF (Scribd mirror). В `pmllib` только `define object NAME` **без** базового типа.

**Следствия для статического анализа типов:**

- Нет цепочки `super`, нет override по иерархии классов
- Тип user object = **один** `.pmlobj`; «семейства» имён — отдельные типы, не подклассы

### Что есть вместо наследования

| Паттерн | Пример |
|---------|--------|
| Композиция | `member .Site is FACTORY` |
| Копирование | `copyFrom(COMPROP)` |
| Полиморфизм операторов/методов | Поведение зависит от типа переменной |
| Перегрузка функций/методов | Несколько `define method .SetValue(...)` |
| Публичность | Всё public; private members **нет** |
| Scope | Только global (`!!`) и local (`!`) |

### Функции и процедуры

```pml
define function !!Area(!Length is REAL, !Width is REAL) is REAL
  !Area = !Length * !Width
  return !Area
endfunction
```

- Глобальные функции: `!!Name` в `.pmlfnc`
- Аргументы передаются **by reference** (read/write) — могут использоваться как output
- Процедуры — без `is TYPE` в заголовке

### Выражения PML1 vs PML2

| Контекст | Стиль |
|----------|--------|
| `if` / `do` / присваивание `=` | **PML2 expressions** |
| Аргумент PDMS-команды, rule/report | **PML1 expressions** (часто `$!var`) |

Официально: [PML 1 and PML 2 Expressions](https://docs.aveva.com/bundle/e3d-design/page/1026760.html)

### Специальные значения

- `UNSET` — переменная существует, значения нет
- `UNDEFINED` — переменной нет; `Defined(!!x)` / `Undefined(!!x)`
- Удаление: `!!x.Delete()` — **не** для members форм/объектов

---

## 4) Файлы pmllib

| Расширение | Содержимое |
|------------|------------|
| `.pmlfnc` | `define function !!…` |
| `.pmlobj` | `define object` + `define method` |
| `.pmlfrm` | `layout form !!…`, gadgets, callbacks |
| `.pmlcmd` | `setup command` |
| `.pmlmac` | Макросы |
| `.pmltsk` | Tasks (ABA и др.) |

- Реестр: **`pml.index`** (дерево папок + файлы)
- Заголовок AVEVA (`-- File:`, `-- Type:`, `-- Group:`, `-- Description:`) — основной источник human-readable meta при статическом анализе
- Published encrypted PML — «Unable to decrypt file»; исходник недоступен

Формы, directives и trace — `kb-pml-runtime-fundamentals.md`.

---

## Anti-patterns

- Говорить «у PML есть наследование объектов»
- Использовать `VAR` для арифметики PML2 без приведения типов
- Класть `pml reload` в callback формы (directives — **командная строка**)
- Ожидать private-поля или namespace
- Путать **DB hierarchy** (PIPE/EQUI) с типами PML

---

## Evidence and updates

- См. `kb-pml-evidence.md`
- **Проверено:** 2026-06-16 (AVEVA docs.aveva.com + PDMS PML Manual PDF corpus)
- Provenance: `META/provenance-contract.md`

**Status:** active

