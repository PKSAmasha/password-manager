import hashlib
import getpass

password_manager = {}

def create_acc():
    username = input("Enter a username:")
    password = getpass.getpass("Enter the password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully")

def login():
    username = input("Enter a username:")
    password = getpass.getpass("Enter the password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful")
    else:
        print("invalid username or password")

def main():
    while True:
        choice = input("Enter 1 to create an account \nEnter 2 to login \nEnter 0 to exit \n")
        if choice == "1":
            create_acc()
        elif choice == "2":
             login()
        elif choice == "0":
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()     
    