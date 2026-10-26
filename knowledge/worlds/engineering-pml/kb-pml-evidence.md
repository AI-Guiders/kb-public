---
type: Evidence Card
title: 'KB evidence: AVEVA PML v1'
description: '**Назначение:** первоисточники и учебные материалы для `kb-pml-fundamentals.md`.'
tags: [engineering-pml, kb, worlds]
world: engineering
subworld: pml
---
# KB evidence: AVEVA PML v1


**Назначение:** первоисточники и учебные материалы для `kb-pml-fundamentals.md`.

**Проверено:** 2026-06-16

---

## Official (AVEVA docs.aveva.com)

| Тема | URL |
|------|-----|
| Programmable Macro Language (обзор PML1/PML2) | https://docs.aveva.com/bundle/e3d-design/page/962699.html |
| Software Customization Reference (PML2 GUI, PML1 expressions) | https://docs.aveva.com/bundle/e3d-design-ue/page/962719.html |
| PML 1 and PML 2 Expressions | https://docs.aveva.com/bundle/e3d-design/page/1026760.html |
| User-defined object types | https://docs.aveva.com/bundle/engineering/page/1026663.html |
| Method overloading (ANY) | https://docs.aveva.com/bundle/engineering/page/1026702.html |
| PML Directives (reload, kill, index) | https://docs.aveva.com/bundle/e3d-design-ue/page/1026916.html |
| How Forms are Loaded and Displayed | https://docs.aveva.com/bundle/e3d-design-ue/page/1026915.html |
| Loading and Showing Forms | https://docs.aveva.com/bundle/engineering/page/1027016.html |
| PML Trace | https://docs.aveva.com/bundle/e3d-design-ue/page/1001368.html |
| PML Tracing (UI) | https://docs.aveva.com/bundle/e3d-design-ue/page/983747.html |

---

## Training / secondary (проверять актуальность под версию продукта)

| Источник | URL | Что взято |
|----------|-----|-----------|
| PDMS PML Manual (vol.1) | https://www.scribd.com/doc/309935059/PDMS-PML-Manual-1 | §12.1 PML1 vs PML2; **lacks inheritance**; VAR=STRING; `pml index` |
| AVEVA PML Basics (PDF) | https://www.scribd.com/document/403919723/PML-Basics-pdf | PML2 variables; polymorphism; no inheritance |
| VPD PML & PML2 slides | https://pdfcoffee.com/download/vdp-programmable-macro-language-pdf-free.html | user objects, constructors, form methods |
| PML Course (Iranpiping) | https://pdfcoffee.com/pml-course-iranpiping-pdf-free.html | mixing PML1/PML2 expressions; DO/IF |

---

## Tooling (Notepad++ LSP client)

| Источник | URL |
|----------|-----|
| NppLspClient | https://github.com/Ekopalypse/NppLspClient |
| N++ community thread | https://community.notepad-plus-plus.org/topic/25398/new-incomplete-lsp-client-plugin |

---

## Ключевые цитаты (для споров)

**PML2 не заменил PML1** — Software Customization Reference, введение.

**Два стиля выражений** — «PML 2 expressions are used in if and do… PML 1 expressions must be used in all other situations, in particular when using an expression as an argument to a command» — PML 1 and PML 2 Expressions.

**Нет наследования** — PDMS PML Manual §12.1 / PML Basics: «almost an object-oriented language… main deficiency is that it lacks inheritance».

**Directives не в callbacks** — PML Directives note.

