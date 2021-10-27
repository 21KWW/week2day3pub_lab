# tests/pub_test.py

import unittest
from src.drinks import Drink

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer", 5, 5)
        self.drink2 = Drink("Wine", 4, 11)


    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink1.name)
        self.assertEqual("Wine", self.drink2.name)

    def test_pub_has_price(self):
        self.assertEqual(5, self.drink1.price)
        self.assertEqual(4, self.drink2.price)

    def test_drink_alcohol_level(self):
        self.assertEqual(5, self.drink1.alcohol_level)
        self.assertEqual(11, self.drink2.alcohol_level)

