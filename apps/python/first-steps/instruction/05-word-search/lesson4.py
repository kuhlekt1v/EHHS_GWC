################################################################
# - Girls Who Code					                           #
# - Word Search Tutorial					                   #
# - Lesson - 4 | Limit number of guesses        		       #
################################################################

import random
import string
import requests

response = requests.get("https://www.randomlists.com/data/words.json").json()
words = response['data']

# Get valid words from a list of words.
def get_valid_word(input_list):
    # Random.choice takes in a list randomly selects an item from that list
    word = random.choice(input_list)

    # The wordlist contains multi-part words by using dashes,
    # to avoid this we will continue to call random.choice until we get a word without dash/space.
    while '-' in word or ' ' in word:
        word = random.choice(input_list)

    # Uppercase the returned word
    return word.upper()


def guess_word():
    word = get_valid_word(words)
    # Set function turns a string into a set.
    word_letters = set(word)

    # Creates a set of all of the letters in an english dictionary.
    # In Python a set is basically a way to store multiple items in a single variable.
    alphabet = set(string.ascii_uppercase)

    # Empty set to keep track of the letters a user has already guessed.
    used_letters = set()

    # Capture user guess.
    user_input = input("Guess a letter: ").upper()

    # If the guess is in the alphabet (excluding letters already guessed)
    if user_input in alphabet - used_letters:
        # Add the guess to the used_letters set.
        used_letters.add(user_input)
    # If the guess is in the set of letters in the word
    if user_input in word_letters:
        # Remove the letter from the set of letters in the word
        word_letters.remove(user_input)
    elif user_input in used_letters:
        print("Guess again. Letter already guessed!")
    else:
        print('Invalid character entered.')

    
    attempts = 6
    while len(word_letters) > 0 and attempts > 0:
        # Let the users know what they have already guessed.
        # Join will join the letters in a list with the separate we define - space here.
        print(f"{attempts} trys left.")
        print('Letters used: ', ' '.join(used_letters))

        # Print the current word
        # So we are saying, print the letter if it is in used letters otherwise print a dash
        # for a letter that has not been guessed yet.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters:
            # Add the guess to the used_letters set.
            used_letters.add(user_input)
            # If the guess is in the set of letters in the word
            if user_input in word_letters:
            # Remove the letter from the set of letters in the word
                word_letters.remove(user_input)
            else:
                attempts = attempts - 1
                print('Letter is not in word')
        elif user_input in used_letters:
            print("Guess again. Letter already guessed!")
        else:
            print('Invalid character entered.')

    if attempts == 0:
        print("Game over. The word was ", word)
    else:
        print("You guessed the word ", word, '!!')
guess_word()