import unittest
from mybank.account import Account
class Testaccount(unittest.TestCase):
    def test_Account(self):
        acc1= Account ('SV',1000)
        acc2= Account ('CH',100)
        self.assertEqual(acc1.account_type,'SV')
        self.assertEqual(acc1.balance,1000)
        self.assertEqual(acc2.account_type,'CH',100 )
        self.assertEqual(acc2.balance,100)
if __name__ == "__main__":
    unittest.main()
