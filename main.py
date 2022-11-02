import random

# Step 1
# Step 2
# Checking if the player has won
# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
blanks = '*'
print(chosen_word)

word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display.append(blanks)
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if blanks not in display:
        end_of_game = True
        print(''.join(display))
        print('You win!')

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')

    # If lives goes down to 0 then the game should stop and it should print "You lose."
    print(f"{' '.join(display)}")
    print(lives)
