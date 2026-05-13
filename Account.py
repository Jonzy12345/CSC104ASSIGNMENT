class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        """Base withdraw method can be overwritten by the subclasses"""
        if amount > 0:
            self._balance += amount
            print(f"Deposit of {amount} successful. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance


class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def withdraw(self, amount):
        """Override withdraw to enforce the $100 withdraw limit"""
        if amount > self.withdraw_limit:
            print(f"Withdrawal failed. Amount exceeds withdraw limit of ${self.withdraw_limit}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Invalid withdrawal amount or insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self._balance}")

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")


if __name__ == "__main__":
    print("---Savings Account---")
    savings = Savings("Samuel", 1000)
    print(f"Initial balance: {savings.get_balance()}")
    savings.deposit(500)
    savings.withdraw(50)
    savings.apply_interest()
