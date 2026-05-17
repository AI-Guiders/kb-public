# Карта глав: Steve McConnell — *Code Complete*, 2nd ed. (software construction)

## Provenance (происхождение)

- **Издание:** Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*, Second Edition, Microsoft Press, 2004. ISBN печати: 0-7356-1967-0; часто указывают 978-0735619678.
- **Локальная копия (пользователь):** `c:\Users\dkara\YandexDisk\Книги\Дискретная математика и программирование\makkonnel.djvu` — формат DJVU; **в среде агента содержимое не извлекается** (бинарный тип). Навигация по книге — в локальном ридере DJVU/PDF.
- **Публичная структура (для сверки нумерации глав):** оглавление 2-го изд. на платформе O’Reilly — `https://www.oreilly.com/library/view/code-complete-2nd/0735619670/` (раздел Table of Contents). Дополнительно: образец страниц Pearson — `https://ptgmedia.pearsoncmg.com/images/9780735619678/samplepages/9780735619678a.pdf` (фрагмент издательства, не полный текст).
- **created_at:** 2026-04-09
- **updated_at:** 2026-04-09

## Metadata

- **card_id:** kb-mcconnell-code-complete-2-chapter-map-v1
- **world:** software / engineering / construction
- **layer:** router + evidence anchor
- **tags:** mcconnell, code-complete, construction, chapter-index, evidence-based-reading
- **status:** active

## Epistemic Linkage

- **epistemic_basis:** fact (структура Parts I–VII и нумерация глав 1–35 по опубликованному оглавлению) + **inference** (сопоставление с практиками в `kb-engineering-evidence-v1.md`, ADR, ревью).
- **evidence_type:** published_table_of_contents + user-local_copy_pointer
- **confidence:** high (оглавление и части книги как артефакт издательства); medium (соответствие перевода/верстки конкретному DJVU без побайтовой сверки).
- **uncertainty:** русское издание («Совершенный код») может отличаться нумерацией страниц и разбивкой подзаголовков; **источник истины по тексту — твоя локальная книга**.
- **falsification_trigger:** расхождение оглавления с ревизией бумаги/DJVU.
- **transfer_boundary:** эта карточка **не цитирует формулировки и таблицы из книги**; для дословных цитат и цифр — только первоисточник у читателя. Полный текст из сети не подставляем (авторское право).

## Evidence-based pass (протокол для агента и человека)

1. **Claim** (утверждение о «хорошей практике» из McConnell) → обязательна **привязка к главе/разделу** (например, «гл. 7 — качество подпрограмм»), не «McConnell говорит, что…» без якоря.
2. **Операционализация:** из карты ниже выбрать главу → открыть в локальном файле → извлечь **свой** конспект или чеклист; при переносе в KB — **сжатая перефразировка + ссылка на главу**, не копипаста абзацев.
3. **Связь с репозиторием Cascade IDE:** пререквизиты и архитектура → ADR; соглашения по именам/модулям → согласовать с `docs/adr/README.md` и стилем кода; тестирование/отладка/рефакторинг — см. также `playbook-pr-review-v1.md`, `worlds/software-dotnet-tooling-roslyn/playbook-csharp-roslyn-mcp-diagnostics-v1.md`.

## Core Unit

- **context:** вопросы уровня «как строить код», качество подпрограмм, защитное программирование, читаемость, интеграция, инструменты.
- **signal:** нужна глава или тема из оглавления.
- **action:** открыть локальный DJVU по закладкам/поиску главы; сверить номер главы с таблицей ниже.
- **outcome:** быстрый переход от темы к первоисточнику без путаницы версий.
- **lesson:** книга — про **конструирование** (implementation quality), не замена ADR/DDD-книг; пересекается с Track C и качеством в `map-engineering-reading-v1.md`.

## Operationalization

- **first_adoption_task:** держать путь к DJVU стабильным или обновить `source_refs` в этой карточке при переносе файла.
- **validation_check:** сравнить заголовок главы 5–9 в ридере с таблицей ниже (англ. оригинал).
- **success_criterion:** любой практический совет из конспекта имеет номер главы в скобках.
- **rollback_or_mitigation:** при отказе от книги — опираться на `kb-engineering-evidence-v1.md` и официальные доки; карта остаётся как исторический якорь.

