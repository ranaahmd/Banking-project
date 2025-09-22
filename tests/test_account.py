import unittest
from mybank.account import Account
class Testaccount(unittest.TestCase):
    def test_Account(self):
        acc1= Account ('SV',1000,'SV12')
        acc2= Account ('CH',100,'CH12') # the last value is acc num
        self.assertEqual(acc1.account_type,'SV')
        self.assertEqual(acc1.balance,1000)
        self.assertEqual(acc1.account_number,'SV12')
        self.assertEqual(acc2.account_type,'CH',100 )
        self.assertEqual(acc2.balance,100)
        self.assertEqual(acc2.account_number,'CH12')
    def test_balance(self):
        acc= Account(100)
        depAccount = acc.deposit(30)
        self.assertEqual(depAccount)
        self.assertEqual(acc.deposit, 130)
    
    
      
if __name__ == "__main__":
    unittest.main()
