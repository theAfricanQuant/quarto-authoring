# EPUB Output

EPUB for e-readers (Kobo, Apple Books, Kindle via conversion). Books are the main use case, but any document can render to EPUB.

## Quick Start

```yaml
# _quarto.yml (book project)
project:
  type: book

book:
  title: "My Book"
  author: "Jane Doe"
  cover-image: cover.png
  chapters:
    - index.qmd
    - intro.qmd
    - summary.qmd
    - references.qmd

format:
  epub: default
```

```bash
quarto render --to epub        # output in _book/My-Book.epub
```

Single document: `format: epub` in the front matter, `quarto render doc.qmd --to epub`.

## Multi-Format Books (HTML + PDF + EPUB)

The standard "book in every format" setup — one source, three outputs, download buttons on the site:

```yaml
project:
  type: book

book:
  title: "My Book"
  cover-image: cover.png
  downloads: [pdf, epub]       # download menu in the HTML navbar
  chapters:
    - index.qmd
    - intro.qmd

format:
  html:
    theme: cosmo
  typst: default               # or pdf: (LaTeX)
  epub:
    toc: true
```

```bash
quarto render                  # renders ALL formats
quarto render --to epub        # just one
```

Use [conditional content](conditional-content.md) for format-specific passages:

```markdown
::: {.content-visible when-format="epub"}
E-reader specific note.
:::
```

## EPUB Metadata

EPUB stores require proper metadata:

```yaml
format:
  epub:
    identifier: "urn:isbn:9780123456789"   # ISBN or UUID
    publisher: "Publisher Name"
    rights: "© 2026 Jane Doe. All rights reserved."
    epub-title-page: true
    lang: en
    date: "2026-07-09"
    description: "Back-cover style description"
    subject: "Data Science"
```

Without an `identifier`, Pandoc generates a random UUID per render — set one for stable store submissions.

## Cover Image

```yaml
book:
  cover-image: cover.png
  cover-image-alt: "Alt text for the cover"
```

Recommended: PNG or JPEG, ~1600×2400px (1:1.5 ratio) for store requirements. The cover also appears on the HTML book homepage.

## Styling with CSS

EPUB uses CSS (a restricted subset — e-reader engines vary widely):

```yaml
format:
  epub:
    css: epub.css
```

```css
/* epub.css — keep it conservative */
body { font-family: serif; line-height: 1.5; }
h1 { page-break-before: always; }     /* chapter on new page */
code { font-size: 0.85em; }
img { max-width: 100%; }
```

Rules of thumb:
- Avoid fixed widths, floats, and CSS grid — many readers ignore them.
- Let the reader control fonts where possible; users override them anyway.
- Test dark mode: don't hardcode `color: black`.

## Fonts

Embed fonts (increases file size; many readers override):

```yaml
format:
  epub:
    epub-fonts:
      - fonts/CrimsonPro-Regular.otf
      - fonts/CrimsonPro-Italic.otf
```

Reference them from `epub.css` with `@font-face`.

## Chapter Splitting

```yaml
format:
  epub:
    epub-chapter-level: 1    # split file at H1 (default); 2 splits at H2
```

Large single files can crash weaker e-readers — keep the default unless chapters are tiny.

## Code, Figures, and Math in EPUB

- Code cells render as static highlighted HTML — interactive HTML widgets (plotly, leaflet) do **not** work; provide static fallbacks with `#| fig-format: png` or conditional content.
- Math renders via MathML (`format: epub` default) — good support in Apple Books/Kobo, weaker on older Kindles.
- Prefer PNG/JPEG/SVG figures; keep each under ~1–2 MB.

## Validation

Validate before submitting to any store:

```bash
# install epubcheck (Java): https://github.com/w3c/epubcheck
epubcheck _book/My-Book.epub
```

Common failures: missing alt text, remote images (embed everything locally), invalid identifiers.

## Kindle

Amazon KDP accepts EPUB directly (since 2022 — no need for MOBI). Preview with Kindle Previewer to check formatting on Kindle engines, which are the most restrictive.
