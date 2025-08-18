from decimal import Decimal
from basket.item import Item
from typing import Dict

class Catalog:
    """Handles catalog of items for a branch."""
    def __init__(self, items: Dict[str, Decimal]):
        self.items = {k.lower(): Item(k, v) for k, v in items.items()}

    def get_item(self, name: str) -> Item:
        """Retrieve an item (case-insensitive)."""
        return self.items.get(name.lower())
