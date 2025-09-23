import uuid
class Customer:
    # copied the idea from stackoverflow
    def __init__(self,usernames,passwords,names,acctype):
        self.names = names
        self.passwords = passwords
        self.usernames = usernames
        self.acctype= acctype
        self.customer_id = str (uuid.uuid4())[:4] # i want short id / copied from geekforgeeks
        # here i want to let the user choose to create type of accont
        self.saving_balance =0
        self.checking_balance=0
customers =[]
def createaccount():
    names = input (' enter your first name:')
    usernames = input (' enter a username:')
    passwords = input('enter a password:')

def login():
    usernames = input("Enter your username:")
    passwords = input("Enter your Password:")
    if usernames in usernames and passwords in passwords:
        print("welcome")
    else:
        print("incorrect!")

while True:
    account_ans = input("choose: 1-Sign Up     2-login    -3quit ")
    if account_ans == "1":
        register()
    if account_ans == "2":
        login()
    if account_ans == "3":
        break
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
       
       # return here after i create login and create account

     