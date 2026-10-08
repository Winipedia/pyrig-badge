"""Test module."""

from pyrig_badge.rig.configs.docs.index import IndexConfigFile


class TestIndexConfigFile:
    """Test class."""

    def test_logo_path(self) -> None:
        """Test method."""
        assert IndexConfigFile.I.logo_path().as_posix() == "assets/logo.svg"
