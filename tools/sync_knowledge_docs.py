#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copy repo knowledge/ into MkDocs docs trees for search and deep links."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
TARGETS = [
    ROOT / "docs" / "knowledge",
    ROOT / "docs" / "en" / "knowledge",
]

SKIP_DIRS = {".git", "__pycache__", ".revisions"}


def copy_tree(src: Path, dst: Path) -> int:
    if dst.exists():
        shutil.rmtree(dst)
    count = 0
    for path in src.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(src)
        if path.is_dir():
            (dst / rel).mkdir(parents=True, exist_ok=True)
        else:
            if path.suffix.lower() not in {".md", ".toml"}:
                continue
            out = dst / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, out)
            count += 1
    return count


def main() -> None:
    if not KNOWLEDGE.is_dir():
        raise SystemExit(f"Missing {KNOWLEDGE}")
    total = 0
    for target in TARGETS:
        n = copy_tree(KNOWLEDGE, target)
        print(f"Synced {n} files -> {target.relative_to(ROOT)}")
        total += n
    print(f"Done ({total} file writes).")


if __name__ == "__main__":
    main()
