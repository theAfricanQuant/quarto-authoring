# quarto-authoring

Comprehensive Quarto + Typst skill — documents, websites, blogs, books (PDF/EPUB), Typst/WeasyPrint PDFs, custom templates, presentations, and publishing.

## What's inside

- **QMD Essentials** — markdown, cross-refs, callouts, figures, tables, citations, code cells, divs/spans
- **Websites & Blogs** — navigation, themes/SCSS, dark mode, search, listings, categories, RSS, about pages, comments
- **Books** — chapters, parts, appendices, numbering, execution (freeze/cache), navbar, sidebar, social metadata
- **EPUB** — multi-format books (HTML+PDF+EPUB), cover images, store metadata, epubcheck, Kindle
- **Typst PDFs** — page layout, fonts, TOC, syntax highlighting, typst-show.typ templates, Pandoc escaping, orange-book, CV/resume/paper templates, brand.yml
- **WeasyPrint PDFs** — standalone HTML+CSS, Bootstrap workaround, dark theme support
- **Presentations** — revealjs (deep), pptx, beamer, Typst slides
- **Publishing** — quarto publish, GitHub Pages, Netlify, GitHub Actions, freeze CI pattern
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
SKILL.md              # Main skill instructions
references/           # 26 detailed reference files
examples/             # Demo QMD, standalone HTML, CSS
scripts/              # Render-demo.sh runner
```
