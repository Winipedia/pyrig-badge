"""Configuration manager for the generated documentation banner."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pyrig.rig.configs.base.config_file import ConfigFile

from pyrig_badge.rig.configs.base.svg import SVGConfigFile
from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class BannerConfigFile(SVGConfigFile):
    """Manage the banner SVG, positioning the logo within its viewBox."""

    def dependencies(self) -> Iterable[type[ConfigFile[Any]]]:
        """Return the logo config file as a dependency.

        Returns:
            A tuple of config file classes that must be validated first.
        """
        return (*super().dependencies(), LogoConfigFile)

    def parent_path(self) -> Path:
        """Return the documentation assets directory.

        Returns:
            The same directory used by the project logo.
        """
        return LogoConfigFile.I.parent_path()

    def stem(self) -> str:
        """Return the banner filename stem."""
        return "banner"

    def svg_configs(self) -> dict[str, Any]:
        """Return the logo embedded within the banner's viewBox.

        Centering offsets are rounded down to integers by `embed_svg`.

        Returns:
            A dictionary representing an `<image>` element for the logo.
        """
        return self.embed_svg(LogoConfigFile)
