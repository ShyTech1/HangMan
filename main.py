from game_logic import *
from hangman_ascii_art import *


def main():
    num_of_tries = 0
    secret_word = choose_word()
    old_letters_guessed = []
    user_progress = ''
    clean_sceen(num_of_tries, secret_word, old_letters_guessed)

    while True:
        #get an input from the user
        while True:
            letter_guessed = input("guess a letter")
            clean_sceen(num_of_tries, secret_word, old_letters_guessed)
        #check valid input
            if try_update_letter_guessed(letter_guessed, old_letters_guessed) == True:
                user_progress = update_hidden_word(secret_word, old_letters_guessed)
                break

        print(user_progress)
        if check_win(secret_word, old_letters_guessed):
            win_clean(num_of_tries)
            break


        #update old letters guessed
        #update secret word
        #check win


if __name__ == "__main__":
    main()