"""Configuration manager for the generated documentation banner."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pyrig.rig.configs.base.config_file import ConfigFile

from pyrig_badge.rig.configs.base.svg import SVGConfigFile
from pyrig_badge.rig.configs.docs.logo import LogoConfigFile


class BannerConfigFile(SVGConfigFile):
    """Manage the banner SVG, centering the logo within a viewBox that fits it."""

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

    def view_box(self) -> str:
        """Return the stored viewBox, enlarged to fit the logo if needed.

        The inserted logo is sized in the banner's user units, so the viewBox
        width and height are raised to at least the logo's width and height
        to prevent cropping. The minimum coordinates are kept, and the
        banner's `width` and `height` are unchanged because the viewBox
        scales to them.

        Returns:
            The viewBox as four whitespace-separated integers.

        Raises:
            ValueError: If the stored viewBox does not contain exactly four
                whitespace-separated values, or its size or the logo's
                dimensions are not integers.
        """
        x, y, width, height = super().view_box().split()
        width = max(int(width), int(LogoConfigFile.I.width()))
        height = max(int(height), int(LogoConfigFile.I.height()))
        return f"{x} {y} {width} {height}"

    def svg_configs(self) -> dict[str, Any]:
        """Return the logo's SVG content inserted within the banner's viewBox.

        Centering offsets are rounded down to integers by `insert_svg`.

        Returns:
            A dictionary representing a nested `<svg>` element that mirrors
            the logo's content.
        """
        return self.insert_svg(LogoConfigFile)
