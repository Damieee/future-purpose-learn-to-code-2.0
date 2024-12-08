class BankAccount:
  def __init__(self, account_number, account_holder, balance, account_type):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = int(balance)
    self.account_type = account_type
    self.transaction_log = []

  def deposit(self, amount):
    if(amount <= 0):
      print('Your deposit amount cannot be less than or equal to 0')
    elif not isinstance(amount, int):
      print('Please enter a valid amount')
    else:
      self.balance  += amount
      self.transaction_log.append(f"Deposited {amount}")
      print('Deposit Successful')


