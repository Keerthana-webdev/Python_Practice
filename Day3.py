#write a program to check wheather a person can vote or note
age = int(input("Enter ur age:"))
if (age>=18):
    print("can vote")
else:
    print("cannot vote")

#Grades of the Students
marks = int(input("Enter student marks: "))
if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks < 90):
    grade="B"
elif( marks >= 70 and marks < 80):
    grade="C"
elif( marks >= 60 and marks < 50):
    grade="C"
else:
    grade="E"

print("Grade pf the student ->", grade)

#Nesting
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot driver")

#write a program to check if a number entered by the user is odd or even.
num = int(input("Enter number:"))
if(num % 2==0):
    print("EVEN")
else:
    print("ODD")

#write a program to find the greatest of 3 numbers entered by the user.
a = int(input("Enter  first number:"))
b = int(input("Enter  second number:"))
c = int(input("Enter  third number:"))
if(a>=b and a>=c):
    print("First number is largest" , a)
elif(b>=c):
    print("Second number is largest" , b)
else:
    print("Third  number is largest" , c)

#write a program to check if a number is a multiple of 7 or not.
x= int(input("enter number:"))

if(x % 7 ==0):
    print("Multiple of5")
else:
    print("Not a multiple")
    