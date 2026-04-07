def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    with open("marks.txt", "a") as f:
        f.write(f"{name} - {marks}\n")

def view_students():
    try:
        with open("marks.txt", "r") as f:
            print("\n📊 Student Records:")
            print(f.read())
    except FileNotFoundError:
        print("❌ No records found.")

while True:
    print("\n1. Add Student\n2. View Records\n3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        break