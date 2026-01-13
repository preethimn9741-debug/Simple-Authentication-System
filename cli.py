import auth


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            print(auth.register_user(u, p))

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            print(auth.login_user(u, p))

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
