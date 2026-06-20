def square(x):
       return x * x

def cube(x) :
      return x * x * x

def half(x) :
      return x / 2

def area(x):
      return 3.14 * x * x

def circumference(c):
      return 2 * 3.14 * x

def examples(x):
      print("Examples:  Eyes, Wheels, Bottle Cap, Ring etc. ")
      return 

x = int(input("Give me the radius of the circle>>  "))

print('''
      1.Area
      2.Circumference
      3.Examples
      ''')

function = int(input("Select any function >>  "))

if function == 1:
      a = area(x)

elif function == 2:
      a = circumference(x)

elif function == 3:
      a = examples(x)

else :
      print("It was an invalid function request.Try Again")

print(a)      

print("Thank you for using Keerthana's Softwares")      
      
           