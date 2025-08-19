from decimal import Decimal

# Represents a single product item.
class Item:
    
    def __init__(self, name: str, price: Decimal):
        self.name = name
        self.price = price
