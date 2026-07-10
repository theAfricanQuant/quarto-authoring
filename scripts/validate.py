#!/usr/bin/env python3
"""Validate a Quarto + Typst report scaffold before rendering.

Usage:
    uv run python scripts/validate.py <folder>
"""
import re
import sys
from pathlib import Path

REQUIRED_FILES = ["report.qmd", "typst-show.typ", "typst-template.typ"]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate.py <folder>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    problems = []

    for filename in REQUIRED_FILES:
        if not (root / filename).exists():
            problems.append(f"missing {filename}")

    qmd_path = root / "report.qmd"
    if qmd_path.exists():
        text = qmd_path.read_text(encoding="utf-8")
        if "template-partials" not in text:
            problems.append(
                "report.qmd YAML is missing 'template-partials' — the custom template won't apply"
            )
        if "typst-show.typ" not in text:
            problems.append("report.qmd doesn't list typst-show.typ under template-partials")
        if re.search(r"format:\s*pdf\b", text):
            problems.append("format: pdf found — use 'format: typst' for a Typst-rendered report")

    show_path = root / "typst-show.typ"
    if show_path.exists() and "report(" not in show_path.read_text(encoding="utf-8"):
        problems.append(
            "typst-show.typ doesn't call a template function — check it bridges into typst-template.typ"
        )

    if not (root / "_brand.yml").exists():
        print("[info] no _brand.yml found — brand styling is optional, skip if not needed")

    if problems:
        print(f"[FAIL] {len(problems)} issue(s) found in {root}:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print(f"[OK] {root} looks ready. Render with: quarto render {qmd_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
