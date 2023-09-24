################################################################
# - Girls Who Code                                             #
# - Tkinter GUI Number Guesser                                 #
# - Lesson - 2 | Create the TKinter GUI                        #
################################################################

import tkinter as tk
import random

# Create a new window
window = tk.Tk()
 
# Set the dimensions of the created window
window.geometry("600x400")
 
# Disable window resize.
window.resizable(width=False,height=False)
 
# Set Window Title
window.title('Number Guessing Game')

# Exit button
exit_button = tk.Button(window,text="Exit Game", command=exit)
# Place the exit button at a suitable place
exit_button.place(x=300,y=275)

# Heading of our game
title = tk.Label(window,text="Guessing Game",)
 
# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game")
 
# Display labels
title.place(x=140, y=50)
result.place(x=135, y=210)

# The play button
play_button = tk.Button(window, text="Play Game")
# The guess button
# This button initially disabled because we don't want the user to guess a number before the game has started
guess_button = tk.Button(window,text="Guess", state="disabled")
 
# Place the buttons in the window
guess_button.place(x=340, y=147) 
play_button.place(x=130, y=275)

# The object that stores the value in the entry field
guessed_number = tk.StringVar()
 
# Create entry field and attach it the guessed_number object that stores the value
number_form = tk.Entry(window, textvariable=guessed_number)
 
# Place it in the window
number_form.place(x=130, y=150)

# Start the window
window.mainloop()
