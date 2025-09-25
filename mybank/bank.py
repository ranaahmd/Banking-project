import csv 
import os 

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

    def add_customer(self,first_name,last_name,balance_checking,balance_savings,password,customer_id=None):
      if customer_id is None:
          customer_id =self.generate_customer_id()
      customer = Customer(first_name,last_name,customer_id,balance_checking,balance_savings,password)
      self.customers.append(customer)
      print (f" Customer {first_name} added with ID {customer_id}")
      return customer
    def find_customer(self,customer_id): 
          for customer in self.customers :
             if customer.customer_id == customer_id:
                print('Customer found',customer.first_name)
                return customer
          print('Customer not found.')
          return None

    # FROM CLASS LAB & YOUTUP
    def save_to_csv(self):
      if not self.customers:
          return
      with open('bank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['customer_id','first_name','last_name','password','balance_checking','balance_savings'])
        for customer in self.customers:
         writer.writerow([
        customer.customer_id,
        customer.first_name,
        customer.last_name,
        customer.password,
        customer.accounts['checking'].balance,
        customer.accounts['saving'].balance
    ])

    def load_from_csv(self):
       if not os.path.exists('bank.csv'):
        return
       with open('bank.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            checking = float(row.get('balance_checking', 0)) if row.get('balance_checking') else 0
            savings = float(row.get('balance_savings', 0)) if row.get('balance_savings') else 0
            customer = Customer(
            first_name=row.get('first_name'),
            last_name=row.get('last_name', ),
            password= row.get('password'),
            customer_id=row.get('customer_id'),
            balance_checking=checking,
            balance_savings=savings  
            )
            self.customers.append(customer)
class Customer:
    # copied the idea from stackoverflow
   def __init__(self,first_name,last_name,customer_id,balance_checking,balance_savings,password):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.password= password
        self.balance_checking = balance_checking
        self.balance_savings= balance_savings
        self.accounts = {
           'saving': Account('saving', balance_savings),
           'checking': Account('checking', balance_checking)
}
      #IM traying to make the user choose the type of account to deposit
      #copied the idea from stackover flow 
   def deposit_account(self,account_type,amount):
       if account_type in self.accounts:
        return self.accounts[account_type].deposit(amount)
       else:
        print(f'Account type "{account_type}" not found')
        return False
   def withdraw_from_account(self, account_type, amount):
        if account_type in self.accounts:
            return self.accounts[account_type].withdraw(amount)
        else:
           print(f'Account type "{account_type}" not found. Available: saving, checking')
           return False  
   def transfer_between_accounts(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].withdraw(amount):
                self.accounts[to_acc].deposit(amount)
                return True
        return False 
   def transfer_to_external(self, from_acc, other_customer_id, amount, bank):
        other_customer = bank.find_customer(other_customer_id)
        if not other_customer:
            print("other customer not found")
            return False
        if from_acc in self.accounts:
            if self.accounts[from_acc].withdraw(amount):
                other_customer.accounts['checking'].deposit(amount)
                print(f"Transferred {amount} to customer {other_customer_id}")
                return True
        return False
class Account:

    def __init__(self,account_type,balance):
        self.account_type = account_type
        self.balance = balance
        
    def deposit(self, amount):
        if amount >0:
          self.balance += amount
          print (f'Deposited {amount} in {self.account_type} New balance {self.balance}')
          return True
        else:
            print(' try another amount')
            return False
    # copied the idea from geektogeeks
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:{amount} ,New balance", {self.balance})
            return True
        else:
            print("\nInsufficient balance")
            return False
            
    def transfer ( self,amount,other_account): 
     other_account =input(' enter customer id to transfer to:',customer_id)
     if self.withdraw(amount):
        other_account.deposit(amount)
        print(f"transfer {self.account_type} to {other_account.customer_id}")
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
         password = input('enter your password:')
         customer = bank.find_customer(customer_id)
         if customer:
            if customer.password == password:
                print(' Welcome!', customer.first_name)
            while True:
             print (' 1-Deposit 2-Withdraw 3-Transfer 4-Exit')
             op =input('Choose:')
             if op == '1':
              acc_type = input('Enter account type (saving/checking): ')
              try:
               amount= float(input('Amount:'))
               customer.deposit_account(acc_type, amount) # calling the new function
               bank.save_to_csv()
              except ValueError:
                print('TRY AGAIN')
             elif op == '2':
               acc_type = input('Enter account type (saving/checking): ')
               try:
                  amount= float(input('Amount:'))
                  customer.withdraw_from_account(acc_type, amount)
                  bank.save_to_csv()
               except ValueError:
                  print("Try again")
             elif op == '3':
                choose_account= input('What account do you want to transfer to? 1-My account ,2-Other account')
                amount = float(input('Amount:'))
                fromacc= input('From account (saving/checking): ')
                if choose_account == '1' :
                 toacc = input('To account (saving/checking): ')
                 customer.transfer_between_accounts(fromacc, toacc, amount)
                 bank.save_to_csv()
                elif choose_account == '2':
                   other_account = input('Enter account_id')
                   customer.transfer_to_external(fromacc, other_account, amount, bank)
                   bank.save_to_csv()

             elif op == '4':
                   break
         bank.save_to_csv()
      elif choice =='2':
         first_name = input('Enter first_name: ')
         last_name = input('enter your last name')
         password= input('enter a password:')
         balance = float(input('Enter initial balance: ') or 0)
         new_customer = bank.add_customer(first_name, last_name,password, balance, balance)
         print(f"Welcome {new_customer.first_name} "
      f"and this is your ID: {new_customer.customer_id} with balance {balance}")
         bank.save_to_csv()
      elif choice=='3':
         is_running= False
      else:
         print('That is not valid choice!')
   print ('Thank you have a nice day!') 

if __name__ == "__main__":
    main()

        