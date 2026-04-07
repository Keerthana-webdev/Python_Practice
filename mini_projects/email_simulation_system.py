class Email:
    def __init__(self, sender, msg):
        self.sender = sender
        self.msg = msg

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send(self, other, msg):
        other.inbox.append(Email(self.name, msg))

    def read(self):
        for mail in self.inbox:
            print(mail.sender, ":", mail.msg)

u1 = User("Keerthi")
u2 = User("Ram")

u1.send(u2, "Hello Ram!")
u2.send(u1, "Hi Keerthi!")
u1.send(u2, "How are you?")

print("\nRam's Inbox:")
u2.read()

print("\nKeerthi's Inbox:")
u1.read()