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
        super().__init__(**kwargs)
