# simple-authentication-system

## Project Description
This project is a **simple user authentication system** implemented in Python.
It allows users to **register** and **log in** using a username and password.
User data is stored in a JSON file.


## How the Script Works
- Users can register with a username and password
- Passwords are stored in hashed form
- Users can log in using their credentials
- After 3 failed login attempts, the user account is locked
- User information is saved in `users.json`

## Project Structure

simple_auth/

├── app.py          # Flask application entry point

├── auth.py         # Authentication logic (no input/output)

├── cli.py          # Command-line interface (interactive)

├── users.json      # User storage (JSON)

├── tests/

│   └── test_auth.py

└── README.md

## Installation Steps
1. Install python and falsk

   pip install flask pytest

2. Go to project folder

   cd C:\simple_auth

3. Run the Flask app

   python app.py

4. Open in browser

   http://127.0.0.1:5000

5. Run CLI or tests (optional)

   python cli.py
   
   pytest

## Menu Options

When the script runs, the following options are shown:
1. Register
2. Login
3. Exit

## Output

Messages are displayed in the console for:

Successful registration

Successful login

Wrong password

Account lock after failed attemp

## terminal output screenshort

<img width="1310" height="803" alt="Screenshot 2026-01-13 103237" src="https://github.com/user-attachments/assets/49b2f3a3-48d1-4539-863a-acb5a9afac40" />

## Conclusion

This project demonstrates a clean and beginner-friendly Flask authentication application with proper separation of concerns. The application is designed to avoid common issues such as pytest stdin errors by keeping all user interaction in the CLI layer and limiting core logic to reusable functions.
By following best practices in project structure and testing, the application is easy to run, extend, and maintain. It serves as a strong foundation for building more advanced authentication systems, including REST APIs, database integration, and secure login mechanisms.
