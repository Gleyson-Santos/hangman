import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# todo-4 - create blanks representing the randon word

chosen_word = random.choice(word_list)
blanks = []
lifes = 5
is_on = True
print(chosen_word)
for _ in chosen_word:
    blanks += '*'

while is_on:
    guess = input('Guess a letter: ')
    print(lifes)

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            blanks[letter] = guess

        if '*' not in blanks:
            is_on = False

    print(blanks)