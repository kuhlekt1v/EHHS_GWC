import tkinter as tk
import random

# GAME CONSTANT VARIABLES
GAME_WIDTH = 700              # Game board width.
GAME_HEIGHT = 700             # Game board height.
SPEED = 100                   # How fast snake moves, lower = faster.
SPACE_SIZE = 50               # How large are items (food/snake body parts).
BODY_PARTS = 3                # How many body parts snake has at beginning of game.
SNAKE_COLOR = "#22FFBE"       # Body color of snake.
FOOD_COLOR = "#FF0000"        # Color of food.
BACKGROUND_COLOR = "#000000"  # Game background color

# Red food object.
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

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

        # For each starting location in list of coordinate lists initialize
        # a new square object.
        for x,y in self.coordinates:
            # Create a square (x,y (start), x,y (end))
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Checks value of direction variable - depending on value increments/decrements
#   x & y to move in the correct direction
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE,
              y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check if head of snake is at food.
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Points:{}".format(score))
        canvas.delete("food")
        food = Food()
    # Delete most recent piece added to snake if coordinate is not food.
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
############### END NEW CODE 1/3  ###############

# Check for snake colliding with game board boundary OR snake object.
def check_collisions(snake):
    # Snake head coordinates
    x, y = snake.coordinates[0]
    # Check x < 0 or > GAME_WIDTH
    if x < 0 or x>= GAME_WIDTH:
        return True
    # Check y< 0 or > GAME_HEIGHT
    if y < 0 or y >= GAME_HEIGHT:
        return True

    # For each body part after the head (x,y item in coordinate list)
    # Check if x,y = x,y at head
    for body_part in snake.coordinates[1:]: # USE [1:] to start loop at 2nd position.
        # List of lists.
        if x == body_part [0] and y == body_part[1]:
            return True

    # If no collisions detected return false
    return False

# Display game over message.
def game_over():
    canvas.delete()
    canvas.create_text(canvas.winfo_height()/2,
                       canvas.winfo_width()/2,
                       font=("consolas", 70),
                       text="GAME OVER",
                       fill="red", tag="gameover")

# Change snake direction with user input.
def change_direction(new_direction):
    # Initialize global variable so we can update direction
    # variable within the function
    global direction

    # For each direction we need to make sure that it is not
    # exact opposite of current direction.
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Initialize TKinter window.
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

# User score display.
label = tk.Label(window, text="Score:{}".format(score),font=('consolas', 40))
label.pack()
# Save & run for students to see.

# Display the game board.
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


# Center window on screen.
# This will not work with multiple monitors.
window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Horizontal position of window.
x_coordinate = int((screen_width/2) - (GAME_WIDTH/2))
y_coordinate = int((screen_height/2) - (GAME_HEIGHT/2))

window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT, x_coordinate, y_coordinate))

# Bind user arrow entry to function.
window.bind('<Left>',
            lambda event: change_direction('left'))
window.bind('<Right>',
            lambda event: change_direction('right'))
window.bind('<Up>',
            lambda event: change_direction('up'))
window.bind('<Down>',
            lambda event: change_direction('down'))

food = Food()
snake = Snake()

next_turn(snake, food)

window.mainloop()

