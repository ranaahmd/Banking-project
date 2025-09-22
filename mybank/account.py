class Account:
    def __init__(self,account_type,balance,account_number):
        self.account_type =account_type
        self.balance =balance 
        self.account_number= account_number
    def deposit(self, amount = 0):
        amount = float(input("Enter amount to be Deposited: "))
        if amount >0:
         self.balance += amount
        print("\nAmount Deposited:", amount)
        return amount
    # copied the idea from geektogeeks
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")
            return amount
    # def deactive (self):