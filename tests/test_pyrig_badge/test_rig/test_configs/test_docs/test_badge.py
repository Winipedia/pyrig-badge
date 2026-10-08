"""Test module."""

from pyrig.core.strings import read_text_utf8
from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.badge import BadgeConfigFile
from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class TestBadgeConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        assert BadgeConfigFile.I.configs() == {
            "label": "",
            "message": PackageManager.I.project_name(),
            "labelColor": "white",
            "color": "white",
            "logoSvg": read_text_utf8(LogoConfigFile.I.path()),
        }

    def test_parent_path(self) -> None:
        """Test method."""
        assert BadgeConfigFile.I.parent_path() == LogoConfigFile.I.parent_path()

    def test_stem(self) -> None:
        """Test method."""
        assert BadgeConfigFile.I.stem() == "badge"

    def test_dependencies(self) -> None:
        """Test method."""
        assert tuple(BadgeConfigFile.I.dependencies()) == (LogoConfigFile,)
