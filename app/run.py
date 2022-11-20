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

    app.run()


if __name__ == "__main__":
    main()
