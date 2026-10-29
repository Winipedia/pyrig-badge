"""Test module."""

from pathlib import Path
from typing import override

from pyrig_badge.rig.configs.base.badges import (
    BadgesConfigFile as BadgeMarkdownConfigFile,
)


class TestBadgesConfigFile:
    """Test class."""

    def test_badges_content(self) -> None:
        """Test method."""
        assert (
            ConcreteBadgesConfigFile().logo_content()
            in ConcreteBadgesConfigFile().badges_content()
        )

    def test_image_path(self) -> None:
        """Test method."""
        assert ConcreteBadgesConfigFile().image_path() == Path("docs/assets/banner.svg")

    def test_logo_content(self) -> None:
        """Test method."""
        assert ConcreteBadgesConfigFile().logo_content() == (
            "[![pyrig-badge](docs/assets/banner.svg)](docs/assets/banner.svg)"
        )


class ConcreteBadgesConfigFile(BadgeMarkdownConfigFile):
    """Test class."""

    @override
    def heading(self) -> str:
        """Test method."""
        return "Test project"

    @override
    def parent_path(self) -> Path:
        """Test method."""
        return Path()

    @override
    def stem(self) -> str:
        """Test method."""
        return "test"
