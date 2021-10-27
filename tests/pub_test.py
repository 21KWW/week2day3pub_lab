# tests/pub_test.py

import unittest
from src.pub import Pub
from src.drinks import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        drink1 = Drink("Beer", 5)
        drink2 = Drink("Wine", 4)
        drinks = [drink1, drink2]
        self.pub = Pub("The Prancing Pony", 100, drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.cash)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))
