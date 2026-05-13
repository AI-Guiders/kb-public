# One-off: migrate digest-engineering-reading-v1.md to kb-engineering-evidence-v1.md by knowledge theme.
# Run from knowledge/ folder. Reads digest, writes kb with entries grouped by theme (not batch).
# Batch -> theme mapping (by batch title and entry content):
BATCH_TO_THEME = {
    "Batch 01": "Language and runtime",
    "Batch 02": "Testing and diagnostics",
    "Batch 03": "Async and reliability",
    "Batch 04": "Platform and data layer",
    "Batch 05": "Diagnostics and query efficiency",
    "Batch 06": "Architecture and testing",
    "Batch 07": "Data stores and resilience",
    "Batch 08": "Architecture and fault isolation",
    "Batch 09": "Algorithms, reliability, security",
    "Batch 10": "Reliability and delivery",
    "Batch 11": "Compilers and language tooling",
    "Batch 12": "F# and interop",
    "Batch 13": "OS and runtime environments",
    "Batch 14": "Cloud, economics, scale",
}

def parse_digest(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    entries = []
    current_batch = None
    current = None
    for line in text.split("\n"):
        if line.startswith("## Batch "):
            # "## Batch 01 (Completed): Platform Baseline" -> "Batch 01"
            part = line.split("(Completed)")[0].replace("## ", "").strip()
            current_batch = part.split(":")[0].strip() if ":" in part else part
            continue
        if line.startswith("### Entry "):
            if current and current.get("fact"):
                current["batch"] = current_batch
                entries.append(current)
            num = line.replace("### Entry ", "").strip()
            current = {"num": num, "source": "", "date": "", "fact": "", "heuristic": "", "first_adoption": "", "success": "", "confidence": ""}
            continue
        if not current:
            continue
        if line.startswith("- Source:"):
            current["source"] = line.replace("- Source:", "").strip()
        elif line.startswith("- Date:"):
            current["date"] = line.replace("- Date:", "").strip()
        elif line.startswith("- Fact:"):
            current["fact"] = line.replace("- Fact:", "").strip()
        elif line.startswith("- Heuristic:"):
            current["heuristic"] = line.replace("- Heuristic:", "").strip()
        elif line.startswith("- First adoption task:"):
            current["first_adoption"] = line.replace("- First adoption task:", "").strip()
        elif line.startswith("- Success criterion:"):
            current["success"] = line.replace("- Success criterion:", "").strip()
        elif line.startswith("- Confidence:"):
            current["confidence"] = line.replace("- Confidence:", "").strip()
    if current and current.get("fact"):
        current["batch"] = current_batch
        entries.append(current)
    return entries

def theme_of(entry):
    return BATCH_TO_THEME.get(entry.get("batch", ""), "General")

def main():
    import os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # knowledge/
    world = os.path.join(base, "worlds", "software-engineering-evidence")
    digest_path = os.path.join(world, "digest-engineering-reading-v1.md")
    kb_path = os.path.join(world, "kb-engineering-evidence-v1.md")

    entries = parse_digest(digest_path)
    by_theme = {}
    for e in entries:
        t = theme_of(e)
        by_theme.setdefault(t, []).append(e)

    theme_order = [
        "Language and runtime",
        "Testing and diagnostics",
        "Async and reliability",
        "Platform and data layer",
        "Diagnostics and query efficiency",
        "Architecture and testing",
        "Data stores and resilience",
        "Architecture and fault isolation",
        "Algorithms, reliability, security",
        "Reliability and delivery",
        "Compilers and language tooling",
        "F# and interop",
        "OS and runtime environments",
        "Cloud, economics, scale",
        "General",
    ]

    lines = [
        "# Engineering knowledge base (evidence) v1",
        "",
        "**Назначение:** база хранит знания, а не книги. Факты, эвристики и задачи внедрения с атрибуцией источника; источники — для цитирования и опционального углублённого чтения.",
        "",
        "**Формат записи:** Fact, Heuristic, First adoption task, Success criterion, Confidence; в конце — *Source* (и дата).",
        "",
        "---",
        "",
    ]

    for theme in theme_order:
        if theme not in by_theme:
            continue
        block = by_theme[theme]
        lines.append(f"## {theme}")
        lines.append("")
        for e in block:
            lines.append(f"- **Fact:** {e['fact']}")
            lines.append(f"- **Heuristic:** {e['heuristic']}")
            lines.append(f"- **First adoption task:** {e['first_adoption']}")
            lines.append(f"- **Success criterion:** {e['success']}")
            lines.append(f"- **Confidence:** {e['confidence']}")
            lines.append(f"- *Source:* {e['source']} ({e['date']})")
            lines.append("")
        lines.append("")

    with open(kb_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {kb_path} with {len(entries)} entries in {len(by_theme)} themes.")

if __name__ == "__main__":
    main()
