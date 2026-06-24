---
name: quarto-authoring
description: Comprehensive Quarto skill covering authoring (QMD syntax, cross-refs, callouts, figures, tables, citations, code cells, divs/spans), books (chapters, parts, appendices, numbering, execution, navbar, sidebar, listings, social metadata), PDF output via Typst (page layout, fonts, typst-show.typ templates, pandoc escaping, orange-book, premade templates, brand.yml), and PDF output via WeasyPrint (standalone HTML+CSS, Bootstrap workaround). Also covers presentations, project setup, and migration from R Markdown/bookdown. Use for any Quarto question.
metadata:
  author: SisengAI (merged from quarto-authoring, quarto-book-structure, colorful-pdf)
  version: "2.0"
---
# Quarto Authoring

Comprehensive reference for Quarto — documents, books, PDFs, and presentations.

---

## 1. QMD Essentials

### Basic Document Structure

```yaml
---
title: "Document Title"
author: "Author Name"
date: today
format: html
---
```

### Divs and Spans

Divs use fenced colons, spans use brackets:
```markdown
::: {.class-name}
Content inside the div.
:::

[important text]{.highlight}
```

Details: [references/divs-and-spans.md](references/divs-and-spans.md)

### Code Cells

Options use the language's comment symbol + `|`. Use **dashes, not dots**:
- R, Python, Julia: `#|`
- Mermaid: `%%|`
- Graphviz/DOT: `//|`

````markdown
```{language}
#| label: fig-example
#| echo: false
#| fig-cap: "A scatter plot."
```
````

Set document-level defaults:
```yaml
execute:
  echo: false
  warning: false
```

**Caching:** `#| cache: true` only works for R (knitr). For Python/Jupyter, use `execute: cache: true` in top-level YAML + `pip install jupyter-cache`.

Details: [references/code-cells.md](references/code-cells.md)

### Cross-References

Labels must start with a type prefix. Reference with `@`:
- Figure: `fig-` → `@fig-plot`
- Table: `tbl-` → `@tbl-data`
- Section: `sec-` → `@sec-intro`
- Equation: `eq-` → `@eq-model`

```markdown
# Introduction {#sec-intro}
See @sec-intro for background.
See @fig-plot for the results.
```

Details: [references/cross-references.md](references/cross-references.md)

### Callout Blocks

Five types: `note`, `warning`, `important`, `tip`, `caution`:
```markdown
::: {.callout-note}
This is a note.
:::

::: {.callout-warning}
## Custom Title
Warning with custom title.
:::
```

Details: [references/callouts.md](references/callouts.md)

### Figures

```markdown
![Caption text](image.png){#fig-name fig-alt="Alt text"}
```

Subfigures:
```markdown
::: {#fig-group layout-ncol=2}
![Sub 1](img1.png){#fig-sub1}
![Sub 2](img2.png){#fig-sub2}
Main caption.
:::
```

Details: [references/figures.md](references/figures.md)

### Tables

```markdown
::: {#tbl-example}
| Col 1 | Col 2 |
|-------|-------|
| Data  | Data  |
Table caption.
:::
```

Details: [references/tables.md](references/tables.md)

### Citations

```markdown
According to @smith2020...
Multiple citations [@smith2020; @jones2021].
```

```yaml
bibliography: references.bib
csl: apa.csl
```

Details: [references/citations.md](references/citations.md)

### Conditional Content & Shortcodes

Details: [references/conditional-content.md](references/conditional-content.md), [references/shortcodes.md](references/shortcodes.md)

### Diagrams (Mermaid, Graphviz)

Details: [references/diagrams.md](references/diagrams.md)

### Compute Engines

Details: [references/engines.md](references/engines.md)

### Page Layout

Details: [references/layout.md](references/layout.md)

### Extensions

Details: [references/extensions.md](references/extensions.md)

### YAML Front Matter

Details: [references/yaml-front-matter.md](references/yaml-front-matter.md)

### Markdown Linting

Details: [references/markdown-linting.md](references/markdown-linting.md)

---

## 2. Projects

### Website Project

```yaml
# _quarto.yml
project:
  type: website

website:
  title: "My Site"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - href: about.qmd
        text: About

format:
  html:
    theme: cosmo
```

---

## 3. Books

### Basic Book Structure

