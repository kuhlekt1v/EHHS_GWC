# Computer Guesses the Number

# This lesson is a continuation from 02-user-guess, please
# see introduction exercises and completed 02-user-guess
# with students before continuing on to this tutorial.

# Instead of the computer generating the number and us guessing,
# we will decide on a number and tell the computer if the guess
# is too (h)igh, (l)ow, or if it is (c)orrect.

import random

def computer_guess(x):
  # Initialize variables.
  low = 1
  high = x
  feedback = ''

  # We are deciding c = Correct.
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = high

    feedback = input(f'Is {guess} too high (h), too low (l), or correct (c) ').lower()
    
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
    
  print(f'The computer guessed your number, {guess} correctly!')

# We are deciding the secret number is... 4.
computer_guess(5)
