# Dashboards

Interactive, grid-based data layouts (`format: dashboard`) built from ordinary markdown headings and code cells — no separate templating language.

## Basic Setup

```yaml
---
title: "Sales Dashboard"
format: dashboard
---
```

```bash
quarto preview dashboard.qmd     # live-reload while building
```

## Layout: Pages, Rows, Columns, Tabsets

Level-1 headings create **pages** (a `##`-only document is single-page). Level-2 headings create **rows** by default; each code cell inside becomes a **card**.

```markdown
## Row {height=60%}

```{python}
#| title: Revenue by Region
# chart code
```

## Row {height=40%}

```{python}
#| title: Top Products
# table code
```
```

Switch the top-level orientation to columns instead of rows:

```yaml
format:
  dashboard:
    orientation: columns
```

Nest columns inside a row (or vice versa) with `.column`/`.row` classes on a heading to mix orientations on one page:

```markdown
## Row {height=70%}

### Column {width=40%}
### Column {width=60%}
```

Turn a row/column's cards into a tabset:

```markdown
## Row {.tabset}

```{python}
#| title: Tab A
```

```{python}
#| title: Tab B
```
```

## Cards

Every code cell is a card by default; give it a title with `#| title:`. Explicit card fencing lets you mix code and static markdown/images in one card:

```markdown
::: {.card title="Notes"}
Static markdown content, not tied to a code cell.
:::
```

`expandable: false` on a card removes the fullscreen-expand icon; `padding`/`fill` control card chrome.

## Value Boxes

A dedicated card type for a single KPI-style number:

```markdown
```{python}
#| content: valuebox
#| title: "Total Revenue"
dict(value = "$1.2M", icon = "currency-dollar", color = "success")
```
```

`color` accepts theme names (`success`, `warning`, `danger`, `primary`, ...) or a hex code. `icon` takes any Bootstrap icon name.

## Sidebars & Toolbars

```yaml
format:
  dashboard:
    scrolling: false      # default: fill viewport height (fixed-height cards)
```

A `.sidebar`-classed column holds input controls (Shiny widgets, or a plain markdown filter note for a static dashboard):

```markdown
## {.sidebar}

```{r}
selectInput("region", "Region", choices = c("East", "West"))
```

## Column
```

`.toolbar` on a row instead of `.sidebar` produces a horizontal input bar above the content instead of a side panel.

## Theming

Dashboards are HTML documents under the hood — the same `theme:`/custom-SCSS mechanism as regular websites applies (see [websites.md](websites.md)). `_brand.yml` colors are picked up automatically.

## Multi-Page Dashboards & Navigation

```yaml
format:
  dashboard:
    nav-buttons: [github, linkedin]
```

Level-1 headings become pages; a page nav bar is generated automatically. `logo:` and `theme:` apply globally across pages.

## Parameters — Rendering Variants

Dashboards support Quarto `params` like any other document — combine with `quarto render --execute-params` (or a small render script) to generate one dashboard per region/product/etc. from a single source:

```yaml
params:
  region: "East"
```

```bash
quarto render dashboard.qmd -P region:West -o west-dashboard.html
```

## Interactivity

Two paths — see [interactivity.md](interactivity.md) for the full comparison:

- **Static (OJS / widgets)** — client-side reactivity, deployable to any static host (GitHub Pages, Netlify, Quarto Pub).
- **Shiny-backed** (`server: shiny` in YAML) — full server-side reactive computation; needs a running Shiny process, not static hosting.

```yaml
server: shiny
```

## Deployment

Static dashboards publish exactly like any HTML output — `quarto publish gh-pages`/`netlify`/`quarto-pub`. Shiny-backed dashboards require a Shiny server or Posit Connect; static hosts will serve the HTML shell but the reactive parts won't function.

## Responsive Behavior

Cards reflow to a single column automatically on narrow (mobile) viewports — no extra configuration needed for basic responsiveness. Test with `quarto preview` at a narrow browser width before assuming a complex nested layout degrades gracefully.
