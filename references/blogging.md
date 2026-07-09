# Blogging

Blogs are website projects with a listing homepage, a `posts/` directory, categories, and an RSS feed.

## Create a Blog

```bash
quarto create project blog myblog
```

Generated structure:

```
myblog/
├── _quarto.yml
├── index.qmd            # listing page (the blog homepage)
├── about.qmd            # about page
├── posts/
│   ├── _metadata.yml    # shared options for all posts
│   ├── welcome/
│   │   ├── index.qmd
│   │   └── thumbnail.jpg
│   └── post-with-code/
│       └── index.qmd
└── styles.css
```

Each post is a **directory** with an `index.qmd` — images and data live alongside the post.

## Blog Config

```yaml
# _quarto.yml
project:
  type: website

website:
  title: "My Blog"
  site-url: https://example.com      # required for RSS
  description: "What this blog is about"
  navbar:
    right:
      - about.qmd
      - icon: github
        href: https://github.com/user
      - icon: rss
        href: index.xml

format:
  html:
    theme: cosmo
    css: styles.css
```

## The Listing Homepage

```yaml
# index.qmd front matter
---
title: "My Blog"
listing:
  contents: posts          # directory, glob, or explicit list
  sort: "date desc"
  type: default            # default | table | grid
  categories: true         # category filter sidebar
  sort-ui: true
  filter-ui: true
  feed: true               # generate RSS at index.xml
page-layout: full
title-block-banner: true
---
```

### Listing types and options

| Option | Values / purpose |
|---|---|
| `type` | `default` (blog stream), `table`, `grid`, `custom` (EJS template) |
| `contents` | `posts`, `posts/**/*.qmd`, explicit list, or YAML metadata files |
| `sort` | `"date desc"`, `"title"`, multiple keys allowed |
| `max-items` | Cap number of items |
| `page-size` | Items per page (pagination) |
| `image-height`, `grid-columns` | Layout tuning |
| `fields` | Which fields to show: `[image, date, title, author, reading-time, description, categories]` |
| `feed` | `true` or `{items: 20, type: partial}` |

Multiple listings on one page: give each `listing` an `id` and place `::: {#listing-id}` divs where they should render.

## Post Front Matter

```yaml
---
title: "Post Title"
description: "One-sentence summary shown in listings and RSS"
author: "Ricky Macharm"
date: "2026-07-09"
date-modified: last-modified
categories: [python, quarto, tutorial]
image: thumbnail.jpg
draft: false
---
```

- `date` in the future = post renders but you control when to publish (Quarto does not auto-hide future dates; use `draft: true` until ready).
- `image` is used in listings and social cards; first image in the post is the fallback.
- `categories` power the filter UI and category pages.

## Shared Post Options (`posts/_metadata.yml`)

Options applied to every post in the directory:

```yaml
# posts/_metadata.yml
freeze: true          # don't re-execute old posts on full render
title-block-banner: true
comments:
  giscus:
    repo: user/repo
```

`freeze: true` here is the canonical blog pattern — old posts never re-execute, so renders stay fast and reproducible even when package versions change. Check `_freeze/` into git.

## Drafts

```yaml
draft: true
```

Draft posts show in `quarto preview` but are excluded from listings, feeds, and search in the rendered site.

## RSS Feed

Requires `site-url` + `description` in `_quarto.yml` and `feed: true` on the listing. Generates `index.xml`. Full-content vs summary:

```yaml
listing:
  feed:
    type: full        # or partial
    items: 20
    categories: [python]    # optional category-specific feed
```

Add the RSS icon to the navbar (`icon: rss`, `href: index.xml`).

## About Pages

Five built-in templates for `about.qmd`:

```yaml
---
title: "Ricky Macharm"
image: profile.jpg
about:
  template: jolla        # jolla | trestles | solana | marquee | broadside
  links:
    - icon: github
      text: GitHub
      href: https://github.com/user
    - icon: linkedin
      text: LinkedIn
      href: https://linkedin.com/in/user
---

Bio text goes here below the front matter.
```

- `jolla` — centered, round image (personal landing page)
- `trestles` — left column image + links, right column content
- `solana` — content left, image right
- `marquee` — large banner image
- `broadside` — image left, content right

## Comments

```yaml
# per post, or in posts/_metadata.yml
comments:
  giscus:                     # GitHub Discussions (recommended)
    repo: user/repo
    mapping: pathname
  # or:
  utterances:
    repo: user/repo           # GitHub Issues
  # or:
  hypothesis: true            # web annotations
```

Disable on a specific page: `comments: false`.

## Subscription / Newsletter Box

Inject raw HTML (e.g., Buttondown, Mailchimp form) on the listing page:

```yaml
# _quarto.yml
website:
  margin-footer: subscribe.html
```

## Category Notes

- Clicking a category filters the listing; URL becomes shareable (`?category=python`).
- Categories also appear under post titles when `categories: true` in the post's title block area.

## Publishing a Blog

Same as any website — `quarto publish gh-pages`, Netlify, or Quarto Pub. See [publishing.md](publishing.md). The freeze pattern above means CI never needs your Python/R environment.
