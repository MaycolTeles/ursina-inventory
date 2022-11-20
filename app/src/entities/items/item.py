"""
Module containing the 'Item' class.
"""

from typing import Any

from ursina import Draggable, color, camera


class Item(Draggable):
    """
    Class to represent an Item.
    """

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        """
        Constructor.
        """
        item_parent = kwargs.get("parent", camera.ui)
        item_model = kwargs.get("model", "quad")
        item_texture = kwargs.get("texture", "sword")
        item_color = kwargs.get("color", color.white)
        item_origin = kwargs.get("origin", (-.5, .5))
        item_position = kwargs.get("position", (0, 0))
        item_z = kwargs.get("z", -.1)

        item_args: dict[str, Any] = {
            "parent": item_parent,
            "model": item_model,
            "texture": item_texture,
            "color": item_color,
            "origin": item_origin,
            "position": item_position,
            "z": item_z
        }

        super().__init__(**item_args)
