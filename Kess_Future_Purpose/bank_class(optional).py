import random

def generate_account_number():
    return random.randint(1000000, 999999999)

#create a bank account class 
class Bank_Account():
    def __init__(self, account_holder, account_type, initial_deposit):
        self.account_holder = account_holder
        self.account_type = account_type
        self.initial_deposit = initial_deposit
        self.account_number = generate_account_number() #create a unique account number
        self.balance = initial_deposit
        self.minimum_balance = 1000

    def apply_interest(self):
        if self.account_type == "Savings":
            interest = self.balance * 0.05 #5% interest
            self.balance += interest
            print(f"Interest of {interest} applied to account {self.account_number}.")

#create a bank class
class Bank():
    def __init__(self):
        self.accounts = []
        self.total_bank_balance = 0

    def create_account(self, account_holder, account_type, initial_deposit):
       
       #create a new account
       new_account = Bank_Account(account_holder,account_type,initial_deposit)

       #ensure valid account type
       if account_type not in ["Checking", "Savings", "Business"]:
           print(f"Invalid account type")
       else:
           print(f"Welcome, {account_holder}! Your new account number is {new_account.account_number}. Kindly make a deposit into your account.")

       #ensure initial deposit is a positive number
       if initial_deposit <= 0:
           print(f"{account_holder}, Kindly deposit a valid amount of cash")

       # Apply interest if it's a savings account 
       if account_type == "Savings":
            new_account.apply_interest()

       #add account to list of bank accounts
       self.accounts.append(new_account)

       #update total bank balance
       self.total_bank_balance += initial_deposit

    #find account number
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number and account.account_type in ["Checking", "Savings", "Business"]:
                print(account)
            else:
                print(f"Account not found")

    #delete account number
    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                self.total_bank_balance -= account.balance
                print(f"Account {account_number} deleted successfully.")
            else:
                print(f"Account not found.")
    
    #list account numbers
    def list_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                print(f"{account}")

bank = Bank()

# Create accounts
acc1 = bank.create_account("Alice", "Balancing", 1000)
acc2 = bank.create_account("Bob", "Checking", 0)
acc3 = bank.create_account("Charlie", "Savings", 2000)

# List all accounts
print(f"List of all accounts:")
print(bank.list_accounts())

# # Find a specific account
print(f"Finding account:")
print(bank.find_account(acc2))

# # Delete an account
print(f"Deleting account:")
bank.delete_account(acc1)

# # List all accounts after deletion
print(f"List of all accounts after deletion:")
bank.list_accounts()

# # Print the bank's overall summary
print(f"Bank Summary:")
print(bank)

       