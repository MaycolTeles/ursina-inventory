"""
Module containing the 'Inventory' class.
"""

from typing import Optional

from ursina import Entity, camera, color, destroy, Text


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

        self._create_parent()

    def _create_parent(self) -> None:
        """
        Private Method to create the parent.
        """
        item_parent_args = {
            "parent": self,
            "scale": (1/5, 1/8)
        }

        self.item_parent = Entity(**item_parent_args)

    def find_next_free_spot(self) -> Optional[tuple[int, int]]:
        """
        Method to find the inventory next free spot.
        """
        taken_spots = [(int(item.x), int(item.y)) for item in self.item_parent.children]

        for y in range(self.SIZE[1]):
            for x in range(self.SIZE[0]):
                if not (x, -y) in taken_spots:
                    return (x, -y)

        self._display_error_message("Impossible to add another item in the Inventory: Inventory is full")

    def _display_error_message(self, error_message: str) -> None:
        """
        Method to display an error message.
        """
        error_text = Text(
            text=f"<red>{error_message}",
            parent=camera.ui,
            origin=(0,-1.5),
            x=-.5,
            scale=2
        )

        destroy(error_text, delay=1)
