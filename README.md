# kb-public

Публичный срез **Agent Notes KB**: обрезанный по `<!-- public-cut -->` файл **`agent-notes.md`** и каталог **`knowledge/`** после фильтров **`public-kb.ignore`**.

## Документация (вместо wiki)

**https://ai-guiders.github.io/kb-public/** — MkDocs (RU/EN): онбординг, три контура, white-label, полное дерево `knowledge/` для поиска.

Локальная сборка:

```powershell
pip install -r requirements-docs.txt
python tools/sync_knowledge_docs.py
mkdocs serve
```

GitHub Pages: Settings → Pages → **GitHub Actions** (workflow `docs-pages`).

## Лицензия

Тексты — **CC BY-SA 4.0** (`LICENSE`). MCP **agent-notes-mcp** — [MIT](https://github.com/KarataevDmitry/agent-notes-mcp).

## Сборка среза из полного канона

В репозитории maintainer’а с `scripts/`: `build-public-kb.ps1`, `push-public-kb.ps1`. Правила: `knowledge/PUBLISHING.md` в полном каноне.
