#################################
#                               #
#        -Whack-A-Mole-         #
# Required functions beyond the #
# scope of student instruction. #
#                               #
#################################

import sys


# Mole to displayed randomly in a hole.
mole = "  ___ \n" + " |o-o|\n" + "|\\---/|\n" + "|  J  |\n"

# Empty game board.
board = (
    " +---+---------+ +---+---------+ +---+---------+ \n"
    + " | 9 |         | | 8 |         | | 7 |         | \n"
    + " +---+         | +---+         | +---+         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     +---------+     +---------+     +---------+ \n"
    + " +---+---------+ +---+---------+ +---+---------+ \n"
    + " | 6 |         | | 5 |         | | 4 |         | \n"
    + " +---+         | +---+         | +---+         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     +---------+     +---------+     +---------+ \n"
    + " +---+---------+ +---+---------+ +---+---------+ \n"
    + " | 3 |         | | 2 |         | | 1 |         | \n"
    + " +---+         | +---+         | +---+         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     |         |     |         |     |         | \n"
    + "     +---------+     +---------+     +---------+ \n"
)

# Empty holes.
empty = (
    "       \n" + "       \n" + "       \n" + "       \n"
)  # Adjust the number of spaces to match the mole

"""Map function used to get the screen coordinates (left, top)
for displaying the mole on the console based on the randomly
generated mole_location. For example, if mole_location = 5
the coordinates returned for displaying the mole will be (20, 9)."""


def map(hole: int) -> tuple:
    return {
        1: (40, 19),
        2: (24, 19),
        3: (8, 19),
        4: (40, 12),
        5: (24, 12),
        6: (8, 12),
        7: (40, 5),
        8: (24, 5),
        9: (8, 5),
    }[hole]


"""Render function responsible for displaying the mole on the screen.
It interates through each line in a given string. If it encounters
the new-line character (\n) it moves to the next line, otherwise it
prints the character."""


def render(string: str, left: int, top: int) -> None:
    x = left
    y = top
    output = ""
    for line in string.split("\n"):
        output += f"\033[{y};{x}H{line}\n"
        y += 1
    sys.stdout.write(output)
    sys.stdout.flush()
