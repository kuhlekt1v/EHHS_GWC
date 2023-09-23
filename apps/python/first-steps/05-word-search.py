# Word Search 					                   

import random
import string
import requests

response = requests.get("https://www.randomlists.com/data/words.json").json()
words = response['data']

# Return a word from a list of words.
def get_valid_word(input_list):
    word = random.choice(input_list)

    while '-' in word or ' ' in word:
        word = random.choice(input_list)

    return word.upper()

# Capture user input and provide game logic.
def guess_word():
    alphabet = set(string.ascii_uppercase)
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()

    user_input = input("Guess a letter: ").upper()

    if user_input in alphabet - used_letters:
        used_letters.add(user_input)

    if user_input in word_letters:
        word_letters.remove(user_input)

    elif user_input in used_letters:
        print("Guess again. Letter already guessed!")
    else:
        print('Invalid character entered.')

    attempts = 6
    while len(word_letters) > 0 and attempts > 0:
        print(f"{attempts} trys left.")
        print('Letters used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            
            if user_input in word_letters:
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