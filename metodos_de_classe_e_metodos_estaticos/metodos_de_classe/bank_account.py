class BankAccount:
    interest_rate = 0.9
    def __init__(self, holder, balance=0):
        self.__holder = holder
        self.__balance = balance
        
        
    @property
    def holder(self):
        return self.__holder
    
    @holder.setter
    def holder(self, holder):
        self.__holder = holder
        
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        self.__balance = balance
        
        
    def deposit(self, value):
        if value <= 0:
            print("Invalid Value")
        else:
            self.__balance+= value
            
    def withdraw(self, value):
        if self.__balance < value:
            print("insufficient balance")
        elif(value <= 0):
            print("Invalid Value")
        else:
            self.__balance-= value
            
    @classmethod
    def alter_interest_rate(cls,interest_rate):
        cls.interest_rate = interest_rate
        
        
    @classmethod
    def create_account_with_balance(cls, holder):
        balance = 100
        return cls(holder,balance)