---
type: KB
title: 'KB fundamentals: AVEVA PML runtime (E3D / PDMS) v1'
description: '**Назначение:** поведение PML **в запущенном продукте** — directives, отладка, жизненный цикл форм, пересборка индекса.'
tags: [engineering-pml, kb, worlds]
language: ru
world: engineering
subworld: pml
---

﻿# KB fundamentals: AVEVA PML runtime (E3D / PDMS) v1

**Назначение:** поведение PML **в запущенном продукте** — directives, отладка, жизненный цикл форм, пересборка индекса.

**Мир:** `engineering.pml`  
**Связь:** `kb-pml-fundamentals.md` (язык) → **этот файл** (среда) → `kb-pml-evidence.md`

---

## Scope

- Командная строка PML и directives
- Trace / отладка
- Загрузка, show/hide/kill форм
- `pml index` / `pml rehash`
- **Не** синтаксис выражений и не модель объектов (см. fundamentals)

---

## 1) PML Directives

Выполняются **только из командной строки PML** (окно ввода PDMS/E3D), **не** из callback gadget на форме.

| Задача | Директива |
|--------|-----------|
| Перезагрузить форму после правки `.pmlfrm` | `pml reload form !!formname` |
| Форма «залипла» | `kill !!formname` затем `pml reload form !!formname` |
| Перезагрузить функцию | `pml reload function !!funcname` |
| Новый/изменённый файл в pmllib | `pml rehash` / `pml index` |
| Показать форму при разработке | `show !!formname` или `show !!formname free` |

Источник: [PML Directives](https://docs.aveva.com/bundle/e3d-design-ue/page/1026916.html)

---

## 2) Формы: загрузка и память

| Действие | Поведение |
|----------|-----------|
| Первый `show !!form` | Загружает `.pmlfrm` автоматически |
| `loadform !!form` | Подгрузить до show (в т.ч. из callback) |
| `!!form.show()` / `!!form.show('free')` | **Не** подгружает файл, если форма ещё не known |
| `hide !!form` | Снять с экрана; определение может остаться в памяти |
| `kill !!form` | Забыть определение формы |

Источники: [How Forms are Loaded](https://docs.aveva.com/bundle/e3d-design-ue/page/1026915.html), [Loading and Showing Forms](https://docs.aveva.com/bundle/engineering/page/1027016.html)

Legacy: `$M path` из macro — не для нового кода.

---

## 3) Индекс pmllib

- **`pml.index`** — реестр файлов; пересборка при старте продукта и по `pml index` / `pml rehash`
- Глобальные `!!` из `pmllib` подхватываются при rebuild index
- После добавления файла в дерево без rehash символ может быть **неизвестен** среде

---

## 4) Отладка

| Приём | Назначение |
|-------|------------|
| `q var !x` / `q var !!x` | Значение переменной в консоли |
| `trace on` / `trace off` | Пошаговое выполнение |
| `$p текст` | Вывод в окно PML |
| PML Trace UI | Basic / Advanced / Expert ([PML Trace](https://docs.aveva.com/bundle/e3d-design-ue/page/1001368.html)) |
| `handle ANY` … `endhandle` | Перехват ошибок вокруг блока |

---

## Anti-patterns

- Вставлять `pml reload` / `pml index` в callback gadget
- Ожидать, что `!!form.show()` подгрузит `.pmlfrm` с диска
- Править encrypted published PML в `pmllib`
- Забыть `pml reload` после изменения уже открытой формы

---

## Evidence and updates

- См. `kb-pml-evidence.md` (Directives, Forms, Trace)
- **Проверено:** 2026-06-16

**Status:** active

