"""Base class for managing dictionary-backed SVG configuration files."""

from pyrig_badge.rig.configs.base.xml import XMLConfigFile


class SVGConfigFile(XMLConfigFile):
    """Manage SVG files using the XML configuration lifecycle."""

    def extension(self) -> str:
        """Return the SVG file extension without a leading dot."""
        return "svg"
