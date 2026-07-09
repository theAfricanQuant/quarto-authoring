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

### With npx (recommended)

```bash
npx quarto-authoring-skill              # Claude Code, user-wide (~/.claude/skills/)
npx quarto-authoring-skill --project    # current project (./.claude/skills/)
npx quarto-authoring-skill --opencode   # OpenCode (~/.config/opencode/skills/)
npx quarto-authoring-skill --all        # Claude Code + OpenCode
npx quarto-authoring-skill --dir <path> # anywhere else
```

Straight from GitHub (no npm registry needed):

```bash
npx github:theAfricanQuant/quarto-authoring
```

Re-run the same command any time to update. The skill auto-loads when you ask about Quarto, Typst, websites, blogs, books (PDF/EPUB), CVs, or publishing.

### Manual (git clone)

```bash
git clone git@github.com:theAfricanQuant/quarto-authoring.git \
  ~/.config/opencode/skills/quarto-authoring
```

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
