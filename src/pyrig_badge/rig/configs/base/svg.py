"""Base class for managing dictionary-backed SVG configuration files."""

from abc import abstractmethod
from typing import Any

from pyrig_badge.rig.configs.base.xml import XMLConfigFile


class SVGConfigFile(XMLConfigFile):
    """Manage SVG files using the XML configuration lifecycle."""

    @abstractmethod
    def svg_configs(self) -> dict[str, Any]:
        """Return the SVG-specific configuration dictionary.

        Do not include the root `<svg>` element or the XML namespace declaration.
        Those are automatically added by the `_configs` method.

        Returns:
            A dictionary representing the SVG configuration.
        """

    def extension(self) -> str:
        """Return the SVG file extension without a leading dot."""
        return "svg"

    def _configs(self) -> dict[str, Any]:
        return {
            "svg": {
                "@xmlns": "http://www.w3.org/2000/svg",
                **self.svg_configs(),
            },
        }