## Lifecycle

- **supersedes:** —
- **superseded_by:** —
- **deprecation_reason:** —

---

## Оглавление (2nd ed., англ. структура глав 1–35)

Ориентир: *Contents at a Glance* / полное оглавление второго издания (Microsoft Press). Названия — на английском как в оригинале; в переводе — по оглавлению твоего DJVU.

| Part | Главы | Тематический фокус |
|------|--------|-------------------|
| **I Laying the Foundation** | 1–4 | Конструирование, метафоры, пререквизиты (требования, архитектура), ключевые решения (язык, соглашения) |
| **II Creating High-Quality Code** | 5–9 | Дизайн в конструировании, классы, качество подпрограмм, защитное программирование, PPP |
| **III Variables** | 10–13 | Переменные, инициализация, числа, строки и типы |
| **IV Statements** | 14–19 | Прямолинейный код, условия, циклы, необычные управляющие конструкции, table-driven, общие вопросы управления |
| **V Code Improvements** | 20–26 | Ландшафт качества, совместная работа, тестирование разработчиком, отладка, рефакторинг, настройка производительности |
| **VI System Considerations** | 27–30 | Размер программы, управление конструированием, интеграция, инструменты |
| **VII Software Craftsmanship** | 31–35 | Вёрстка и стиль, самодокументируемый код, обработка ошибок, пределы конструирования, дальнейшее чтение |

### Список глав (для поиска по номеру)

1. Welcome to Software Construction  
2. Metaphors for a Richer Understanding of Software Development  
3. Measure Twice, Cut Once: Upstream Prerequisites  
4. Key Construction Decisions  
5. Design in Construction  
6. Working Classes  
7. High-Quality Routines  
8. Defensive Programming  
9. The Pseudocode Programming Process  
10. General Issues in Using Variables  
11. (Specific issues — initialization, etc.)  
12. (Numbers — integers, floating-point)  
13. (Characters, strings, unusual types)  
14. Organizing Straight-Line Code  
15. Using Conditionals  
16. Controlling Loops  
17. Unusual Control Structures  
18. Table-Driven Methods  
19. General Control Issues  
20. The Software-Quality Landscape  
21. Collaborative Construction  
22. Developer Testing  
23. Debugging  
24. Refactoring  
25. Code-Tuning Strategies  
26. Code-Tuning Techniques  
27. How Program Size Affects Construction  
28. Managing Construction  
29. Integration  
30. Programming Tools  
31. Layout and Style  
32. Self-Documenting Code  
33. Error-Handling Techniques  
34. The Limits of Construction  
35. Where to Find More Information  

*Примечание:* полные подзаголовки § 11–13 уточнять по оглавлению O’Reilly или по книге; для карты маршрутизации достаточно номеров глав.

## Указатель (связи KB)

- Общая инженерная эвиденция: `kb-engineering-evidence-v1.md`
- Карта литературы: `map-engineering-reading-v1.md` (добавить практику конструирования при разборе Track C / качества)
- Роутер: `index-knowledge-router-v1.md` (строка Engineering)
- Шаблон карточки: `templates/template-knowledge-card-v1.md`

## Ограничение

Полный текст «Совершенный код» / *Code Complete* в KB **не хранится** и не воспроизводится. Работа идёт по **оглавлению + локальному чтению + конспектам пользователя**.
## Инструмент извлечения текста (локальный workspace)

- В репозитории **PersonalCursorFolder** (корень воркспейса): `tools/djvu-text/Extract-DjvuText.ps1` — обёртка над **DjVuLibre `djvutxt`**; см. `tools/djvu-text/README.md`.
- Без установленного DjVuLibre скрипт укажет ссылку на установщик и переменную `DJVUTXT`.
- Ограничение: извлекается **скрытый текстовый слой**; сканы без слоя дадут пустой вывод (OCR — отдельно).