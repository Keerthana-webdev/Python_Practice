def write_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("✅ Note saved!")

def read_notes():
    try:
        with open("notes.txt", "r") as f:
            print("\n📒 Your Notes:")
            print(f.read())
    except FileNotFoundError:
        print("❌ No notes found.")

while True:
    print("\n1. Write Note\n2. Read Notes\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        write_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice")