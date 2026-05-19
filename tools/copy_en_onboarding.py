#!/usr/bin/env python3
"""Copy RU guide/setup pages to en/ for translation pass (paths adjusted)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAIRS = [
    ("docs/onboarding/three-contours.md", "docs/en/onboarding/three-contours.md"),
    ("docs/onboarding/protocols.md", "docs/en/onboarding/protocols.md"),
    ("docs/onboarding/quick-start-30min.md", "docs/en/onboarding/quick-start-30min.md"),
    ("docs/onboarding/white-label.md", "docs/en/onboarding/white-label.md"),
    ("docs/guide/faq.md", "docs/en/guide/faq.md"),
    ("docs/guide/memory-and-kb.md", "docs/en/guide/memory-and-kb.md"),
    ("docs/guide/scenarios-recovery.md", "docs/en/guide/scenarios-recovery.md"),
    ("docs/guide/decision-template.md", "docs/en/guide/decision-template.md"),
    ("docs/guide/glossary.md", "docs/en/guide/glossary.md"),
    ("docs/setup/chatgpt-desktop-stack.md", "docs/en/setup/chatgpt-desktop-stack.md"),
]


def adjust_for_en(text: str) -> str:
    text = text.replace("../knowledge/", "../knowledge/")
    text = text.replace("](onboarding/", "](../onboarding/")
    text = text.replace("](guide/", "](../guide/")
    text = text.replace("](setup/", "](../setup/")
    text = text.replace("](index.md)", "](../index.md)")
    return text


def main() -> None:
    for src_rel, dst_rel in PAIRS:
        src = ROOT / src_rel
        dst = ROOT / dst_rel
        body = adjust_for_en(src.read_text(encoding="utf-8"))
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(body, encoding="utf-8", newline="\n")
        print(dst_rel)


if __name__ == "__main__":
    main()
