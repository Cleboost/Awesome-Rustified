#!/usr/bin/env python3
"""Build README.md from listing fields in each apps/*.md metadata table."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

GITHUB_DIR = Path(__file__).resolve().parent
ROOT = GITHUB_DIR.parent
APPS_DIR = ROOT / "apps"
README = ROOT / "README.md"
CATEGORIES = GITHUB_DIR / "data" / "categories.json"
INTRO = GITHUB_DIR / "templates" / "readme_intro.md"
FOOTER = GITHUB_DIR / "templates" / "readme_footer.md"

DETAILS_BADGE = (
    '[![Details](https://img.shields.io/badge/Details-→-555?style=flat)]'
)
BACK_LINK = "[← Back to list](../README.md)"

ROW_RE = re.compile(r"^\|\s*\*\*([^*]+)\*\*\s*\|\s*(.+?)\s*\|\s*$")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def strip_cell(value: str) -> str:
    return value.strip()


def extract_url(value: str) -> str:
    value = strip_cell(value)
    m = IMG_RE.search(value)
    if m:
        return m.group(1).strip()
    m = LINK_RE.search(value)
    if m:
        return m.group(2).strip()
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return value


def extract_table_block(text: str) -> str:
    lines: list[str] = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| | |"):
            in_table = True
        if in_table:
            if not line.startswith("|"):
                break
            lines.append(line)
    if not lines:
        raise ValueError("no metadata table found (| **Key** | value |)")
    return "\n".join(lines)


def body_from_summary(text: str) -> str:
    idx = text.find("## Summary")
    if idx < 0:
        raise ValueError("missing ## Summary section")
    return text[idx:].lstrip("\n")


def format_app_page(name: str, table_block: str, body: str) -> str:
    return f"# {name}\n\n{BACK_LINK}\n\n{table_block}\n\n{body.rstrip()}\n"


def sync_app_page(path: Path, name: str, table_block: str, body: str) -> None:
    path.write_text(format_app_page(name, table_block, body), encoding="utf-8")


def parse_metadata_table(text: str) -> dict[str, str]:
    """First two-column | **Key** | value | table in the file."""
    rows: dict[str, str] = {}
    in_table = False
    for line in text.splitlines():
        if not line.startswith("|"):
            if in_table and rows:
                break
            continue
        if re.match(r"^\|\s*[-:]+\s*\|", line):
            in_table = True
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        in_table = True
        key = m.group(1).strip().lower()
        rows[key] = strip_cell(m.group(2))
    if not rows:
        raise ValueError("no metadata table found (| **Key** | value |)")
    return rows


def listing_meta(path: Path, rows: dict[str, str]) -> dict:
    def need(key: str) -> str:
        if key not in rows or not rows[key]:
            raise ValueError(f"missing table row **{key.title()}**")
        return rows[key]

    category = need("category")
    icon = extract_url(need("icon"))
    name = rows.get("name") or path.stem
    repo = extract_url(need("repo"))
    description = need("description")
    return {
        "category": category,
        "icon": icon,
        "name": name,
        "repo": repo,
        "description": description,
    }


def table_row(meta: dict, slug: str) -> str:
    details = f"{DETAILS_BADGE}(apps/{slug}.md)"
    return (
        f'| <img src="{meta["icon"]}" width="32" height="32" alt=""> '
        f'| [**{meta["name"]}**]({meta["repo"]}) | {meta["description"]} | {details} |'
    )


def load_categories() -> list[dict]:
    return json.loads(CATEGORIES.read_text(encoding="utf-8"))["categories"]


def build_apps_section(apps: list[tuple[str, dict]]) -> str:
    by_cat: dict[str, list[tuple[str, dict]]] = {}
    for slug, meta in apps:
        by_cat.setdefault(meta["category"], []).append((slug, meta))

    sections: list[str] = ["## Apps", ""]
    for cat in load_categories():
        cat_id = cat["id"]
        entries = by_cat.get(cat_id, [])
        if not entries:
            continue
        entries.sort(key=lambda x: x[1]["name"].casefold())
        title = cat["title"]
        subtitle = cat.get("subtitle", "")
        heading = f"### {title} {subtitle}".rstrip()
        sections.append(heading)
        sections.append("")
        sections.append("| | Name | Description | |")
        sections.append("|:---:|:---|:---|:---:|")
        for slug, meta in entries:
            sections.append(table_row(meta, slug))
        sections.append("")

    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    cat_ids = {c["id"] for c in load_categories()}
    app_files = sorted(p for p in APPS_DIR.glob("*.md") if p.name != "_template.md")
    apps: list[tuple[str, dict]] = []

    for path in app_files:
        slug = path.stem
        text = path.read_text(encoding="utf-8")
        try:
            rows = parse_metadata_table(text)
            meta = listing_meta(path, rows)
        except ValueError as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            return 1
        if meta["category"] not in cat_ids:
            print(f"{path}: unknown category '{meta['category']}'", file=sys.stderr)
            return 1
        table_block = extract_table_block(text)
        body = body_from_summary(text)
        sync_app_page(path, meta["name"], table_block, body)
        apps.append((slug, meta))

    intro = INTRO.read_text(encoding="utf-8").rstrip() + "\n\n"
    readme = intro + build_apps_section(apps) + FOOTER.read_text(encoding="utf-8")
    README.write_text(readme, encoding="utf-8")
    print(f"Wrote {README} ({len(apps)} apps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
