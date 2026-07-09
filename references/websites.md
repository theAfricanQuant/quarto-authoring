# Websites

Full-featured multi-page websites with navigation, themes, and search. Zero JavaScript frameworks required.

## Create a Website Project

```bash
quarto create project website mysite
cd mysite
quarto preview          # live-reload dev server
quarto render           # build to _site/
```

Generated structure:

```
mysite/
├── _quarto.yml       # project config
├── index.qmd         # homepage
├── about.qmd
└── styles.css
```

## Minimal Config

```yaml
# _quarto.yml
project:
  type: website
  output-dir: _site

website:
  title: "My Site"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - about.qmd

format:
  html:
    theme: cosmo
    css: styles.css
    toc: true
```

## Navigation

### Navbar (top)

```yaml
website:
  navbar:
    logo: logo.png
    background: primary
    search: true
    left:
      - text: "Guide"
        href: guide.qmd
      - text: "Reference"
        menu:                    # dropdown
          - text: "Functions"
            href: functions.qmd
          - text: "Options"
            href: options.qmd
    right:
      - icon: github
        href: https://github.com/user/repo
      - icon: rss
        href: index.xml
```

### Sidebar (side)

```yaml
website:
  sidebar:
    style: docked            # or floating
    search: true
    collapse-level: 2
    contents:
      - index.qmd
      - section: "Basics"
        contents:
          - basics-intro.qmd
          - basics-setup.qmd
      - section: "Advanced"
        contents: advanced/*.qmd    # glob patterns work
```

`contents: auto` generates the sidebar from the file system.

### Hybrid navigation (navbar + per-section sidebars)

Give each sidebar an `id` matching a navbar entry — each top-level section gets its own sidebar:

```yaml
website:
  navbar:
    left:
      - text: "Guide"
        href: guide/index.qmd
      - text: "Reference"
        href: reference/index.qmd
  sidebar:
    - id: guide
      title: "Guide"
      contents: guide/*.qmd
    - id: reference
      title: "Reference"
      contents: reference/*.qmd
```

### Breadcrumbs and page navigation

```yaml
website:
  bread-crumbs: true        # default true, shown when sidebar has >1 level
  page-navigation: true     # prev/next links at page bottom
  back-to-top-navigation: true
```

## Themes

25+ built-in Bootswatch themes: `cosmo` (default), `flatly`, `darkly`, `litera`, `lumen`, `minty`, `pulse`, `sandstone`, `simplex`, `sketchy`, `slate`, `solar`, `spacelab`, `superhero`, `united`, `yeti`, `zephyr`, ...

```yaml
format:
  html:
    theme: litera
```

### Dark mode toggle

```yaml
format:
  html:
    theme:
      light: flatly
      dark: darkly
```

Quarto adds a toggle to the navbar automatically. Respect OS preference by listing the preferred default first.

### Custom SCSS theme

```yaml
format:
  html:
    theme:
      - cosmo
      - custom.scss      # layered on top of cosmo
```

```scss
/*-- scss:defaults --*/
$primary: #2563eb;
$font-family-sans-serif: "Inter", sans-serif;
$navbar-bg: $primary;
$code-block-bg: #f8f9fa;

/*-- scss:rules --*/
h1, h2 { letter-spacing: -0.02em; }
```

The `/*-- scss:defaults --*/` and `/*-- scss:rules --*/` comment markers are required — defaults set Bootstrap variables, rules add CSS. `_brand.yml` colors are also picked up automatically by HTML output.

## Search

Built-in client-side search (no server needed):

```yaml
website:
  search:
    location: navbar      # or sidebar
    type: overlay         # or textbox
```

Algolia for large sites:

```yaml
website:
  search:
    algolia:
      index-name: <index>
      application-id: <id>
      search-only-api-key: <key>
```

## Drafts

```yaml
# in a page's front matter
draft: true
```

Drafts render in `quarto preview` but are excluded from listings, navigation, and search in full renders. Control site-wide:

```yaml
website:
  drafts:
    - posts/wip-post.qmd
  draft-mode: unlinked    # visible | unlinked | gone
```

## Site Metadata & Social Cards

```yaml
website:
  title: "My Site"
  site-url: https://example.com     # required for RSS + sitemap
  repo-url: https://github.com/user/repo
  repo-actions: [edit, issue]
  favicon: favicon.png
  open-graph: true
  twitter-card:
    creator: "@handle"
    card-style: summary_large_image
  page-footer:
    left: "© 2026"
    center: "[License](license.qmd)"
    right:
      - icon: github
        href: https://github.com/user/repo
```

`site-url` also enables `sitemap.xml` generation.

## Announcement Bar

```yaml
website:
  announcement:
    icon: info-circle
    dismissable: true
    content: "**New** — version 2.0 released"
    type: primary
    position: below-navbar
```

## Redirects & Aliases

Preserve old URLs when moving pages:

```yaml
# in the page's front matter
aliases:
  - /old-path/page.html
```

## Multi-Format Pages

Offer the same page as HTML + PDF:

```yaml
format:
  html: default
  typst: default
```

Quarto adds an "Other Formats" link automatically. Limit which pages: set formats per-page in front matter instead of `_quarto.yml`.

## Includes Across Pages

Shared content (headers, contact blocks):

```markdown
{{< include _shared-note.qmd >}}
```

Files starting with `_` or in directories starting with `_` are not rendered as standalone pages.

## Execution on Websites

Use freeze so a full site render doesn't re-run every notebook:

```yaml
execute:
  freeze: auto      # re-execute only when the source file changes
```

Check `_freeze/` into version control — this is what makes CI rendering work without R/Python installed (see [publishing.md](publishing.md)).

## Preview Options

```bash
quarto preview                    # default port 4200 (random if taken)
quarto preview --port 8080 --no-browser
quarto render && quarto preview --no-watch-inputs   # serve without re-render
```
