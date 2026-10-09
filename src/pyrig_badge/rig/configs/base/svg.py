"""Base class for managing dictionary-backed SVG configuration files."""

from abc import abstractmethod
from typing import Any

from pyrig_badge.rig.configs.base.xml import XMLConfigFile


class SVGConfigFile(XMLConfigFile):
    """Manage SVG files using the XML configuration lifecycle."""

    @abstractmethod
    def svg_configs(self) -> dict[str, Any]:
        """Return the SVG-specific configuration dictionary.

        The `_configs` method adds the root `<svg>` element, namespace,
        dimensions, and viewBox. Returned attributes override those defaults.

        Returns:
            A dictionary representing the SVG configuration.
        """

    def extension(self) -> str:
        """Return the SVG file extension without a leading dot."""
        return "svg"

    def _configs(self) -> dict[str, Any]:
        return {
            "svg": {
                "@xmlns": "http://www.w3.org/2000/svg",
                "@width": self.width(),
                "@height": self.height(),
                "@viewBox": self.view_box(),
                **self.svg_configs(),
            },
        }

    def insert_svg(self, svg: "type[SVGConfigFile]") -> dict[str, Any]:
        """Return `svg`'s content as a nested `<svg>` element.

        The nested element mirrors the loaded root of `svg`, including its
        attributes and children, so this SVG is self-contained and changes to
        `svg` propagate on sync. Its `width`, `height`, and `viewBox` are
        `svg`'s values, and its `x` and `y` place it at this SVG's viewBox
        origin plus half the remaining space, rounded down to integers; these
        five attributes override any same-named attributes of `svg`. The
        inserted dimensions must be integer strings and are used unchanged as
        this SVG's user-space dimensions, so `svg` is not scaled to fit.

        Args:
            svg: The `SVGConfigFile` subclass whose content is inserted. If its
                file does not exist, only the generated attributes are set.

        Returns:
            A dictionary representing a nested `<svg>` element containing
            `svg`'s content, sized to its dimensions and positioned within
            this SVG's viewBox.

        Raises:
            ValueError: If the inserted dimensions are not integer strings or
                the viewBox is not four whitespace-separated integer values.
        """
        x = int(self.view_box_x()) + (
            (int(self.view_box_width()) - int(svg.I.width())) // 2
        )
        y = int(self.view_box_y()) + (
            (int(self.view_box_height()) - int(svg.I.height())) // 2
        )
        return {
            "svg": {
                **svg.I.safe_load_svg(),
                "@x": str(x),
                "@y": str(y),
                "@width": svg.I.width(),
                "@height": svg.I.height(),
                "@viewBox": svg.I.view_box(),
            },
        }

    def width(self) -> str:
        """Return the stored SVG width, or `"200"` if absent."""
        return self.safe_load_svg().get("@width", "200")

    def height(self) -> str:
        """Return the stored SVG height, or `"200"` if absent."""
        return self.safe_load_svg().get("@height", "200")

    def view_box_x(self) -> str:
        """Return the minimum x-coordinate of the viewBox."""
        x, _, _, _ = self.view_box_attributes()
        return x

    def view_box_y(self) -> str:
        """Return the minimum y-coordinate of the viewBox."""
        _, y, _, _ = self.view_box_attributes()
        return y

    def view_box_height(self) -> str:
        """Return the height of the viewBox."""
        _, _, _, height = self.view_box_attributes()
        return height

    def view_box_width(self) -> str:
        """Return the width of the viewBox."""
        _, _, width, _ = self.view_box_attributes()
        return width

    def view_box_attributes(self) -> tuple[str, str, str, str]:
        """Split the viewBox into its four whitespace-separated values.

        Returns:
            Minimum x, minimum y, width, and height, in that order, as strings.

        Raises:
            ValueError: If the viewBox does not contain exactly four
                whitespace-separated values.
        """
        x, y, width, height = self.view_box().split()
        return x, y, width, height

    def view_box(self) -> str:
        """Return the stored viewBox, or `"0 0 200 200"` if absent."""
        return self.safe_load_svg().get("@viewBox", "0 0 200 200")

    def safe_load_svg(self) -> dict[str, Any]:
        """Return the loaded SVG root, or an empty dict if the file/root is absent."""
        return self.safe_load().get("svg", {})
