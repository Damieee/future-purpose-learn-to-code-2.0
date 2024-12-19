class BankAccount:
    def __init__(self, account_number, account_holder, account_type, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Your new balance is: {self.balance}")
        else:
            print("This amount is invalid, please check and try again")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Your new balance is: {self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount} to {target_account.account_holder}. Your new balance is: {self.balance}")
        else:
            print("Insufficient funds for transfer")


# output

# account1 = BankAccount(1, "Popoola", "Savings", 100000)
account2 = BankAccount(2, "Owoyanturu", "Savings", 50000)

account1.deposit(5000)
account1.withdraw(10000)
account1.transfer(50000, account2)

print(f"Account 1 balance: {account1.check_balance()}")
print(f"Account 2 balance: {account2.check_balance()}")
