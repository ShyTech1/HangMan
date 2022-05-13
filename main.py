from game_logic import *
import os
from hangman_ascii_art import *


def main():
    num_of_tries = 0
    secret_word = choose_word()
    old_letters_guessed = []
    user_progress = ''
    clean_screen(num_of_tries, secret_word, old_letters_guessed)
    game_over = False

    while num_of_tries <= 6:
        # get an input from the user
        while True:
            letter_guessed = input("guess a letter: ")
            if letter_guessed == "hint":
                print(secret_word)
                input()
            clean_screen(num_of_tries, secret_word, old_letters_guessed)
        # check valid input
            if try_update_letter_guessed(letter_guessed, old_letters_guessed) == True:
                user_progress = update_hidden_word(
                    secret_word, old_letters_guessed)
                break
            else:
                print(user_progress)

        if not is_letter_in_secret_word(letter_guessed, secret_word):
            num_of_tries += 1
        clean_screen(num_of_tries, secret_word, old_letters_guessed)

        print(user_progress)
        if check_win(secret_word, old_letters_guessed):
            game_over = True
            win_clean(num_of_tries)
            break
    game_over = True
    if game_over:
        if game_over_screen():
            if __name__ == "__main__":
                main()

        # update old letters guessed
        # update secret word
        # check win


if __name__ == "__main__":
    main()
