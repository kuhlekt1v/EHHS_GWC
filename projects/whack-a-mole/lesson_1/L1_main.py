# -*- coding: utf-8 -*-
import os
import sys

# Whack-a-mole game board.
board = (
    " ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n"
    + " ║ 7 ║       ║ ║ 8 ║       ║ ║ 9 ║       ║\n"
    + " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ╚═══════╝     ╚═══════╝     ╚═══════╝\n"
    + " ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n"
    + " ║ 4 ║       ║ ║ 5 ║       ║ ║ 6 ║       ║\n"
    + " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ╚═══════╝     ╚═══════╝     ╚═══════╝\n"
    + " ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n"
    + " ║ 1 ║       ║ ║ 2 ║       ║ ║ 3 ║       ║\n"
    + " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ║       ║     ║       ║     ║       ║\n"
    + "     ╚═══════╝     ╚═══════╝     ╚═══════╝"
)

# Mole to displayed randomly in a hole.
mole = " ╔══─┐ \n" + " │o-o│ \n" + "┌└───┘┐\n" + "││ J ││\n"

# Empty holes.
empty = "       " + "       " + "       " + "       "

play_time = 30

while True:
    # Initial game instructions should be provided within this while loop.
    os.system("cls" if os.name == "nt" else "clear")
    print("Whack A Mole")
    print()
    print(
        f"You have {play_time} seconds to whack as many moles as you can before "
        + "the timer runs out. Use the number keys 1-9 to whack. Are you ready?"
    )
    print()
    print("Press [y] to play, or [n] to quit.")

    key = input()

    if key == "n" or key == "N":
        os.system("cls" if os.name == "nt" else "clear")  # Clear console
        print("Whack A Mole was closed...")
        sys.exit(0)
    else:
        pass
