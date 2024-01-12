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

# create a set to track guessed letters
def join_guessed_letters(guessed_letters):
    # sorted with alphabetize the guessed letters to be returned
    return " ".join(sorted(guessed_letters))

# display the word to show the player
def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    # build current_letters list with for loop
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

# draw the hang man with raw strings
# hangman.py
# ...

def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])


# need a variable to check for max incorrect guesses allowed
MAX_GUESSES = 6 

# game over function to check for max guesses reached or word was guessed correctly
def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_GUESSES:
        return True
    # sets are unique so using the <= compartor checks every item left hand set is a member of the right hand set, if all are the same, the word has been guessed
    if set(target_word) <= guessed_letters:
        return True
    return False

#!! START GAME AREA
if __name__ == "__main__":
    # grab word from word list
    target_word = select_word()
    # create a new set of guessed letters for player
    guessed_letters = set() 
    guessed_word = build_guessed_word(target_word, guessed_letters)
    # set wrong guesses to 0 for game over function
    wrong_guesses = 0
    print("Welcome to CLI Hangman, Good Luck!")

    #!! Main Game Loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"YOur word is: {guessed_word}")
        print(
            "Current Guessed Letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Nice Guess!")
        else:
            print("Uh Oh, that one isn't there.")
            wrong_guesses += 1
        
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

        