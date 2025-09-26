import unittest
from mybank.bank import Bank
from mybank.bank import Customer
from mybank.bank import Account
from unittest.mock import Mock
class Testbank(unittest.TestCase):
    def test_generate_customer_id(self):
        customer_id = (10007,'Rafa')
        self.assertTrue(customer_id, True)
    def test_add_customer(self):
        bank = Bank()
        bank.generate_customer_id = Mock(customer= 10008) 
        adding = bank.add_customer(
            first_name= 'sahar',
            last_name='mohammed',
            customer_id=10008,
            password='12345',
            balance_checking='900',
            balance_savings='900',
        )
        self.assertEqual(adding.customer_id,10008)