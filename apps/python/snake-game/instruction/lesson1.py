################################################################
# - Girls Who Code                                             #
# - Snake Game Tutorial                                        #
# - Lesson - 1 | Initial setup                                 #
################################################################

from Tkinter import *
import random

# CONSTANTS - These can be thought of as settings.
# In Python there are no such things as constants - In other languages
# there are, so we are just using these variables to be our constant
# settings

GAME_WIDTH = 700              # Game board width.
GAME_HEIGHT = 700             # Game board height.
SPEED = 50                    # How fast snake moves, lower = faster.
SPACE_SIZE = 50               # How large are items (food/snake body parts).
BODY_PARTS = 3                # How many body parts snake has at beginning of game.
SNAKE_COLOR = "#22FFBE"       # Body color of snake.
FOOD_COLOR = "#FF0000"        # Color of food.
BACKGROUND_COLOR = "#000000"  # Game background color

# Initialize TKinter window.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Code will go in here

window.mainloop()

