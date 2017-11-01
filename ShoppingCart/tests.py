import unittest
from .models import Cart, Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.name = "Sweets"
        self.type = "confectionery"
        self.price = 1.00


class TestCart(unittest.TestCase):
    item1 = Item("Crisps", "confectionery", 0.50)
    item2 = Item("Crisps", "luxury", 0.50)
    cart = Cart({item1: 3, item2: 3})

    def setUp(self):
        self.items = Cart({self.item1: 6, self.item2: 2})

    def test_item_total(self):
        result1 = round(self.cart.item_total(self.item1), 2)
        result2 = round(self.cart.item_total(self.item2), 2)

        self.assertEqual(result1, 1.80)
        self.assertEqual(result2, 1.50)

    def test_cart_total(self):
        result = round(self.cart.cart_total(), 2)
        self.assertEqual(result, 3.30)

    def test_remove_item(self):
        item = self.cart
        result = item.remove_item(self.item1, 2)
        updated_price = round(item.cart_total(), 2)

        self.assertEqual(result, {self.item1: 1, self.item2: 3})
        self.assertEqual(updated_price, 2.10)
