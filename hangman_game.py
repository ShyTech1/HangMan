from game_logic import *
from hangman_ascii_art import *


def main():
    num_of_tries = 0
    secret_word = choose_word()
    old_letters_guessed = []
    clean_sceen(num_of_tries, secret_word, old_letters_guessed)

    #get an input from the user
    while True:
        letter_guessed = input("guess a letter")
    #check valid input
        if try_update_letter_guessed(letter_guessed, old_letters_guessed) ==True:
            update_hidden_word(secret_word, old_letters_guessed)
    #update old letters guessed
    #update secret word
    #check win


if __name__ == "__main__":
    main()