"""Test module."""

from pathlib import Path

from pyrig_badge.rig.configs.base.badges import (
    BadgesConfigFile as BadgeMarkdownConfigFile,
)


class ConcreteBadgesConfigFile(BadgeMarkdownConfigFile):
    """Test class."""

    def heading(self) -> str:
        """Test method."""
        return "Test project"

    def parent_path(self) -> Path:
        """Test method."""
        return Path()

    def stem(self) -> str:
        """Test method."""
        return "test"


class TestBadgesConfigFile:
    """Test class."""

    def test_badges_content(self) -> None:
        """Test method."""
        assert (
            ConcreteBadgesConfigFile().logo_content()
            in ConcreteBadgesConfigFile().badges_content()
        )

    def test_logo_content(self) -> None:
        """Test method."""
        assert ConcreteBadgesConfigFile().logo_content() == (
            "[![pyrig-badge](docs/assets/logo.svg)](docs/assets/logo.svg)"
        )

    def test_logo_path(self) -> None:
        """Test method."""
        assert ConcreteBadgesConfigFile().logo_path() == Path("docs/assets/logo.svg")
