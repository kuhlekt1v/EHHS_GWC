################################################################
# - Girls Who Code					                           #
# - Snake Game Tutorial					                       #
# - Lesson - 3 | Adding the Food class        		           #
# - NOTE: IF NECESSARY TEACH OOP FIRST FROM                    # 
#         samples/OOP_intro.py                                 #
################################################################

from Tkinter import *
import random

# GAME CONSTANT VARIABLES
GAME_WIDTH = 700              # Game board width.
GAME_HEIGHT = 700             # Game board height.
SPEED = 50                    # How fast snake moves, lower = faster.
SPACE_SIZE = 50               # How large are items (food/snake body parts).
BODY_PARTS = 3                # How many body parts snake has at beginning of game.
SNAKE_COLOR = "#22FFBE"       # Body color of snake.
FOOD_COLOR = "#FF0000"        # Color of food.
BACKGROUND_COLOR = "#000000"  # Game background color


################# THIS IS THE NEW CODE (1/2) #################

# Classes
class Food():
    # Initializing class variables
    def __init__(self):
        # Random number b/w 0 & 14, excluding 14
        # 14 = 700 (game_width or height) / 50 (space_size)
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        # create_oval (x,y (start), x,y (end))
        # Fill sets the color of the object
        # Tag lets us easily select/delete food later.
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

#################     END NEW CODE (2/2)     #################

# Initialize TKinter window.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)


######### MAIN SECTION REDACTED FOR PRINT PURPOSES   #########



################# THIS IS THE NEW CODE (2/2) #################

food = Food()

#################     END NEW CODE (2/2)     #################


window.mainloop()


