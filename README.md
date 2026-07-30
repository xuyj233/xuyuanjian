# Yuanjian Xu — Academic Website

Personal academic website built with [Jekyll](https://jekyllrb.com/) and deployed to [GitHub Pages](https://docs.github.com/en/pages) via GitHub Actions.

## Project structure

- `_pages/about.md` — main homepage content (introduction, research map, publications, experience, awards). Most edits happen here.
- `_data/news.yml` — the "News" list shown in the sidebar. Add one Markdown line per item.
- `_layouts/` — page templates (`default.html` for the overall shell and navigation, `single.html` for the tabbed content sections).
- `assets/css/main.css`, `assets/js/main.js` — site styles and interactive behavior (tab switching, etc.).
- `static/` — images and icons (`me.jpg`, favicons, `logos/` for institution logos).
- `source/resume.tex` — LaTeX source of the CV.
- `resume-4-6.pdf` — the compiled CV linked from the homepage. When publishing a newer CV, replace this file (or add a new one) and update the link in `_layouts/default.html`.
- `_config.yml`, `Gemfile` — Jekyll configuration and Ruby dependencies.
- `.github/workflows/pages.yml` — GitHub Actions workflow that builds and deploys the site on every push to `main`.

## Local development

```bash
bundle install        # first time only
bundle exec jekyll serve
```

The site is served at http://localhost:4000 and rebuilds automatically as you edit.

## Deployment

Every push to `main` triggers the GitHub Actions workflow, which builds the site with Jekyll and publishes it to GitHub Pages. No manual build step is required.

## License

This repository is licensed under the [MIT License](LICENSE.md).
