"""Configuration manager for the Shields.io badge JSON asset."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.json import JSONDictConfigFile
from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class BadgeConfigFile(JSONDictConfigFile):
    """Generate project badge data and embed the configured logo SVG."""

    def dependencies(self) -> Iterable[type[ConfigFile[Any]]]:
        """Return the logo asset required to construct this badge.

        Returns:
            The logo configuration file, appended to inherited dependencies.
        """
        return (*super().dependencies(), LogoConfigFile)

    def _configs(self) -> dict[str, Any]:
        """Build badge data using optional values from the existing JSON file.

        Returns:
            Badge configuration with label and color defaults, the current
            project name, and the logo's SVG content.
        """
        return {
            "label": self.safe_load().get("label", ""),
            "message": PackageManager.I.project_name(),
            "labelColor": self.safe_load().get("labelColor", "white"),
            "color": self.safe_load().get("color", "white"),
            "logoSvg": LogoConfigFile.I.read_content(),
        }

    def parent_path(self) -> Path:
        """Return the directory containing the logo and badge assets.

        Returns:
            Parent directory used by the logo configuration file.
        """
        return LogoConfigFile.I.parent_path()

    def stem(self) -> str:
        """Return the filename stem `"badge"`."""
        return "badge"
