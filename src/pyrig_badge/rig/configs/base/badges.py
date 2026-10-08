"""Badge-augmented Markdown configuration base class."""

from pathlib import Path

from pyrig.rig.configs.base.badges import BadgesConfigFile as BaseBadgesConfigFile
from pyrig.rig.tools.packages.manager import PackageManager

from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class BadgesConfigFile(BaseBadgesConfigFile):
    """Add the generated project logo before the base class's badge groups."""

    def badges_content(self) -> str:
        """Return the project logo followed by the generated badge groups.

        Returns:
            Markdown containing the logo image and the base badge content.
        """
        return f"""{self.logo_content()}

{super().badges_content()}"""

    def logo_content(self) -> str:
        """Return a linked Markdown image for the project's logo.

        Returns:
            Markdown linking the logo image to its own file, using the
            project name as its alternative text.
        """
        logo_path = self.logo_path().as_posix()
        return f"[![{PackageManager.I.project_name()}]({logo_path})]({logo_path})"

    def logo_path(self) -> Path:
        """Return the configured logo file's path.

        Returns:
            Path to the project's logo asset.
        """
        return LogoConfigFile.I.path()
