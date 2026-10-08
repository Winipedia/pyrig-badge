"""Base class for managing dictionary-backed XML configuration files."""

from typing import Any

import xmltodict
from pyrig.core.strings import read_text_utf8, write_text_utf8
from pyrig.rig.configs.base.config_file import DictConfigFile


class XMLConfigFile(DictConfigFile):
    """Manage XML using element names, `@` attributes, and `#text` content.

    Repeated elements are represented as lists. Subclasses must implement
    `parent_path()`, `stem()`, and `_configs()`, returning one root element.
    Values should use the strings and structures returned by `xmltodict.parse`.
    This dictionary representation does not preserve mixed-content ordering.
    """

    def _dump(self, configs: dict[str, Any]) -> None:
        """Write XML as UTF-8 with a declaration and default indentation."""
        content = xmltodict.unparse(
            configs,
            pretty=True,
        )
        write_text_utf8(self.path(), f"{content}\n")

    def _load(self) -> dict[str, Any]:
        """Parse XML without expanding entities."""
        return xmltodict.parse(read_text_utf8(self.path()), disable_entities=True)

    def extension(self) -> str:
        """Return the XML file extension without a leading dot."""
        return "xml"
