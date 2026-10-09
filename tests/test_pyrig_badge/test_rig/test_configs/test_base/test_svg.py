"""Tests for dictionary-backed SVG configuration files."""

from contextlib import chdir
from pathlib import Path
from typing import Any

from pyrig_badge.rig.configs.base.svg import SVGConfigFile

TEST_VIEW_BOX_ATTRIBUTES = ("10", "20", "300", "400")


class ConcreteSVGConfigFile(SVGConfigFile):
    """SVG configuration for SVG defaults and insertion tests."""

    def parent_path(self) -> Path:
        """Return the configuration directory."""
        return Path("configs")

    def stem(self) -> str:
        """Return the configuration filename stem."""
        return "example"

    def svg_configs(self) -> dict[str, Any]:
        """Return one child element for the SVG root."""
        return {"smth": {}}


class ConcreteSmallSVGConfigFile(SVGConfigFile):
    """SVG configuration with fixed, smaller dimensions for insertion tests."""

    def parent_path(self) -> Path:
        """Return the configuration directory."""
        return Path("configs")

    def stem(self) -> str:
        """Return the configuration filename stem."""
        return "small"

    def svg_configs(self) -> dict[str, Any]:
        """Return no additional SVG elements or attributes."""
        return {}

    def width(self) -> str:
        """Return a fixed width smaller than the default."""
        return "50"

    def height(self) -> str:
        """Return a fixed height smaller than the default."""
        return "80"


class ConcreteOffsetSVGConfigFile(ConcreteSVGConfigFile):
    """SVG configuration with a non-default viewBox for parsing tests."""

    def view_box(self) -> str:
        """Return a viewBox with distinct coordinates and dimensions."""
        return " ".join(TEST_VIEW_BOX_ATTRIBUTES)


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
                "@width": "200",
                "@height": "200",
                "@viewBox": "0 0 200 200",
                "smth": {},
            },
        }

    def test_insert_svg(self, tmp_path: Path) -> None:
        """Test method."""
        with chdir(tmp_path):
            assert ConcreteSVGConfigFile().insert_svg(ConcreteSmallSVGConfigFile) == {
                "svg": {
                    "@x": "75",
                    "@y": "60",
                    "@width": "50",
                    "@height": "80",
                    "@viewBox": "0 0 200 200",
                },
            }

            small = ConcreteSmallSVGConfigFile()
            small.path().parent.mkdir()
            small.path().write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5 8">'
                '<circle r="1"/></svg>',
                encoding="utf-8",
            )
            ConcreteSmallSVGConfigFile.load.cache_clear()
            assert ConcreteSVGConfigFile().insert_svg(ConcreteSmallSVGConfigFile) == {
                "svg": {
                    "@xmlns": "http://www.w3.org/2000/svg",
                    "@viewBox": "0 0 5 8",
                    "circle": {"@r": "1"},
                    "@x": "75",
                    "@y": "60",
                    "@width": "50",
                    "@height": "80",
                },
            }
            ConcreteSmallSVGConfigFile.load.cache_clear()

    def test_width(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().width() == "200"

    def test_height(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().height() == "200"

    def test_view_box(self) -> None:
        """Test method."""
        assert ConcreteSVGConfigFile().view_box() == "0 0 200 200"

    def test_view_box_x(self) -> None:
        """Return the viewBox's minimum x-coordinate."""
        assert ConcreteOffsetSVGConfigFile().view_box_x() == TEST_VIEW_BOX_ATTRIBUTES[0]

    def test_view_box_y(self) -> None:
        """Return the viewBox's minimum y-coordinate."""
        assert ConcreteOffsetSVGConfigFile().view_box_y() == TEST_VIEW_BOX_ATTRIBUTES[1]

    def test_view_box_height(self) -> None:
        """Return the viewBox height."""
        assert (
            ConcreteOffsetSVGConfigFile().view_box_height()
            == TEST_VIEW_BOX_ATTRIBUTES[3]
        )

    def test_view_box_width(self) -> None:
        """Return the viewBox width."""
        assert (
            ConcreteOffsetSVGConfigFile().view_box_width()
            == TEST_VIEW_BOX_ATTRIBUTES[2]
        )

    def test_view_box_attributes(self) -> None:
        """Parse viewBox coordinates and dimensions in order."""
        assert (
            ConcreteOffsetSVGConfigFile().view_box_attributes()
            == TEST_VIEW_BOX_ATTRIBUTES
        )

    def test_safe_load_svg(self, tmp_path: Path) -> None:
        """Return the parsed SVG root, or an empty dict when absent."""
        config = ConcreteSVGConfigFile()
        with chdir(tmp_path):
            assert config.safe_load_svg() == {}

            config.path().parent.mkdir()
            config.path().write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="100"/>',
                encoding="utf-8",
            )
            assert config.safe_load_svg() == {
                "@xmlns": "http://www.w3.org/2000/svg",
                "@width": "100",
            }
