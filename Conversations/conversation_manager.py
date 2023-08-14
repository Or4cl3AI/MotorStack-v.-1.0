```python
from Motorhead.user_profile import UserProfile
from Motorhead.conversation import Conversation
from Alana.alana import Alana

class ConversationManager:
    def __init__(self):
        self.alana = Alana()

    def start_conversation(self, user_id, input):
        user = UserProfile.find(user_id)
        context = Conversation.for_user(user_id)
        return self.alana.chat(input, user_id)

    def save_conversation(self, input, response, user_id):
        self.alana.save_exchange(input, response, user_id)

    def generate_response(self, input, context, user):
        return self.alana.generate_response(input, context, user)
```