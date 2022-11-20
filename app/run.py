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

    for _ in range(7):
        inventory.append_item("item_1")

    app.run()


if __name__ == "__main__":
    main()
