#!/usr/bin/env python3
"""Print reusable Typst/Quarto snippets for branded reports.

Usage:
    uv run python scripts/snippets.py [name]
    uv run python scripts/snippets.py           # lists all snippet names
"""
import sys

SNIPPETS = {
    "blueline": """#let blueline() = {
  line(length: 100%, stroke: 2pt + rgb("#68ACE5"))
}""",
    "source_text": """#let source_text(source_info) = {
  align(right)[
    #text(source_info, font: "Bitter", size: 9pt, style: "italic")
  ]
}""",
    "status-box": """#let status-box(top-box-text: "", bottom-box-text: "") = {
  let top_box = box(width: 2in, height: 0.7in, fill: rgb("#002D72"), inset: 6pt,
    align(center + horizon)[#text(fill: white, weight: "bold", size: 9pt)[#top-box-text]])
  let bottom_box = box(width: 2in, height: 0.7in, fill: white, inset: 6pt,
    align(center + horizon)[#text(fill: black, size: 14pt)[#bottom-box-text]])
  stack(top_box, bottom_box, spacing: 0pt)
}""",
    "two-column-figures": """:::{layout-ncol=2}
![](chart-a.svg)

![](chart-b.svg)
:::""",
    "gray-section": """<div style="background-color: #F8F8F8;">

### Section title

Content here.

</div>""",
}


def main() -> int:
    if len(sys.argv) == 1:
        print("Available snippets:")
        for name in SNIPPETS:
            print(f"  - {name}")
        return 0

    name = sys.argv[1]
    snippet = SNIPPETS.get(name)
    if snippet is None:
        print(
            f"Unknown snippet '{name}'. Run without arguments to list available names.",
            file=sys.stderr,
        )
        return 1

    print(snippet)
    return 0


if __name__ == "__main__":
    sys.exit(main())
