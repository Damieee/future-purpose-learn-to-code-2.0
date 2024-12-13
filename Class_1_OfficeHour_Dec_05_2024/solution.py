class BankAccount:
    def __init__(self, account_number, account_holder, balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transaction_history.append(f"Withdraw {amount}")

    def check_balance(self):
        return f"Account balance: {self.balance}"

    def transfer(self, amount, target_account):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transaction_history.append(
            f"Transferred {amount} to account {target_account.account_number}"
        )


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, account_type, initial_deposit):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(
            account_number, account_holder, initial_deposit, account_type
        )
        self.accounts[account_number] = new_account
        return new_account

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account not found.")

    def list_accounts(self):
        return [
            {
                "Account Number": account.account_number,
                "Account Holder": account.account_holder,
                "Account Type": account.account_type,
                "Balance": account.balance,
            }
            for account in self.accounts.values()
        ]


# Usage Example
if __name__ == "__main__":
    bank = Bank()

    # Create accounts
    account1 = bank.create_account("John Doe", "Savings", 1000)
    account2 = bank.create_account("Jane Smith", "Checking", 500)

    # Perform transactions
    account1.deposit(-500)
    account1.withdraw(200)
    account1.transfer(300, account2)

    # Check balances
    print(account1.check_balance())
    print(account2.check_balance())

    # List all accounts
    print(bank.list_accounts())
