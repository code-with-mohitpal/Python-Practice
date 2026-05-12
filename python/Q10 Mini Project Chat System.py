# =========================
# Q10 Mini Project Chat System
# =========================

class User:
    def __init__(self, username):
        self.username = username


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display(self):
        print(f"{self.sender.username}: {self.text}")


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.username, "joined the chatroom")

    def leave(self, user):
        self.users.remove(user)
        print(user.username, "left the chatroom")

    def send_message(self, message):
        self.messages.append(message)

    def show_chat_history(self):
        print("\nChat History:")
        for msg in self.messages:
            msg.display()


u1 = User("Mohit")
u2 = User("Rahul")

chat = ChatRoom()

chat.join(u1)
chat.join(u2)

m1 = Message(u1, "Hello")
m2 = Message(u2, "Hi Mohit")

chat.send_message(m1)
chat.send_message(m2)

chat.show_chat_history()

chat.leave(u2)
