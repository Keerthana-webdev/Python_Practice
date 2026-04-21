
def add(a, b):
    return int(a)+int(b)


def sub(a, b):
    return int(a)-int(b)


def div(a, b):
    return float(a)/float(b)


def multipy(a, b):
    return int(a)*int(b)


def percent(a):
    return float(a)*100


def square(a):
    return int(a)*int(a)


def cube(a):
    return int(a)*int(a)*int(a)


def main():
    while True:

        print("""
Menu:
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Percentage
6. Square
7. Cube
8. Exit
        """)

        userInput = input("Choose from Menu: ")

        if userInput == "1":
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print("Value is: ", add(a, b))

        if userInput == "2":
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print("Value is: ", sub(a, b))

        if userInput == "3":
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print("Value is: ", div(a, b))

        if userInput == "4":
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print("Value is: ", multipy(a, b))

        if userInput == "5":
            a = input("Enter number: ")
            print("Value is: ", percent(a))

        if userInput == "6":
            a = input("Enter number: ")
            print("Value is: ", square(a))

        if userInput == "7":
            a = input("Enter number: ")
            print("Value is: ", cube(a))

        if userInput == "8":
            break


if __name__ == "__main__":
    main()