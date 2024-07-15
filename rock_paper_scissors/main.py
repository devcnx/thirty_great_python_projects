"""
Rock, Paper, Scissors Game.

This is a game of Rock, Paper, Scissors. The user will be prompted to enter their choice of Rock, Paper, or Scissors.
The computer will randomly select one of the three choices. The winner will be determined based on the following rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock

The module imports the random module to randomly select the computer's choice. It also imports the GAME_OPTIONS
dictionary from the constants module. The GAME_OPTIONS dictionary contains the three choices for the game: Rock, Paper,
and Scissors.
"""
import random
import sys
from constants import GAME_OPTIONS


def display_welcome() -> str:
    """
    Display the welcome message to the user.

    This function displays the welcome message to the user. The welcome message is displayed when the game is started.
    It also provides instructions on how to play the game. It takes no parameters and returns the welcome message as a
    string.

    Returns:
        The welcome message as a string.
        :rtype: str
    """
    return f'''
    Welcome to Rock, Paper, Scissors!

    To play the game, you will be prompted to enter your choice of Rock, Paper, or Scissors.
    The computer will randomly select one of the three choices. The winner will be determined based on the
    following rules:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock

    Good luck!
    '''


def get_user_choice(prompt: str) -> str:
    """
    Get the user's choice for the game.

    This function prompts the user to enter their choice of Rock, Paper, or Scissors. The function takes a prompt as a
    parameter to display to the user. The function will continue to prompt the user until a valid choice is entered. The
    function returns the user's choice as a string.

    Parameters:
        prompt: The prompt to display to the user.
        :type prompt: str

    Returns:
        The user's choice as a string.
        :rtype: str
    """
    while True:
        user_choice = input(prompt).lower()
        if user_choice not in GAME_OPTIONS:
            print(f'{" " * 2}*** Invalid Choice. Please Enter Rock, Paper, or Scissors.\n')
        else:
            return user_choice


def get_computer_choice() -> str:
    """
    Get the computer's choice for the game.

    This function randomly selects the computer's choice of Rock, Paper, or Scissors. The function uses the random
    module to randomly select the computer's choice. The function returns the computer's choice as a string. It
    selects the computer's choice from the GAME_OPTIONS dictionary. The function takes no parameters and returns the
    computer's choice as a string.

    Returns:
        The computer's choice as a string.
        :rtype: str
    """
    return random.choice(list(GAME_OPTIONS.keys())).lower()


def check_moves(user_choice: str, computer_choice: str) -> str:
    """
    Check the moves and determine the winner.

    This function checks the user's choice and the computer's choice to determine the winner of the game. The function
    compares the choices based on the rules of the game: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. If the user and the computer have the same choice, the game is a tie and the function returns 'tie'. If
    the user wins, the function returns 'user'. If the computer wins, the function returns 'computer'. The function
    takes the user's choice and the computer's choice as parameters and returns the winner as a string in lowercase.

    Parameters:
        user_choice: The user's choice for the game.
        :type user_choice: str

        computer_choice: The computer's choice for the game.

    Returns:
        The winner of the game as a string.
        :rtype: str
    """
    if user_choice == computer_choice:
        return 'It\'s a Tie!'
    match = (user_choice, computer_choice)
    if match in ([('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]):
        return 'You Win!'
    return 'Computer Wins!'


def play_again() -> bool:
    """
    Ask the user if they want to play again.

    This function prompts the user to play the game again. The function takes no parameters and returns True if the user
    wants to play again, and False if the user does not want to play again. The function will continue to prompt the
    user until a valid choice is entered. Valid choices are 'y' or 'Y' for Yes, and 'n' or 'N' for No. The function
    returns the user's choice as a boolean.

    Returns:
        True if the user wants to play again, and False if the user does not want to play again.
        :rtype: bool
    """
    while True:
        play_again = input('Would You Like to Play Again? (Y/N): ').lower()
        if play_again not in ['y', 'n']:
            print(f'{" " * 2}*** Invalid Choice. Please Enter Y or N.\n')
        else:
            return play_again == 'y'


if __name__ == '__main__':
    print(display_welcome())
    while True:
        user_choice = get_user_choice('Enter Your Choice (Rock, Paper, Scissors): ')
        computer_choice = get_computer_choice()
        print(f'\n{" " * 2}Your Choice: {user_choice.capitalize()}')
        print(f'{" " * 2}Computer\'s Choice: {computer_choice.capitalize()}')
        print(f'{" " * 2}\n{check_moves(user_choice, computer_choice)}\n')
        if not play_again():
            print('Thanks for Playing!')
            sys.exit()
        print()
