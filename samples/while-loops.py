# Introduction to While Loops

# Example 1: Simple while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Example 2: While loop with user input
user_input = input("Enter a number: ")
number = int(user_input)

while number > 0:
    print(f"Current number: {number}")
    number -= 1

# Example 3: While loop with condition and user interaction
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
    else:
        print("Try again!")

print("End of the game. Thanks for playing!")
