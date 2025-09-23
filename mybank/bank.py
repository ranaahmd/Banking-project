import csv 
import os 
import uuid
class Bank:
    def __init__(self):
       self.customers=[] # i want to save all customers here 

    def add_customer(self,name,customer_id,balance=0):
      customer = Customer(name, customer_id, balance)
      self.customers.append(customer)
      print (f" Customer {name} added with ID {customer.customer_id}")
      return customer

    def find_customer(self,customer_id): # it should serch by ID
       for ppl  in self.customers :
          if ppl.customer_id == customer_id:
             print('Customer is:',ppl)
             return ppl
       print('Customer not found.')
       return None

    # FROM CLASS LAB & YOUTUP
def save_to_csv(self):
    with open('customers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Customer_ID', 'Balance']) 
        for customer in self.customers:
            writer.writerow([customer.name, customer.customer_id, customer.balance])

def load_from_csv(self):
    if not os.path.exists('customers.csv'):
        return
    with open('customers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            self.add_customer(row['Name'], row['Customer_ID'], float(row['Balance']))
def main():
   bank=Bank()
   bank.load_from_csv()
   is_running = True
   while is_running:
     print(' WELCOME TO BANK!')
     print('1-Login to Account:')
     print('2-Create an Account:')
     print('3-Exit')
     choice = input('Enter your chpice(1-3):')
     if choice =='1':
        cid = input('Enter customer ID: ')
        bank.find_customer(cid)
     elif choice =='2':
        name = input('Enter customer name: ')
        cid = input('Enter customer ID: ')
        bank.add_customer(name, cid)
        bank.save_to_csv()
     elif choice=='3':
        is_running= False
     else:
        print('That is not valid choice!')
   print ('Thank you have a nice day!') # when user choice 3 


if __name__ == "__main__":
    main()
class Customer:
    # copied the idea from stackoverflow
    def __init__(self,usernames,passwords,names,acctype):
        self.names = names
        self.passwords = passwords
        self.usernames = usernames
        self.acctype= acctype
        self.customer_id = str (uuid.uuid4())[:4] # i want short id / copied from geekforgeeks
        self.account = {
            'saving': Account('saving',0,str (uuid.uuid4())[:4]),
            'checking': Account('checking',0,str (uuid.uuid4())[:4])

        }
        # here i want to let the user choose to create type of accont
        self.saving_balance =0
        self.checking_balance=0
customers =[]
def createaccount():
    names = input (' enter your first name:')
    usernames = input (' enter a username:')
    passwords = input('enter a password:')
    print(' choose account type:')
    print(' 1-saving account, 2- checking account')
    choose = input(' enter 1 or 2')
    if choose == '1':
        acctype = 'saving'
    else:
        acctype = 'checking'
    customer =Customer(names,usernames,passwords,acctype)
    customers.append(customer)
def login():
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    for customer in customers:
        if customer.usernames == username_input and customer.passwords == password_input:
            print("Welcome")
            return customer
    print("Incorrect username or password!")
    return
class Account:
    def __init__(self,account_type,balance,account_number):
        self.account_type =account_type
        self.balance =balance 
        self.account_number= account_number
    def deposit(self,account_type, amount = 0):
        self.account_type = account_type()
        amount = float(input("Enter amount to be Deposited and choose the account: "))
        if amount >0:
          self.balance += amount
          print ('f Deposited {amount} in {self.account_type}')
        else:
            print(' try another amount')

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
while True:
    account_ans = input('1-Sign Up   2-Login   3-Quit: ')
    if account_ans == "1":
        createaccount()
    elif account_ans == "2":
        customer = login()
        if customer:
            while True:
                act = input("1-Deposit  2-Withdraw  3-Logout: ")
                if act == "1":
                    customer.account.deposit()
                elif act== "2":
                    customer.account.withdraw()
                elif act == "3":
                    break
    elif account_ans == "3":
        break
                             
                         




        