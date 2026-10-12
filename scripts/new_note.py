#!/usr/bin/env python3
"""Create a new note from templates/note-template.md.

Examples
--------
    python scripts/new_note.py ai "Diffusion Models" --tags ai,generative
    python scripts/new_note.py chemistry "Reaction Kinetics" --tags chemistry --new-topic

The script only creates the file. It then prints the remaining manual steps
(nav entry, topic index entry, cross-links) so nothing gets forgotten.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATE = ROOT / "templates" / "note-template.md"

INDEX_STUB = """---
title: {title}
tags: [{topic}]
status: seed
updated: {today}
---

# {title}

> **Scope** — What this topic covers, in one or two sentences.

## Visual summary

```mermaid
flowchart TD
    T["{title}"] --> A["Subtopic A"]
    T --> B["Subtopic B"]
```

## Notes

| Note | Status | One-line summary |
|---|---|---|

## Related topics

- (add links to neighbouring topics)
"""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("topic", help="Topic folder under docs/, e.g. ai, robotics, physics")
    parser.add_argument("title", help='Human title, e.g. "Diffusion Models"')
    parser.add_argument("--tags", default="", help="Comma-separated tags (defaults to the topic name)")
    parser.add_argument("--new-topic", action="store_true", help="Create the topic folder and an index.md if missing")
    args = parser.parse_args()

    topic = slugify(args.topic)
    slug = slugify(args.title)
    if not topic or not slug:
        print("error: topic and title must contain letters or digits", file=sys.stderr)
        return 2

    topic_dir = DOCS / topic
    today = date.today().isoformat()

    if not topic_dir.exists():
        if not args.new_topic:
            known = sorted(p.name for p in DOCS.iterdir() if p.is_dir() and (p / "index.md").exists())
            print(f"error: topic '{topic}' does not exist. Known topics: {', '.join(known)}", file=sys.stderr)
            print("       Use --new-topic to create it.", file=sys.stderr)
            return 2
        topic_dir.mkdir(parents=True)
        (topic_dir / "index.md").write_text(
            INDEX_STUB.format(title=args.topic.replace("-", " ").title(), topic=topic, today=today),
            encoding="utf-8",
        )
        print(f"created topic index: {(topic_dir / 'index.md').relative_to(ROOT)}")

    target = topic_dir / f"{slug}.md"
    if target.exists():
        print(f"error: {target.relative_to(ROOT)} already exists", file=sys.stderr)
        return 1

    tags = ", ".join(t.strip() for t in (args.tags or topic).split(",") if t.strip())
    content = (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("{{title}}", args.title)
        .replace("{{tags}}", tags)
        .replace("{{date}}", today)
    )
    target.write_text(content, encoding="utf-8")

    rel = target.relative_to(DOCS).as_posix()
    print(f"created note: {target.relative_to(ROOT)}\n")
    print("Next steps:")
    print(f"  1. Add it to the nav in mkdocs.yml:   - {args.title}: {rel}")
    print(f"  2. Add a row to docs/{topic}/index.md (Notes table)")
    print("  3. Link it from at least one related note (Related section)")
    print("  4. Run: python scripts/check_links.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
