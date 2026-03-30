class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        if BankAccount.valid_value(value):
            self.balance += value

    @staticmethod
    def valid_value(value):
        return value > 0