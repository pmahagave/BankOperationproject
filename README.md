

 Features

 Open a new account with auto-generated account number
Deposit money into an account Withdraw money with balance check
 Search if an account exists
 View details of a single account
 Data is stored using Python's pickle module (serialization)
 Robust input validation using custom exceptions
 
Technologies Used
File handling
Pickle module for binary data storage
Custom Exception Handling

Account Data Format
Each bank account is stored as a list:
python
[account_number, customer_name, pin, balance]

Sample Operations:
Open Account → Creates a new user with account number and initial balance
Deposit → Updates balance for the given account
Withdraw → Deducts amount if sufficient balance is available
Search → Checks whether an account number exists
View Single Account Detail → Displays full info of one account
