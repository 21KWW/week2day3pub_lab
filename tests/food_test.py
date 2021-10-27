import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food1 = Food("Pie", 2, 2)
        self.food2 = Food("Chips", 3, 1)

    def test_food_has_price(self):
        self.assertEqual(2, self.food1.price)
        self.assertEqual(3, self.food2.price)

    def test_food_has_name(self):
        self.assertEqual("Pie", self.food1.name)
        self.assertEqual("Chips", self.food2.name)

    def test_food_has_rejuvination(self):
        self.assertEqual(2, self.food1.rejuvination)
        self.assertEqual(1, self.food2.rejuvination)
