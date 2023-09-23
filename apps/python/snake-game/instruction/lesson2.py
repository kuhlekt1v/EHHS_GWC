################################################################
# - Girls Who Code					                           #    
# - Snake Game Tutorial					                       #
# - Lesson - 2 | Displaying the game board.		               #
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

# Initialize TKinter window.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

################# THIS IS THE NEW CODE #################

score = 0
direction = 'down'

# User score display - Save and run for students to see
label = Label(window, text="Score:{}".format(score),font=('consolas', 40))
label.pack()


# Display the game board - Save and run for students to see
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


# Center window on screen when it opens
# This will NOT work with multiple monitors.
window.update()     # here we are forcing the window to render or display.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Horizontal position of window.
# Must be full integers, so we cast them to integer.
x_coordinate = int((screen_width/2) - (GAME_WIDTH/2))
y_coordinate = int((screen_height/2) - (GAME_HEIGHT/2))

# window_width * window_height + x + y
window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT, x_coordinate, y_coordinate))


#################     END NEW CODE     #################
window.mainloop()


