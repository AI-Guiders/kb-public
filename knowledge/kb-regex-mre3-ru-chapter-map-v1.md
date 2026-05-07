# Карта глав: Jeffrey Friedl — «Регулярные выражения», 3-е изд. (рус. перевод O'Reilly)

## Provenance (происхождение)

- source_refs: локальный PDF `c:\Users\dkara\Downloads\OReilly-Регулярные-выражения-3-е-изд.-Дж.Фридл.pdf` (закладки/оглавление извлечены программно, 598 стр.); оригинал: *Mastering Regular Expressions*, 3rd ed.
- created_at: 2026-03-21
- updated_at: 2026-03-21
- author: (агент; сверка структуры по PDF)

## Metadata

- card_id: kb-regex-mre3-ru-chapter-map-v1
- world: programming / regex
- layer: router
- tags: regex, friedl, mre3, ru-translation, chapter-index
- status: active

## Epistemic Linkage

- epistemic_basis: fact (структура оглавления PDF) + inference (сопоставление с карточками KB)
- evidence_type: machine-extracted bookmarks
- confidence: high (оглавление), medium (сопоставление с KB)
- uncertainty: названия подпунктов в закладках иногда обрезаны; нумерация страниц в PDF может отличаться от бумажного издания
- falsification_trigger: расхождение оглавления с ревизией файла PDF
- transfer_boundary: карточки KB не цитируют текст книги; для формулировок и доказательств — только первоисточник

## Core Unit

- context: чтение/поиск по книге и параллельная работа с кластером `regex-friedl-mre3`
- signal: нужна глава или тема из оглавления
- action: открыть соответствующие файлы KB по таблице ниже; при расхождении — книга первична
- outcome: быстрый переход от главы к сжатой памяти агента
- lesson: гл. 4–6 книги = теория движка и эффективность; гл. 7–10 = конкретные API языков

## Operationalization

- first_adoption_task: держать PDF в стабильном пути или обновить `source_refs` при переносе файла
- validation_check: открыть закладку «Глава N» в ридере и сравнить с таблицей
- success_criterion: любая глава 1–10 имеет хотя бы одну карточку KB
- rollback_or_mitigation: при удалении кластера — карта теряет смысл; хранить в каноне вместе с `kb-regex-*`

## Lifecycle

- supersedes: —
- superseded_by: —
- deprecation_reason: —

---

## Соответствие глав → карточки KB (кластер `regex-friedl-mre3`)

| Глава (рус. изд.) | О чём (кратко) | Карточки KB |
|-------------------|----------------|-------------|
| **1.** Знакомство с регулярными выражениями | egrep, метасимволы, классы, якоря, квантификаторы, скобки, обратные ссылки | `kb-regex-quickref-v1.md`, `kb-regex-syntax-features-v1.md` |
| **2.** Дополнительные примеры | разбор задач, закрепление синтаксиса | `kb-regex-syntax-features-v1.md`, `kb-regex-flavors-practice-v1.md` (раздел workflow) |
| **3.** Возможности и диалекты | отличия инструментов, Unicode-свойства, POSIX | `kb-regex-flavors-practice-v1.md`, `kb-regex-unicode-boundaries-v1.md` |
| **4.** Механика обработки | НКА, откат, жадность, атомарность, владение, сравнение с ДКА | `kb-regex-engines-efficiency-v1.md` |
| **5.** Практические приёмы построения | баланс скобок, IP, HTML/URL, CSV и т.д. | `kb-regex-syntax-features-v1.md` + для вложенных грамматик — не только regex; детали — в книге |
| **6.** Эффективные выражения | катастрофический backtracking, оптимизации | `kb-regex-engines-efficiency-v1.md`, `kb-regex-flavors-practice-v1.md` (таймауты, API) |
| **7.** Perl | специфика Perl/PCRE-наследия | `kb-regex-flavors-practice-v1.md` (раздел PCRE / Perl-стиль) |
| **8.** Java | `java.util.regex`, Matcher, split | `kb-regex-flavors-practice-v1.md` (раздел Java) |
| **9.** .NET | `Regex`, `Match`, `Group`, опции | `kb-regex-flavors-practice-v1.md` (раздел .NET) |
| **10.** PHP | `preg_*` | `kb-regex-flavors-practice-v1.md` (упоминание PHP/preg; при расширении — отдельная секция) |

## Указатель

- Роутер кластера: `index-knowledge-regex-cluster-v1.md`
- Шаблон карточки KB: `template-knowledge-card-v1.md`
- Операционный контракт: `regex-playbook.md`

<!-- section:bookmarks-note -->
Оглавление в PDF содержит **294** закладки верхнего уровня (плоский список в экспорте); для навигации по подпунктам удобнее сам ридер PDF.
<!-- /section:bookmarks-note -->
