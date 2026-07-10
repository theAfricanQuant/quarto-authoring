#!/usr/bin/env python3
"""Scaffold a Quarto + Typst branded report project.

Usage:
    uv run python scripts/scaffold.py <folder> [--title TITLE] [--date DATE]
"""
import argparse
import sys
from pathlib import Path

REPORT_QMD = """---
title: {title}
date: {date}
date-format: "MMMM YYYY"
format:
  typst:
    template-partials:
      - typst-show.typ
      - typst-template.typ
---

## Overview

Write the report content here.
"""

TYPST_SHOW = """#show: body => report(
  title: [$title$],
  date: [$date$],
  body,
)
"""

TYPST_TEMPLATE = """#let blueline() = {
  line(length: 100%, stroke: 2pt + rgb("#68ACE5"))
}

#let source_text(source_info) = {
  align(right)[
    #text(source_info, font: "Bitter", size: 9pt, style: "italic")
  ]
}

#let status-box(top-box-text: "", bottom-box-text: "") = {
  let top_box = box(width: 2in, height: 0.7in, fill: rgb("#002D72"), inset: 6pt,
    align(center + horizon)[#text(fill: white, weight: "bold", size: 9pt)[#top-box-text]])
  let bottom_box = box(width: 2in, height: 0.7in, fill: white, inset: 6pt,
    align(center + horizon)[#text(fill: black, size: 14pt)[#bottom-box-text]])
  stack(top_box, bottom_box, spacing: 0pt)
}

#let report(
  title: none,
  date: none,
  content,
) = {
  set page(
    paper: "us-letter",
    margin: (top: 0.5in, bottom: 1in, x: 0.75in),
  )
  set text(font: "Lato", size: 11pt)
  content
}
"""

BRAND_YML = """color:
  primary: "#002D72"
  secondary: "#68ACE5"
"""

PYPROJECT_TOML = """[project]
name = "{name}"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
"""

FILES = {
    "report.qmd": REPORT_QMD,
    "typst-show.typ": TYPST_SHOW,
    "typst-template.typ": TYPST_TEMPLATE,
    "_brand.yml": BRAND_YML,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Target project folder (created if missing)")
    parser.add_argument("--title", default="Report Title")
    parser.add_argument("--date", default="")
    args = parser.parse_args()

    root = Path(args.folder)
    (root / "images").mkdir(parents=True, exist_ok=True)

    for filename, template in FILES.items():
        path = root / filename
        if path.exists():
            print(f"[skip] {path} already exists")
            continue
        if filename == "report.qmd":
            content = template.format(title=args.title, date=args.date or "today")
        else:
            content = template
        path.write_text(content, encoding="utf-8")
        print(f"[create] {path}")

    pyproject_path = root / "pyproject.toml"
    if not pyproject_path.exists():
        pyproject_path.write_text(
            PYPROJECT_TOML.format(name=root.name or "report"), encoding="utf-8"
        )
        print(f"[create] {pyproject_path}")

    print(f"\nScaffold ready at {root}/. Next: uv run python scripts/validate.py {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
