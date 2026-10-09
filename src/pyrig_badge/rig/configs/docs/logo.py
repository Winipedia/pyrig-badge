"""Configuration manager for the generated documentation logo."""

from pathlib import Path
from typing import Any

from pyrig.rig.tools.docs.builder import DocsBuilder

from pyrig_badge.rig.configs.base.svg import SVGConfigFile


class LogoConfigFile(SVGConfigFile):
    """Manage the project logo SVG under the documentation assets directory."""

    def parent_path(self) -> Path:
        """Return the documentation assets directory.

        Returns:
            The documentation source directory joined with `"assets"`.
        """
        return DocsBuilder.I.docs_dir() / "assets"

    def stem(self) -> str:
        """Return the logo filename stem."""
        return "logo"

    def svg_configs(self) -> dict[str, Any]:
        """Return no additional SVG elements or attributes.

        Returns:
            An empty dictionary; the base SVG config supplies the required
            root element, namespace, dimensions, and viewBox, and Pyrig merges
            existing SVG content.
        """
        return {}
