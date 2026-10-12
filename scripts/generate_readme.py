#!/usr/bin/env python3
"""Build README.md from listing fields in each apps/*.md metadata table."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "apps"
DATA_DIR = ROOT / "data"
README = ROOT / "README.md"
INTRO = ROOT / "templates" / "readme_intro.md"
FOOTER = ROOT / "templates" / "readme_footer.md"

DETAILS_BADGE = (
    '[![Details](https://img.shields.io/badge/Details-→-555?style=flat)]'
)

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
    sort = int(rows.get("sort") or "100")
    return {
        "category": category,
        "sort": sort,
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


def build_apps_section(apps: list[tuple[str, dict]]) -> str:
    categories = json.loads((DATA_DIR / "categories.json").read_text(encoding="utf-8"))[
        "categories"
    ]
    by_cat: dict[str, list[tuple[int, str, dict]]] = {}
    for slug, meta in apps:
        by_cat.setdefault(meta["category"], []).append((meta["sort"], slug, meta))

    sections: list[str] = ["## Apps", ""]
    for cat in categories:
        cat_id = cat["id"]
        entries = by_cat.get(cat_id, [])
        if not entries:
            continue
        entries.sort(key=lambda x: (x[0], x[1]))
        title = cat["title"]
        subtitle = cat.get("subtitle", "")
        heading = f"### {title} {subtitle}".rstrip()
        sections.append(heading)
        sections.append("")
        sections.append("| | Name | Description | |")
        sections.append("|:---:|:---|:---|:---:|")
        for _, slug, meta in entries:
            sections.append(table_row(meta, slug))
        sections.append("")

    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    cat_ids = {
        c["id"]
        for c in json.loads(
            (DATA_DIR / "categories.json").read_text(encoding="utf-8")
        )["categories"]
    }
    app_files = sorted(
        p for p in APPS_DIR.glob("*.md") if p.name != "_template.md"
    )
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
        apps.append((slug, meta))

    intro = INTRO.read_text(encoding="utf-8").rstrip() + "\n\n"
    readme = intro + build_apps_section(apps) + FOOTER.read_text(encoding="utf-8")
    README.write_text(readme, encoding="utf-8")
    print(f"Wrote {README} ({len(apps)} apps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
