"""Test module."""

import pytest

from pyrig_badge.rig.configs.base.svg import SVGConfigFile
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

    def test_view_box(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test method."""
        monkeypatch.setattr(SVGConfigFile, "view_box", lambda _: "5 6 300 100")
        monkeypatch.setattr(LogoConfigFile, "width", lambda _: "200")
        monkeypatch.setattr(LogoConfigFile, "height", lambda _: "400")
        assert BannerConfigFile.I.view_box() == "5 6 300 400"

    def test_svg_configs(self) -> None:
        """Test method."""
        logo = BannerConfigFile.I.svg_configs()["svg"]
        assert logo["@viewBox"] == LogoConfigFile.I.view_box()
        assert logo["@width"] == LogoConfigFile.I.width()
        assert logo["@height"] == LogoConfigFile.I.height()
