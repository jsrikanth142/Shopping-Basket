from decimal import Decimal

def format_money(value: Decimal, discount: bool = False, currency_symbol: str = "£") -> str:
    if discount and value < 1:
        return f"{int(value * 100)}p"
    return f"{currency_symbol}{value:.2f}"

def normalize_items(items):
    return [i.lower() for i in items]
