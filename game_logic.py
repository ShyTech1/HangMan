import os
from wonderwords import RandomWord
import hangman_ascii_art as ac

print(ac.hangman_start_screen())


def choose_word():
    """return a random word as a string"""
    return RandomWord().word()


def check_valid_input(letter_guessed, old_letters_guessed) -> bool:
    """chack input.
    return : bool
    valid input:  one english letter only."""

    valid_input = (
        (len(letter_guessed)) == 1  # letter_guessed is 1 chr length
        and letter_guessed.isalpha()  # letter_guessed is an alphabeit chr
        and letter_guessed not in old_letters_guessed
    )
    invalid_input = (
        (len(letter_guessed)) > 1  # letter_guessed is bigger than 1
        or not letter_guessed.isalpha()  # letter_guessed is not an alphabeit chr
        or letter_guessed in old_letters_guessed
    )

    if valid_input:
        return True
    elif invalid_input:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """if valid input, add to old_letter_guessed, return True
    if it's not valid input, return str('X')  the list old_letter_guessed, and False."""

    letter_guessed = letter_guessed.lower()

    if not check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.sort()
        return False

    else:
        old_letters_guessed.append(letter_guessed)
        return True


def is_letter_in_secret_word(letter_guessed, secret_word) -> bool:
    """ check if the guessed letter in the secret word
    return: bool"""

    if secret_word.count(letter_guessed) >= 1:
        return True
    return False


def update_hidden_word(secret_word, old_letters_guessed) -> str:
    """represent to the user his progress in the game.
    secret_word - the word should be guessed
    old_letters_guessed - list of guessed letters
    return a string with the letter's guessed separated by underscore
    return_type: str"""

    return ' '.join([x if x in old_letters_guessed else '_' for x in secret_word])


def check_win(secret_word, old_letters_guessed):
    """check if the user guessed the word
    return: bool
    """

    show_list = update_hidden_word(
        secret_word, old_letters_guessed).replace(" ", "")
    if show_list == secret_word:

        return True
    else:
        return False


def clean_screen(num_of_tries, secret_word, old_letters_guessed):
    print(secret_word)
    os.system('cls||clear')
    ac.hangman_start_screen()
    print(ac.hangman_start_screen())
    print(ac.hangman_level(num_of_tries))
    print(f'letters guessed> {sorted(old_letters_guessed)}\n')


def win_clean():
    os.system('cls||clear')
    print(ac.hangman_start_screen())
    print(ac.win_art())


def game_over_screen():
    print(ac.lose_art())
    again = input("would you like to play again?[Y/N] ")
    return True if again == "Y".lower() else quit()
