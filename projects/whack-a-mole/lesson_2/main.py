import sys
import random

# import msvcrt
import getch
from getpass import getpass
from datetime import timedelta, datetime
from Game import board, mole, empty, render, map

PLAY_TIME = 10


def get_input():
    while True:
        # key = msvcrt.getch()
        key = getch.getch()

        if key.isdigit() and 1 <= int(key) <= 9:
            return int(key)
        elif key == "\x1b":  # esc key
            print("\033c")
            print("Whack A Mole was closed...")
            sys.exit(0)


def Play():
    # Clear game instructions from console.
    print("\033c")

    # Hide Cursor
    sys.stdout.write("\033[?25l")

    # Display title & empty board.
    print("Whack A Mole")
    print()
    print(board)

    start = datetime.now()
    score = 0

    # Randomly generate a mole location between 1 & 9.
    mole_location = random.randint(1, 9)

    # Continue game for the number of seconds specified by
    # play_time variable.
    while datetime.now() - start < timedelta(seconds=PLAY_TIME):
        left, top = map(mole_location)
        render(mole, left, top)

        # guess = msvcrt.getch()
        selection = get_input()

        if mole_location == selection:
            score += 1
            new_mole_location = random.randint(1, 9)
            render(empty, left, top)

            mole_location = (
                new_mole_location + 1
                if new_mole_location >= mole_location and new_mole_location + 1 <= 9
                else new_mole_location
            )

    # Clear console.
    print("\033c")
    print("Whack-A-Mole\n")
    print(board)
    print(f"\nGame Over. Score: {score}")


while True:
    # Print instructions for users.
    print("Whack A Mole")
    print()
    print(
        f"You have {PLAY_TIME} seconds to whack as many moles as you can before "
        + "the timer runs out. Use the number keys 1-9 to whack. Are you ready?"
    )
    print()
    print("Press [y] to play, or [n] to quit.")

    # Store user input to variable.
    key = input()

    # Quit if user enters an n/N, start game if user enters y/Y.
    # Continue asking if any other key is entered.
    if key == "n" or key == "N":
        print("\033c")
        print("Whack A Mole was closed...")
        sys.exit(0)
    elif key == "y" or key == "Y":
        break

Play()
