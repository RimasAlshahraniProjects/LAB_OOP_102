# create BankAccount class
class BankAccount:
    # initializer / constructor
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.__account_holder = account_holder   # private attribute -> encapsulation
        self.__balance = initial_balance         # private attribute -> encapsulation

    # deposit method with validation
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.__balance += amount
        return self.__balance  

    # withdraw method with validation and exception
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise Exception("insufficient funds")
        self.__balance -= amount
        return self.__balance 

    # get current balance
    def get_balance(self):
        return self.__balance 

    # get account holder name
    def get_account_holder(self):
        return self.__account_holder 