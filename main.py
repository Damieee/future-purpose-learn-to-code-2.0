class BankAccount:
    def __init__(self, account_number, account_holder, balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    print("\nBank Management System\n")

    def deposit(self):
        amount = int(input("Enter the amount you will like to deposit: "))
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print(f"You have successfully deposited {amount} into your account. Your new balance is {self.balance}\n")

    def withdraw(self):
        amount = int(input("Enter the amount you will like to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount} from your account. Your new balance is {self.balance}\n")

    def check_balance(self):
        print(f"Your current balance is {self.balance}\n")

    def transfer(self, beneficiary_account):
        amount = int(input("Enter the amount you will like to transfer: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            beneficiary_account.balance += amount
            print(f"You have successfully transferred {amount} to \n Account Number: {beneficiary_account.account_number},\n Account Holder: {beneficiary_account.account_holder}.\n Your new balance is {self.balance}\n")



account1 = BankAccount("1234567890", "Jane Doe", 0, "Savings")
account2 = BankAccount("0987654321", "John Doe", 0, "Checking")

account1.deposit()
account1.withdraw()
account1.check_balance()
account1.transfer(account2)