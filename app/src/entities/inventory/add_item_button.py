"""
Module containing the "AddItemButton" Class.
"""

import random
from typing import Any

from ursina import Button, color, Tooltip

from .inventory import Inventory


class AddItemButton(Button):
    """
    Class to represent the button to add a item to inventory.
    """

    def __init__(self, **kwargs: dict[str, Any]):
        """
        Constructor.
        """
        self.inventory: Inventory = kwargs.get("inventory", Inventory())

        add_item_button_args = {
            "scale": (.1, .1),
            "x": -.5,
            "color": color.lime.tint(-.25),
            "text": "+",
            "tooltip": Tooltip("Add random item to inventory."),
            "on_click": self.add_item_to_inventory
        }

        super().__init__(**add_item_button_args)

    def add_item_to_inventory(self) -> None:
        """
        Method to add the item into the inventory.
        """
        item_choices = ["bag", "bow_arrow", "gem", "orb", "sword"]
        self.inventory.append_item(random.choice(item_choices))
