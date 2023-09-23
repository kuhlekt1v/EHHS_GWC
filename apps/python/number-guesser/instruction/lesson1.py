################################################################
# - Girls Who Code					                           #
# - Tkinter GUI Number Guesser				                   #
# - Lesson - 1 | Develop game logic in a console app		   #
################################################################


# Import the random module.
import random

# Computer chooses a number between 1 and 5.
target = random.randint(1, 10)

retries = 0
while(True):
    # Taking user choice and cast string input as integer
    choice = int(input("Enter a number between 1 and 10: "))
    retries += 1
 
    # Wrong guess
    if target != choice:
        print("Wrong Guess!! Try Again")
        # Hint
        if target < choice:
            print(f"The number lies between 0 and {choice}")
        else:
            print(f"The number lies between {choice} and 10")

        previous_choice = choice
    # Correct choice
    else:
        print(f"You guessed the correct number after {retries} tries.")
        # User guessed the correct value
        # So let's end the infinite loop
        break;