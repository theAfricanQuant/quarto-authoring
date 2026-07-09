# Presentations

Three Quarto formats — `revealjs` (HTML, the most capable), `pptx` (PowerPoint), `beamer` (LaTeX PDF) — plus standalone Typst slide options.

## Slide Basics (all formats)

```yaml
---
title: "Habits"
author: "John Doe"
format: revealjs
---
```

```markdown
# Section Title        <!-- level 1 = section/title slide -->

## Slide Title         <!-- level 2 = new slide -->

- Point one
- Point two

---                    <!-- horizontal rule = untitled slide -->
```

## revealjs

### Common config

```yaml
format:
  revealjs:
    theme: default          # dark | league | sky | night | serif | simple | solarized | moon | dracula | beige | blood
    slide-number: true
    footer: "Conference 2026"
    logo: logo.png
    transition: slide       # none | fade | slide | convex | concave | zoom
    incremental: false
    chalkboard: true        # draw on slides (c/b keys)
    preview-links: auto
    code-line-numbers: true
    center: false           # vertical centering
```

### Incremental lists

Globally (`incremental: true`) or per list:

```markdown
::: {.incremental}
- Appears first
- Then this
:::

::: {.nonincremental}
- All at once (when global incremental is on)
:::
```

Pause within any content: `. . .` on its own line.

### Columns

```markdown
:::: {.columns}
::: {.column width="60%"}
Left content
:::
::: {.column width="40%"}
Right content
:::
::::
```

### Code highlighting & stepping

````markdown
```{.python code-line-numbers="2-3|5|7-8"}
import pandas as pd
df = pd.read_csv("data.csv")
df = df.dropna()

result = df.groupby("cat").mean()

fig = result.plot()
fig.show()
```
````

`|` steps through highlights on successive key presses. For executed cells use `#| code-line-numbers: "2-3|5"`.

### Speaker notes & presenter view

```markdown
## Slide Title

Content.

::: {.notes}
Only visible in presenter view (press S).
:::
```

### Slide-level options

```markdown
## Big Reveal {.smaller background-color="black" transition="zoom"}

## Image Background {background-image="bg.jpg" background-size="cover"}

## Video Background {background-video="clip.mp4" background-video-loop="true"}

## Scrollable Output {.scrollable}
```

`{.smaller}` shrinks text ~80%; `{.scrollable}` allows overflow scrolling — both also settable globally.

### Fragments & auto-animate

```markdown
::: {.fragment}
Fades in
:::
::: {.fragment .fade-out}
Fades out
:::
::: {.fragment .highlight-red}
Highlights red
:::
```

```markdown
## Code Morph {auto-animate=true}
<!-- next slide with same elements + auto-animate=true morphs between them -->
```

### Absolute positioning

```markdown
![](image.png){.absolute top=200 left=0 width="350"}
```

### Custom revealjs theme

```yaml
format:
  revealjs:
    theme: [default, custom.scss]
```

```scss
/*-- scss:defaults --*/
$body-bg: #0b1220;
$body-color: #e6edf7;
$link-color: #e8b949;
$presentation-heading-font: "Inter", sans-serif;
$presentation-font-size-root: 36px;
```

### Print to PDF

Open the presentation, press `E` (print view), then browser Print → Save as PDF. Or:

```bash
quarto render slides.qmd --to revealjs
# then use decktape for automated export:
npx decktape reveal slides.html slides.pdf
```

## PowerPoint (pptx)

```yaml
format:
  pptx:
    reference-doc: template.pptx    # corporate template
```

Create a starter template: `quarto pandoc -o template.pptx --print-default-data-file reference.pptx`. Edit its Slide Master in PowerPoint — Quarto maps content onto the master layouts (Title Slide, Title and Content, Two Content, ...). Two-column via `::: {.columns}` works; most revealjs-only features (fragments, backgrounds) do not.

## Beamer (LaTeX PDF)

```yaml
format:
  beamer:
    theme: metropolis
    colortheme: seahorse
    aspectratio: 169
    navigation: horizontal
```

Requires a LaTeX distribution (`quarto install tinytex`). Use when a PDF deck with LaTeX math quality is required; otherwise prefer revealjs + print-to-PDF or Typst slides.

## Typst Slides (standalone, outside Quarto)

Quarto has no native Typst slide format yet — for Typst-powered decks use Typst directly:

- **touying** — the most capable Typst slides package (themes, animations, sections):
  ```bash
  typst init @preview/touying-simpl 
  ```
- **polylux** — simpler, `#slide[]`-based
- **icicle / badformer** — official template gallery slides (`typst init @preview/...`)

Or keep authoring in Quarto with `format: typst` and design slide-sized pages yourself:

```yaml
format:
  typst:
    papersize: presentation-16-9
    margin: {x: 1.5cm, y: 1.2cm}
```

with a `typst-show.typ` that styles headings and adds `pagebreak()` per H1 — see [SKILL.md §6](../SKILL.md).

## Choosing a Format

| Need | Use |
|---|---|
| Web sharing, animations, speaker view | `revealjs` |
| Boss wants editable .pptx | `pptx` + `reference-doc` |
| PDF deck, heavy math, classic academia | `beamer` |
| PDF deck, modern look, no LaTeX | Typst (touying) |
