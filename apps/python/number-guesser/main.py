# TKinter Number Guesser GUI


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

################ GAME LOGIC ################
TARGET = random.randint(1, 10)
RETRIES = 0

# Function to update the text displayed to user.
def update_result(text):
  result.configure(text=text)

# Function to start a new game.
# Don't forget to add command=new_game to play_button.
def new_game():
  # Enable guess button & reset all variables
  guess_button.config(state='normal')
  global TARGET, RETRIES
  TARGET = random.randint(0, 10)
  RETRIES = 0
  update_result(text="Guess a number between\n 1 and 10")

# Function that implements console-game logic into ui.
# Don't forget to add command=guess to guess_button.
def guess():
  # Explain global variables to students
  global RETRIES
  choice = int(number_form.get())
  if choice != TARGET:
      RETRIES += 1
   
      result = "Wrong Guess!! Try Again"
      if TARGET < choice:
          hint = f"The required number lies between 0 and {choice}"
      else:
          hint = f"The required number lies between {choice} and 10"
      result += "\n\nHINT :\n" + hint
   
  else:
      result = f"You guessed the correct number after {RETRIES} tries"
      guess_button.configure(state='disabled')
      result += "\n" + "Click on Play to start a new game"
   
  update_result(result)
  
  
################ UI STYLING ################

# Exit button
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
# Place the exit button at a suitable place
exit_button.place(x=300,y=350)

# Heading of our game
title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
 
# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
 
# Display labels
title.place(x=140, y=50)
result.place(x=135, y=210)

# The play button
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
# The guess button
# This button initially disabled because we don't want the user to guess a number before the game has started
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=guess)
 
# Place the buttons in the window
guess_button.place(x=340, y=147) 
play_button.place(x=130, y=350)


# The object that stores the value in the entry field
guessed_number = tk.StringVar()
 
# Create entry field and attach it the guessed_number object that stores the value
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
 
# Place it in the window
number_form.place(x=130, y=150)

# Start the window
window.mainloop()