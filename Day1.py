# Print Sum
a= 19
b= 15
sum =a+b
print(sum)

# Print Diff
a= 19
b= 15
diff =a-b
print(diff)

#Taking input from user and printing it
name = input("name:")
print(name)

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

#Grades of Students
marks = int(input("Marks: "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif( marks >= 70 and marks < 80):
    print("C")
elif( marks >= 60 and marks < 50):
    print("C")
else:
    print("E")

#Single Line IF / Ternary Operator
#<var> = <val1> if <condition> else <val2>
food = input("food: ")
eat = "Yes" if food== "cake" else "No"
print(eat)

#<statement1> if <condition> else <statement2>
food = input("food: ")
print("sweet") if food=="cake" or food=="icecream" else print("not sweet")


#Clever If/ Ternary Operator
#<var> =(false_val , true_val) [<condition>]
age= int(input("Age: "))
vote = ("Yes" , "No") [age<18]

sal = float(input("Salary: "))
tax= sal*(0.1 , 0.2) [sal<=50000]
print("TAX:" ,tax)

