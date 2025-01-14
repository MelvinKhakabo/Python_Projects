# Password Manager

## Objective
Create a Python-based Password Manager to securely store and retrieve passwords for different accounts.

## Features

### Add New Passwords
Save account names, usernames, and passwords.
### View Stored Passwords
Retrieve saved passwords securely.

### Password Generation
Generate strong, random passwords.

### Search Functionality
Search for passwords by account name.

### Encryption:
Encrypt stored passwords for enhanced security.

--------------------------------------------------------------------------------------------------------------------

# How It Works
## Encryption
A unique key is generated and stored in secret.key.
Password data is encrypted using the Fernet symmetric encryption from the cryptography library.

## Adding Passwords
Users can manually input passwords or let the app generate strong random passwords.

## Viewing Passwords
Decrypts and displays all stored passwords securely.

## Searching
Allows users to search for credentials by account name.

## Data Storage
Encrypted data is stored in passwords.json.

--------------------------------------------------------------------------------------------------------------------

