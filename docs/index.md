# Home

[![pyrig-badge](assets/banner.svg)](assets/banner.svg)

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-badge/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-badge/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-badge/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-badge/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-badge/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-badge)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/j178/prek)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/CI/CD-zizmor-yellow)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/j178/prek)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/j178/prek)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/j178/prek)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/j178/prek)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/j178/prek)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/j178/prek)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/j178/prek)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://github.com/j178/prek)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Winipedia/pyrig/main/docs/assets/badge.json)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-badge?style=social)](https://github.com/Winipedia/pyrig-badge)
[![VersionControlHookManager](https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge.svg)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-badge)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-badge?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-badge)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-badge)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-badge)](https://github.com/Winipedia/pyrig-badge/blob/main/LICENSE)

---

> A pyrig plugin that configures a project badge.

---

## Overview

`pyrig-badge` is a [pyrig](https://github.com/Winipedia/pyrig) plugin that
manages a project logo SVG, a banner embedding the logo, and Shields.io badge
data, then adds a linked banner image to the project README and this
documentation landing page.

## Generated assets

- [`docs/assets/logo.svg`](assets/logo.svg) contains the project logo. The plugin
  supplies the standard SVG root element and namespace, with default dimensions
  of `200` by `200` and a viewBox of `0 0 200 200` when those attributes are absent.
  A new file starts as an empty SVG for you to customize.
- [`docs/assets/banner.svg`](assets/banner.svg) contains an `<image>` element
  referencing `logo.svg`. The logo is positioned within the banner's viewBox
  using its original dimensions, with centering offsets rounded down to integers.
  The banner has the same default dimensions and viewBox as the logo.
- [`docs/assets/badge.json`](assets/badge.json) contains the Shields.io badge configuration,
  including the project name, badge colors, and embedded logo markup. Its
  `logoSvg` value is synced from `docs/assets/logo.svg`.

## Customization

During `pyrig sync`, Pyrig enforces the following:

- In [`docs/assets/logo.svg`](assets/logo.svg) and
  [`docs/assets/banner.svg`](assets/banner.svg), the root element is `<svg>` with
  `xmlns="http://www.w3.org/2000/svg"`. Missing `width`, `height`, and `viewBox`
  attributes are filled with `200`, `200`, and `0 0 200 200`, respectively;
  existing values are preserved.
- In the banner's embedded logo `<image>`, `href` is `logo.svg`, and `width` and
  `height` match the logo's dimensions. Its `x` and `y` are the banner viewBox's
  minimum coordinates plus half the remaining width and height, rounded down to
  integers. The logo is not scaled to fit the banner.
- In [`docs/assets/badge.json`](assets/badge.json), `message` is the project name
  and `logoSvg` is the content of `logo.svg`. Missing `label` defaults to an empty
  string, and missing `labelColor` and `color` default to `white`; existing values
  are preserved.

Artwork, additional SVG attributes and elements, SVG dimensions and viewBoxes,
and badge labels and colors can be customized. Banner embedding requires the
logo's dimensions to be integers without units and the banner viewBox to contain
exactly four whitespace-separated integers. The logo is positioned but not
scaled to fit the banner.

## Usage

Add the plugin as a development dependency and run `pyrig sync` to regenerate
the project configuration:

```bash
uv add pyrig-badge --dev
uv run pyrig sync
```

## API Reference

For class- and method-level details, see the [API reference](api.md), generated
automatically from the source.
