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

    def embed_svg(self, svg: "type[SVGConfigFile]") -> dict[str, Any]:
        """Return an `<image>` element positioned within this SVG's viewBox.

        Position uses the viewBox origin and half the remaining space, rounded
        down to an integer. Embedded dimensions must be integer strings and
        are used unchanged as this SVG's user-space dimensions.

        Args:
            svg: The `SVGConfigFile` subclass to embed, referenced by path
                relative to this file's parent directory. Its path must be
                beneath that directory.

        Returns:
            A dictionary representing an `<image>` element sized to `svg`'s
            dimensions and positioned within this SVG's viewBox.

        Raises:
            ValueError: If the embedded path is not beneath this file's parent,
                the embedded dimensions are not integer strings, or the
                viewBox is not four whitespace-separated integer values.
        """
        x = self.view_box_x() + ((self.view_box_width() - int(svg.I.width())) // 2)
        y = self.view_box_y() + ((self.view_box_height() - int(svg.I.height())) // 2)
        return {
            "image": {
                "@href": svg.I.path().relative_to(self.parent_path()).as_posix(),
                "@x": str(x),
                "@y": str(y),
                "@width": svg.I.width(),
                "@height": svg.I.height(),
            },
        }

    def width(self) -> str:
        """Return the stored SVG width, or `"200"` if absent."""
        return self.safe_load_svg().get("@width", "200")

    def height(self) -> str:
        """Return the stored SVG height, or `"200"` if absent."""
        return self.safe_load_svg().get("@height", "200")

    def view_box_x(self) -> int:
        """Return the minimum x-coordinate of the viewBox."""
        x, _, _, _ = self.view_box_attributes()
        return x

    def view_box_y(self) -> int:
        """Return the minimum y-coordinate of the viewBox."""
        _, y, _, _ = self.view_box_attributes()
        return y

    def view_box_height(self) -> int:
        """Return the height of the viewBox."""
        _, _, _, height = self.view_box_attributes()
        return height

    def view_box_width(self) -> int:
        """Return the width of the viewBox."""
        _, _, width, _ = self.view_box_attributes()
        return width

    def view_box_attributes(self) -> tuple[int, int, int, int]:
        """Parse the viewBox as four whitespace-separated integers.

        Returns:
            Minimum x, minimum y, width, and height, in that order.

        Raises:
            ValueError: If the viewBox does not contain exactly four
                whitespace-separated integer values.
        """
        view_box = self.view_box().split()
        x, y, width, height = view_box
        return int(x), int(y), int(width), int(height)

    def view_box(self) -> str:
        """Return the stored viewBox, or `"0 0 200 200"` if absent."""
        return self.safe_load_svg().get("@viewBox", "0 0 200 200")

    def safe_load_svg(self) -> dict[str, Any]:
        """Return the loaded SVG root, or an empty dict if the file/root is absent."""
        return self.safe_load().get("svg", {})
