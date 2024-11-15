"""
Hangman Game.

This is an implementation of the Hangman game. The game randomly selects a word from a list of words and asks the player
to guess the word by suggesting letters. The player has a limited number of attempts to guess the word. The game
displays the word with underscores representing the letters that have not been guessed yet. The player wins the game if
they guess all the letters in the word before running out of attempts. The player loses the game if they run out of
attempts before guessing the word. After each guess, the game displays the current state of the word and the letters
guessed so far, along with the number of attempts remaining and the letters that have not been guessed yet. The game
also provides feedback to the player after each guess, indicating whether the guessed letter is correct or incorrect.
Correct guesses reveal the position of the letter in the word, for multiple occurrences of the same letter. Incorrect
guesses reduce the number of attempts remaining. The game ends when the player wins or loses, and the final result is
displayed to the player. The player can choose to play again or exit the game. The module imports the choice function
from the random module to select a random word from the list of words, stored in the WORDS constant.
"""

from random import choice
from constants import WORDS, MAX_ATTEMPTS


def get_word():
    """
    Get a random word from the list of words.

    This function returns a random word from the list of words stored in the WORDS constant. The choice function from
    the random module is used to select a random word from the list. The selected word is returned to the caller.

    Returns:
        A random word from the list of words.
        :rtype: str
    """
    return choice(WORDS)


def get_user_input(prompt: str) -> str:
    """
    Get the user's input.

    This function prompts the user to enter a value and returns the input provided by the user. The prompt parameter is
    displayed to the user to request input. The input provided by the user is returned as a string. This function does
    not perform any validation on the input provided by the user.

    Parameters:
        prompt: The message displayed to the user to request input.
        :type prompt: str

    Returns:
        The input provided by the user.
        :rtype: str
    """
    return input(prompt)


def is_valid_input(user_input: str) -> bool:
    """
    Check if the user's input is valid.

    This function checks if the user's input is valid. The input is considered valid if it is not an empty string. The function returns True if the input is valid and False otherwise.

    Parameters:
        user_input: The input provided by the user.
        :type user_input: str

    Returns:
        A boolean value indicating whether the input is valid.
        :rtype: bool
    """
    return user_input != ""


def is_valid_guess(guess: str) -> bool:
    """
    Check if the user's guess is valid.

    This function checks if the user's guess is valid. The guess is considered valid if it is a single letter. The
    function returns True if the guess is valid and False otherwise. The function takes a single parameter, guess, which
    is the user's input. The function uses the strip method to remove any leading or trailing whitespace from the guess
    and, checks if the length of the guess is equal to 1 and if the guess is an alphabetic character.

    Parameters:
        guess: The user's guess.
        :type guess: str

    Returns:
        A boolean value indicating whether the guess is valid.
        :rtype: bool
    """
    return len(guess.strip()) == 1 and guess.isalpha()


def display_word(word: str, guessed_letters: set) -> str:
    """
    Display the word with underscores for missing letters.

    This function displays the word with underscores representing the letters that have not been guessed yet. The word
    parameter contains the word to be guessed, and the guessed_letters parameter is a set containing the letters that
    have been guessed so far. The function iterates over each character in the word and checks if the character has been
    guessed. If the character has been guessed, it is displayed as is; otherwise, an underscore is displayed. The
    function returns the word with underscores for missing letters.

    Parameters:
        word: The word to be guessed.
        :type word: str

        guessed_letters: The letters that have been guessed so far.
        :type guessed_letters: set

    Returns:
        The word with underscores for missing letters.
        :rtype: str
    """
    return "".join(char if char in guessed_letters else "_" for char in word)


