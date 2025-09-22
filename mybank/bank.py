import csv 
import os 

class Bank:
     
    def add_customer(self):
      pass
    def find_customer(self):
       pass
    #    for customer in find_customer:
    #       if account_type = ''
    def main():
       bank=Bank()
       is_running = True
       while is_running:
         print(' WELCOME TO BANK!')
         print('1-Login to Account:')
         print('2-Create an Account:')
         print('3-Exit')
         choice = input('Enter your chpice(1-3):')
         if choice =='1':
            bank.find_customer()
         elif choice =='2':
            bank.add_customer()
         elif choice=='3':
            is_running= False
         else:
            print('That is not valid choice!')
    print ('Thank you have a nice day!') # when user choice 3 
# FROM CLASS LAB & YOUTUP
    def save_to_csv(self):
        with open('data/bank.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.customers)
            print("Data saved ")
    def load_from_csv(self):
        try:
            with open('data/bank.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                self.customers = [row for row in reader]
            print("Data loaded ")
        except FileNotFoundError:
            print("No data found")





        