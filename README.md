# simple-authentication-syste

## Project Description
This project is a **simple user authentication system** implemented in Python.
It allows users to **register** and **log in** using a username and password.
User data is stored in a JSON file.

---

## Files
- `auth.py` – Authentication script
- `users.json` – Stores user credentials and login status
- `README.md` – Project documentation

---

## How the Script Works
- Users can register with a username and password
- Passwords are stored in hashed form
- Users can log in using their credentials
- After 3 failed login attempts, the user account is locked
- User information is saved in `users.json`

---

## Menu Options
When the script runs, the following options are shown:
1. Register
2. Login
3. Exit

---

## How to Run

python auth.py

Output

Messages are displayed in the console for:

Successful registration

Successful login

Wrong password

Account lock after failed attemp

Notes

User data is persisted in users.json

Accounts are locked after three failed login attempts

No external libraries are required