```yaml
# _quarto.yml
project:
  type: book

book:
  title: "mybook"
  author: "Jane Doe"
  chapters:
    - index.qmd       # Required — homepage in HTML output
    - intro.qmd
    - summary.qmd
    - references.qmd  # Auto-generated bibliography
```

**Key rules:**
- `index.qmd` is required
- `references.qmd` holds the generated bibliography
- Top-level rendering options go at root of `_quarto.yml`
- Format-specific options under `format:`

### Titles and Chapter Numbers

```markdown
# Preface {.unnumbered}
```

Numbering depth (format option):
```yaml
number-depth: 1
```

`toc-depth` is independent of `number-depth`.

### References / Bibliography

Place a `#refs` div where the bibliography should appear:
```markdown
# References {.unnumbered}
::: {#refs}
:::
```

### Parts & Appendices

**Parts with content files:**
```yaml
book:
  chapters:
    - index.qmd
    - part: dice.qmd       # part intro file
      chapters:
        - basics.qmd
        - packages.qmd
    - part: "Dice"          # title-only (no intro file)
      chapters:
        - objects.qmd
```

**Appendices:**
```yaml
book:
  chapters:
    - index.qmd
  appendices:
    - tools.qmd
    - resources.qmd
```

Appendices are uppercase alpha. Customize:
```yaml
crossref:
  appendix-title: "App."
  appendix-delim: ":"
```

### Cross-References (Books)

Cross-references work across chapters:
```markdown
See @fig-penguins for details.
See @sec-introduction for background.
```

Label must start with `sec-` for chapter/section refs. Suppress prefix: `[-@sec-intro]`. Custom prefix: `[Chapter @sec-vis]`.

Chapter-level figure numbering is automatic.

### Hyperlinks Within a Book

Use source `.qmd` filename as link target:
```markdown
[about](about.qmd)
[section](about.qmd#section)
```

For print output, use cross-references instead of hyperlinks.

### Managing Execution

**Incremental render:** `quarto render intro.qmd` or `quarto render subdir/`

**Freeze** (prevent re-execution on global renders):
```yaml
execute:
  freeze: true    # never re-render
  freeze: auto    # re-render only when source changes
```

Freeze results stored in `_freeze/` — check into version control.

**Cache:**
```yaml
execute:
  cache: true
```
Refresh: `quarto render --cache-refresh`

**Notebooks (.ipynb):** cells not executed by default. To execute: `quarto render notebook.ipynb --execute` or `execute: enabled: true`.

**Working directory:**
```yaml
project:
  execute-dir: project   # use project root
```

### Page Navigation & Footer

```yaml
book:
  page-navigation: true
  page-footer: "Copyright 2021"
```

Targeted footer:
```yaml
book:
  page-footer:
    left: "Copyright 2021"
    right:
      - icon: github
        href: https://github.com/
```

### Typst Books (orange-book)

Quarto 1.9.17+ bundles `orange-book` as the default for book projects:
```yaml
project:
  type: book
book:
  title: "My Book"
  chapters: [index.qmd, intro.qmd, summary.qmd]
format: typst
```

Features: chapter numbering, decorative headers, parts/appendices, styled TOC, `_brand.yml` integration.

Explicit format:
```bash
quarto add quarto-ext/orange-book
```
```yaml
format: orange-book-typst
```

### Typst Books (bookly)

Third-party extension with 6 visual themes, LOF/LOT, and Tufte layout:
```bash
quarto add maucejo/quarto-bookly
```
```yaml
project:
  type: book
book:
  title: "My Book"
  chapters: [index.qmd, chapters/intro.qmd]
  appendices: [appendices/appendixA.qmd]
format:
  bookly-typst:
    theme: modern           # classic, modern, fancy, obook, orly, pretty
    toc: true
    lof: true               # list of figures
    lot: true               # list of tables
    tufte: false            # Tufte-style margin notes
    part-numbering: "1"     # "A", "I", etc.
    colors:
      primary: rgb("#2563EB")
    fonts:
      body: "Lato"
```
Maps callouts to bookly info boxes. Requires Quarto >= 1.9.17.

### Multi-Chapter Typst ({{< include >}})

Without a book project, use a master `.qmd`:
```markdown
---
title: "My Document"
format:
  typst:
    template-partials:
      - typst-show.typ
---

# Chapter One
{{< include 01-chapter.qmd >}}

# Chapter Two
{{< include 02-chapter.qmd >}}
```

