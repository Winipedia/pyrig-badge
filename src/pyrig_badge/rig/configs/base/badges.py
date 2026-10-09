"""Badge-augmented Markdown configuration base class."""

from pathlib import Path

from pyrig.rig.configs.base.badges import BadgesConfigFile as BaseBadgesConfigFile
from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.banner import BannerConfigFile


class BadgesConfigFile(BaseBadgesConfigFile):
    """Add the generated project banner before the base class's badge groups."""

    def badges_content(self) -> str:
        """Return the project banner followed by the generated badge groups.

        Returns:
            Markdown containing the banner image and the base badge content.
        """
        return f"""{self.logo_content()}

{super().badges_content()}"""

    def logo_content(self) -> str:
        """Return a linked Markdown image for the project's banner.

        Returns:
            Markdown linking the banner image to its own file, using the
            project name as its alternative text.
        """
        image_path = self.image_path().as_posix()
        return f"[![{PackageManager.I.project_name()}]({image_path})]({image_path})"

    def image_path(self) -> Path:
        """Return the configured banner file's path.

        Returns:
            Path to the project's banner asset.
        """
        return BannerConfigFile.I.path()
