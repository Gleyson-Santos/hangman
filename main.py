from stages import stages
from hangman_words import word_list
import random
from art_logo import logo
lives = 6
chosen_word = random.choice(word_list)
blanks = '*'
print(logo)
print('The chosen word is: ', chosen_word)

word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display.append(blanks)

end_of_game = False
while not end_of_game:
    print(stages[lives])
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
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')

    print(f"{' '.join(display)}")
    print(lives)
