"""Tests for dictionary-backed SVG configuration files."""

from pathlib import Path
from typing import Any

from pyrig_badge.rig.configs.base.svg import SVGConfigFile


class ConcreteSVGConfigFile(SVGConfigFile):
    """SVG configuration for extension tests."""

    def parent_path(self) -> Path:
        """Return the configuration directory."""
        return Path("configs")

    def stem(self) -> str:
        """Return the configuration filename stem."""
        return "example"

    def _configs(self) -> dict[str, Any]:
        """Return one SVG root element."""
        return {"svg": {}}


class TestSVGConfigFile:
    """Test class."""

    def test_extension(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().extension() == "svg"
