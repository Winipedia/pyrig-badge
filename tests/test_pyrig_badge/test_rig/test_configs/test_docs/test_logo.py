"""Test module."""

from pathlib import Path

from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class TestLogoConfigFile:
    """Test class."""

    def test_extension(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.extension() == "svg"

    def test_parent_path(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.parent_path() == Path("docs/assets")

    def test_stem(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.stem() == "logo"

    def test_content(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.content() == LogoConfigFile.I.read_content()

    def test_default_content(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.default_content() == (
            "<svg\n"
            '  xmlns="http://www.w3.org/2000/svg"\n'
            '  width="200"\n'
            '  height="200"\n'
            '  viewBox="0 0 200 200"\n'
            ">\n"
            '  <circle cx="100" cy="100" r="95" fill="none" stroke="black" '
            'stroke-width="4" />\n'
            "  <text\n"
            '    x="100"\n'
            '    y="100"\n'
            '    fill="black"\n'
            '    text-anchor="middle"\n'
            '    dominant-baseline="middle"\n'
            "  >"
            f"{PackageManager.I.project_name()}</text>\n"
            "</svg>\n"
        )
