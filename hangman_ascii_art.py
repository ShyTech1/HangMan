def hangman_start_screen():
    HANGMAN_ASCII_ART = ("""
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| by shai kelman
                        __/ /                      
                       |___/""")

    return HANGMAN_ASCII_ART


def hangman_level(num_of_tries):

    zero = """
    x-------x
    |
    |
    |
    |
    |"""

    first = """
    x-------x
    |       |
    |
    |
    |
    |"""

    second = """
    x-------x
    |       |
    |       O
    |
    |
    |"""
    third = """    x-------x
    |       |
    |       O
    |       |
    |
    |"""

    fourth = """    x-------x
    |       |
    |       O
    |      /|
    |
    |"""

    fith = r"""    x-------x
    |       |
    |       O
    |      /|\
    |      
    |"""

    sixth = r"""    x-------x
    |       |
    |       O
    |      /|\
    |      / 
    |"""

    sevens = r"""    x-------x
     |       |
     |       O
     |      /|\
     |      /|\
     |"""

    HANGMAN_PHOTOS = {0: zero, 1: first, 2: second, 3: third,
                      4: fourth, 5: fith, 6: sixth, 7: sevens}
    return f'this is your man:\n {HANGMAN_PHOTOS[num_of_tries]}\n'


def win_art():
    return """ __   __  _______  __   __             _     _  _______  __    _    __
|  | |  ||       ||  | |  |           | | _ | ||       ||  |  | |  |  |
|  |_|  ||   _   ||  | |  |   ____    | || || ||   _   ||   |_| |  |  |
|       ||  | |  ||  |_|  |  |____|   |       ||  | |  ||       |  |  |
|_     _||  |_|  ||       |           |       ||  |_|  ||  _    |  |__|
  |   |  |       ||       |           |   _   ||       || | |   |   __
  |___|  |_______||_______|           |__| |__||_______||_|  |__|  |__| """