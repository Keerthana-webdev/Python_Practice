class Chat:
    def __init__(self):
        self.messages = []

    def send_message(self, user, msg):
        self.messages.append(f"{user}: {msg}")

    def show_chat(self):
        for m in self.messages:
            print(m)

chat = Chat()

chat.send_message("Keerthi", "Hello!")
chat.send_message("Ram", "Hi!")
chat.send_message("Keerthi", "How are you?")

chat.show_chat()