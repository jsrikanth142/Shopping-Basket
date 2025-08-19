
import unittest
from decimal import Decimal
from basket.basket import Basket

class TestBasket(unittest.TestCase):

    def setUp(self):
        # Catalog matches your current Catalog class input
        self.catalog_data = {
            "Soup": Decimal("0.65"),
            "Bread": Decimal("0.80"),
            "Milk": Decimal("1.30"),
            "Apples": Decimal("1.00")
        }

        # Offers compatible with OfferManager
        self.offers_data = [
            {"type": "percentage_discount", "product": "Apples", "value": 10},
            {"type": "multi_buy", "trigger_product": "Soup", "trigger_qty": 2, "discount_product": "Bread", "discount_value": 50}
        ]

    def test_subtotal_calculation(self):
        basket = Basket(["Apples", "Milk", "Bread"], self.catalog_data, [])
        subtotal, discounts, total, unknown = basket.calculate_totals()
        self.assertEqual(subtotal, Decimal("3.10"))
        self.assertEqual(total, Decimal("3.10"))
        self.assertEqual(unknown, [])

    def test_apples_discount(self):
        basket = Basket(["Apples"], self.catalog_data, self.offers_data)
        subtotal, discounts, total, unknown = basket.calculate_totals()
        self.assertEqual(subtotal, Decimal("1.00"))
        self.assertEqual(total, Decimal("0.90"))
        self.assertEqual(len(discounts), 1)

    def test_multiple_offers_applied(self):
        basket = Basket(["Apples", "Soup", "Soup", "Bread"], self.catalog_data, self.offers_data)
        subtotal, discounts, total, unknown = basket.calculate_totals()
        self.assertEqual(subtotal, Decimal("3.10"))  # 1+0.65*2+0.8
        self.assertEqual(total, Decimal("2.60"))     # 10% off Apples + 50% off 1 Bread
        self.assertEqual(len(discounts), 2)

    def test_no_offers(self):
        basket = Basket(["Milk", "Bread"], self.catalog_data, [])
        subtotal, discounts, total, unknown = basket.calculate_totals()
        self.assertEqual(subtotal, Decimal("2.10"))
        self.assertEqual(total, Decimal("2.10"))
        self.assertEqual(discounts, [])

    def test_unknown_items(self):
        basket = Basket(["Apples", "Chocolate", "Milk"], self.catalog_data, self.offers_data)
        subtotal, discounts, total, unknown = basket.calculate_totals()
        self.assertEqual(subtotal, Decimal("2.30"))  # apples + milk
        self.assertEqual(total, Decimal("2.20"))     # apples 10% off
        self.assertIn("chocolate", unknown)          # Catalog is case-insensitive

if __name__ == "__main__":
    unittest.main()
