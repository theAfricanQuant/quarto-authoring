# Interactivity

Three ways to make a Quarto document (or dashboard) interactive, in increasing order of infrastructure required.

## Widgets — client-side, zero server, easiest

**Jupyter Widgets** (Python/Jupyter engine) and **htmlwidgets** (R/Knitr engine — plotly, leaflet, DT, etc.) render to self-contained HTML+JS at render time. Nothing to deploy beyond static files.

```python
import plotly.express as px
px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
```

Works identically inside a dashboard card — no special configuration needed beyond having the library render its normal HTML output.

## Observable JS (OJS) — reactive, client-side

A `{ojs}` cell is JavaScript with a reactive runtime layered on top: any cell referencing a value automatically re-runs when that value changes, no manual event wiring.

```{ojs}
viewof minimum = Inputs.range([-2, 2], {value: 1, step: 0.01, label: "minimum"})
```

```{ojs}
filtered = data.filter(d => d.value > minimum)
```

`filtered` recomputes automatically whenever the `minimum` slider moves. Deployable as pure static HTML — no server, works on GitHub Pages/Netlify/Quarto Pub.

### Data sources into OJS

```{ojs}
data = FileAttachment("data.csv").csv({typed: true})
```

Or pull a value computed in a Python/R cell across into OJS via `ojs_define()`:

```python
#| echo: false
ojs_define(data_from_python = my_dataframe.to_dict('records'))
```

```{ojs}
data = transpose(data_from_python)
```

### Reusing OJS code across documents

```{ojs}
import {chart} from "./helpers.qmd"
```

Import a named cell from another `.qmd`/`.js` file to share chart/component definitions across a site or dashboard.

## Shiny — reactive, server-backed

Needs the knitr engine (R) or the Shiny for Python integration, plus a running Shiny process. Full server-side computation on every interaction — appropriate when the reaction needs real computation (a model refit, a database query) rather than just filtering already-loaded data.

```r
selectInput("type", "Trend index", choices = unique(trend_data$type))

selected_trends <- reactive({
  trend_data[trend_data$type == input$type, ]
})

output$lineplot <- renderPlot({
  plot(x = selected_trends()$date, y = selected_trends()$close)
})
```

```yaml
# document-level
server: shiny
```

Run locally with `shiny::runApp()` (R) or the Python Shiny equivalent; deploy to a Shiny server or Posit Connect in production — **not** compatible with static-only hosts (GitHub Pages, Netlify) since the server process must keep running.

## Layout for Interactive Inputs

```markdown
:::: {.columns}
::: {.column width="30%"}
Input controls here.
:::
::: {.column width="70%"}
Output/chart here.
:::
::::
```

Or use the same sidebar/toolbar pattern as dashboards (see [dashboards.md](dashboards.md)) even in a plain document.

## Choosing Which One

| Need | Use |
|---|---|
| Ship as static HTML (GitHub Pages, Netlify, Quarto Pub) | OJS or a client-side widget |
| Python/R computation must genuinely re-run per interaction (model, DB query) | Shiny |
| Just embedding an existing interactive plot, no new controls needed | Jupyter Widgets / htmlwidgets |
| Filtering/reshaping data already loaded in the browser | OJS |

## Gotchas

- Mixing Shiny and OJS in the same document is possible (OJS can read Shiny outputs) but adds real complexity — default to one or the other unless there's a specific reason to combine them.
- OJS cells execute in the reader's browser at view time — anything sensitive (API keys, private data) must not be embedded in an OJS cell or its data source.
- Widgets embedded via Jupyter/htmlwidgets bloat the rendered HTML file size (the JS library ships inline); fine for a handful of charts, worth checking output size for many-widget dashboards.
