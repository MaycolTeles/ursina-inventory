"""
Module containing the 'Inventory' class.
"""

from ursina import Entity, camera, color


class Inventory(Entity):
    """
    Class to represent an Inventory.
    """

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
            "texture_scale": (5, 8),
            "color": color.dark_gray
        }

        super().__init__(**inventory_args)

        item_parent_args = {
            "parent": self,
            "scale": (1/5, 1/8)
        }

        self.item_parent = Entity(**item_parent_args)
