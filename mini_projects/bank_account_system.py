class BankAccount:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
        self.transactions = []

    def check_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

    def show_transactions(self):
        for t in self.transactions:
            print(t)

acc = BankAccount(1000, 1234)

if acc.check_pin(1234):
    acc.deposit(500)
    acc.withdraw(200)
    acc.show_balance()
    acc.show_transactions()
else:
    print("Wrong PIN")