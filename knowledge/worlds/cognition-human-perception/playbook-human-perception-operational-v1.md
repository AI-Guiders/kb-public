# Human perception — operational playbook v1

**Purpose:** переводить фундамент из [`kb-human-perception-fundamentals-v1.md`](kb-human-perception-fundamentals-v1.md) в **действия и проверки** для UX, IDE и агентского контура.  
**Мир:** `cognition.human-perception` — см. [`README.md`](README.md).  
**Научные якоря (цитирование, DOI):** [`kb-human-perception-scientific-evidence-v1.md`](kb-human-perception-scientific-evidence-v1.md).  
**Order:** сначала этот playbook; при узком UI‑вопросе — [`playbook-hci-core-v1.md`](../hci-ux-dx/playbook-hci-core-v1.md); классика эвристик — [`kb-ui-ux-literature-evidence-v1.md`](../hci-ux-dx/kb-ui-ux-literature-evidence-v1.md).

---

## 1. Когда загружать этот playbook

- Ревью или проектирование **плотного** интерфейса (IDE, кокпит, много панелей).
- Вопросы «почему это бесит / утомляет / незаметно» без явного бага.
- Решения про **уведомления**, **агентские всплытия**, **прерывания** потока.
- Спор о **приоритете зон** (что первично на экране) в продукте вроде CascadeIDE (см. ADR в репо: `0021`, `0076` и др.).
- **Не заменяет:** клиническую психологию, терапию, медицинские протоколы — при необходимости см. домен Psychology и [`../medicine-evidence/kb-therapy-and-support-boundaries-v1.md`](../medicine-evidence/kb-therapy-and-support-boundaries-v1.md).

---

## 2. Мост «Fundamentals → вопрос дизайна»

| Идея (fundamentals) | Вопрос для ревью |
|---------------------|------------------|
| Салентность + предсказание | Новый движущийся/яркий элемент **конкурирует** с задачей или поддерживает ожидаемое место фидбека? |
| Рабочая память / чанки | Пользователь может **сгруппировать** новое в 5–7 знакомых кусков или каждый элемент «сам по себе»? |
| Extraneous load | Сколько **независимых** решений на одном экране? Можно ли убрать шаг без потери смысла? |
| Стресс / tunneling | **Критический путь** (сборка, потеря данных, безопасность) виден при усталости или спрятан в «ещё одной вкладке»? |
| Change blindness | **Критическое** изменение состояния сопровождается явным маркером, а не только «что-то изменилось в углу»? |

---

## 3. Мини-чеклист перед добавлением UI/агентского элемента

1. **Один новый фокус за раз?** Если нет — что уходит в периферию по смыслу (не в «мелкий шрифт»).
2. **Фидбек предсказуем по месту?** (см. HCI: state visibility.)
3. **Прерывание** — осознанное (пользователь вызвал) или **вторжение** в поток?
4. Для агента: **гранулярность** ответа соответствует намерению; не «простыня» при запросе на один шаг (см. [`playbook-hci-core-v1.md`](../hci-ux-dx/playbook-hci-core-v1.md) § Dialogue).

---

## 4. Связь с соседними артефактами канона

| Тема | Куда |
|------|------|
| Первоисточники по вниманию, РП, CLT, change/inattentional blindness | `kb-human-perception-scientific-evidence-v1.md` |
| Общие контракты HCI, доступность, диалог | `worlds/hci-ux-dx/playbook-hci-core-v1.md`, `worlds/hci-ux-dx/kb-hci-usability-and-dialog-rules-v1.md` |
| Эвристики Norman/Nielsen/… | `worlds/hci-ux-dx/kb-ui-ux-literature-evidence-v1.md` |
| DX инструмента, трение | `worlds/hci-ux-dx/de-dx-playbook.md`, `worlds/hci-ux-dx/kb-ide-dx-literature-evidence-v1.md` |
| Метафора кокпита / PFD/MFD в IDE | `worlds/aviation-human-factors/kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md` (авиация как язык), **конкретные** нормы — ADR репозитория CascadeIDE |
| Зловещая долина человек–агент | `kb-uncanny-valley-inverse-v1.md` |
| Ситуационная осведомлённость (метрики SA) | `kb-situational-awareness-measurement-dynamic-systems-v1.md` |

---

## 5. Правило для агента

- При **спорном UX** без явного технического бага: сначала один проход по §2 таблице; затем **HCI**; не дублировать длинные нормативы из ADR — **ссылаться** на репозиторий продукта.
- Не использовать этот playbook как **оправдание** манипуляции вниманием во вред; baseline целостности — [`playbook-integrity-under-pressure-v1.md`](../../playbook-integrity-under-pressure-v1.md).

---

*Версия: v1.0 · 2026-04-20*
