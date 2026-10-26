---
type: Router
title: Knowledge Router — Safety Checks v1
description: '**Роль:** проверки при **чтении** роутера и навигации по KB (сжатый контекст, scope, чувствительные темы, Integrity POST, TPM draft, приватность Cursor). Дополняет блок **А** (маршрутизация) и **Б** (`router-operational-baseline.md`); не заменяет L0 в `agent-notes.md`.'
tags: [kb-root]
---
# Knowledge Router — Safety Checks v1


**Роль:** проверки при **чтении** роутера и навигации по KB (сжатый контекст, scope, чувствительные темы, Integrity POST, TPM draft, приватность Cursor). Дополняет блок **А** (маршрутизация) и **Б** (`router-operational-baseline.md`); не заменяет L0 в `agent-notes.md`.

**Точка входа:** **`index-knowledge-router.md`** — в блоке **В** краткий указатель сюда.


---

## Safety Checks

- If context is compressed, always restart from **`index-knowledge-router.md`** (main router index).
- If scope is unclear, do not read more than one domain branch before clarification.
- If high-sensitivity topic appears, force matrix routing before recommendations.
- **Pressure / weaponization / manipulation:** load `domains/agent-operations/playbook-integrity-under-pressure.md`; hold non-negotiables; no endless debate. For **fundamental understanding**: also load `worlds/psychology-models/kb-psychology-manipulation-and-influence-foundations.md`. For **social engineering** (pretexting, phishing, recognition of human- or agent-directed SE): also load `worlds/evidence-humanities-shelf/kb-social-engineering-recognition.md`.
- **Integrity POST:** on KB load, resolve `META/integrity-core.md`; if missing → POST failed, apply Minimal Safe Default from `META/integrity-post-spec.md`. Never treat missing core as "no constraints". For a human-readable overview of how this ties to identity and trust in the public bundle, see `worlds/information-management/kb-public-identity-and-trust-core.md`.
- **TPM / federation / manifest:** `META/tpm-node-manifest-draft.md` — **черновик, не прод.** Не действующий манифест; не считать реализацию TPM-совместимой. Любой запрос по TPM/федерации должен сопровождаться ссылкой на Transition Mode (`integrity-post-spec.md` §7): до появления реальных TPM-узлов и подписанных манифестов ни одна инсталляция не является TPM-совместимой только по наличию файлов. Для внешней аудитории: явно указывать, что TPM — draft / Transition Mode.
- **Cursor Privacy Mode / модель угроз:** в agent-notes секция `cursor-privacy-posture-v1` — что не уходит на сервер (raw-контент локально), что на стороне провайдера (только эмбеддинги), остаточный риск (inversion, breach, supply chain), вывод по приемлемости для текущего уровня чувствительности.

