# KB canonical publication v1

---

<!-- section:kb-canonical-push-contract-v1 -->
## KB Canonical Push Contract v1

Правило: KB считается обновленной только после коммита и пуша в каноничный репозиторий `d:\Experiments\agent-notes`.

### Обязательный цикл
1) Обновить KB через notes-инструменты.
2) Проверить `git status` в каноничном репо.
3) Сделать логический коммит KB-изменений.
4) `git push origin main`.
5) Зафиксировать short SHA в рабочем отчете.

### Stop rule
Если KB-правка есть, а коммита в каноничном репо нет -> задача не считается завершенной.
<!-- /section:kb-canonical-push-contract-v1 -->

<!-- section:kb-public-trust-source-roadmap-v1 -->
## kb-public и полный аналог TPM (контекст 2026-03)

- **kb-public:** отдельный репо для выхода в паблик; добавлены аналоги POST, TPM, необсуждаемое, защита от манипуляций, эпистемическое недоверие.
- **Ограничение:** полный аналог TPM требует **независимый Trust Source** (сейчас нет).
- **Возможный путь:** ДЦ Миши Ушакова — уточнить Tier и SLA; при Tier 2/3 и SLA ≥ 99% — поднять GitLab там и выложить kb-public; тогда цепочка доверия даёт полный аналог TPM.
- Источник: обмен идеями, не решение; фиксирую для контекста.
<!-- /section:kb-public-trust-source-roadmap-v1 -->


