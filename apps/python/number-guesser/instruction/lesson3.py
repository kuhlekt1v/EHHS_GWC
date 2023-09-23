################################################################
# - Girls Who Code					                           #
# - Tkinter GUI Number Guesser				                   #
# - Lesson - 3 | Apply style to the gui. 	                   #
################################################################

import tkinter as tk
import random

# Create a new window
window = tk.Tk()
 
# Set the dimensions of the created window
window.geometry("600x400")
 
# Set the background color of the window
window.config(bg="#065569")
 
window.resizable(width=False,height=False)
 
# Set Window Title
window.title('Number Guessing Game')


# The code for the buttons and text and other 
# interactive UI elements go here 

# Exit button
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
# Place the exit button at a suitable place
exit_button.place(x=300,y=275)

# Heading of our game
title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
 
# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
 
# Display labels
title.place(x=140, y=50)
result.place(x=135, y=210)

# The play button
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a")
# The guess button
# This button initially disabled because we don't want the user to guess a number before the game has started
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black")
 
# Place the buttons in the window
guess_button.place(x=340, y=147) 
play_button.place(x=130, y=275)


# The object that stores the value in the entry field
guessed_number = tk.StringVar()
 
# Create entry field and attach it the guessed_number object that stores the value
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
 
# Place it in the window
number_form.place(x=130, y=150)

# Start the window
window.mainloop()