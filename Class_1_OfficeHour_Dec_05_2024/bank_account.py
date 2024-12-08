# Define the Class
class BankAccount:
  def __init__(self, account_number, account_holder, balance, account_type):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = int(balance)
    self.account_type = account_type
    self.transaction_log = []

  def deposit(self, amount):
    # Checks if the amount to be deposited is a negative number
    if(amount <= 0):
      print('Your deposit amount cannot be less than or equal to 0')
    # Checks if the amount is not a number
    elif not isinstance(amount, int):
      print('Please enter a valid amount')
    # Update balance and Log the transaction
    else:
      self.balance  += amount
      self.transaction_log.append(f"Deposited {amount}")
      print('Deposit Successful')

  def withdraw(self, amount):
    # Checks if the amount to be deposited is a negative number
    if(amount <= 0):
      print('Your deposit amount cannot be less than or equal to 0')
    # Checks for Insufficient Balance
    elif(amount > self.balance):
      print('Insufficient Funds')
    # Checks if the amount is not a number
    elif not isinstance(amount, int):
      print('Please enter a valid amount')
    # Update balance and Log the transaction
    else:
      self.balance  -= amount
      self.transaction_log.append(f"Withdrew {amount}")
      print('Withdrawal Successful')

  def check_balance(self):
    print(f'Your balance is ${self.balance}')

  def transfer(self, amount, target_account):
    # Checks if the amount to be deposited is a negative number
    if(amount <= 0):
      print('Your deposit amount cannot be less than or equal to 0')
    # Checks for Insufficient Balance
    elif(amount > self.balance):
      print('Insufficient Funds')
    # Checks if the amount is not a number
    elif not isinstance(amount, int):
      print('Please enter a valid amount')
    # Update balance and log transaction in both accounts
    else:
      self.balance -= amount
      target_account.balance += amount
      self.transaction_log.append(f"Transferred {amount} to {target_account.account_holder} ")
      target_account.transaction_log.append(f'Received {amount} from {self.account_holder}')
      print('Transfer Successful')





myBankAccount = BankAccount(203333333, 'Dami', 1000, 'Savings')
myBankAccount.check_balance()