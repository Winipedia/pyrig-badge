"""Configuration manager for the generated documentation logo."""

from pathlib import Path
from typing import Any

from pyrig.rig.tools.docs.builder import DocsBuilder
from pyrig.rig.tools.packages.manager import PackageManager

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

    def _configs(self) -> dict[str, Any]:
        """Return existing logo configuration or the default SVG structure.

        Returns:
            Parsed file content when non-empty, otherwise the default SVG.
        """
        return self.safe_load() or self.default_configs()

    def default_configs(self) -> dict[str, Any]:
        """Build a circular SVG logo containing the current project name.

        Returns:
            XML configuration for a 200-by-200 SVG with centered project-name
            text inside a circle.
        """
        return {
            "svg": {
                "@xmlns": "http://www.w3.org/2000/svg",
                "@width": "200",
                "@height": "200",
                "@viewBox": "0 0 200 200",
                "circle": {
                    "@cx": "100",
                    "@cy": "100",
                    "@r": "95",
                    "@fill": "none",
                    "@stroke": "black",
                    "@stroke-width": "4",
                },
                "text": {
                    "@x": "100",
                    "@y": "100",
                    "@fill": "black",
                    "@text-anchor": "middle",
                    "@dominant-baseline": "middle",
                    "#text": PackageManager.I.project_name(),
                },
            },
        }
