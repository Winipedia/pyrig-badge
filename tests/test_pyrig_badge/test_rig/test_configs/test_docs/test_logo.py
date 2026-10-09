"""Test module."""

from pathlib import Path

from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class TestLogoConfigFile:
    """Test class."""

    def test_parent_path(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.parent_path() == Path("docs/assets")

    def test_stem(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.stem() == "logo"

    def test_svg_configs(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.svg_configs() == {}
