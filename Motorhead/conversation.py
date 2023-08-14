```python
# Motorhead/conversation.py

class Conversation:
    def __init__(self):
        self.conversations = {}

    def for_user(self, user_id):
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        return self.conversations[user_id]

    def add_message(self, user_id, message):
        self.for_user(user_id).append(message)

    def get_conversation(self, user_id):
        return self.for_user(user_id)
```