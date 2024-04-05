#Password Generator

import os
import time
import string
import random


def restart():
    """Prompts user to restart the program."""
    while True:
        restart = input("\nPress (ENTER) to restart the program ").lower().replace(' ', '')
        if restart == "":
            print("\n***Restarting Program***")
            time.sleep(1)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("**Invalid Input**")
            print("\nTry Again")
            time.sleep(2)
            os.system("cls")


def generate_password(length):
    """Generates a random password with at least one digit, uppercase, lowercase, and special character."""

    # Ensure minimum length of 4
    if length < 4:
        raise ValueError("\nPassword length must be at least 4 characters.")

    digits = string.digits
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    special_chars = string.punctuation

    # Generate password characters
    password_chars = []
    password_chars.extend(random.sample(digits, 1))  # Guaranteed 1 digit
    password_chars.extend(random.sample(uppercase, 1))  # Guaranteed 1 uppercase letter
    password_chars.extend(random.sample(lowercase, 1))  # Guaranteed 1 lowercase letter
    password_chars.extend(random.sample(special_chars, 1))  # Guaranteed 1 special character
    password_chars.extend(random.sample(digits + uppercase + lowercase + special_chars, length - 4))  # Fill remaining characters

    # Shuffle the characters for better randomness
    random.shuffle(password_chars)

    # Join the characters into a string
    password = ''.join(password_chars)

    return password


def user_input():
    """Gets password length from the user."""
    # Get password length from user (ensure at least 4)
    while True:
        try:
            os.system("cls")
            desired_length = int(input("Enter desired password length (minimum 4): "))
            if desired_length >= 4:
                break
            else:
                print("\nPassword length must be at least 4 characters. Please try again.")
                time.sleep(1)
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            time.sleep(1)
    # Generate the password using the obtained length
    password = generate_password(desired_length)
    print("\nYour generated password is:", password)


def main():
    while True:
        os.system("cls")
        user_input()  # Call user input only once per loop iteration
        restart()      # Call restart function after user input and password generation


if __name__ == "__main__":
    main()



