# Home

[![pyrig-badge](assets/banner.svg)](assets/banner.svg)

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-badge/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-badge/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-badge/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-badge/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-badge/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-badge)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://prek.j178.dev/reference/built-in-hooks/#fix-byte-order-marker)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/%F0%9F%8C%88-zizmor-white?labelColor=white)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-case-conflict)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://prek.j178.dev/reference/built-in-hooks/#end-of-file-fixer)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://prek.j178.dev/reference/built-in-hooks/#mixed-line-ending)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://prek.j178.dev/reference/built-in-hooks/#pretty-format-json)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-json)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-added-large-files)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-merge-conflict)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks#name-tests-test)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://prek.j178.dev/reference/built-in-hooks/#trailing-whitespace)
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
manages a project logo SVG, a banner containing the logo inline, and Shields.io
badge data, then adds a linked banner image to the project README and this
documentation landing page.

## Generated assets

- [`docs/assets/logo.svg`](assets/logo.svg) contains the project logo. The plugin
  supplies the standard SVG root element and namespace, with default dimensions
  of `200` by `200` and a viewBox of `0 0 200 200` when those attributes are absent.
  A new file starts as an empty SVG for you to customize.
- [`docs/assets/banner.svg`](assets/banner.svg) contains the logo's SVG content
  inlined as a nested `<svg>` element, synced from `docs/assets/logo.svg`, so the
  banner renders without referencing another file. The logo is positioned within
  the banner's viewBox using its original dimensions, with centering offsets
  rounded down to integers.
  The banner has the same default dimensions and viewBox as the logo, and its
  viewBox grows to fit a larger logo.
- [`docs/assets/badge.json`](assets/badge.json) contains the Shields.io badge configuration,
  including the project name, badge colors, and embedded logo markup. Its
  `logoSvg` value is synced from `docs/assets/logo.svg`.

## Customization

During `pyrig sync`, Pyrig enforces the following:

- In [`docs/assets/logo.svg`](assets/logo.svg) and
  [`docs/assets/banner.svg`](assets/banner.svg), the root element is `<svg>` with
  `xmlns="http://www.w3.org/2000/svg"`. Missing `width`, `height`, and `viewBox`
  attributes are filled with default values, but existing logo values are preserved.
- In the banner's nested logo `<svg>`, the logo's attributes and elements are
  mirrored, and `width`, `height`, and `viewBox` match the logo's.
  Its `x` and `y` are the banner viewBox's minimum coordinates plus half
  the remaining width and height, rounded down to integers; these override any
  `x` or `y` set on the logo itself. The logo is drawn at its own size in the
  banner's viewBox units.
  Sync adds and updates content but never removes it, so elements or attributes
  deleted from the logo must also be deleted from the banner's nested `<svg>`.
- The banner's viewBox width and height are raised to at least the logo's width
  and height, so the logo is never cropped. The viewBox's minimum coordinates
  and the banner's `width` and `height` are kept; the viewBox scales to them.
- In [`docs/assets/badge.json`](assets/badge.json), `message` is the project name
  and `logoSvg` is the content of `logo.svg`. Missing `label` defaults to an empty
  string, and missing `labelColor` and `color` default to `white`; existing values
  are preserved.

Artwork, additional SVG attributes and elements, SVG dimensions and viewBoxes,
and badge labels and colors can be customized. Inserting the logo into the banner
requires the logo's dimensions to be integers without units and the banner
viewBox to contain exactly four whitespace-separated integers.

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
