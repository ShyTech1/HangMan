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

    first = """
    x-------x
    |
    |
    |
    |
    |"""

    second = """
    x-------x
    |       |
    |
    |
    |
    |"""

    third = """
    x-------x
    |       |
    |       0
    |
    |
    |"""
    fourth = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""

    fith = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""

    sixth = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""

    sevens = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

    HANGMAN_PHOTOS = {0: first, 1: second, 2: third,
                      3: fourth, 4: fith, 5: sixth, 6: sevens}
    return f'this is your man:\n {HANGMAN_PHOTOS[num_of_tries]}\n'


def win_art():
    return
"""" __   __  _______  __   __             _     _  _______  __    _    __
|  | |  ||       ||  | |  |           | | _ | ||       ||  |  | |  |  |
|  |_|  ||   _   ||  | |  |   ____    | || || ||   _   ||   |_| |  |  |
|       ||  | |  ||  |_|  |  |____|   |       ||  | |  ||       |  |  |
|_     _||  |_|  ||       |           |       ||  |_|  ||  _    |  |__|
  |   |  |       ||       |           |   _   ||       || | |   |   __
  |___|  |_______||_______|           |__| |__||_______||_|  |__|  |__| """