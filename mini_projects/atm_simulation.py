balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amt = int(input("Enter amount: "))
        balance += amt

    elif choice == "3":
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")

    elif choice == "4":
        break

    else:
        print("Invalid choice")