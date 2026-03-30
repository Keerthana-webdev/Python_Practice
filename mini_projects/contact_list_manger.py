contacts = {}

while True:
    print("1.Add 2.Search 3.Delete 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif choice == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)

    else:
        break