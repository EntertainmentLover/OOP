from datetime import datetime
class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type} | {self.amount:.2f}"


class PersonalAccount:
    def __init__(self, account_id: int, owner: str):
        self.account_id = account_id
        self.owner = owner
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        transaction = Amount(amount, "DEPOSIT")
        self.balance += amount
        self.transaction_history.append(transaction)
        print("Deposit successful")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        transaction = Amount(amount, "WITHDRAWAL")
        self.balance -= amount
        self.transaction_history.append(transaction)
        print("Withdrawal successful")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found.")
            return
        print("\nTransaction History:")
        for t in self.transaction_history:
            print(t)

    def get_account_id(self):
        return self.account_id

    def set_account_id(self, new_id: int):
        self.account_id = new_id

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner: str):
        self.owner = new_owner

    def __str__(self):
        return (f"Account ID: {self.account_id}\n"
                f"Owner: {self.owner}\n"
                f"Balance: {self.balance:.2f}")

    def __add__(self, amount: float):
        self.deposit(amount)
        return self

    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self

def main():
    print("Creating a personal account...")
    account_id = int(input("Enter account ID: "))
    owner = input("Enter account owner name: ")
    account = PersonalAccount(account_id, owner)
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current Balance: {account.get_balance():.2f}")
        elif choice == '4':
            account.get_transaction_history()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()