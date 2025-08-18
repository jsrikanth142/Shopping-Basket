from decimal import Decimal

def format_money(value: Decimal, discount: bool = False, currency_symbol: str = "£") -> str:
    """Format currency according to spec."""
    if discount and value < 1:
        return f"{int(value * 100)}p"
    return f"{currency_symbol}{value:.2f}"

def normalize_items(items):
    """Normalize items for case-insensitive lookup."""
    return [i.lower() for i in items]
