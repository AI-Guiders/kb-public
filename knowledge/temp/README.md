# `knowledge/temp/` — external WM агента (scratch)

**Статус:** операционная корзина · не kb-public · не канон  
**Playbook:** [`domains/agent-operations/playbook-external-memory-workaround-v1.md`](../domains/agent-operations/playbook-external-memory-workaround-v1.md)

---

## Зачем

Папка для **временных записей**, когда harness не держит нить: summarization, длинная сессия, риск потери решения. **Workaround**, не целевой слой памяти — см. playbook.

Агент пишет сюда **без запроса оператора**, если видит риск потери. «Куда в канон?» — решает агент после стабилизации; до merge файл живёт здесь.

---

## Именование

```text
{YYYY-MM-DD}-{slug}-scratch.md
```

Примеры: `2026-06-14-cursor-harness-autonomy-scratch.md`, `2026-06-14-forge-handoff-verify-scratch.md`

`slug` — короткий kebab-case по теме turn. Суффикс `-scratch` обязателен (отличие от канона).

---

## Жизненный цикл

```text
temp/*.md  →  задача дожита  →  merge в playbook / work / domains / …  →  delete из temp/
```

- **Merge** — содержательное попало в SSOT; scratch удалить.
- **Delete без merge** — устарело или дублирует канон.
- **Оставить в temp** — только пока thread открыт (дни, не месяцы).

---

## Git и контуры

| | |
|---|---|
| **agent-notes (личный/org)** | коммитить **можно** — continuity между сессиями; после merge предпочтительно удалить файл |
| **kb-public** | **`temp/README.md`** — один раз в публичном срезе (каркас корзины); `*-scratch.md` **не** экспортировать (`public-kb.ignore`) |
| **Чужие репо** | не создавать `temp/` без задачи; для product-кода — только если явно нужно |

---

## Не класть сюда

- ADR, playbooks, status — сразу в целевую корзину по [`META/kb-taxonomy-v1.md`](../META/kb-taxonomy-v1.md)
- секреты, токены, `.env`
- дампы логов и бинарники

---

**Hub:** [`agent-memory-and-operating-principles-v1.md`](../agent-memory-and-operating-principles-v1.md)

