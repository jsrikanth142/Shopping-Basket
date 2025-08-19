from decimal import Decimal
from typing import List, Dict
from collections import namedtuple

Discount = namedtuple("Discount", ["description", "amount"])

class OfferManager:
    def __init__(self, offers: List[Dict]):
        self.offers = offers

    def apply_offers(self, item_counts: Dict[str, int], catalog) -> List[Discount]:
        discounts = []

        for offer in self.offers:
            try:
                if offer["type"] == "percentage_discount":
                    product_key = offer["product"].lower()
                    if product_key in item_counts:
                        item = catalog.get_item(product_key)
                        discount_amount = item.price * item_counts[product_key] * Decimal(offer["value"]) / 100
                        discounts.append(Discount(f"{item.name} {offer['value']}% off", discount_amount))

                elif offer["type"] == "multi_buy":
                    trigger_key = offer["trigger_product"].lower()
                    discount_key = offer["discount_product"].lower()
                    trigger_qty = offer["trigger_qty"]
                    if item_counts.get(trigger_key, 0) >= trigger_qty:
                        item = catalog.get_item(discount_key)
                        discount_amount = item.price * Decimal(offer["discount_value"]) / 100
                        discounts.append(Discount(f"{item.name} {offer['discount_value']}% off", discount_amount))
            except Exception:
                continue  # This used to skip faulty offer
        return discounts
