```python
# Motorhead/user_profile.py

class UserProfile:
    def __init__(self, user_id, name, personality, conversations):
        self.user_id = user_id
        self.name = name
        self.personality = personality
        self.conversations = conversations

    @classmethod
    def find(cls, user_id):
        # Implementation to find a user profile
        # This is a placeholder and should be replaced with actual implementation
        return cls(user_id, "name", "personality", [])

    def update_profile(self, name=None, personality=None):
        if name:
            self.name = name
        if personality:
            self.personality = personality

    def get_conversations(self):
        return self.conversations

    def add_conversation(self, conversation):
        self.conversations.append(conversation)
```