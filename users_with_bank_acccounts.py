

class BankAccount:

    def __init__(self, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("You cannot deposit a negative amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def display_account_info(self):
        print(f"balance: {self.balance}")

    def yield_interest(self):
        # Interest rate will be variable,
        # calculate interest and add it to the balance.
        self.balance += self.int_rate*self.balance


bank_account = BankAccount(0.0325, 90)
bank_account.display_account_info()
bank_account.deposit(10)
bank_account.display_account_info()
bank_account.yield_interest()
bank_account.display_account_info()
