import random

# Step 1
# Step 2

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in chosen_word:
    display.append('*')
print(display)

guess = input('Guess a letter: ').lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
