import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input('Guess a letter: ')
for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')

