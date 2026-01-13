import json
import hashlib
import os

FILE_NAME = "users.json"


def load_users():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    users = load_users()

    if username in users:
        return "User already exists"

    users[username] = {
        "password": hash_password(password),
        "failed_attempts": 0,
        "locked": False
    }

    save_users(users)
    return "User registered successfully"


def login_user(username, password):
    users = load_users()

    if username not in users:
        return "User not found"

    user = users[username]

    if user["locked"]:
        return "Account is locked"

    if user["password"] == hash_password(password):
        user["failed_attempts"] = 0
        save_users(users)
        return "Login successful"

    user["failed_attempts"] += 1
    if user["failed_attempts"] >= 3:
        user["locked"] = True
        save_users(users)
        return "Account locked after 3 failed attempts"

    save_users(users)
    return "Wrong password"

