"""
Module to run the application.
"""

from ursina import Ursina

from src.entities.inventory.inventory import Inventory
from src.entities.items.add_item_button import AddItemButton


def main() -> None:
    """
    Main function to run the application.
    """
    app = Ursina()
    inventory = Inventory()
    add_item_button = AddItemButton(inventory=inventory)

    for _ in range(7):
        add_item_button.add_item_to_inventory()

    app.run()


if __name__ == "__main__":
    main()
