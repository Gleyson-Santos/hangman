import random

# Step 1
# Step 2
# Checking if the player has won

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display.append('*')
print(display)

player_has_won = False
while not player_has_won:
    guess = input('Guess a letter: ').lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if '*' not in display:
        player_has_won = True

    print(display)
