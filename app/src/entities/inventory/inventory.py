"""
Module containing the 'Inventory' class.
"""

from typing import Optional

from ursina import Entity, camera, color

from ..items.item import Item


class Inventory(Entity):
    """
    Class to represent an Inventory.
    """
    SIZE = (5, 8)
    items: list[Item] = []

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

    def append_item(self, item: Item) -> None:
        """
        Method to append an item to inventory.
        """
        self.items.append(item)

    def find_next_free_spot(self) -> Optional[tuple[int, int]]:
        """
        Method to find the inventory next free spot.
        """
        taken_spots = [(int(item.x), int(item.y)) for item in self.item_parent.children]

        for y in range(self.SIZE[1]):
            for x in range(self.SIZE[0]):
                if not (x, -y) in taken_spots:
                    return (x, -y)

        print("NO MORE SPACE IN THE INVENTORY!")
