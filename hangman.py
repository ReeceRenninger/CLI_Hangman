from random import choice
import string

# create a select word function to grab a word from our words.txt file
def select_word():
    # creating a words variable to have readlines() iterate over
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

# grab player input function
def get_player_input(guessed_letters):
    while True:
        #normalize player input with .lower()
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input
        
# validator function to ensure player is inputting correct guess types
def _validate_input(player_input, guessed_letters):
    return (
        # checking if input by player has length of 1
        len(player_input) == 1
        # making sure input is lowercase and between a to z
        and player_input in string.ascii_lowercase
        # making sure guess is NOT a repeat letter
        and player_input not in guessed_letters
    )