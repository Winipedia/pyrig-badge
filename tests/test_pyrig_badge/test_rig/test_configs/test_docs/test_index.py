"""Test module."""

from pyrig_badge.rig.configs.docs.index import IndexConfigFile


class TestIndexConfigFile:
    """Test class."""

    def test_image_path(self) -> None:
        """Test method."""
        assert IndexConfigFile.I.image_path().as_posix() == "assets/banner.svg"
