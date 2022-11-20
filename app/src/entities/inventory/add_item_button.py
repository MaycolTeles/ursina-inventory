"""
Module containing the "AddItemButton" Class.
"""

import random
from typing import Any

from ursina import Button, color, Tooltip

from .inventory import Inventory
from ..items.item import Item


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
        Private Method to add the item into the inventory.
        """
        item_types = ["bag", "bow_arrow", "gem", "orb", "sword"]
        selected_item_type = random.choice(item_types)

        item = self._get_item(selected_item_type)
        self.inventory.append_item(item)

    def _get_item(self, item_type: str) -> Item:
        """
        Private Method to get an item based on its type received as argument.
        """
        item_args: dict[str, Any] = {
            "parent": self.inventory.item_parent,
            "model": "quad",
            "texture": item_type,
            "color": color.white,
            "origin": (-.5, .5),
            "position": self.inventory.find_next_free_spot(),
            "z": -.1
        }

        name = item_type.replace('_', ' ').title()

        item = Item(**item_args)

        item.tooltip = Tooltip(name)                                    
        item.tooltip.background.color = color.color(0,0,0,.8)           

        return item
