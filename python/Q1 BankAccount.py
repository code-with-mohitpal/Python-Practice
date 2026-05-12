# =========================
# Q1 BankAccount
# =========================

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


acc = BankAccount(101, "Mohit", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()
