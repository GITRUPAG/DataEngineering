class  BankAccount:

    Bank = "HDFC"
    def __init__(self, balance):
        # self.balance = balance
        self.__balance = balance  # name mangling - accessed through class methods rather than directly

    # Getter and Setter Methods

    # Getter Method - used to retrieve data
    def get_balance(self):
        return self.__balance

    # setter method - modify the attribute

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

# Encapsulation - controlled access

# creating object
account = BankAccount(50000)

account.set_balance(500)

print("Balance : ", account.get_balance())

# print(account.balance)
#
# account.balance = 25000
#
# print(account.balance)