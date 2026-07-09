# Publishing & Deployment

Deploy websites, blogs, and books with `quarto publish`, or automate with GitHub Actions.

## quarto publish

One command, interactive prompts, remembers config in `_publish.yml`:

```bash
quarto publish gh-pages          # GitHub Pages
quarto publish quarto-pub       # quartopub.com (free, public)
quarto publish netlify           # Netlify
quarto publish connect           # Posit Connect
quarto publish confluence        # Atlassian Confluence
quarto publish huggingface       # Hugging Face Spaces
```

Useful flags:

```bash
quarto publish gh-pages --no-prompt      # CI-safe, no confirmation
quarto publish gh-pages --no-render      # publish existing _site/
quarto publish gh-pages --no-browser
```

## GitHub Pages

### One-time setup

```bash
# from the repo root, on a clean working tree
quarto publish gh-pages
```

This renders the site, pushes output to a `gh-pages` branch, and configures Pages source. Requirements:

- `.gitignore` should include `/_site/` (or `/_book/`) and `/.quarto/`
- Repo Settings → Pages → Source: `gh-pages` branch (quarto sets this up on first publish)

`_publish.yml` gets written and should be committed:

```yaml
- source: project
  gh-pages:
    - url: "https://user.github.io/repo/"
```

### Custom domain

Add a `CNAME` file to the project and include it in site resources:

```yaml
# _quarto.yml
project:
  resources:
    - CNAME
```

## The Freeze + CI Pattern

The key to CI publishing for computational sites: **execute locally, render in CI**.

```yaml
# _quarto.yml
execute:
  freeze: auto
```

1. Run `quarto render` locally — executes code, stores results in `_freeze/`
2. Commit `_freeze/` to the repo
3. CI re-renders markdown from frozen results — **no R/Python/Julia needed in CI**

## GitHub Actions

`.github/workflows/publish.yml`:

```yaml
on:
  push:
    branches: [main]

name: Render and Publish

permissions:
  contents: write
  pages: write

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        with:
          tinytex: false      # true only if using LaTeX PDF

      - name: Render and publish to gh-pages
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Before the first Actions run, run `quarto publish gh-pages` once locally to create the branch and `_publish.yml`.

### If code must execute in CI

Add language setup before the publish step:

```yaml
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install jupyter -r requirements.txt
```

(Or `r-lib/actions/setup-r` + `setup-renv` for R.) Freeze is still preferable — it's faster and reproducible.

## Netlify

```bash
quarto publish netlify
```

Or continuous deployment: commit `_freeze/`, then in Netlify set:

- Build command: `quarto render` (install via netlify plugin or build image)
- Publish directory: `_site`

The `quarto-dev/quarto-actions` approach with `target: netlify` also works from GitHub Actions.

## Quarto Pub

Free hosting for public content at `<username>.quarto.pub`:

```bash
quarto publish quarto-pub
```

Fastest path for demos and personal blogs — account signup at [quartopub.com](https://quartopub.com).

## Books

Books publish identically (output dir is `_book/` instead of `_site/`):

```bash
quarto publish gh-pages    # from the book project root
```

PDF/EPUB produced during render land in `_book/` and are served as downloadable files via `book: downloads: [pdf, epub]`.

## Output Dir Reference

| Project type | Output dir |
|---|---|
| website / blog | `_site/` |
| book | `_book/` |
| manuscript | `_manuscript/` |

Override with `project: output-dir:`.

## Preview vs Production

- `site-url` in `_quarto.yml` must match the production URL (RSS, sitemap, and social cards embed absolute URLs).
- Check `robots.txt`/`sitemap.xml` generation happens only when `site-url` is set.
- `quarto render --profile production` + `_quarto-production.yml` for environment-specific config (e.g., analytics only in prod):

```yaml
# _quarto-production.yml
website:
  google-analytics: "G-XXXXXXX"
```
