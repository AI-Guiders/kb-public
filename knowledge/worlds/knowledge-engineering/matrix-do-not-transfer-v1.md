# Do-Not-Transfer Matrix v1

Назначение: фиксировать, какие знания нельзя переносить между мирами без явной валидации.

## Core Rule

Если элемент зависит от локальной истории, права, языка, символики или травматического контекста, он **не переносится по умолчанию**.

## Matrix

| Source World | Candidate Transfer | Default | Why |
| --- | --- | --- | --- |
| `culture.country-specific` | в другую страну | deny | разные исторические коннотации и границы допустимого |
| `law.country-specific` | в другой legal regime | deny | несовместимые нормы и ответственность |
| `communication.local-idioms` | в другой язык/регион | deny | потеря смысла и риск оскорбления |
| `politics.local-framing` | в глобальный слой | deny | локальные нарративы не универсальны |
| `psychology.personal-trauma-context` | как универсальная модель | deny | высокая вариативность и риск вреда |
| `culture.global` | в страновой контекст | allow-with-check | нужен conflict-check и local adaptation |
| `methodology.evidence-hygiene` | в любой мир | allow | это инвариантный мета-слой |

## Mandatory Checks Before Any Cross-World Transfer

- указать `transfer_boundary` и `falsification_trigger`;
- проверить локальные ограничения (право, этика, язык, история);
- зафиксировать уровень уверенности (`low/medium/high`);
- если уверенность `low` или данных мало -> включать `fallback`.

## Red Flags (Stop Transfer)

- "похоже" вместо фактов;
- отсутствие источника локального контекста;
- высокая тема чувствительности (политика, идентичность, травма) без проверки;
- конфликт между global принципом и локальной нормой без conflict-check.
