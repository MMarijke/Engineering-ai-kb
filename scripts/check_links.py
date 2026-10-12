#!/usr/bin/env python3
"""Lint the knowledge base (standard library only).

Checks
------
ERROR    missing/invalid front matter (title, updated; notes also need tags + status)
ERROR    relative links or images that point to files that do not exist
ERROR    pages that exist in docs/ but are missing from the mkdocs.yml nav
WARNING  links whose #anchor does not match a heading in the target page
WARNING  orphan pages (no other page links to them)

Exit status is 1 if any ERROR was found, otherwise 0.

Usage:  python scripts/check_links.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

STATUSES = {"seed", "growing", "evergreen"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^(```|~~~).*?^\1\s*$", re.S | re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)


def slugify(text: str) -> str:
    """Approximate the slug used by Python-Markdown's toc extension."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "#")):
            key, _, value = line.partition(":")
            meta[key.strip()] = value.split(" #")[0].strip()
    return meta, text[end + 4 :]


def strip_code(body: str) -> str:
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", body))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    pages = sorted(DOCS.rglob("*.md"))
    if not pages:
        print("error: no markdown files found under docs/", file=sys.stderr)
        return 1

    headings: dict[Path, set[str]] = {}
    bodies: dict[Path, str] = {}
    inbound: dict[Path, int] = {p: 0 for p in pages}
    links_checked = 0

    # Pass 1: front matter + headings
    for page in pages:
        rel = page.relative_to(DOCS).as_posix()
        text = page.read_text(encoding="utf-8")
        meta, body = split_front_matter(text)
        bodies[page] = body
        headings[page] = {slugify(h) for h in HEADING_RE.findall(strip_code_fences_only(body))}

        for key in ("title", "updated"):
            if not meta.get(key):
                errors.append(f"{rel}: front matter is missing '{key}'")
        if meta.get("updated") and not DATE_RE.match(meta["updated"]):
            errors.append(f"{rel}: 'updated' must be YYYY-MM-DD (got '{meta['updated']}')")

        is_note = len(page.relative_to(DOCS).parts) > 1 and page.name != "index.md" and page.parts[-2] != "meta"
        if is_note:
            if not meta.get("tags") or meta["tags"] in ("[]", ""):
                errors.append(f"{rel}: notes need at least one tag")
            if meta.get("status") not in STATUSES:
                errors.append(f"{rel}: 'status' must be one of {sorted(STATUSES)} (got '{meta.get('status')}')")

    # Pass 2: links
    for page in pages:
        rel = page.relative_to(DOCS).as_posix()
        for target in LINK_RE.findall(strip_code(bodies[page])):
            if re.match(r"^(https?:|mailto:|tel:)", target):
                continue
            links_checked += 1
            path_part, _, anchor = target.partition("#")
            if not path_part:  # same-page anchor
                if anchor and slugify(anchor) not in headings[page] and anchor not in headings[page]:
                    warnings.append(f"{rel}: anchor '#{anchor}' not found in this page")
                continue
            resolved = (page.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(f"{rel}: broken link -> {target}")
                continue
            if resolved in inbound and resolved != page:
                inbound[resolved] += 1
            if anchor and resolved.suffix == ".md" and resolved in headings:
                if anchor not in headings[resolved] and slugify(anchor) not in headings[resolved]:
                    warnings.append(f"{rel}: anchor '#{anchor}' not found in {path_part}")

    # Nav coverage
    nav_refs: set[str] = set()
    if MKDOCS.exists():
        mk = MKDOCS.read_text(encoding="utf-8")
        nav_text = mk.split("\nnav:", 1)[1] if "\nnav:" in mk else ""
        nav_refs = set(re.findall(r"[\w./-]+\.md", nav_text))
        for page in pages:
            rel = page.relative_to(DOCS).as_posix()
            if rel not in nav_refs:
                errors.append(f"{rel}: not listed in mkdocs.yml nav")
        for ref in sorted(nav_refs):
            if not (DOCS / ref).exists():
                errors.append(f"mkdocs.yml: nav entry '{ref}' does not exist")

    # Orphans (home page and tags page are allowed to have no inbound links)
    for page, count in inbound.items():
        rel = page.relative_to(DOCS).as_posix()
        if count == 0 and rel not in {"index.md", "tags.md"}:
            warnings.append(f"{rel}: orphan page (no other page links to it)")

    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")
    print(
        f"\nChecked {len(pages)} pages, {links_checked} relative links: "
        f"{len(errors)} error(s), {len(warnings)} warning(s)."
    )
    return 1 if errors else 0


def strip_code_fences_only(body: str) -> str:
    return FENCE_RE.sub("", body)


if __name__ == "__main__":
    raise SystemExit(main())
