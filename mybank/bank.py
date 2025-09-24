import csv 
import os 
import uuid
class Bank:
    def __init__(self):
       self.customers=[] # i want to save all customers here 
    def generate_customer_id(self): #copied from conor
       if not self.customers:
        return "10001"
       ids = [int(customer.customer_id) for customer in self.customers if customer.customer_id and customer.customer_id.isdigit()]
       if not ids:   # to make sure
        return "10001"
       max_id = max(ids)
       return str(max_id + 1)

    def add_customer(self,name,balance=0,customer_id=None,username=None):
      if customer_id is None:
          customer_id =self.generate_customer_id()
      customer = Customer(name,customer_id,balance,username)
      self.customers.append(customer)
      print (f" Customer {name} added with ID {customer_id}")
      return customer
    def find_customer(self,customer_id): 
          for customer in self.customers :
             if customer.customer_id == customer_id:
                print('Customer found',customer.name)
                return customer
          print('Customer not found.')
          return None

    # FROM CLASS LAB & YOUTUP
    def save_to_csv(self):
      if not self.customers:
          return
      with open('customers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'customer_id', 'balance']) 
        for customer in self.customers:
            writer.writerow([customer.name, customer.customer_id, customer.balance])

    def load_from_csv(self):
       if not os.path.exists('customers.csv'):
        return
       with open('customers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
           try:
            balance = float(row['balance']) if row['balance'] else 0
            customer = Customer(row['name'], row['customer_id'], balance) # i saw this in tiketok!
            self.customers.append(customer)
           except ValueError:
              print('Error loading customer')

class Customer:
    # copied the idea from stackoverflow
   def __init__(self,name,customer_id,balance=0,username=None):
        self.name = name
        self.customer_id = customer_id
        self.balance = balance
        self.username= username
        self.accounts = {
            'saving': Account('saving',balance,customer_id),
            'checking': Account('checking',0,customer_id)
        }
        
   def transfer_between(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].withdraw(amount):
                self.accounts[to_acc].deposit(amount)
                return True
        return False 
class Account:
    def __init__(self,account_type,balance,account_number):
        self.account_type =account_type
        self.balance =balance 
        self.account_number= account_number
        
    def deposit(self, amount):
        if amount >0:
          self.balance += amount
          print (f'Deposited {amount} in {self.account_type}')
        else:
            print(' try another amount')

    # copied the idea from geektogeeks
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
            return True
        else:
            print("\nInsufficient balance")
            return False
            
    def transfer ( self,amount,other_account): # note for me: i should make it tranfer between acc and to another
     if self.withdraw(amount):
        other_account.deposit(amount)
        print(f"transfer {self.account_type} to {other_account.account_type}")
        return True

def main():
   bank=Bank()
   bank.load_from_csv()
   is_running = True
   while is_running:
      print(' WELCOME TO BANK!')
      print('1-Login to Account:')
      print('2-Create an Account:')
      print('3-Exit')
      choice = input('Enter your choice(1-3):')
      if choice =='1':
         customer_id = input('Enter customer ID: ')
         customer = bank.find_customer(customer_id)
         if customer:
            while True:
                print(' Welcome!', customer.name)
                print (' 1-Deposit 2-Withdraw 3-Transfer 4-Exit')
                op =input('Choose:')
                if op == '1':
                   acc_type = input('Enter account type (saving/checking): ')
                   amount= float(input('Amount:'))
                   if acc_type in customer.accounts:
                       customer.accounts[acc_type].deposit(amount)
                elif op == '2':
                   acc_type = input('Enter account type (saving/checking): ')
                   amount= float(input('Amount:'))
                   if acc_type in customer.accounts:
                       customer.accounts[acc_type].withdraw(amount)
                elif op == '3':
                   fromacc= input('From account (saving/checking): ')
                   toacc = input('To account (saving/checking): ')
                   amount= float(input('Amount:'))
                   customer.transfer_between(fromacc, toacc, amount)
                elif op == '4':
                   break
         bank.save_to_csv()
      elif choice =='2':
         name = input('Enter customer name: ')
         username = input('Enter username: ')
         balance = float(input('Enter initial balance: ') or 0)
         new_customer= bank.add_customer(name, balance,username=username)
         print(f"Welcome {new_customer.name}, this is your username: {new_customer.username}, "
      f"and this is your ID: {new_customer.customer_id} with balance {balance}")
         bank.save_to_csv()
      elif choice=='3':
         is_running= False
      else:
         print('That is not valid choice!')
   print ('Thank you have a nice day!') 

if __name__ == "__main__":
    main()

        