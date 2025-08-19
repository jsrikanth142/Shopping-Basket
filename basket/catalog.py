from decimal import Decimal
from basket.item import Item
from typing import Dict

# Handles catalog of items for a branch.Retrieve an item (case-insensitive)
class Catalog:
    
    def __init__(self, items: Dict[str, Decimal]):
        self.items = {k.lower(): Item(k, v) for k, v in items.items()}

    def get_item(self, name: str) -> Item:
        return self.items.get(name.lower())
