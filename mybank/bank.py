import csv 
import os 
from customer import Customer
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
        os.makedirs('data', exist_ok=True)
        with open('data/bank.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            print("Data saved ")
        # note for me i need to reveiw this again
    def load_from_csv(self):
        try:
            with open('data/bank.csv', 'r', newline='') as file:
                self.customers = []
            print("Data loaded ")
        except FileNotFoundError:
            print("No data found")


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





        