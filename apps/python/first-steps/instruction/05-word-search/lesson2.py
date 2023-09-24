################################################################
# - Girls Who Code                                             #
# - Word Search Tutorial                                       #
# - Lesson - 2 | Get random item from list                     #
################################################################

import random
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

print(get_valid_word(words))
