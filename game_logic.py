import os
from wonderwords import RandomWord
import hangman_ascii_art as ac

print(ac.hangman_start_screen())


def choose_word():
    """return a random word as a string"""
    return RandomWord().word()


def check_valid_input(letter_guessed, old_letters_guessed):
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
    )

    if valid_input:
        return True
    elif invalid_input:
        return False
    if letter_guessed in old_letters_guessed:
        print(f'{letter_guessed} is already guessed')# todo check if this line is necessary.
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """if valid input, add to old_letter_guessed, return True
    if it's not valid input, return str('X')  the list old_letter_guessed, and False."""

    letter_guessed = letter_guessed.lower()

    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        old_letters_guessed.sort()
        print('[ THIS IS NOT A VALID INPUT ]', old_letters_guessed.sort())
        return False

    elif check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        print('[ THIS IS A VALID INPUT ]')
        return True


def is_letter_in_secret_word(letter_guessed, secret_word):
    """ check if the guessed letter in the secret word
    return: bool"""

    if secret_word.count(letter_guessed) >= 1:
        return True
    return False


def update_hidden_word(secret_word, old_letters_guessed):
    """represent to the user his progress in the game.
    secret_word - the word should be guessed
    old_letters_guessed - list of guessed letters
    return a string with the letter's guessed separated by underscore
    return_type: str"""

    return ''.join([x if x in old_letters_guessed else '_' for x in secret_word])


def check_win(secret_word, old_letters_guessed):
    """check if the user guessed the word
    return: bool
    """
    show_list = update_hidden_word(secret_word, old_letters_guessed)

    if show_list == secret_word:
        return True
    else:
        return False


def clean_sceen(num_of_tries, secret_word, old_letters_guessed):

    os.system('cls||clear')
    ac.hangman_start_screen()
    print(ac.hangman_level(num_of_tries))
    print(update_hidden_word(secret_word, old_letters_guessed))
    print(f'letters guessed: {sorted(old_letters_guessed)}\n')


def win_clean(num_of_tries):
    os.system('cls||clear')
    ac.hangman_start_screen()
    ac.hangman_level(num_of_tries)
    print(ac.win_art())

