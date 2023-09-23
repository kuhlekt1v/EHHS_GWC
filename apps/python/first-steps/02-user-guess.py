# User Guesses the Number

import random

def guess(x):
  # Generate a random number b/w two integers.
  random_number = random.randint(1, x)

  # Initialize variable to avoid infinite loop/
  user_guess = 0

  # Loop until our guess is equal to the random number.
  while user_guess != random_number:
    # int() Here we are casting the guess variable to an integer
    # this is required to match the randint() function. Input()
    # returns a user's input as a string.
    user_guess = int(input(f"Guess a number between 1 and {x}: "))

    if user_guess < random_number:
      print('Too low! Try again')
    elif user_guess > random_number:
      print('Too high! Try again')

  # If the number is neither too low or too high- it's correct
  # adn the game ends.
  print('You guessed it!!')

guess(5)