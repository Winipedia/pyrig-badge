"""Configuration manager for the generated documentation logo."""

from pathlib import Path

from pyrig.rig.configs.base.string_ import StringConfigFile
from pyrig.rig.tools.docs.builder import DocsBuilder
from pyrig.rig.tools.packages.manager import PackageManager


class LogoConfigFile(StringConfigFile):
    """Manage the project logo SVG under the documentation assets directory."""

    def extension(self) -> str:
        """Return the SVG file extension without a leading dot."""
        return "svg"

    def parent_path(self) -> Path:
        """Return the documentation assets directory.

        Returns:
            The documentation source directory joined with `"assets"`.
        """
        return DocsBuilder.I.docs_dir() / "assets"

    def stem(self) -> str:
        """Return the logo filename stem."""
        return "logo"

    def content(self) -> str:
        """Return existing logo content or generated default SVG markup.

        Returns:
            Existing file content when non-empty, otherwise the default SVG.
        """
        return self.read_content() or self.default_content()

    def default_content(self) -> str:
        """Build a circular SVG logo containing the current project name.

        Returns:
            A 200-by-200 SVG with centered project-name text inside a circle.
        """
        project_name = PackageManager.I.project_name()
        return f"""<svg
  xmlns="http://www.w3.org/2000/svg"
  width="200"
  height="200"
  viewBox="0 0 200 200"
>
  <circle cx="100" cy="100" r="95" fill="none" stroke="black" stroke-width="4" />
  <text
    x="100"
    y="100"
    fill="black"
    text-anchor="middle"
    dominant-baseline="middle"
  >{project_name}</text>
</svg>
"""
