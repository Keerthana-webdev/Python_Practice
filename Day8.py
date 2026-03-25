#Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi" , self.name , "your avg score is:" , sum/3)

s1 = Student("Tony stark" , [99,92,95])
s1.get_avg()

s1.name ="ironman"
s1.get_avg()

#Create Account class with 2 attributes-balance & account no.Create methods for debit , credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self , amount):
        self.balance -= amount
        print("Rs." , amount , "was debited")
        print("Total balance=" , self.get_balance())

    def credit(self , amount):
        self.balance += amount
        print("Rs." , amount , "was credited")
        print("Total balance=" , self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1600)
acc1.credit(300)
acc1.debit(1600)
acc1.credit(300)
