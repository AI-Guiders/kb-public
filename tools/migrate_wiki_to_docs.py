#!/usr/bin/env python3
"""Import kb-public.wiki pages into docs/ with MkDocs-friendly links."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT.parent / ".kb-public-wiki-push"

# wiki filename -> path under docs/ (RU)
WIKI_TO_DOC: dict[str, str] = {
    "Карта-трёх-контуров-KB.md": "docs/onboarding/three-contours.md",
    # white-label: curated in docs/onboarding/white-label.md (wiki was stub-only)
    "Протоколы-и-сущности.md": "docs/onboarding/protocols.md",
    "Onboarding-за-30-минут.md": "docs/onboarding/quick-start-30min.md",
    "FAQ-быстрый-вход.md": "docs/guide/faq.md",
    "Память-и-KB-как-устроено.md": "docs/guide/memory-and-kb.md",
    "Типовые-сценарии-и-recovery.md": "docs/guide/scenarios-recovery.md",
    "Шаблон-решения-KB.md": "docs/guide/decision-template.md",
    "Глоссарий.md": "docs/guide/glossary.md",
    "ChatGPT-Desktop-—-установка-стека.md": "docs/setup/chatgpt-desktop-stack.md",
}

# wiki page title (without .md) -> target path from docs/
WIKI_LINK_TARGETS: dict[str, str] = {
    "Home": "index.md",
    "Карта-трёх-контуров-KB": "onboarding/three-contours.md",
    "Подключить-свой-org-KB-white-label": "onboarding/white-label.md",
    "Протоколы-и-сущности": "onboarding/protocols.md",
    "Onboarding-за-30-минут": "onboarding/quick-start-30min.md",
    "FAQ-быстрый-вход": "guide/faq.md",
    "Память-и-KB-как-устроено": "guide/memory-and-kb.md",
    "Типовые-сценарии-и-recovery": "guide/scenarios-recovery.md",
    "Шаблон-решения-KB": "guide/decision-template.md",
    "Глоссарий": "guide/glossary.md",
    "ChatGPT-Desktop-—-установка-стека": "setup/chatgpt-desktop-stack.md",
}

GH_KB = re.compile(
    r"https://github\.com/AI-Guiders/kb-public/blob/main/(knowledge/[^\s\)]+)"
)


def rel_link(from_doc: str, target: str) -> str:
    """Relative markdown link from from_doc to target (paths under docs/)."""
    base = Path("docs") / from_doc
    dest = Path("docs") / target
    return os_relpath(dest, base.parent).as_posix()


def os_relpath(dest: Path, start: Path) -> Path:
    import os

    return Path(os.path.relpath(dest, start))


def convert_body(text: str, from_doc: str) -> str:
    text = text.replace(
        "Agent Notes Wiki — Home",
        "[главная](index.md)",
    )
    text = text.replace(
        "`Первые принципы среды`",
        "[Entry KB](../knowledge/00-entry-kb-v1.md)",
    )
    text = text.replace(
        "Первые принципы среды",
        "[Entry KB](../knowledge/00-entry-kb-v1.md)",
    )
    text = text.replace(
        "`Как работать в среде каждый день`",
        "[роутер](../knowledge/index-knowledge-router-v1.md)",
    )
    text = text.replace(
        "`Протокол режимов WORK и HUMAN`",
        "[протоколы](protocols.md)" if from_doc.startswith("onboarding/") else "[протоколы](../onboarding/protocols.md)",
    )

    def wiki_link(m: re.Match[str]) -> str:
        label = m.group(1)
        key = label.strip()
        if key not in WIKI_LINK_TARGETS:
            return m.group(0)
        target = WIKI_LINK_TARGETS[key]
        href = rel_link(from_doc, target)
        return f"[{label}]({href})"

    text = re.sub(r"\[\[([^\]]+)\]\]", wiki_link, text)

    def gh_link(m: re.Match[str]) -> str:
        path = m.group(1)
        href = rel_link(from_doc, path)
        return href

    text = GH_KB.sub(lambda m: rel_link(from_doc, m.group(1)), text)
    return text


def main() -> None:
    if not WIKI.is_dir():
        raise SystemExit(f"Wiki clone not found: {WIKI}")

    for wiki_name, doc_rel in WIKI_TO_DOC.items():
        src = WIKI / wiki_name
        if not src.is_file():
            raise SystemExit(f"Missing wiki page: {src}")
        body = src.read_text(encoding="utf-8")
        from_doc = doc_rel.removeprefix("docs/")
        converted = convert_body(body, from_doc)
        out = ROOT / doc_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(converted, encoding="utf-8", newline="\n")
        print(f"Wrote {out.relative_to(ROOT)}")

    print("Done.")


if __name__ == "__main__":
    main()
