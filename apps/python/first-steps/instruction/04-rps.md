# (R)ock, (P)aper, (S)cissors

## Determine What a Win Is

**Here we will create a function that decide what is considered a win. In RPS we know...**

- Rock beats scissors (r > s)
- Scissors beats paper (p > s)
- Paper beats rock (p > r)

### User Has Won Function

```
def user_has_won(player, oponent):
  if (
    (player == "r" and opponent == "s") or
    (player == "p" and opponent == "r") or
    (player == "s" and opponent == "p")
  ):
    return true
```

Here we have used both OR & AND conditions.

- AND - Returns true of BOTH conditions are true, otherwise false.
- OR - Returns true if either condtion is true, otherwise false.
  <br>

### Define Play Function

```
def play():
  user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors ").lower()

  # In the last tutorials we used the random module to generate random numbers,
  # but random also has a function called "choice" that excepts an array as a parameter.
  # We can use this to allow the computer to randomly select rock, paper, scissors.
  computer_choice = random.choice(['r', 'p', 's'])

  print(f"User Chose: {user_choice} | Computer Chose: {computer_choice}")

  # Define the rules of the game (i.e. decides who wins based on what was selected)
  if user_choice == computer_choice:
    return "It's a tie."

  if user_has_won(user_choice, computer_choice):
    return "You won!"

  # You will notice that there is no if/else statement here.
  # As all of the previous conditions return (and exit the program),
  # this line will only ever be reached if the other conditions are not true/
  return "You lost!"

# Don't forget to wrap the play function in print. Otherwise you won't see
# the results!
print(play())
```
