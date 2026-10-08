"""Tests for dictionary-backed XML configuration files."""

from contextlib import chdir
from pathlib import Path
from typing import Any

from pyrig_badge.rig.configs.base.xml import XMLConfigFile


class ConcreteXMLConfigFile(XMLConfigFile):
    """XML configuration for isolated lifecycle tests."""

    def parent_path(self) -> Path:
        """Return the configuration directory."""
        return Path("configs")

    def stem(self) -> str:
        """Return the configuration filename stem."""
        return "example"

    def _configs(self) -> dict[str, Any]:
        """Return attributes, repeated elements, and escaped text."""
        return {
            "config": {
                "@xmlns": "https://example.com/config",
                "@version": "1",
                "item": [
                    {"@name": "first", "#text": "A & <B>"},
                    {"@name": "second", "#text": "calf\u00e9"},
                ],
                "empty": None,
            },
        }


class TestXMLConfigFile:
    """Test XML parsing, serialization, and the inherited config lifecycle."""

    def test_extension(self) -> None:
        """Use XML as the default extension."""
        assert ConcreteXMLConfigFile().extension() == "xml"

    def test__dump(self, tmp_path: Path) -> None:
        """Test method."""
        config = ConcreteXMLConfigFile()
        with chdir(tmp_path):
            config.create_file()
            config._dump(config.configs())  # noqa: SLF001
            content = config.path().read_text(encoding="utf-8")
            assert content == (
                '<?xml version="1.0" encoding="utf-8"?>\n'
                '<config xmlns="https://example.com/config" version="1">\n'
                '\t<item name="first">A &amp; &lt;B&gt;</item>\n'
                '\t<item name="second">calf\u00e9</item>\n'
                "\t<empty></empty>\n"
                "</config>\n"
            )

    def test__load(self, tmp_path: Path) -> None:
        """Test method."""
        config = ConcreteXMLConfigFile()
        with chdir(tmp_path):
            config.create_file()
            config.path().write_text(
                '<config xmlns="https://example.com/config" version="1">'
                '<item name="first">A &amp; &lt;B&gt;</item>'
                '<item name="second">calf\u00e9</item>'
                "<empty/>"
                "</config>",
                encoding="utf-8",
            )
            assert config._load() == config.configs()  # noqa: SLF001
