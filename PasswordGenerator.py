# Programmer: Ash
# Date: 3.12.2024
# Program: Password Generator
# Resourse: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA


import hashlib
import os


def hash_password(password, salt):
    # Combine password and salt
    password_with_salt = password.encode('utf-8') + salt.encode('utf-8')

    # Hash the combined password and salt using SHA-256
    hashed_password = hashlib.sha256(password_with_salt).hexdigest()

    return hashed_password


def main():
    # Get user input for password
    password = input("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16).hex()

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)


if __name__ == "__main__":
    main()

