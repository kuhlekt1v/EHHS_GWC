################################################################
# - Girls Who Code                                             #
# - Snake Game Tutorial                                        #
# - Lesson - 6 | Game over, complete next turn, change         #
#		         direction. Game complete!                     #
################################################################

### Display game over message to students first.
### Change direction/binding and play.
### Check head of snake is food/delete pieces.

def next_turn(snake, food):

################# REDACTED FOR PRINT #################
    snake.squares.insert(0, square)
    
################# NEW CODE 1/3  #################
    
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

################# NEW CODE 2/3  #################
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
############### END NEW CODE 2/3  ###############

# Initialize TKinter window.

################# REDACTED FOR PRINT #################

window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT, x_coordinate, y_coordinate))

################# NEW CODE 3/3 #################
# Bind user arrow entry to function.
window.bind('<Left>',
            lambda event: change_direction('left'))
window.bind('<Right>',
            lambda event: change_direction('right'))
window.bind('<Up>',
            lambda event: change_direction('up'))
window.bind('<Down>',
            lambda event: change_direction('down'))
############### END NEW CODE 3/3  ###############
food = Food()


################# REDACTED FOR PRINT #################

window.mainloop()


