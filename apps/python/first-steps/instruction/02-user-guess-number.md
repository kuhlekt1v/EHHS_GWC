# User Guesses Number

_This lesson will take us a bit further and dive into importing packages loops, and functions. In this application the computer will generate a random number and the user will have to guess it._
<br>

## Intro to Functions

There are 2 steps to functions.

1. Defining the function
2. Calling the function

```
def example():
  print("Hello world!")

example()
```

We can also define a function that excepts parameters.

```
def new_example(my_string):
  print(my_string)

new_example("Hello world!")
```

<br>

## Intro to Loops

**Question:** Is everyone familiar with loops?... Do you know the 2 primary loops?

1. **For Loops** - used when we have a predefined range. (Ex. a list of numbers)

```
my_list = [1, 2, 3]
for x in my_list:
  print(x)
```

2. **While Loops** - used we don't know the size of what we are looping through. (Ex. While a condition is true continue looping.)

```
x = 0
while x != 3:
  print(x)
  x = x + 1
```

_It can be easy to get stuck in an "inifinite loop" with while loops. If this happens and your loop continues to run press `Ctrl + C`_
<br>

## Final Result

- For this program we need to generate a secret number and to do this we will use the Python 'random' package.
- There are a ton of programs that come built in with Python and many others that can be easily installed to extend Python's functionality.
- The random package has more capabilities than what we will actually use.

```
import random

def guess(x):
  # Generate a random number b/w two integers.
  random_number = random.randint(1, x)

  # Initialize variable to avoid infinite loop/
  user_guess = 0

  # Loop until our guess is equal to the random number.
  while user_guess != random_number:
    # int() Here we are casting the guess variable to an integer
    # this is required to match the randint() function. Input()
    # returns a user's input as a string.
    user_guess = int(input(f"Guess a number between 1 and {x}: "))

    if user_guess < random_number:
      print('Too low! Try again')
    elif user_guess > random_number:
      print('Too high! Try again')

  # If the number is neither too low or too high- it's correct
  # adn the game ends.
  print('You guessed it!!')

guess(5)

```
