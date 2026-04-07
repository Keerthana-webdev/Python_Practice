def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with open("contacts.txt", "a") as f:
        f.write(f"{name}:{phone}\n")

def search_contact():
    name = input("Enter name to search: ")

    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                n, p = line.strip().split(":")
                if n == name:
                    print(f"📞 {name} -> {p}")
                    return
        print("❌ Not found")
    except FileNotFoundError:
        print("❌ No contacts found")

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        search_contact()
    elif ch == "3":
        break