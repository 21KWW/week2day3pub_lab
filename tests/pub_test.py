# tests/pub_test.py

import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        drink1 = Drink("Beer", 5, 5, 40)
        drink2 = Drink("Wine", 4, 11, 10)
        drinks = [drink1, drink2]

        customer1 = Customer("Andrew", 20, 29)
        customer2 = Customer("Betty", 8, 34)
        customer3 = Customer("Charlie", 30, 16)
        customers = [customer1, customer2, customer3]

        food1 = Food("Pie", 2, 2)
        food2 = Food("Chips", 3, 1)
        foods = [food1, food2]

        self.pub = Pub("The Prancing Pony", 100, drinks, customers, foods)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.cash)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))
    
    def test_pub_drink_has_name(self):
        self.assertEqual("Beer", self.pub.drinks[0].name)
        self.assertEqual("Wine", self.pub.drinks[1].name)

    def test_pub_drink_has_price(self):
        self.assertEqual(5, self.pub.drinks[0].price)
        self.assertEqual(4, self.pub.drinks[1].price)

    def test_pub_customer_has_name(self):
        self.assertEqual("Andrew", self.pub.customers[0].name)
        self.assertEqual("Betty", self.pub.customers[1].name)

    def test_pub_customer_has_wallet(self):
        self.assertEqual(20, self.pub.customers[0].wallet)
        self.assertEqual(8, self.pub.customers[1].wallet)

    def test_pub_find_customer_by_name(self):
        self.assertEqual(self.pub.customers[0], self.pub.find_customer_by_name("Andrew"))

    def test_pub_find_drink_by_name(self):
        self.assertEqual(self.pub.drinks[0], self.pub.find_drink_by_name("Beer"))

    def test_pub_find_food_by_name(self):
        self.assertEqual(self.pub.foods[0], self.pub.find_food_by_name("Pie"))

    def test_pub_customer_can_buy_drink(self):
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.assertEqual(105, self.pub.cash)
        self.assertEqual(15, self.pub.customers[0].wallet)

    def test_pub_under_age_cant_buy_drink(self):
        self.pub.customer_buys_drink("Charlie", "Beer")
        self.assertEqual(100, self.pub.cash)
        self.assertEqual(30, self.pub.customers[2].wallet)

    def test_pub_drunkenness_level(self):
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.assertEqual(5, self.pub.customers[0].drunkenness)

    def test_pub_too_drunk(self):
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.pub.customer_buys_drink("Andrew", "Beer")
        self.assertEqual(15, self.pub.customers[0].drunkenness)
        self.assertEqual(115, self.pub.cash)
        self.assertEqual(5, self.pub.customers[0].wallet)

    def test_pub_customer_buys_food_without_drink(self):
        self.pub.customer_buys_food("Andrew", "Chips")
        self.assertEqual(103, self.pub.cash)
        self.assertEqual(17, self.pub.customers[0].wallet)
        self.assertEqual(0, self.pub.customers[0].drunkenness)

    def test_pub_customer_buys_food_with_drink(self):
         self.pub.customer_buys_drink("Andrew", "Beer")
         self.pub.customer_buys_food("Andrew", "Chips")
         self.assertEqual(108, self.pub.cash)
         self.assertEqual(12, self.pub.customers[0].wallet)
         self.assertEqual(4, self.pub.customers[0].drunkenness)

