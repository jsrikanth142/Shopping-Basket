from collections import Counter
from decimal import Decimal
from basket.catalog import Catalog
from basket.offer import OfferManager
from basket.utils import normalize_items

class Basket:
    """Main basket class orchestrating items and offers."""
    def __init__(self, items, catalog_data, offers_data):
        self.catalog = Catalog(catalog_data)
        self.offer_manager = OfferManager(offers_data)
        self.items = normalize_items(items)

    def calculate_totals(self):
        subtotal = Decimal("0.00")
        item_counts = Counter()
        unknown_items = []

        for name in self.items:
            item = self.catalog.get_item(name)
            if item:
                subtotal += item.price
                item_counts[name] += 1
            else:
                unknown_items.append(name)

        discounts = self.offer_manager.apply_offers(item_counts, self.catalog)
        total_discount = sum(d.amount for d in discounts)
        total = subtotal - total_discount

        return subtotal, discounts, total, unknown_items
