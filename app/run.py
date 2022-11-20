"""
Module to run the application.
"""

from ursina import Ursina, color

from src.entities.inventory.inventory import Inventory
from src.entities.items.item import Item


def main() -> None:
    """
    Main function to run the application.
    """
    app = Ursina()
    inventory = Inventory()

    item_1 = Item(parent=inventory.item_parent)
    item_2 = Item(parent=inventory.item_parent, color=color.green, position=(2, 0))

    app.run()


if __name__ == "__main__":
    main()
