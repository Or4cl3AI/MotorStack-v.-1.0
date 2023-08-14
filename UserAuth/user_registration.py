```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from Motorhead.user_profile import UserProfile

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if username already exists
    user = UserProfile.find(data['username'])
    if user:
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create a new user
    new_user = UserProfile(data['username'], hashed_password)
    new_user.save()

    return jsonify({'message': 'Registered successfully'}), 201
```
This Python script uses Flask to create a simple API endpoint for user registration. It receives a POST request with a JSON payload containing a username and password. It checks if the username already exists in the database, and if not, it hashes the password and creates a new user. The hashed password is stored in the database for security reasons.