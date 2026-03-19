import random
import string
import re
from datetime import datetime
class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}"

    def get_age(self):
        today = datetime.now()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age


class UserService:
    users = {}
    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user
        print("User added!")
    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)
    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]
            print("User deleted!")
        else:
            print("User not found")
    @classmethod
    def update_user(cls, user_id, user_update):
        user = cls.find_user(user_id)
        if user:
            user.name = user_update.name
            user.surname = user_update.surname
            user.email = user_update.email
            user.password = user_update.password
            user.birthday = user_update.birthday
            print("User updated!")
        else:
            print("User not found")
    @classmethod
    def get_number(cls):
        return len(cls.users)
    
class UserUtil:
    @staticmethod
    def generate_user_id():
        year = str(datetime.now().year)[-2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(year + random_digits)
    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices(
                string.ascii_letters + string.digits + "!@#$%^&*()", k=10
            ))
            if UserUtil.is_strong_password(password):
                return password
    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()" for c in password)
        )
    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$'
        return re.match(pattern, email) is not None

def create_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    domain = input("Enter email domain (e.g. gmail.com): ")
    email = UserUtil.generate_email(name, surname, domain)
    password = UserUtil.generate_password()
    print(f"Generated email: {email}")
    print(f"Generated password: {password}")
    date_str = input("Enter birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(date_str, "%Y-%m-%d")
    user_id = UserUtil.generate_user_id()
    user = User(user_id, name, surname, email, password, birthday)
    UserService.add_user(user)

def show_user():
    user_id = int(input("Enter user ID: "))
    user = UserService.find_user(user_id)
    if user:
        print(user.get_details())
        print("Age:", user.get_age())
    else:
        print("User not found")

def delete_user():
    user_id = int(input("Enter user ID: "))
    UserService.delete_user(user_id)

def update_user():
    user_id = int(input("Enter user ID to update: "))
    name = input("New name: ")
    surname = input("New surname: ")
    domain = input("New domain: ")
    email = UserUtil.generate_email(name, surname, domain)
    password = UserUtil.generate_password()
    date_str = input("New birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(date_str, "%Y-%m-%d")
    updated_user = User(user_id, name, surname, email, password, birthday)
    UserService.update_user(user_id, updated_user)

def menu():
    while True:
        print("\n=== USER MANAGEMENT ===")
        print("1. Add user")
        print("2. Find user")
        print("3. Delete user")
        print("4. Update user")
        print("5. Count users")
        print("0. Exit")
        choice = input("Choose: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            show_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            print("Total users:", UserService.get_number())
        elif choice == "0":
            break
        else: 
            print("Invalid choice")

if __name__ == "__main__":
    menu()
