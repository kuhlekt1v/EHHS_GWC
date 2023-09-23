# (R)ock, (P)aper, (S)cissors

import random

def user_has_won(player, opponent):
  # Return true if the player wins.
  if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and player == "r"):
    return True


def play():
  user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors ").lower()

  # Check that users enters a valid choice.
  if (user_choice not in ['r', 'p', 's']):
    print('Invalid choice. Try again.')
    print(play())

  # In the last tutorials we used the random module to generate random numbers,
  # but random also has a function called "choice" that excepts an array as a parameter.
  # We can use this to allow the computer to randomly select rock, paper, scissors.
  computer_choice = random.choice(['r', 'p', 's'])

  print(f"User Chose: {user_choice} | Computer Chose: {computer_choice}")
 
  # Define the rules of the game based on original selections.
  if user_choice == computer_choice:
    return "It's a tie."

  if user_has_won(user_choice, computer_choice):
    return "You won!"

  return "You lost!"

print(play())