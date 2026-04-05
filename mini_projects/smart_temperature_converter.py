def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", f_to_c(f))

    elif choice == "3":
        break
    else:
        print("Invalid choice!")