class Account:
    def __init__(self,account_type,balance,account_number):
        self.account_type =account_type
        self.balance =balance 
        self.account_number= account_number
    def deposit(self,account_type, amount = 0):
        self.account_type = account_type()
        amount = float(input("Enter amount to be Deposited and choose the account: "))
        if amount >0 and account_type == "saving":
          self.saving_balance += amount
          print ('f Deposited {amount} in saving account')
        elif amount >0 and account_type == "cheaking":
         self.saving_balance += amount
         print ('f Deposited {amount} in cheaking account')
         return amount

    # copied the idea from geektogeeks
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
            return amount
        else:
            print("\nInsufficient balance")
            return amount
    def transfer ( self,amount,other):
        if self.withdraw(amount):
          other.deposit(amount) # rno dont forget to put 'other' in customer class
       
       

     