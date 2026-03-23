#function definition
def calc_sum(a,b): #parameters
    return a+b

sum = calc_sum(1,2) #sunction call: arguments
print(sum)

#function example
def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()

#Average pf 3 numbers.
def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(19,8,24)

#Write a program to print the length of a list.(list is the parameter)
fruits = ["apple" , "mango" , "banana" , "grapes" ,"papaya" , "orange"]
def print_len(list):
    print(len(list))

print_len(fruits)

#Write a program to print the elements of a list in a single line.(list is the parameter)
fruits = ["apple" , "mango" , "banana" , "grapes" ,"papaya" , "orange"]
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(fruits)
print()

#Write a program to find the factorial of n.(n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(19)

#Write a program to convert USB to INR.
def converter(usd_val):
    inr_val = usd_val * 84
    print(usd_val , "USD =" , inr_val , "INR")

converter(100)

#Write a simple python function that atkes a number as a parameter and prints wheather it is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("ODD")

even_odd(19)
even_odd(24)

#recursive function example1
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

show(5)

#recursive function example2
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print("END")

show(3)

#Write a recursive function to calculate factorial n numbers.
def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))

#Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1)+n
sum = calc_sum(100)
print(sum)

#Write a recursive function to print all elements in a list.
#Hint: Use list & index as parameters.
def print_list(list , idx=0):
    if (idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple" , "mango" , "banana" , "grapes" ,"papaya" , "orange"]
print_list(fruits)