def display_game_state(word: str, guessed_letters: set, attempts: int) -> None:
    """
    Display the current state of the game.

    This function displays the current state of the game, including the word with underscores for missing letters, the
    letters that have been guessed so far, the number of attempts remaining, and a blank like to separate the output
    from the previous output. The function takes three parameters: word, guessed_letters, and attempts. The word
    parameter contains the word to be guessed, the guessed_letters parameter is a set containing the letters that have
    been guessed so far, and the attempts parameter is an integer representing the number of attempts remaining. The
    function displays the word with underscores for missing letters, the guessed letters separated by commas, and the
    number of attempts remaining. The function does not return a value. It only displays the game state to the user.

    Parameters:
        word: The word to be guessed.
        :type word: str

        guessed_letters: The letters that have been guessed so far.
        :type guessed_letters: set

        attempts: The number of attempts remaining.
        :type attempts: int

    Returns:
        None
    """
    print(f"Word: {display_word(word, guessed_letters)}")
    print(f'Guessed Letters: {", ".join(sorted(guessed_letters))}')
    print(f"Attempts Remaining: {attempts}")
    print()


def play_again() -> bool:
    """
    Ask the user if they want to play again.

    This function prompts the user to enter a value to indicate whether they want to play the game again. The function
    returns True if the user wants to play again and False otherwise. The function displays a message to the user
    requesting input and reads the input provided by the user. The function checks if the input is valid and returns
    True if the input is 'Y' or 'y' and False if the input is 'N' or 'n'. If the input provided by the user is not
    valid, the function displays an error message and prompts the user to enter a valid input. The function continues to
    prompt the user until a valid input is provided.

    Returns:
        A boolean value indicating whether the user wants to play again.
        :rtype: bool
    """
    while True:
        play_again = get_user_input("Play Again? (Y/N): ").lower()
        if play_again not in ["y", "n"]:
            print(f'{" " * 2}*** Invalid Input. Please Enter Y or N.\n')
            continue
        return play_again == "y"


def play_hangman() -> None:
    """
    Play the Hangman game.

    This function implements the Hangman game. The function displays a welcome message to the user and starts the game
    loop. The game loop continues until the user chooses to exit the game. The function selects a random word from the
    list of words and initializes the guessed_letters set and the attempts variable. The game loop prompts the user to
    enter a letter and processes the user's input. The function checks if the input is valid, a valid guess, and whether
    the letter has already been guessed. If the input is valid, the function adds the letter to the guessed_letters set
    and checks if the letter is in the word. If the letter is in the word, the function displays a message indicating a
    correct guess. Otherwise, the function displays a message indicating an incorrect guess and decrements the attempts
    variable. The function checks if the user has guessed all the letters in the word or run out of attempts. If the
    user has guessed all the letters, the function displays a message indicating that the user has won the game. If the
    user has run out of attempts, the function displays a message indicating that the user has lost the game. The
    function prompts the user to play again and continues the game loop if the user chooses to play again, picking
    another random word. The function displays a thank you message when the user chooses to exit the game. The function
    takes no parameters and does not return a value.

    Returns:
        None
    """
    print(f"\nWelcome to Hangman!\n")
    while True:
        word = get_word()
        guessed_letters = set()
        attempts = MAX_ATTEMPTS
        while True:
            display_game_state(word, guessed_letters, attempts)
            guess = get_user_input("Enter a Letter: ").lower()
            if not is_valid_input(guess):
                print(f'{" " * 2}*** Invalid. Please Enter a Letter.\n')
                continue
            if not is_valid_guess(guess):
                print(f'{" " * 2}*** Invalid Guess. Please Enter a Single Letter.\n')
                continue
            if guess in guessed_letters:
                print(f'{" " * 2}*** You Already Guessed That Letter.\n')
                continue
            guessed_letters.add(guess)
            if guess in word:
                print(f'{" " * 2}*** Correct Guess!')
            else:
                print(f'{" " * 2}*** Incorrect Guess!')
                attempts -= 1
            if set(word) <= guessed_letters:
                display_game_state(word, guessed_letters, attempts)
                print(f"Congratulations! You Guessed the Word: {word.upper()}")
                break
            if attempts == 0:
                display_game_state(word, guessed_letters, attempts)
                print(f"Out of Attempts! The Word was: {word.upper()}")
                break
        if not play_again():
            break
    print(f"\nThanks for Playing Hangman!\n")


if __name__ == "__main__":
    play_hangman()
