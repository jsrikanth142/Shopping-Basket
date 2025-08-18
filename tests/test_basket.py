import unittest
from decimal import Decimal
from basket.basket import Basket

# Sample catalog and offers
CATALOG = [
    {"name": "apples", "price": "1.00"},
    {"name": "milk", "price": "1.30"},
    {"name": "bread", "price": "0.80"},
    {"name": "soup", "price": "0.65"}
]

OFFERS = [
    {"type": "percentage", "item": "apples", "discount": 10},
    {"type": "buy_x_get_y", "buy_item": "soup", "buy_qty": 2, "free_item": "bread", "discount_percent": 50}
]

class TestBasket(unittest.TestCase):

    def test_valid_items_with_offers(self):
        basket = Basket(["apples", "milk", "bread", "soup", "soup"], CATALOG, OFFERS)
        subtotal, discounts, total, unknown_items = basket.calculate_totals()

        self.assertEqual(subtotal, Decimal("4.40"))
        self.assertAlmostEqual(total, Decimal("3.95"))
        self.assertEqual(len(discounts), 2)
        self.assertEqual(unknown_items, [])

    def test_unknown_items(self):
        basket = Basket(["apples", "chocolate", "milk"], CATALOG, OFFERS)
        subtotal, discounts, total, unknown_items = basket.calculate_totals()

        self.assertEqual(subtotal, Decimal("2.30"))  # apples + milk
        self.assertEqual(unknown_items, ["chocolate"])
        self.assertEqual(total, Decimal("2.20"))  # includes apple 10% discount

    def test_no_offer
