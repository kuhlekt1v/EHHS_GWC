################################################################
# - Girls Who Code                                             #
# - Snake Game Tutorial                                        #
# - Lesson - 5 | Begin next turn & check collisions            #
################################################################


########## CLASSES & MAIN GAME REDACTED FOR PRINT PURPOSES   ###########
### ALL CODE BELOW IS NEW - next_turn is NOT complete, see snake-game-5b
### Use print statements and comments below to explain to students what is going on.

# Checks value of direction variable - depending on value increments/decrements
#   x & y to move in the correct direction
def next_turn(snake, food):
    # Gets x,y coordinate of head of snake (first element in coordinate list)
    x, y = snake.coordinates[0]
    # First print initial location
    #print("x {}".format(x))
    #print("y {}".format(y))

    # (x,y) home is at bottom left corner
    #print("before: {}".format(snake.coordinates))

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert coordinates at beginning of list.
    snake.coordinates.insert(0, (x, y))
    # Create new square at x,y location.
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)
    #print("after: {}".format(snake.coordinates))

    # Check for collisions and game over

    if check_collisions(snake):
        # Will only be called if check collisions returns True.
        game_over()


    # After is a method built into Tkinter
    # after(delay_ms, callback=None, *args)
    # After delay, call this function with, these arguments - forever unless told to stop.
    window.after(SPEED, next_turn, snake, food)

# Check for snake colliding with game board boundary OR snake object
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







