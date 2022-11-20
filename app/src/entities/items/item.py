"""
Module containing the 'Item' class.
"""

from typing import Any

from ursina import Button, camera, color


class Item(Button):
    """
    Class to represent an Item.
    """

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        """
        Constructor.
        """
        item_parent = kwargs.get("parent", camera.ui)
        item_color = kwargs.get("color", color.red)
        item_position = kwargs.get("position", (0, 0))
        item_origin = kwargs.get("origin", (-.5, .5))

        item_args: dict[str, Any] = {
            "parent": item_parent,
            "position": item_position,
            "color": item_color,
            "origin": item_origin
        }

        super().__init__(**item_args)
