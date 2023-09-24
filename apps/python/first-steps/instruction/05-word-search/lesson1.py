################################################################
# - Girls Who Code                                             #
# - Word Search Tutorial                                       #
# - Lesson - 1 | Use an API to generate a random word          #
################################################################

# There are two options for getting the list of random words
# depending on interest/experience level of students.

# 1. Navigate to https://www.randomlists.com/data/words.json
#    and copy list of words to an array called words.
words = ["aback", "abaft", "abandoned", "abashed"]

# 2. Use Python's request package to perform a get request.
import requests
response = requests.get("https://www.randomlists.com/data/words.json").json()
words = response['data']

print(words)
