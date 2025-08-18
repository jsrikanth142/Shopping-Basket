from decimal import Decimal

class Item:
    """Represents a single product item."""
    def __init__(self, name: str, price: Decimal):
        self.name = name       # Original name for display
        self.price = price
