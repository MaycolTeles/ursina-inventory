"""
Module containing the 'Item' class.
"""

from __future__ import annotations
from typing import Any

from ursina import Draggable, color, camera, Tooltip


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

        name = item_texture.replace('_', ' ').title()
        self.tooltip = Tooltip(name)
        self.tooltip.background.color = color.color(0,0,0,.8)

        self.item_parent = item_parent

    def drop(self) -> None:
        """
        Method to round the item position on drop.
        """
        self.x = int(self.x)
        self.y = int(self.y)

        self._check_if_swap()

    def drag(self) -> None:
        """
        Method to drag and swap the items.
        """
        self.org_pos = (self.x, self.y)

    def _check_if_swap(self) -> None:
        """
        Private Method to check if there's a need to swap the item.
        """
        for item in self.item_parent.children:
            if item == self:
                continue

            if item.x == self.x and item.y == self.y:
                self._swap(item)

    def _swap(self, item: Item) -> None:
        """
        Method to swap the item.
        """
        item.position = self.org_pos
