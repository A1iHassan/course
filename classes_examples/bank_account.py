class BankAccount:
    # Class property
    total_accounts = 0

    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1

    # Instance Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds. Your balance is: {self.balance}.")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and len(name) > 0

# Example Usage:
account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob", 200)
print(BankAccount.get_total_accounts()) # Output: 2
