# quarto-authoring

Comprehensive Quarto skill — documents, books, Typst/WeasyPrint PDFs, custom templates, and presentations.

## What's inside

- **QMD Essentials** — markdown, cross-refs, callouts, figures, tables, citations, code cells, divs/spans
- **Books** — chapters, parts, appendices, numbering, execution (freeze/cache), navbar, sidebar, listings, social metadata
- **Typst PDFs** — page layout, fonts, TOC, syntax highlighting, typst-show.typ templates, Pandoc escaping, orange-book, premade templates, brand.yml
- **WeasyPrint PDFs** — standalone HTML+CSS, Bootstrap workaround, dark theme support
- **Presentations** — revealjs, pptx, beamer
- **Migration** — from R Markdown, bookdown, xaringan, distill, blogdown, Jupyter

## Install

### As an OpenCode skill

```bash
git clone git@github.com:theAfricanQuant/quarto-authoring.git \
  ~/.config/opencode/skills/quarto-authoring
```

The skill auto-loads when you ask about Quarto, Typst PDFs, books, or colorful PDFs.

### As a Quarto extension (for `typst-show.typ` templates)

```bash
quarto add theAfricanQuant/quarto-authoring
```

Then in your `.qmd`:

```yaml
format:
  quarto-authoring-typst: default
```

## File structure

```
SKILL.md              # Main skill instructions (945 lines)
references/           # 21 detailed reference files
examples/             # Demo QMD, standalone HTML, CSS
scripts/              # Render-demo.sh runner
typst-template/       # typst-show.typ for Typst custom templates
```
