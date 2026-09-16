# Playbook: накопление troubleshooting-гайдов
**Tags:** #living #meta #playbook


**Статус:** v1 · консолидация по мирам  
**Индекс:** [`index-troubleshooting.md`](index-troubleshooting.md)  
**Шаблон README мира:** [`templates/worlds/template-world-troubleshooting-readme.md`](../templates/worlds/template-world-troubleshooting-readme.md)

---

## Два контура

| Контур | Путь | kb-public |
|--------|------|-----------|
| **A** | `worlds/<world>/troubleshooting/` | Да |
| **B** | `work/projects/<scope>/` | Нет |

Product-only (пути репо, `settings.toml` продукта, ADR одного IDE, имена контролов продукта) — **только B** в `work/projects/…`. Реестр: [`work/troubleshooting/README.md`](../work/troubleshooting/README.md).  
**В `worlds/…/troubleshooting/` запрещены** имена продуктов и product paths — только обобщённые симптомы стека + ссылка «карточка в work по `[PRIMARY]`».

---

## Структура мира (таксономия)

В зрелом `worlds/<slug>/`:

```
worlds/<slug>/
  status-*.md
  playbook-*.md          # операции
  kb-*.md                # факты
  troubleshooting/
    README.md
    playbook-<slug>-troubleshooting.md
```

- **Не** класть troubleshooting в корень мира (расползание имён).
- **Не** дублировать длинные § «Диагностика» в operational playbook — одна ссылка на `troubleshooting/`.
- Исключение: `matrix-*` в корне мира, если это роутер (software-authoring); troubleshooting дублирует fast router и ссылается на matrix.

---

## Когда создавать / расширять

| Ситуация | Действие |
|----------|----------|
| Новый повторяющийся симптом в домене | Строка в `troubleshooting/playbook-…` |
| § Диагностика > ~8 пунктов в operational playbook | Перенос в troubleshooting, в operational — ссылка |
| Симптом только одного продукта | `work/projects/…`, не worlds |
| Два+ продукта, без product paths | Вынос B → A |

---

## Регистрация

1. Строка в [`index-troubleshooting.md`](index-troubleshooting.md)
2. `troubleshooting/README.md` в hub мира (`worlds/<slug>/README.md`)
3. Supplement router при частых формулировках
4. Product: [`work/troubleshooting/README.md`](../work/troubleshooting/README.md) + `work/projects/<id>/README.md`  
5. Шаблон product playbook: [`templates/work/template-product-troubleshooting.md`](../templates/work/template-product-troubleshooting.md)

---

## Provenance

meta / process · 2026-05 world consolidation

