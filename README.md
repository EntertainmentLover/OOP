# OOP
# Third activity: Personal Account Management System
## Description
This project is a Python-based application that simulates a personal bank account system using Object-Oriented Programming (OOP).
It allows users to:
- Deposit money
- Withdraw money
- Check account balance
- View transaction history

## Concepts Used
- Classes and Objects
- Encapsulation
- Lists (for storing transactions)
- Operator Overloading (`+` and `-`)
- Datetime handling

## Project Structure
- `Amount` class -> represents a single transaction
- `PersonalAccount` class -> manages the account and operations
- `main()` -> user interface (menu system)

## How to Run
### Requirements:
- Python 3.x



# UML Class Diagram

+----------------------+
|        Amount        |
+----------------------+
| - amount: float      |
| - timestamp: datetime|
| - transaction_type: str |
+----------------------+
| + __init__()         |
| + __str__()          |
+----------------------+

            ▲
            | uses
            |

+----------------------------------+
|        PersonalAccount           |
+----------------------------------+
| - account_id: int                |
| - owner: str                     |
| - balance: float                 |
| - transaction_history: list      |
+----------------------------------+
| + deposit(amount)                |
| + withdraw(amount)               |
| + get_balance()                  |
| + get_transaction_history()      |
| + get_account_id()               |
| + set_account_id()               |
| + get_owner()                    |
| + set_owner()                    |
| + __str__()                      |
| + __add__(amount)                |
| + __sub__(amount)                |
+----------------------------------+



# Forth activity: User Management System
## Description
This project is a simple **User Management System** implemented in Python using Object-Oriented Programming (OOP).
It allows you to:
- Create users
- Find users
- Update users
- Delete users
- Count total users
The system also includes utility functions for generating IDs, emails, and strong passwords.

## Project Structure:
file, README.md

## Classes Overview
### 1. User
Represents a user.
**Attributes:**
- user_id (int)
- name (str)
- surname (str)
- email (str)
- password (str)
- birthday (datetime)
**Methods:**
- get_details() -> returns user info
- get_age() -> calculates ages

### 2. UserService
Manages users using a dictionary.
**Methods:**
- add_user(user)
- find_user(user_id)
- delete_user(user_id)
- update_user(user_id, user_update)
- get_number()

### 3. UserUtil
Provides utility functions.
**Methods:**
- generate_user_id()
- generate_password()
- is_strong_password(password)
- generate_email(name, surname, domain)
- validate_email(email)

## How to Run
1. Make sure Python is installed
2. Run the program: bash
python forth_ass.py

## Example of usage
=== USER MANAGEMENT ===
1. Add user
2. Find user
3. Delete user
4. Update user
5. Count users
0. Exit
Choose: 1
Enter name: John
Enter surname: Doe
Enter email domain: gmail.com
Generated email: john.doe@gmail.com
Generated password: A1b@9kLm2
Enter birthday: 2000-05-15
User added!
