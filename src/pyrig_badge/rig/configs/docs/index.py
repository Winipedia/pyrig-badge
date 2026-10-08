"""Configuration file manager for the documentation landing page."""

from pathlib import Path

from pyrig.rig.configs.docs.index import IndexConfigFile as BaseIndexConfigFile
from pyrig.rig.tools.docs.builder import DocsBuilder

from pyrig_badge.rig.configs.base.badges import BadgesConfigFile


class IndexConfigFile(BadgesConfigFile, BaseIndexConfigFile):
    """Generate the documentation landing page with its logo and badges."""

    def logo_path(self) -> Path:
        """Return the logo path relative to the documentation source directory.

        Returns:
            Documentation-relative path to the configured logo asset.
        """
        return super().logo_path().relative_to(DocsBuilder.I.docs_dir())
