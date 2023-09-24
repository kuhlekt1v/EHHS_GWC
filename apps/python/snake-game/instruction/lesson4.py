################################################################
# - Girls Who Code                                             #
# - Snake Game Tutorial                                        #
# - Lesson - 4 | Adding the Snake class                        #
################################################################


from Tkinter import *
import random


# GAME CONSTANT VARIABLES
########## CONSTANTS REDACTED FOR PRINT PURPOSES   ###########

# Classes

# Red food object.
class Food:
######### FOOD CLASS REDACTED FOR PRINT PURPOSES   ###########

################# THIS IS THE NEW CODE (1/2) #################
# Snake object.
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        # Initialize empty lists to hold snake body parts & new squares.
        self.coordinates = []
        self.squares = []

        # For each number of body parts add new starting coordinate.
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
            print(self.coordinates)
            # Save & run for students to see - uncomment after run

        # For each starting location in list of coordinate lists initialize
        # a new square object.
        for x,y in self.coordinates:
            # Create a square (x,y (start), x,y (end))
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
            print(self.squares)
            # Save & run for students to see - uncomment after run

###################     END NEW CODE (1/2)     #################



# Initialize TKinter window.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

######### MAIN SECTION REDACTED FOR PRINT PURPOSES   #########


food = Food()

################# THIS IS THE NEW CODE (2/2) #################
snake = Snake()
#################     END NEW CODE (2/2)     #################


window.mainloop()


