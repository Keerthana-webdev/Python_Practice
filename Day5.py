#Print numbers from 1 to 100...........Using while loop
i=1
while i<=100:
    print(i)
    i+=1

#Print numbers from 100 to 1...........Using while loop
i=100
while i>=1:
    print(i)
    i-=1

#Print the multiplication table of a number n...........Using while loop
n= int(input("Enter number: "))
i=1
while i<= 10:
    print(n*i)
    i+=1
    
#Print the elements of the following list using a loop...........Using while loop
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i< len(nums):
    print(nums[i])
    i+=1

#Traverse
heroes=["ironman" , "thor" , "superman" , "batman"]
i=0
while i< len(heroes):
    print(heroes[i])
    i+=1

#Search for a number x in this tuple using loop...........Using while loop
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
x=49

i=0
while i< len(nums):
    if(nums[i] ==x):
        print("Found at idx" , i)
    else:
        print("finding...")
    i+=1

#Print the elements of the following list using a loop...........Using for loop
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
for el in nums:
    print(nums[i])
    i+=1

#Search for a number x in this tuple using loop...........Using for loop
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
x=49

i=0
for el in nums:
    if(el == x):
        print("Number found at idx" , i)
        break
    i+=1

#Print numbers from 1 to 100...........Using for & range loop.
for i in range(1 , 101):
    print(i)

#Print numbers from 100 to 1..........Using for & range loop.
for i in range(100 , 0 , -1):
    print(i)

#Print the multiplication table of a number n...........Using for & range loop.
n = int(input("Enter number: "))
for i in range(1 ,11):
    print(n*i)

#Write a program to find the sum of first n numbers.........Using while loop
n = 6
sum = 0
i= 1
while i <= n:
    sum += i
    i += 1
print("Total sum=", sum)

#Write a program to find the sum of first n numbers.........Using for loop
n = 7
sum = 0
for i in range(1 , n+1):
    sum += i
print("Total sum=", sum)

#Write a program to find the factorial of first numbers.........Using while loop
n = 8
fact = 1
i= 1
while i <= n:
    fact *= i
    i += 1
print("Factorial=", fact)

#Write a program to find the factorial of first numbers.........Using for loop
n = 9
fact = 1
for i in range(1 , n+1):
    fact *= i
print("Factorial=", fact)




