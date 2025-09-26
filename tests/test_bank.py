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
        bank.generate_customer_id = Mock(return_value=10008) 
        adding = bank.add_customer(
            first_name= 'sahar',
            last_name='mohammed',
            customer_id=10008,
            password='12345',
            balance_checking='900',
            balance_savings='900',
        )
        self.assertEqual(adding.customer_id,10008)
    def test_find_customer(self):
        bank =Bank()
        mock_customer = Mock()
        mock_customer.customer_id = 10009
        bank.find_customer= Mock(return_value=mock_customer)
        testrsult =bank.find_customer(10009)
        self.assertEqual(testrsult,mock_customer)

        # note for me DONT FORGET TO TEST CSV 
class TestCustomer(unittest.TestCase):
    def test_deposit_account_checking(self):
       account_type = Account("checking",100)
       account_type.deposit(50)
       self.assertEqual(account_type.balance,150)
    def test_deposit_account_saving(self):
       account_type = Account("saving",100)
       account_type.deposit(50)
       self.assertEqual(account_type.balance,150)

    def test_withdraw_from_account_checking(self):
       account_type = Account("checking",100)
       account_type.withdraw(50)
       self.assertEqual(account_type.balance,50)
    def test_withdraw_account_saving(self):
       account_type = Account("saving",100)
       account_type.withdraw(50)
       self.assertEqual(account_type.balance,50)
    def test_transfer_between_accounts(self):
        customer = Customer(10007,'Rafa','ahmed',1000.0,1434.0,-135.0)
        customer.accounts['checking'] = Account('checking',balance=200)
        customer.accounts['saving'] = Account('saving',balance=200)
        customer.transfer_between_accounts('checking','saving',50)
        self.assertEqual(customer.accounts['checking'].balance,150)
        self.assertEqual(customer.accounts['saving'].balance,250)
        

       



