#Password Strength Test

import string
import time
import os

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

def check_password_strength(password):
  """Checks password strength and provides suggestions for improvement.

  Args:
      password: The password to be evaluated.

  Returns:
      A tuple containing:
          - Strength score (integer): 0 (weakest) to 5 (strongest)
          - List of suggestions (strings) to improve the password
  """

  score = 0
  suggestions = []

  # Length check
  if len(password) >= 12:
    score += 2
  else:
    suggestions.append("Password should be at least 12 characters long.")

  # Character type checks
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_symbol = any(char in string.punctuation for char in password)

  if has_uppercase:
    score += 1
  else:
    suggestions.append("Password should contain at least one uppercase letter.")
  if has_lowercase:
    score += 1
  else:
    suggestions.append("Password should contain at least one lowercase letter.")
  if has_digit:
    score += 1
  else:
    suggestions.append("Password should contain at least one number.")
  if has_symbol:
    score += 1
  else:
    suggestions.append("Password should contain at least one special character (e.g., !@#$%^&*)")

  # Dictionary word check (optional, improve with external library)
  # if password.lower() in wordlist:  # Assuming you have a wordlist loaded
  #   score -= 1
  #   suggestions.append("Password should not be a dictionary word.")

  # Overall strength rating
  strength_rating = "Weak"
  if score == 0:
    strength_rating = "Very Weak"
  elif score == 1 or score == 2:
    strength_rating = "Weak"
  elif score == 3:
    strength_rating = "Medium"
  elif score == 4:
    strength_rating = "Strong"
  else:
    strength_rating = "Very Strong"

  return score, suggestions, strength_rating

def main():
    while True:
        os.system("cls")
        password = input("Enter your password: ")
        score, suggestions, strength_rating = check_password_strength(password)

        print(f"\nYour password strength: {strength_rating}")
    
        if suggestions:
            print("\nSuggestions for improvement:")
            for suggestion in suggestions:
                print("-", suggestion)

        restart()


if __name__ == "__main__":
  main()
