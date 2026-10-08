"""Test module."""

from pathlib import Path

from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class TestLogoConfigFile:
    """Test class."""

    def test_parent_path(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.parent_path() == Path("docs/assets")

    def test_stem(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.stem() == "logo"

    def test__configs(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.configs() == LogoConfigFile.I.load()

    def test_default_configs(self) -> None:
        """Test method."""
        assert LogoConfigFile.I.default_configs() == {
            "svg": {
                "@xmlns": "http://www.w3.org/2000/svg",
                "@width": "200",
                "@height": "200",
                "@viewBox": "0 0 200 200",
                "circle": {
                    "@cx": "100",
                    "@cy": "100",
                    "@r": "95",
                    "@fill": "none",
                    "@stroke": "black",
                    "@stroke-width": "4",
                },
                "text": {
                    "@x": "100",
                    "@y": "100",
                    "@fill": "black",
                    "@text-anchor": "middle",
                    "@dominant-baseline": "middle",
                    "#text": PackageManager.I.project_name(),
                },
            },
        }
