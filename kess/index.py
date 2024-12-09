from datetime import datetime
import random

def generate_account_number():
    return random.randint(1000000, 999999999)

class Bank_Account:
    def __init__(self, account_number, account_holder, balance, account_type):
        self.account_number = generate_account_number()
        #self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def transaction_log(self, transaction_type, amount, target_account=None):
        timestamp = datetime.now().isoformat()
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
            "timestamp": timestamp,
            "target_account": target_account,
        }
        print(transaction)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.balance += amount
            print(f"Deposit successful! Your account balance is {self.balance} naira")
            self.transaction_log("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient funds!!! Please kindly make a Deposit or withdraw less than balance")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! Your account balance is {self.balance} naira")
            self.transaction_log("Withdrawal", amount)

    def check_balance(self):
        print(f"Hi {self.account_holder}! Your account balance is {self.balance} naira. Thank you.")

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient funds!!! Please kindly make a Deposit or withdraw less than balance")
        else:
            #deduct from sender's account
            self.balance -= amount
            print(f"{amount} naira has been successfully transfered to {target_account.account_number}! Your account balance is {self.balance} naira")
            self.transaction_log("Transfer", amount, target_account.account_number)

            #update receiver's account
            target_account.balance += amount
            print(f"{amount} naira has been successfully received from {self.account_number}! Your account balance is {target_account.balance} naira")
            target_account.transaction_log("Transfer", amount, self.account_number)





account1 = Bank_Account(generate_account_number(), "Doris", 0, "savings")
account2 = Bank_Account(generate_account_number(), "Chioma", 200, "savings")

account1.deposit(1000)
account1.check_balance()
account1.withdraw(200)
account2.transfer(50,account1)
 







