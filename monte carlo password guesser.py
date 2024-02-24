import random
import matplotlib.pyplot as plt
import numpy as np

used_numb = []

def password_graph():
    graph = str(input("Would you like to graph? (yes) or (no) ")).replace(' ', '').lower()
    if graph == "yes":
        plt.hist(used_numb, bins=30, edgecolor='black')  
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of the Previously Correct Passwords')
        plt.show()
        
    elif graph == "no":
        print("Continueing Program")
    else:
        print("please enter valid input (yes) or (no)")

    print()


while True:
    user_input = str(input("Continue? (yes) or (no) ")).replace(' ', '').lower()
    print()
    
    if user_input == "yes":

        # The correct password
        correct_password = random.randint(0, 9)

        # Counter
        amount = 0

        while True:
            guess = int(input(f"Guess the number between 0 and 9: "))
            amount += 1

            if guess == correct_password:
                print("Correct")
                print(f"Goal achieved in {amount} tries.")
                print()
                used_numb.append(correct_password)
                print(used_numb)
                print()
                password_graph()
                break              

            else:
                print("wrong")
                print()
    
    elif user_input == "no":
        print(used_numb)
        print()
        print("Ending Program")
        break

    else:
        print("Invalid input. Please enter (yes) or (no)")