# AGENTS.md

## Project Overview

zrythm-web is the source code for https://www.zrythm.org — the website for Zrythm, a highly automated Digital Audio Workstation (DAW). It is a **Python-based static site generator** using Jinja2 templates with i18n support, building localized HTML pages for ~30 languages. Licensed AGPL-3.0-or-later.

## Tech Stack

- **Python 3** — primary language
- **Jinja2** — HTML templating (with `jinja2.ext.i18n` extension)
- **Sass/SCSS** — CSS preprocessing (compiled via `sass` CLI)
- **Babel + gettext** — internationalization (`.po`/`.mo` files)
- **GNU Make** — build system
- **No JavaScript** — the site is purely static HTML + CSS

## Build Commands

```bash
# Setup (first time)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Full build (extract translations, render templates, compile SCSS, generate sitemap)
make

# Individual targets
make locale          # Update translations (extract + compile)
make locale-update   # Extract translatable strings into POT, merge into PO files
make locale-compile  # Compile .po to .mo binary files
make template        # Render HTML from Jinja2 templates + compile SCSS
make run             # Build + start local HTTP server on port 8000 + open browser
make clean           # Remove rendered/, __pycache__, .pyc files
```

## System Dependencies

- `python3` and `pip`
- `sass` CLI (for SCSS compilation)
- `pybabel` (installed via Babel Python package)
- Standard Unix tools (make, cp, find, sed, awk)

## Testing

**No test framework is configured.** There are no test files or test commands. The CI had a commented-out `linkchecker` stage.

## Linting/Formatting

**No linters or formatters are configured.** No eslint, prettier, flake8, black, or similar tools.

## Project Structure

```
template.py        # Main build script (Jinja2 renderer, fetches API data)
i18nfix.py         # Custom Babel extractor (whitespace normalization)
config.mk          # Build config (PYTHON, BABEL, DEBUG vars)
Makefile           # Build system
requirements.txt   # Pinned Python dependencies
.credentials       # Gitignored env vars (optional API tokens)

template/          # Page templates (*.html.j2) + styles.scss
common/            # Shared includes: base.j2, header/navigation/footer .j2.inc
locale/            # i18n: babel.map, messages.pot, <lang>/LC_MESSAGES/*.po
static/            # Assets copied as-is to rendered/<locale>/ (icons/, images/)
static-unprefixed/ # Assets copied to rendered/ root (robots.txt, plugins/)
dist/              # Vendored third-party assets (manrope-font/, fork-awesome/)
rendered/          # Build output (gitignored) — generated HTML per locale
```

## Key Patterns

### Templates
- Pages extend `common/base.j2` with `{% block head_content %}` and `{% block body_content %}`
- Includes use `.j2.inc` extension: `{% include "common/navigation.j2.inc" %}`
- Translations: `{{ _('text') }}` or `{% trans %}...{% endtrans %}`

### CSS
- BEM-like naming: `.navbar__link`, `.hero__container`, `.highlights__row--alt`
- CSS custom properties for colors/spacing
- SCSS nesting for pseudo-elements and media queries
- Dark theme with grayscale + accent colors

### Python (template.py)
- URL helpers: `url()`, `self_localized()`, `url_localized()`, `svg_localized()`
- Data classes defined inline (`Plugin`, `FeatureGroup`, `Feature`)
- Feature/plugin data hardcoded in Python dicts/lists
- Fuzzy translation entries auto-cleared before rendering
- API data fetched at build time (forex rates, product/order info)

### i18n
- Custom Babel extractor in `i18nfix.py` normalizes whitespace
- Babel mapping in `locale/babel.map`
- 34 active languages defined in `langs_full` dict in `template.py`
- Each language entry: flag emoji, native name, default currency
- Weblate integration via `weblate` git remote

## Environment Variables (.credentials)

The `.credentials` file (gitignored) is sourced by the Makefile. Leave values empty to skip API fetches (site still builds):

```bash
export ZRYTHM_ACCOUNTS_TOKEN=  # accounts.zrythm.org API (optional)
export VERIFY_TRIAL_PACKAGE_URLS=  # "YES" to verify download URLs
export GET_VERSION=            # "YES" to fetch latest Zrythm version
```

## CI/CD

- **Platform**: GitLab CI (`.gitlab-ci.yml`)
- **Pipeline**: `setup` → `build` → `deploy`
- **Deploy**: rsync over SSH to www.zrythm.org (only on `master` branch and tags)
- **Runner**: `archlinux` tagged runner

## Important Notes

- When adding translatable text, use `{{ _('...') }}` then run `make locale-update` to update POT/PO files
- SCSS changes require `make template` to recompile to CSS
- The main branch is `master`
