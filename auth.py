import json
import hashlib
import os

FILE_NAME = "users.json"


# ----------------- Helper functions -----------------

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


# ----------------- Core functions -----------------

def register_user(username, password):
    users = load_users()

    if username in users:
        print("User already exists")
        return

    users[username] = {
        "password": hash_password(password),
        "failed_attempts": 0,
        "locked": False
    }

    save_users(users)
    print("User registered successfully")


def login_user(username, password):
    users = load_users()

    if username not in users:
        print("User not found")
        return

    user = users[username]

    if user["locked"]:
        print("Account is locked")
        return

    if user["password"] == hash_password(password):
        print("Login successful")
        user["failed_attempts"] = 0
    else:
        user["failed_attempts"] += 1
        print("Wrong password")

        if user["failed_attempts"] >= 3:
            user["locked"] = True
            print("Account locked after 3 failed attempts")

    save_users(users)


# ----------------- Menu -----------------

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        register_user(u, p)

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        login_user(u, p)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
