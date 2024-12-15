# FuturePurpose Learn to Code <2.0> - Bank Management System - OOP Python Project

## Project Overview
In this assignment, you will design and implement a comprehensive Bank Management System using Object-Oriented Programming (OOP) principles in Python. This project will help you apply your recently learned OOP concepts to create a practical, real-world application.

## Learning Objectives
- Apply Object-Oriented Programming principles
- Design and implement class structures
- Practice encapsulation, inheritance, and polymorphism
- Develop error handling and input validation skills
- Create a modular and extensible software design

## Project Requirements

### 1. Bank Account Class
Create a `BankAccount` class with the following specifications:

#### Attributes
- `account_number`: A unique identifier for the account
- `account_holder`: Name of the account holder
- `balance`: Current account balance
- `account_type`: Type of account (e.g., Savings, Checking)

#### Methods
1. `__init__()`: Constructor method to initialize account details
2. `deposit(amount)`: 
   - Add money to the account
   - Validate that deposit amount is positive
   - Update balance
   - Log the transaction
3. `withdraw(amount)`:
   - Remove money from the account
   - Validate sufficient funds
   - Prevent overdrafts
   - Log the transaction
4. `check_balance()`: 
   - Return current account balance
   - Optional: Format balance display
5. `transfer(amount, target_account)`:
   - Transfer money between accounts
   - Validate sufficient funds
   - Update balances of both accounts
   - Log the transaction

### 2. Bank Class (Optional Challenges)
Create a `Bank` class to manage multiple accounts:

#### Attributes
- `accounts`: A list or dictionary to store bank accounts
- `total_bank_balance`: Total money in the bank

#### Methods
1. `create_account(account_holder, account_type, initial_deposit)`:
   - Generate a unique account number
   - Create a new bank account
   - Add account to bank's account list
2. `find_account(account_number)`:
   - Retrieve an account by its account number
3. `delete_account(account_number)`:
   - Remove an account from the bank
4. `list_accounts()`:
   - Display all accounts in the bank

### 3. Additional Features (Optional Challenges)
- Implement interest calculation for savings accounts
- Add account types (Checking, Savings, Business)
- Create a simple authentication system
- Add transaction history for each account
- Implement minimum balance requirements
- Create different fee structures for different account types

## Bonus Challenges
1. Implement error handling with custom exceptions
2. Add input validation for all methods
3. Create a simple command-line interface (CLI) for interaction
4. Implement basic data persistence (saving/loading accounts)

## Submission Guidelines
1. Create a Branch of this repository on github and use your name as the name of the branch (e-g, obinna_future_purpose). 
2. clone the repository and push your commits to  your branch. I ll review it there.
3. Ensure your code is clean and readable.
4. Provide a brief README explaining how to run your program

## Example Usage
```python
# Example of how the code might be used
bank = Bank()

# Create accounts
account1 = bank.create_account("John Doe", "Savings", 1000)
account2 = bank.create_account("Jane Smith", "Checking", 500)

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.transfer(300, account2)

# Check balance
print(account1.check_balance())
```

## Hints and Tips
- Start by designing your classes on paper
- Break down the problem into smaller, manageable parts
- Test each method thoroughly as you implement it
- Use print statements or logging to debug
- Don't try to implement everything at once

## Resources
- Python Official Documentation
- Real Python OOP Tutorials
- GeeksforGeeks Python OOP Guide

## Submission Deadline
Next week Monday - 9TH Dec,2024

## Good Luck!
This project is an excellent opportunity to demonstrate your understanding of Object-Oriented Programming. Be creative, have fun, and don't hesitate to ask for help if you get stuck!
