import json
import os
import random
import string
from cryptography.fernet import Fernet

# File to store encrypted passwords
DATA_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Generate or load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

# Save encrypted data to file
def save_data(data, fernet):
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)

# Load and decrypt data from file
def load_data(fernet):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
    except Exception:
        return {}

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Add a new password
def add_password(data, fernet):
    account = input("Enter the account name: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password (leave blank to generate a random password): ").strip()
    if not password:
        password = generate_password()
        print(f"Generated Password: {password}")
    data[account] = {"username": username, "password": password}
    save_data(data, fernet)
    print("Password saved successfully!")

# View all stored passwords
def view_passwords(data):
    if not data:
        print("No passwords stored yet.")
        return
    print("\n--- Stored Passwords ---")
    for account, credentials in data.items():
        print(f"Account: {account}")
        print(f"  Username: {credentials['username']}")
        print(f"  Password: {credentials['password']}\n")

# Search for a password
def search_password(data):
    account = input("Enter the account name to search: ").strip()
    if account in data:
        print("\n--- Account Found ---")
        print(f"Account: {account}")
        print(f"Username: {data[account]['username']}")
        print(f"Password: {data[account]['password']}")
    else:
        print("Account not found.")

# Main menu
def main():
    fernet = load_key()
    data = load_data(fernet)

    while True:
        print("\n--- Password Manager ---")
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search for a Password")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_password(data, fernet)
        elif choice == "2":
            view_passwords(data)
        elif choice == "3":
            search_password(data)
        elif choice == "4":
            print("Goodbye! Stay secure.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
