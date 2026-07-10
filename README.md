# quarto-authoring

Comprehensive Quarto + Typst skill for AI coding agents (Claude Code, OpenCode, and anything else that reads `SKILL.md`) — documents, websites, blogs, books (PDF/EPUB), Typst/WeasyPrint PDFs, custom templates, presentations, and publishing.

## What's inside

- **QMD Essentials** — markdown, cross-refs, callouts, figures, tables, citations, code cells, divs/spans
- **Websites & Blogs** — navigation, themes/SCSS, dark mode, search, listings, categories, RSS, about pages, comments
- **Books** — chapters, parts, appendices, numbering, execution (freeze/cache), navbar, sidebar, social metadata
- **EPUB** — multi-format books (HTML+PDF+EPUB), cover images, store metadata, epubcheck, Kindle
- **Typst PDFs** — page layout, fonts, TOC, syntax highlighting, typst-show.typ templates, Pandoc escaping, orange-book, CV/resume/paper templates, brand.yml
- **WeasyPrint PDFs** — standalone HTML+CSS, Bootstrap workaround, dark theme support
- **Presentations** — revealjs (deep), pptx, beamer, Typst slides
- **Dashboards** — rows/columns/pages, value boxes, cards, tabsets, sidebars/toolbars, static vs. Shiny-backed interactivity, deployment
- **Interactivity** — Observable JS (reactive cells, data sources, cross-file imports), Shiny (R/Python), Jupyter widgets/htmlwidgets
- **MS Word** — docx output, reference-doc templates for matching a corporate style
- **Manuscripts** — notebook-first scholarly articles, journal formats, MECA bundles
- **Projects** — profiles, pre/post-render scripts, virtual environments, Binder
- **Publishing** — quarto publish, GitHub Pages, Netlify, GitHub Actions, freeze CI pattern
- **Migration** — from R Markdown, bookdown, xaringan, distill, blogdown, Jupyter
- **Report scaffolding** — `scripts/scaffold.py` / `validate.py` / `snippets.py` for repeatable, branded PDF-report projects (report.qmd + typst-show.typ + typst-template.typ + _brand.yml)

## Install

One command, straight from GitHub — no account, nothing else to set up:

```bash
npx github:theAfricanQuant/quarto-authoring
```

That installs the skill user-wide for Claude Code (`~/.claude/skills/quarto-authoring`). Other targets:

```bash
npx github:theAfricanQuant/quarto-authoring --project    # this project only (./.claude/skills/)
npx github:theAfricanQuant/quarto-authoring --opencode   # OpenCode (~/.config/opencode/skills/)
npx github:theAfricanQuant/quarto-authoring --all        # Claude Code + OpenCode
npx github:theAfricanQuant/quarto-authoring --dir <path> # anywhere else
npx github:theAfricanQuant/quarto-authoring --help       # list all options
```

If the package is published to the npm registry, the short form works too, with the same flags:

```bash
npx quarto-authoring-skill
```

**To update:** re-run the same command — it replaces the installed copy in place.

**Manual install (no Node/npx):**

```bash
git clone https://github.com/theAfricanQuant/quarto-authoring.git \
  ~/.claude/skills/quarto-authoring        # or ~/.config/opencode/skills/...
```

> **Tip:** if you already have another Quarto skill installed (e.g. an older `quarto` skill in `~/.claude/skills`), remove it — two skills covering the same topic compete for the same questions, and this one is a superset.

## Use

Nothing to invoke manually. Once installed, your agent auto-loads the skill whenever a task touches Quarto or Typst. Just ask things like:

- "set up a quarto blog with categories and an RSS feed"
- "I'm writing a book — I want a website, a PDF and an epub from the same source, no LaTeX"
- "make me a one-page CV pdf with typst, navy header, gold accents"
- "publish my quarto site to GitHub Pages without CI needing python"
- "my typst template is eating dollar signs"
- "convert my bookdown project to quarto"
- "scaffold a branded Typst report project for this quarterly brief"
- "build me a dashboard with a value box for revenue and a chart tab"
- "add an interactive filter to my report without needing a server"
- "set up a manuscript project so reviewers can see the notebooks behind my figures"
- "give me a production profile that turns off freeze for a clean CI build"

The agent reads `SKILL.md` first and pulls in the relevant file from `references/` (30 focused guides) only when needed, so it stays fast and doesn't flood its context.

You need [Quarto](https://quarto.org) ≥ 1.5 installed for the agent to actually render things (≥ 1.9.17 for Typst book templates). Typst itself is bundled with Quarto — no LaTeX required for any of the PDF workflows in this skill.

## File structure

```
SKILL.md              # Main skill instructions (read first by the agent)
references/           # 30 detailed reference files, loaded on demand
examples/             # Demo QMD, standalone HTML, CSS
scripts/              # render-demo.sh runner + scaffold.py/validate.py/snippets.py for report projects
bin/install.js        # the npx installer
evals/                # test prompts + trigger queries used to validate the skill
```

## Development

Test changes locally without publishing:

```bash
npm pack
npm exec --yes --package=./quarto-authoring-skill-*.tgz -- quarto-authoring-skill --dir /tmp/skill-test
```

### Running the evals

The `evals/` directory is the skill's test suite — run it after any meaningful edit so you know whether the change helped or broke something.

**Task evals** (`evals/evals.json` — 4 end-to-end scenarios: blog+RSS, multi-format book, Typst CV, GitHub Pages CI). These check that an agent *using the skill* produces working output. Easiest way — ask your agent:

> run the evals in evals/evals.json against this skill and show me pass/fail per assertion

It will spawn a fresh agent per scenario in a scratch folder with the skill installed, run the prompt, and verify the output against each eval's checks (RSS file exists, PDF is 1 page, workflow installs no Python, ...).

To run one by hand instead:

1. Install the edited skill somewhere isolated:
   `npx github:theAfricanQuant/quarto-authoring --dir /tmp/skill-test`
2. Open a **fresh** agent session in an empty folder (a session that already discussed the skill isn't a fair test)
3. Paste one prompt from `evals.json` verbatim and let it finish
4. Check the output against that eval's `expected_output` / assertions

**Trigger evals** (`evals/trigger-eval.json` — 20 realistic queries labeled `should_trigger` true/false). These test the `description` field in SKILL.md frontmatter — whether the skill *activates* at the right moments — so only re-run them when you edit the description. Manual version: fresh session, paste a query, watch whether the agent loads the skill. The should-trigger queries are on-topic in disguise; the should-not-trigger ones are deliberate near-misses (WordPress posts, LaTeX theses, PowerPoint decks) that share keywords but belong to other tools.

> **Important:** uninstall any other Quarto skill before running trigger evals — a competing skill intercepts the queries and makes every measurement read as "didn't trigger".

## Credits

Independently authored. Thanks to Posit and the Quarto core team for building and documenting Quarto itself — the foundation everything in this skill sits on top of. Posit also maintains their own [quarto-authoring skill](https://github.com/posit-dev/skills) covering core QMD authoring; this skill additionally covers websites/blogs, books/EPUB, Typst/WeasyPrint PDFs, custom Typst templates, presentations, dashboards, interactivity, MS Word, manuscripts, projects, and publishing.

## License

MIT
