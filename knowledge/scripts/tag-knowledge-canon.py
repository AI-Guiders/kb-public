#!/usr/bin/env python3
"""One-shot: add **Tags:** to agent-notes knowledge canon (path heuristics).

Skip: scratch, .revisions, temp, personal (optional), archive.
Merge with existing **Tags:** lines. Idempotent.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

TAGS_LINE_RE = re.compile(r"(?m)^\*\*Tags:\*\*\s*(.+)$")
HASH_RE = re.compile(r"#([A-Za-z][A-Za-z0-9_-]*)")
SKIP_DIR_PARTS = {".revisions", "scratch", "temp", "archive", "handoff"}
# personal is operator-private; still tag with #personal if --include-personal

ROLE_FROM_NAME = (
    ("playbook-", "playbook"),
    ("note-", "note"),
    ("template-", "template"),
    ("status-", "status"),
    ("kb-", "kb"),
    ("map-", "map"),
    ("runbook-", "runbook"),
    ("checklist-", "checklist"),
)


def normalize(tag: str) -> str:
    t = tag.strip().lstrip("#").lower()
    return t if t and t[0].isalpha() else ""


def parse_existing(text: str) -> set[str]:
    m = TAGS_LINE_RE.search(text)
    if not m:
        return set()
    return {normalize(x) for x in HASH_RE.findall(m.group(1)) if normalize(x)}


def heuristic_tags(rel: str, name: str) -> set[str]:
    tags: set[str] = set()
    parts = rel.replace("\\", "/").split("/")
    low = name.lower()

    for prefix, role in ROLE_FROM_NAME:
        if low.startswith(prefix):
            tags.add(role)
            break
    if low == "readme.md":
        tags.add("readme")
    if "adr" in parts[0:1] or low.startswith("adr-") or re.match(r"^\d{3}-", low):
        tags.add("adr")

    top = parts[0] if parts else ""
    if top == "META":
        tags.add("meta")
    elif top == "domains" and len(parts) > 1:
        tags.add(parts[1])
        tags.add("domains")
    elif top == "worlds" and len(parts) > 1:
        tags.add(parts[1])
        tags.add("worlds")
    elif top == "adr":
        tags.add("adr")
    elif top == "templates":
        tags.add("templates")
    elif top == "work":
        tags.add("work")
        if len(parts) > 2 and parts[1] == "projects":
            tags.add(parts[2])
            if len(parts) > 3:
                tags.add(parts[3])
    elif top == "personal":
        tags.add("personal")
    elif top == "":
        pass
    else:
        # root knowledge/*.md
        if len(parts) == 1:
            tags.add("kb-root")

    if low.startswith("note-") or "research" in low:
        tags.add("research")
    if low.startswith("playbook-"):
        tags.add("living")

    # sanitize tag tokens (path segments may have dots)
    cleaned = set()
    for t in tags:
        t2 = re.sub(r"[^a-z0-9_-]", "-", t.lower()).strip("-")
        if t2 and t2[0].isalpha():
            cleaned.add(t2)
    return cleaned


def should_skip(rel: str, include_personal: bool) -> bool:
    parts = set(rel.replace("\\", "/").split("/"))
    if parts & SKIP_DIR_PARTS:
        return True
    if not include_personal and "personal" in parts:
        return True
    return False


def insert_or_merge(text: str, tags: set[str]) -> str | None:
    existing = parse_existing(text)
    merged = existing | tags
    if not merged:
        return None
    line = "**Tags:** " + " ".join("#" + t for t in sorted(merged))
    if TAGS_LINE_RE.search(text):
        if existing == merged:
            return None
        return TAGS_LINE_RE.sub(line, text, count=1)

    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            return "".join(lines[: i + 1]) + line + "\n\n" + "".join(lines[i + 1 :])
    return line + "\n\n" + text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--knowledge-root", type=Path, required=True, help="…/knowledge directory")
    ap.add_argument("--include-personal", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root: Path = args.knowledge_root.resolve()
    changed = 0
    scanned = 0
    skipped = 0
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if should_skip(rel, args.include_personal):
            skipped += 1
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8")
        tags = heuristic_tags(rel, path.name)
        new = insert_or_merge(text, tags)
        if new is None:
            continue
        changed += 1
        if args.dry_run:
            print(f"WOULD {rel}: {TAGS_LINE_RE.search(new).group(0) if TAGS_LINE_RE.search(new) else '?'}")
        else:
            path.write_text(new, encoding="utf-8", newline="\n")
    print(f"scanned={scanned} changed={changed} skipped={skipped} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()

