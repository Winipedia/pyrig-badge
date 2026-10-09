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

    def svg_configs(self) -> dict[str, Any]:
        """Return one child element for the SVG root."""
        return {"smth": {}}


class TestSVGConfigFile:
    """Test class."""

    def test_extension(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().extension() == "svg"

    def test_svg_configs(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().svg_configs() == {"smth": {}}

    def test__configs(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile()._configs() == {  # noqa: SLF001
            "svg": {
                "@xmlns": "http://www.w3.org/2000/svg",
                "smth": {},
            },
        }
