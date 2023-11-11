# Lesson 2 mini lesson on Python's 'random' module.

# The Python programming language provides many modules that can be
# be used to extend it's functionality. You may have noticed these
# at the top of the file (import <package-name>).
# - Modules provide built in functions that we can use in our programs.

import random

# The random module allows us to generate random numbers using a
# a built in function called randint (random integer)1

dice_role = random.randint(1, 6)
print(f"Dice roll: {dice_role}")
