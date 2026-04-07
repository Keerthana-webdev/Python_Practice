class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def login(self, pin):
        return self.__pin == pin

    def withdraw(self, amount):
        if amount > 5000:
            print("Limit exceeded")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def check_balance(self):
        print("Balance:", self.__balance)

atm = ATM(10000, 1234)

pin = int(input("Enter PIN: "))

if atm.login(pin):
    atm.deposit(2000)
    atm.withdraw(3000)
    atm.check_balance()
else:
    print("Wrong PIN")