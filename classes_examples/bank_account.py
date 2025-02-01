class BankAccount:
    # Class property
    branch1 = 0
    branch2 = 0
    total_accounts = branch1 + branch2

    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        if BankAccount.branch1 < 50:
            BankAccount.branch1 += 1
        else:
            BankAccount.branch2 += 1

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
    
    @classmethod
    def transfer(cls, account1, account2, money):
        if account1.balance >= money:
            account1.withdraw(money)
            account2.deposit(money)
        else:
            print("No sufficient balance")

    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and len(name) > 0

# Example Usage:
account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob", 200)
print(BankAccount.get_total_accounts()) # Output: 2
BankAccount.transfer(account2, account1, 150)
print(account1.balance, account2.balance)
