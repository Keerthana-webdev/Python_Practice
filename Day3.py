#write a program to check wheather a person can vote or note
age = int(input("Enter ur age:"))
if (age>=18):
    print("can vote")
else:
    print("cannot vote")

#Traffic Lights Code
light = input("light: ")
if(light== "red"):
    print("stop")
elif(light== "yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

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
    print("Multiple of 7")
else:
    print("Not a multiple")

#Write a program to ask the user to enter web series of their 3 favorite movies & store them in a list.
web_series = []
web_series.append(input("Enter 1st web_serie: "))
web_series.append(input("Enter 2nd web_serie: "))
web_series.append(input("Enter 3rd web_serie: "))

print(web_series)

#Write a program to check if a list contains a palindrome of elements.(hint:use copy()method.
list1 = ["k" , "a" , "r" , "a", "k"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

#Write a program to count the number of students with the "A" grade in the follwing tuple.
#["C" , "D" , "A" , "A" , "B" , "B" , "A"]
grade = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]
print(grade.count("A"))

#Store the above values in a list & sort them from "A" To "D".
grade = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]
grade.sort()
print(grade)



