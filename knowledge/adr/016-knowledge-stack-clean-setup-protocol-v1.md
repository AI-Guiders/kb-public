# ADR 016: Протокол чистой установки стека (ANM + kb-public → personal)

**Статус:** Accepted  
**Дата:** 2026-05-18  
**Связано:** [009](009-kb-entry-structure-and-pre-open-onboarding.md), [013](013-knowledge-roots-toml-and-chmod-ugo-v1.md), MCP ADR 014/015

---

## Контекст

Новый пользователь скачивает **agent-notes-mcp** и **kb-public**, но без **personal** канона агент не имеет единого чеклиста: README ANM описывает сборку, ADR 009 — вход в уже существующую KB, `map-kb-three-contours` — куда писать после того, как контуры есть. Пробел: **пошаговый onboarding** и контракт поведения агента («скажи 1, 2, 3» / сделай за меня шаблоны).

## Решение

1. Канонический playbook: **`knowledge/domains/agent-operations/playbook-knowledge-stack-clean-setup-v1.md`** (фазы 0–5, DoD, chmod ugo).
2. Маршрутизация: секция **`router-clean-setup`** в `index-knowledge-router-supplement-v1.md`.
3. Опциональный hot: **`clean-setup-routing-v1`** (шаблон `work/local/hot-section-clean-setup-routing-v1.example.md`).
4. Тонкий вход: ссылка в **`00-entry-kb-v1.md`**.

## Последствия

- После `build-public-kb` playbook доступен в kb-public — агент может вести пользователя до появения personal (TOML `primary=public` временно).
- TOML и реальные пути остаются **вне** git канона (`work/local/`, диск).

## Не в scope v1

- Автоматический setup wizard в ANM (CLI).
- `route_context` overlay для onboarding (достаточно router + hot).
**v1.1 (2026-05-18):** шаблоны перенесены в **`knowledge/templates/template-clean-setup-*`** (корзина `templates/` по таксономии); каталог `domains/agent-operations/clean-setup-templates-v1/` снят.
**v1.2 (2026-05-18):** подкаталоги `templates/cards/` и `templates/newcomer/`; корень `templates/` — только README-индекс.