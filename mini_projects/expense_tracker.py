class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

class Tracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append(Expense(amount, category))

    def total(self):
        return sum(e.amount for e in self.expenses)

    def show(self):
        for e in self.expenses:
            print(e.category, e.amount)

tracker = Tracker()

tracker.add_expense(100, "Food")
tracker.add_expense(50, "Travel")
tracker.add_expense(200, "Shopping")

tracker.show()
print("Total Expense:", tracker.total())