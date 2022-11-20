"""
Module containing the 'Inventory' class.
"""

from typing import Any, Optional

from ursina import Entity, Button, camera, color


class Inventory(Entity):
    """
    Class to represent an Inventory.
    """
    SIZE = (5, 8)

    def __init__(self) -> None:
        """
        Constructor.
        """
        inventory_args = {
            "parent": camera.ui,
            "model": "quad",
            "scale": (.5, .8),
            "origin": (-.5, .5),
            "position": (-.3, .4),
            "texture": "white_cube",
            "texture_scale": self.SIZE,
            "color": color.dark_gray
        }

        super().__init__(**inventory_args)

        item_parent_args = {
            "parent": self,
            "scale": (1/5, 1/8)
        }

        self.item_parent = Entity(**item_parent_args)

    def append_item(self, item: str) -> None:
        """
        Method to append an item to inventory.
        """
        item_args: dict[str, Any] = {
            "parent": self.item_parent,
            "model": "quad",
            "origin": (-.5, .5),
            "color": color.random_color(),
            "z": -.1,
            "position": self.find_next_free_spot()
        }

        Button(**item_args)

    def find_next_free_spot(self) -> Optional[tuple]:
        """
        Method to find the inventory next free spot.
        """
        taken_spots = [(int(item.x), int(item.y)) for item in self.item_parent.children]

        for y in range(self.SIZE[1]):
            for x in range(self.SIZE[0]):
                if not (x, -y) in taken_spots:
                    return (x, -y)