Real-world example: [christopherkenny/harvard-diss](https://github.com/christopherkenny/harvard-diss) — open-source Harvard dissertation using Typst + Quarto.

### Navbar Options

```yaml
book:
  navbar:
    title: "Title"
    logo: logo.png
    background: "#fff"
    pinned: true
    search: true
    left: [{text: "Home", href: index.qmd}]
    right: [{icon: github, href: "https://github.com/"}]
```

### Sidebar Options

```yaml
book:
  sidebar:
    style: docked         # or floating
    background: light
    search: true
    collapse-level: 2
    logo: false           # disable brand logo
```

### Search

```yaml
book:
  search:
    location: navbar      # or sidebar
    type: overlay         # or textbox
```

Algolia:
```yaml
search:
  algolia:
    index-name: <index>
    application-id: <id>
    search-only-api-key: <key>
```

### Social Metadata

**Twitter card:**
```yaml
book:
  twitter-card:
    site: "@handle"
    title: "..."
    description: "..."
    image: path/to/image.png
    card-style: summary_large_image
```

**Open Graph:**
```yaml
book:
  open-graph:
    title: "OG Title"
    description: "..."
    image: path/to/image.png
    locale: en_US
```

### Comments

Hypothesis, Utterances, or Giscus:
```yaml
book:
  comments:
    hypothesis: true
    # or:
    giscus:
      repo: owner/repo
      mapping: pathname
```

### Listings

Auto-generate content:
```yaml
---
title: "Listing"
listing:
  contents: posts
  type: grid
  grid-columns: 2
---
```

Types: `default`, `table`, `grid`, `custom`. Options: `sort`, `max-items`, `page-size`, `categories`, `feed` (RSS).

### Book Options Reference

| Option | Description |
|--------|-------------|
| `title`, `subtitle`, `author`, `date` | Book metadata |
| `cover-image` | Cover image (HTML + ePub) |
| `sharing` | `twitter`, `facebook`, `linkedin` |
| `downloads` | `pdf`, `epub`, `docx` |
| `doi` | Digital Object Identifier |
| `favicon`, `site-url` | Site identity |
| `repo-url`, `repo-actions` | Source repository links (`edit`, `source`, `issue`) |
| `output-file` | Output filename (no extension) |

---

## 4. PDF Output — WeasyPrint (HTML+CSS)

For visually rich, colorful PDFs. Zero LaTeX.

### Prerequisites

```bash
uv tool install weasyprint
```

### Critical: Quarto's Bootstrap overrides dark themes

Quarto HTML always sets `body { background-color: #fff }` even with `theme: none` or `minimal: true`. For dark/styled PDFs use a **standalone HTML file** with embedded CSS — bypass Quarto's HTML output entirely.

### Workflow

```bash
weasyprint standalone.html output.pdf
```

### CSS tips

- `@page { size: A4; margin: 2cm; }` for page control
- `@page { @bottom-center { content: counter(page); } }` for page numbers
- Gradients, `border-radius`, `box-shadow`, `background-image` all work
- `page-break-after/before: always` for page control
- `min-height: 297mm` (A4 height) for full-page sections
- `-webkit-print-color-adjust: exact; print-color-adjust: exact;` for reliable color

### Quarto + WeasyPrint hack (keeps .qmd)

```bash
quarto render doc.qmd --to html
sed -i 's/background-color:#fff/background-color:#050D1A/g' doc.html
weasyprint doc.html output.pdf
```

---

## 5. PDF Output — Typst

Zero LaTeX. Blazing fast. Quarto >=1.5 includes the Typst CLI.

### Quick start

```yaml
---
title: "My Document"
format: typst
---
```

```bash
quarto render doc.qmd --to typst
```

### Page layout

```yaml
format:
  typst:
    papersize: a4
    margin:
      x: 2.5cm
      y: 2cm
    columns: 1
    page-numbering: false
```

Article layout (Tufte-style): `grid: { margin-width: 2in, body-width: 4in, gutter-width: 0.25in }`

### Table of contents

```yaml
format:
  typst:
    toc: true
    toc-depth: 3
    toc-title: "Contents"
    toc-indent: 1.5em
```

Exclude: `### Heading {.unnumbered .unlisted}`

### Section numbering

```yaml
number-sections: true       # OFF by default
number-depth: 3
section-numbering: 1.A.a
```

Exclude: `### Heading {.unnumbered}`

### Fonts

```yaml
format:
  typst:
    mainfont: "Inter"
    fontsize: "11pt"
    font-paths: ["fonts/"]
```

### Syntax highlighting

```yaml
format:
  typst:
    syntax-highlighting: arrow   # default
    # 20+ themes: pygments, tango, monokai, nord, github, dracula...
    # Special: none, idiomatic (Typst native)
```

### Typst CSS — inline styles

Quarto 1.5+ translates CSS → Typst:
```markdown
[amber text]{style="color: #D4720A"}
[blue bg]{style="background-color: #2563EB; color: white; padding: 4pt"}
```

### Typst blocks

```markdown
::: {.block fill="luma(230)" inset="8pt" radius="4pt"}
Gray rounded box.
:::
```

Any `#block()` arg: `fill`, `stroke`, `inset`, `radius`, `width`, `height`.

### Theorems

```yaml
format:
  typst:
    theorem-appearance: fancy   # colored boxes, brand colors
    # Options: simple, fancy, clouds, rainbow
```

### Raw Typst

````markdown
```{=typst}
#set par(justify: true)
#block(fill: rgb("#050D1A"), inset: 10pt)[Dark block]
```
````

### PDF accessibility

```yaml
format:
  typst:
    pdf-standard: ua-1
    pdf-standard: [a-2b, ua-1]
```

Validate: `quarto install verapdf`

### Includes & keep-typ

```yaml
format:
  typst:
    keep-typ: true
    include-before-body:
      text: |
        #show heading: set text(fill: rgb("#E8B949"))
```

---

## 6. Custom Typst Templates

### Quick: template-partials (one file)

Create `typst-show.typ` alongside `.qmd`:

```typst
#let navy = rgb("#050D1A")
#let gold = rgb("#E8B949")

#show: doc => {
  set page(fill: navy, margin: (top: 2cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
    footer: [Your footer],
  )
  set text(font: "Inter", size: 10pt, fill: rgb("#9DB0CF"))

  show heading.where(level: 1): it => {
    pagebreak()
    v(0.8cm)
    set text(size: 28pt, weight: "black", fill: gold)
    it
  }
  show strong: it => text(weight: "semibold", fill: rgb("#EDF2FA"), it)
  show table: it => {
    show table.cell.where(y: 0): cell => {
      set text(fill: gold, weight: "semibold")
      cell
    }
    it
  }
  doc
}
```

```yaml
format:
  typst:
    template-partials:
      - typst-show.typ
```

### Pandoc escaping gotchas

**`$` signs:** Pandoc strips `\$` in `typst-show.typ`. Use `#let d = sym.dollar` then `["He turned #d 5,000"]`.

**Variable escaping:** Use `[$variable$]` (content blocks) instead of `"$variable$"` (strings).

**`to-string()` helper:**
```typst
#let to-string(content) = {
  if content.has("text") { content.text }
  else if content.has("children") { content.children.map(to-string).join("") }
  else if content.has("body") { to-string(content.body) }
  else if content == [ ] { " " }
}
```

### Full: custom format extension

```bash
quarto create extension format   # pick typst, name it
```

Generates: `_extension.yml`, `typst-template.typ`, `typst-show.typ`, `template.qmd`.

### Template patterns & tips

**Parameterized reports:** Pass Quarto `params` to Typst via the show file:
```yaml
# QMD frontmatter:
params:
  species: "Penguin"
```
```typst
// typst-show.typ:
#show: article.with(
  species: "$params.species$",
)
```
```typst
// typst-template.typ uses `species` as a variable throughout.
```
Useful for batch-rendering per-state/product/category reports.

**Colored sidebar:** Add a persistent colored strip to every page via `set page(background: place(top, rect(width: 2cm, height: 100%, fill: ...)))`.

**Heading level shift:** Quarto shifts Typst headings up one level on render. A QMD `# Heading` becomes Typst level 2. Design show rules accordingly (target `where(level: 2)` for QMD-level-1 headings).

**Custom functions** (callable from both template and `{=typst}` chunks):
```typst
#let blueline() = { line(length: 100%, stroke: 2pt + rgb("#68ACE5")) }
#let source_text(src) = { align(right, text(src, font: "Bitter", size: 9pt, style: "italic")) }
```

**Date formatting:**
```yaml
date: September 2025
date-format: "MMMM YYYY"   # "September 2025" instead of "2025-09-01"
```

**Columns via layout-ncol** (works in Typst output):
```markdown
:::{layout-ncol=2}
![Image 1](img1.svg)
![Image 2](img2.svg)
:::
```

**HTML divs for backgrounds** (Quarto translates CSS → Typst):
```html
<div style="background-color: #F8F8F8;">
Content with gray background.
</div>
```

**`#` hash rule:** Inside brackets `[...]`, use `#` before function calls. In `{=typst}` chunks, also use `#`. Example: `#blueline()`, `#text(fill: white)[Title]`.

**Tools:** [Typst LSP](https://open-vsx.org/extension/nvarner/typst-lsp) (tooltips/autocomplete), [Tinymist](https://open-vsx.org/extension/myriad-dreamin/tinymist) (formatter), both for Positron/VS Code.

### Premade Typst templates

| Typst template | Quarto wrapper | Use |
|---|---|---|
| `charged-ieee` | `quarto-ext/typst-templates/ieee` | IEEE papers |
| `unequivocal-ams` | `quarto-ext/typst-templates/ams` | AMS math papers |
| `appreciated-letter` | `quarto-ext/typst-templates/letter` | Formal letters |
| `dashing-dept-news` | `quarto-ext/typst-templates/dept-news` | Newsletters |
| `wonderous-book` | `quarto-ext/typst-templates/fiction` | Fiction books |
| `typst-poster` | `quarto-ext/typst-templates/poster` | Academic posters |
| `orange-book` | Bundled (book projects) | Technical books |
| `cereal-words` | *no wrapper* | Resume/CV |
| `bare-bones-cv` | *no wrapper* | Minimal single-page CV |
| `imprecv` | *no wrapper* | YAML-driven CV (easy version control) |
| `icicle`, `badformer` | *no wrapper* | Presentation slides |
| `typst-invoice` | *no wrapper* | Invoice generator (TOML→PDF) |
| `typst-palettes` | *no wrapper* | Color palette library |

Install: `quarto use template quarto-ext/typst-templates/<name>`. Full list: [github.com/typst/templates](https://github.com/typst/templates).

Usage examples — IEEE:
```yaml
---
title: "Paper Title"
authors:
  - name: Author Name
    email: "email@example.com"
    affiliations:
      - name: University
        city: City
        country: Country
abstract: |
  Abstract content...
format:
  ieee-typst: default
bibliography: refs.bib
---
```

AMS:
```yaml
---
title: "Mathematical Theorems"
authors:
  - name: Author
    affiliations:
      - name: University
        department: Mathematics
format: ams-typst: default
bibliography: refs.bib
---
```

Letter:
```yaml
---
subject: "Subject"
name: "Sender Name"
sender: "Sender Address"
recipient: |
  Recipient Name \\
  Address
sent: "City, Date"
format: letter-typst: default
---
```

Fiction:
```yaml
---
title: "Book Title"
author: Author Name
dedication: "for Someone"
publishing-info: "Publisher Info"
format: fiction-typst: default
---
```

Poster:
```yaml
---
title: "Academic Poster"
format:
  poster-typst:
    size: "36x24"
    poster-authors: "A. Smith, B. Jones"
    departments: "Department Name"
    institution-logo: "./images/logo.png"
    footer-text: "Conference 2026"
    keywords: ["Typst", "Quarto"]
---
```

### Bundling Typst packages

```bash
quarto call typst-gather          # auto-detect from _extension.yml
quarto call typst-gather --init-config
```

Downloads `@preview` packages into `typst/packages/` for offline use.

---

## 7. _brand.yml Integration

```yaml
color:
  primary: "#D4720A"
  secondary: "#321208"
logo:
  images:
    site-logo:
      path: logo.svg
  medium: site-logo
```

Typst templates read via `brand-color.primary`, `brand-color.secondary`. `fancy` theorem appearance and `orange-book` respect brand colors automatically.

---

## 8. Presentations

Formats: `revealjs` (HTML), `pptx` (PowerPoint), `beamer` (LaTeX/PDF).

```yaml
---
title: "Habits"
author: "John Doe"
format: revealjs
---
```

```markdown
## Getting up
- Turn off alarm
- Get out of bed

## Going to sleep
- Get in bed
- Count sheep
```

Level-1 headings create section title slides. Horizontal rules (`---`) create slides without titles.

---

## 9. WeasyPrint vs Typst

|                | WeasyPrint              | Typst                  |
| -------------- | ----------------------- | ---------------------- |
| Color power    | Full CSS                | Good (fills, borders)  |
| Page layout    | CSS @page               | `papersize`, `margin`  |
| Page numbers   | CSS counters             | `page-numbering`       |
| TOC            | Manual CSS              | `toc: true`            |
| Cross-refs     | Manual                  | Native `@sec-/@fig-`   |
| Templates      | HTML+CSS                | `typst-show.typ`       |
| Bootstrap issue| Must use standalone HTML| None                   |
| Accessibility  | Manual                  | `pdf-standard: ua-1`   |

**Rule:** Typst for structure (TOC, cross-refs). WeasyPrint for visual design (gradients, dark themes).

---

## 10. LaTeX Parity — Typst Workarounds

| Feature       | Typst equivalent                                 |
| ------------- | ------------------------------------------------ |
| `linestretch` | `set par(leading: linestretch * 0.65em)`         |
| `mathfont`    | `#show math.equation: set text(font: mathfont)`  |
| `codefont`    | `#show raw: set text(font: codefont)`            |
| `linkcolor`   | `#show link: set text(fill: rgb(linkcolor))`     |
| `citecolor`   | `#show ref: set text(fill: rgb(citecolor))`      |
| `thanks`      | `footnote(thanks, numbering: "*")` on title      |

---

## 11. Migration

Only when converting existing projects. Do NOT read for new Quarto documents:
- R Markdown → [references/conversion-rmarkdown.md](references/conversion-rmarkdown.md)
- bookdown → [references/conversion-bookdown.md](references/conversion-bookdown.md)
- xaringan → [references/conversion-xaringan.md](references/conversion-xaringan.md)
- distill → [references/conversion-distill.md](references/conversion-distill.md)
- blogdown → [references/conversion-blogdown.md](references/conversion-blogdown.md)
- Jupyter → [references/conversion-jupyter.md](references/conversion-jupyter.md)

---

## 12. Reference Links

**Quarto docs:**
- [Quarto Documentation](https://quarto.org/docs/)
- [Quarto Extensions](https://quarto.org/docs/extensions/)
- [Community Extensions](https://m.canouil.dev/quarto-extensions/)
- [Typst Basics](https://quarto.org/docs/output-formats/typst.html)
- [Custom Typst Formats](https://quarto.org/docs/output-formats/typst-custom.html)
- [Book Output (Typst)](https://quarto.org/docs/books/book-output.html#typst-output)
- [Article Layout](https://quarto.org/docs/authoring/article-layout.html)
- [Typst format reference](https://quarto.org/docs/reference/formats/typst.html)
- [Typst Gather](https://quarto.org/docs/advanced/typst/typst-gather.html)

**Typst resources:**
- [Typst Reference](https://typst.app/docs/reference/)
- [Making a Template](https://typst.app/docs/tutorial/making-a-template/)
- [Typst Universe (packages)](https://typst.app/universe/)
- [Typst Forum](https://forum.typst.app/)
- [Official Typst templates](https://github.com/typst/templates)
- [Awesome Typst](https://github.com/qjcg/awesome-typst) — curated directory of 300+ tools, templates, and libraries
- Python bindings: [typst-py](https://github.com/messense/typst-py) (compile .typ from Python), [pypst](https://github.com/tilman151/pypst) (declarative Typst in Python), [mpl-typst](https://github.com/daskol/mpl-typst) (Matplotlib→Typst backend)
- Formatter: [typstyle](https://github.com/typstyle-rs/typstyle) — opinionated Typst code formatter

**Discussions & examples:**
- [Typst template parity #10223](https://github.com/orgs/quarto-dev/discussions/10223)
- [Typst book support #6979](https://github.com/orgs/quarto-dev/discussions/6979)
- [Harvard dissertation (Typst+Quarto)](https://github.com/christopherkenny/harvard-diss)
- [State immunization reports](https://github.com/claritydatastudio/state-immunization-reports) — production Typst template with custom functions (`#source()`, `#blueline()`, `#status-boxes()`), R-based but Typst patterns are language-agnostic
