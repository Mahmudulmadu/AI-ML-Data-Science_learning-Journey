class BankAccount:
    def __init__(self, id, name, balance):
        self.name = name
        self._id = id
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance


c1 = BankAccount("123", "Mahmudul", 10_000)

print(c1.name, c1._id, c1.get_balance())  #c1._BankAccount__balance not true private
        