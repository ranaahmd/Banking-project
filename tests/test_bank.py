import unittest
from mybank.bank import Bank
from mybank.bank import Customer
from mybank.bank import Account
class Testbank(unittest.TestCase):
    def test_generate_customer_id(self):
        customer_id = (10007,'Rafa')
        self.assertTrue(customer_id, True)