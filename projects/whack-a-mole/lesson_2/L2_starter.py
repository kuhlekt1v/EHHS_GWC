import sys
import tty
import termios
from datetime import timedelta, datetime
from Game import board, mole, empty, render, map, get_input

PLAY_TIME = 30

# 1. Import the 'random' module


def Play():
  # Clear game instructions from console.
  print("\033c")

  # Hide Cursor
  sys.stdout.write("\033[?25l")

  # 2. Display the title of the game and an empty game board. 

  start = datetime.now()
  score = 0

  # Randomly generate a mole location between 1 & 9.
  # 3. Define mole_location variable.

  
  # Continue game for the number of seconds specified by
  # play_time variable.
  while datetime.now() - start < timedelta(seconds=PLAY_TIME):
    left, top = map(mole_location)
    render(mole, left, top)

    # 4. Use the custom get_input function to capture user input invisibly.

    
    # 5. Check if mole_location is equal to user selection.
    #    A. Add 1 to the current score
    #    B. Set new_mole_location equal to random number between 1 & 9

      render(empty, left, top)
      
      mole_location = (
          new_mole_location + 1
          if new_mole_location >= mole_location and new_mole_location + 1 <= 9
          else new_mole_location
      )

  # Clear console.
  print("\033c")
    
  #6. Display the game title, an empty board, and the user's final score. 


#### START -  Code from Challenge 1 do not alter.
while True:
  print("Whack-A-Mole")
  print()
  print(
      f"You have {PLAY_TIME} seconds to whack as many moles as you can before "
      + "the timer runs out. Use the number keys 1-9 to whack. Are you ready?"
  )
  print()
  print("Press [y] to play, or [n] to quit.")

  key = input()

  # Quit if user enters an n/N, start game if user enters y/Y.
  # Continue asking if any other key is entered.
  if key == "n" or key == "N":
      print("\033c")
      print("Whack A Mole was closed...")
      sys.exit(0)
  elif key == "y" or key == "Y":
      break
#### END -  Code from Challenge 1 do not alter.

# 7. Call the play function to begin the game.
