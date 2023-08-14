```python
import bcrypt
from Motorhead.user_profile import UserProfile

class UserAuthentication:

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    @staticmethod
    def verify_password(user_id, password):
        user = UserProfile.find(user_id)
        if user:
            return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        return False

    @staticmethod
    def authenticate_user(user_id, password):
        if UserAuthentication.verify_password(user_id, password):
            return True
        return False
```