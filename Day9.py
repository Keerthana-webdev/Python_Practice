#Dunder method using __add__();
class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self , num2):
        newReal = self.real +num2.real
        newImg = self.img +num2.img
        return Complex(newImg , newImg)
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

#Dunder method using __sub__();
class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

    def __sub__(self , num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newImg , newImg)
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()

#Define a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle.
#Define a Perimetr() method of the class which allows you to calculate the perimeter of the circle.
class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#Define a Employee class with attributes role, department & salary.This class also a showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.
class Employee:
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =" , self.role)
        print("dept =", self.dept)
        print("salary =" , self.salary)

class Engineer(Employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer" , "IT" , "75,000")
    
eng1 = Engineer("Keerthana" , "21")
eng1.showDetails()

#Create a class called Order which stores item & its price.
#Use Dunder function __gt__() to convey that: order1>order2 if price of order1>price of order2
class Order:
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self , odr2):
        return self.price > odr2.price

odr1 = Order("chips" , 20)
odr2 = Order("tea" , 15)
print(odr1 > odr2) #True
