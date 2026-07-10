# Manuscripts

Notebook-first scholarly articles: write in Jupyter, VS Code, or RStudio; Quarto produces the article (PDF/Word/journal format) *and* a manuscript website that gives readers the rendered article, the source notebooks, and links to data/code — all from one source.

## Project Setup

```bash
quarto create project manuscript mymanuscript
```

```yaml
# _quarto.yml
project:
  type: manuscript

manuscript:
  article: index.qmd        # the main article source (.qmd or .ipynb)
  notebooks:                 # supplementary/computational notebooks, linked from the article
    - notebook-data-cleaning.ipynb
    - notebook-figures.qmd
```

`project: type: manuscript` is what distinguishes this from a plain `book`/`website` project — it adds the multi-format article pipeline and the notebook-linking behavior on top.

## Authoring Environments

Content is authored as ordinary `.qmd`/`.ipynb` files in whichever tool is comfortable:

- **JupyterLab** — write cells directly in a notebook; Quarto extracts narrative + code for the article.
- **VS Code** — notebook editor or plain `.qmd`, same underlying project.
- **RStudio / Positron** — visual editor works the same as any other Quarto project.

All three produce the same manuscript project structure; pick based on where the actual analysis work already happens rather than switching tools for the writing step.

## Journal / Multi-Format Output

Manuscripts commonly need journal-required output formats (LaTeX-derived PDF templates, MS Word) in addition to HTML:

```yaml
format:
  html: default
  docx: default          # journal submission often requires Word
  jats: default           # JATS XML, common publisher ingestion format
```

Community journal templates (AGU, Elsevier, and others) install like any Quarto extension:

```bash
quarto add quarto-journals/agu
```

## Components: Notebooks Inside the Article

Individual notebooks referenced under `manuscript: notebooks:` get their own standalone HTML view (so a reader can open just the data-cleaning notebook) while also contributing cells/figures back into the main article via normal `{{< embed >}}`-style inclusion. This is the mechanism that keeps "the code that produced Figure 3" one click away from Figure 3 itself, without duplicating the code into the article source.

## Publishing

- **Manuscript website** — publishes like any Quarto HTML project (`quarto publish gh-pages`/`netlify`/`quarto-pub`), giving readers the article plus every linked notebook.
- **MECA bundle** — Manuscript Exchange Common Approach archive, the standard interchange format publishers accept for direct submission; generated as part of the project render output for submission to a journal's system.
- **Plain PDF/Word** — the `format:` outputs above work standalone too, for reviewers who just want the manuscript file rather than the full website.

## When to Reach for This vs. a Plain Book/Document

| Situation | Use |
|---|---|
| Single-author paper, no notebooks to expose | Plain `.qmd` with `format: pdf`/`typst` — a manuscript project is unnecessary overhead |
| Reproducible research paper — readers should see the actual analysis notebooks | Manuscript project |
| Multi-chapter book, not a journal submission | `project: type: book` (see Part 3), not manuscript |
| Journal explicitly requires a MECA bundle or JATS XML | Manuscript project |
