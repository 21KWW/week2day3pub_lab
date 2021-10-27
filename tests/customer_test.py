# tests/customer_test.py

import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Andrew", 10, 29)
        self.customer2 = Customer("Betty", 8, 34)

    def test_customer_has_name(self):
        self.assertEqual("Andrew", self.customer1.name)
        self.assertEqual("Betty", self.customer2.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer1.wallet)
        self.assertEqual(8, self.customer2.wallet)
    
    def test_customer_has_age(self):
        self.assertEqual(29, self.customer1.age)
        self.assertEqual(34, self.customer2.age)