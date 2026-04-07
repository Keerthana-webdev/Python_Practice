class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def register(user):
    with open("users.txt", "a") as f:
        f.write(user.username + "," + user.password + "\n")

def login(username, password):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    return True
    except FileNotFoundError:
        print("⚠️ No users registered yet!")
    return False

user1 = User("abhi", "1234")
register(user1)

username = input("Enter username: ")
password = input("Enter password: ")

if login(username, password):
    print("✅ Login successful")
else:
    print("❌ Invalid credentials")