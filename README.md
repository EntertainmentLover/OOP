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



# Fifth activity: Electronic Device Shopping Cart
## Project Overview
This project is a console-based shopping cart system for an electronic device store. It demonstrates Object-Oriented Programming concepts in Python, especially **inheritance**.
The store contains three device categories:
- Smartphone
- Laptop
- Tablet
Each category inherits common features from the base class `Device`, while also adding its own specific attributes and methods.

## Features
- Display all available devices
- Add devices to cart
- Remove devices from cart
- Checkout and reduce stock
- Apply discounts to devices
- Print cart items and total price
- Use inheritance with subclasses
- Includes unit tests

## Classes
### 1. Device
Base class for all electronic devices.
**Attributes:**
- `name`
- `price`
- `stock`
- `warranty_period`
**Methods:**
- `display_info()`
- `__str__()`
- `apply_discount(discount_percentage)`
- `is_available(amount)`
- `reduce_stock(amount)`

### 2. Smartphone(Device)
**Extra attributes:**
- `screen_size`
- `battery_life`
**Extra methods:**
- `make_call()`
- `install_app()`

### 3. Laptop(Device)
**Extra attributes:**
- `ram_size`
- `processor_speed`
**Extra methods:**
- `run_program()`
- `use_keyboard()`

### 4. Tablet(Device)
**Extra attributes:**
- `screen_resolution`
- `weight`
**Extra methods:**
- `browse_internet()`
- `use_touchscreen()`

### 5. Cart
Manages the shopping cart.
**Methods:**
- `add_device(device, amount)`
- `remove_device(device, amount)`
- `get_total_price()`
- `print_items()`
- `checkout()`

## How to Run
1. Make sure Python 3 is installed.
2. Open terminal in the project folder.
3. Run the program:
```bash
python fifth_ass.py
```

## How to Run Tests
```bash
python -m unittest test_fifth.py
```

## Sample Input / Output
### Sample Run 1
```text
=== Electronic Device Store ===
1. Show Devices
2. Show Cart
3. Remove Item From Cart
4. Checkout
5. Exit
Select an option: 1

--- Available Devices ---
1. Smartphone -> iPhone 15 | Price: $999.00 | Stock: 10 | Warranty: 12 months | Screen: 6.1" | Battery: 20h
2. Smartphone -> Samsung Galaxy S24 | Price: $899.00 | Stock: 8 | Warranty: 24 months | Screen: 6.2" | Battery: 22h
...

Enter device number to add to cart (or b to go back): 1
How many iPhone 15 do you want to add? 2
Added 2 x iPhone 15 to cart.
```

### Sample Run 2
```text
=== Electronic Device Store ===
1. Show Devices
2. Show Cart
3. Remove Item From Cart
4. Checkout
5. Exit
Select an option: 2

--- Cart Items ---
1. iPhone 15 | Qty: 2 | Unit Price: $999.00 | Subtotal: $1998.00
Total Price: $1998.00
```

### Sample Run 3
```text
=== Electronic Device Store ===
1. Show Devices
2. Show Cart
3. Remove Item From Cart
4. Checkout
5. Exit
Select an option: 4

--- Receipt ---
iPhone 15 x 2 = $1998.00
Final Total: $1998.00
Thank you for your purchase!
```

## Files Included
- `fifth_ass.py`
- `test_fifth.py`
- `README.md`

## Notes
- The project includes more than 20 devices.
- Inheritance is used correctly.
- Stock is updated only after successful checkout.
