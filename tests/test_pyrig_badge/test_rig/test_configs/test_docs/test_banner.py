"""Test module."""

from pyrig_badge.rig.configs.docs.banner import BannerConfigFile
from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class TestBannerConfigFile:
    """Test class."""

    def test_dependencies(self) -> None:
        """Test method."""
        assert BannerConfigFile.I.dependencies() == (LogoConfigFile,)

    def test_parent_path(self) -> None:
        """Test method."""
        assert BannerConfigFile.I.parent_path() == LogoConfigFile.I.parent_path()

    def test_stem(self) -> None:
        """Test method."""
        assert BannerConfigFile.I.stem() == "banner"

    def test_svg_configs(self) -> None:
        """Test method."""
        assert BannerConfigFile.I.svg_configs()["image"]["@href"] == "logo.svg"
