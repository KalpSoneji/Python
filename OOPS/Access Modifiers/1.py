class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def checkBalance(self):
        return self.__balance
    
BA = BankAccount(10000)
BA.deposit(2000)
print(BA.checkBalance())