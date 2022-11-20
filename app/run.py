"""
Module to run the application.
"""

from ursina import Ursina

from src.entities.inventory.inventory import Inventory


def main() -> None:
    """
    Main function to run the application.
    """
    app = Ursina()
    inventory = Inventory()

    inventory.append_item("item_1")
    inventory.append_item("item_2")

    app.run()


if __name__ == "__main__":
    main()
