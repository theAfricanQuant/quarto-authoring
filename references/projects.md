# Projects

The operational layer underneath website/book/dashboard/manuscript projects: what gets rendered, in what order, with what environment, and what runs before/after.

## Project Types

```bash
quarto create project <type> <name>
# type: default | website | blog | book | manuscript | confluence
```

`type: default` is a plain multi-file project with no navigation/book/dashboard structure layered on — just shared `_quarto.yml` metadata across files.

## Core `_quarto.yml`

```yaml
project:
  output-dir: _output

toc: true
number-sections: true
bibliography: references.bib

format:
  html:
    css: styles.css
  pdf:
    documentclass: report
```

Anything at the root of `_quarto.yml` (outside `project:`) applies to every document in the project as a metadata default — individual files can still override per-document in their own front matter.

## Controlling What Renders, and in What Order

By default Quarto renders every `.qmd`/`.ipynb`/`.md`/`.Rmd` except dotfiles, `_`-prefixed files/dirs, `README.*`, and AI config files (`CLAUDE.md`, `AGENTS.md`). Override explicitly:

```yaml
project:
  render:
    - section1.qmd
    - section2.qmd
    - "*.qmd"
    - "!ignored.qmd"
    - "!ignored-dir/"
```

Order in the list is render order — matters when one file's execution has side effects another depends on.

## Directory-Level Config: `_metadata.yml`

Drop a `_metadata.yml` in a subdirectory to apply settings only to files in that folder (and its children), merged on top of the project-level `_quarto.yml`. This is the standard way to `freeze: true` an entire `posts/` folder in a blog without repeating it per-post front matter.

## Profiles — Multiple Variants From One Source

```yaml
# _quarto.yml
execute:
  freeze: true
```

```yaml
# _quarto-production.yml
execute:
  freeze: false
```

Activate with an env var or CLI flag:

```bash
export QUARTO_PROFILE=production
quarto render
# or
quarto render --profile production
# multiple at once — first-listed wins on scalar conflicts:
quarto render --profile production,advanced
```

Conditional content inside a document:

```markdown
::: {.content-visible when-profile="production"}
Only shown when the production profile is active.
:::
```

Mutually-exclusive profile groups with a default:

```yaml
profile:
  group:
    - [basic, advanced]
  default: development
```

`QUARTO_PROFILE` is also readable from Python/R code cells for conditional logic at execution time, not just at the markdown-visibility level.

## Pre-render / Post-render Scripts

```yaml
project:
  type: website
  pre-render: prepare.py
  post-render:
    - compress.ts
    - fix-links.py
```

Both accept a single script or a list, and either can be an arbitrary shell command (so this composes with `make`, a Python script, a Node script, whatever already exists).

Environment variables Quarto sets for these scripts (paths relative to the project root):

| Variable | Meaning |
|---|---|
| `QUARTO_PROJECT_RENDER_ALL` | `"1"` on a full-project render; unset on an incremental single-file render |
| `QUARTO_PROJECT_OUTPUT_DIR` | Where output is being written |
| `QUARTO_PROJECT_INPUT_FILES` | Newline-separated input file list (pre-render only) |
| `QUARTO_PROJECT_OUTPUT_FILES` | Newline-separated output file list (post-render only) |
| `QUARTO_PROJECT_SCRIPT_QUIET` | `"1"` when `--quiet` was passed |

Common pattern — skip an expensive pre-render step on incremental renders:

```python
import os
if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
    exit()
```

## Virtual Environments

**Python:** `venv` (`python3 -m venv env`, `pip freeze > requirements.txt`) or `conda` (`conda env export > environment.yml`) — either is auto-detected by RStudio/Positron; VS Code auto-discovers `venv` but conda needs manual interpreter selection.

**R:** `renv::init()` → work normally → `renv::snapshot()` writes `renv.lock`.

Quarto reads whichever of these is present to configure reproducible execution, and the same files (`requirements.txt`/`environment.yml`/`renv.lock`) are what Binder needs — see below.

## Binder

Quarto detects the virtual-environment files above and uses them to configure a Binder-launchable environment automatically, so "render this project in the browser with no local install" works from the same dependency files already being maintained for reproducibility — no separate Binder-specific config to hand-write in the common case.
