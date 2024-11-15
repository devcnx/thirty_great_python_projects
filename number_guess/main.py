"""
Number Guessing Game.

This module contains the main game logic for the number guessing game. The game is a simple game where the player has
to guess a number between (1) and (100). The player has a maximum of (10) guesses to guess the correct number. The game
will provide feedback to the player if the guess is too high or too low. If the player guesses the correct number, the
game will end and the player will be congratulated. Also, the user will be provided with the number of guesses it took
to guess the correct number. If the player is unable to guess the correct number within the maximum number of guesses,
the game will end and the player will be informed that they lost the game, and the correct number will be displayed.
The application also imports the NUMBER_RANGE constant from the constants module, which defines the range of numbers
that the player can guess from, and the MAX_GUESSES constant, which defines the maximum number of guesses the player
has to guess the correct number.
"""

from constants import MAX_GUESSES, NUMBER_RANGE
from random import randint


def display_welcome() -> str:
    """
    Display the welcome message to the player.

    This function displays the welcome message to the player when they start the game. It provides a brief description
    of the game and the rules. The function takes no parameters and returns the welcome message.

    Returns:
        The welcome message to the player.
        :rtype: str
    """
    return f"""
    Welcome to the Number Guessing Game!

    In this game, you have to guess a number between {NUMBER_RANGE[0]} and {NUMBER_RANGE[1]}. The game will provide
    feedback to you if your guess is too high or too low. You have a maximum of {MAX_GUESSES} guesses to guess the
    correct number. If you guess the correct number, you win! If you are unable to guess the correct number within the
    maximum number of guesses, you lose :(.

    Let's get started!
    """


def is_valid_input(user_input: str) -> bool:
    """
    Check if the user's input is valid.

    This function is used to validate the user's input. It returns True if the input is not an empty string,
    otherwise, it returns False. It takes a single parameter, user_input, which is the input entered by the user.

    Parameters:
        user_input: The input entered by the user.
        :type user_input: str

    Returns:
        A boolean value indicating whether the user's input is valid.
        :rtype: bool
    """
    return user_input != "" and user_input is not None


def is_valid_int(user_input: str) -> bool:
    """
    Check if the user's input is a valid integer.

    This function is used to determine if the user enters a valid integer. It returns True if the input can be converted
    to an integer, otherwise, it returns False. It takes a single parameter, user_input, which is the input entered by
    the user.

    Parameters:
        user_input: The input entered by the user.
        :type user_input: str

    Returns:
        A boolean value indicating whether the user's input is a valid integer.
        :rtype: bool
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid_int_in_range(user_input: str) -> bool:
    """
    Check if the user's input is a valid integer within the specified range.

    This function is used to determine if the user's input is a valid integer within the specified range. It returns
    True if the input can be converted to an integer and is within the specified range, otherwise, it returns False.
    It takes a single parameter, user_input, which is the input entered by the user. It uses the NUMBER_RANGE constant
    to determine the valid range of numbers.

    Parameters:
        user_input: The input entered by the user.
        :type user_input: str

    Returns:
        A boolean value indicating whether the user's input is a valid integer within the specified range.
        :rtype: bool
    """
    if is_valid_int(user_input):
        number = int(user_input)
        return NUMBER_RANGE[0] <= number <= NUMBER_RANGE[1]
    return False


def validate_user_input(prompt: str, validation_func: callable) -> str:
    """
    Validate the user's input based on the specified validation function.

    This function is used to validate the user's input based on the specified validation function. It prompts the user
    to enter their input and continues to prompt the user until the input passes the validation function. The function
    takes two parameters, prompt, which is the message displayed to the user, and validation_func, which is the function
    used to validate the user's input. The function returns the user's input once it passes the validation function.

    Parameters:
        prompt: The message displayed to the user.
        :type prompt: str

        validation_func: The function used to validate the user's input.
        :type validation_func: callable

    Returns:
        The user's input once it passes the validation function.
        :rtype: str
    """
    user_input = input(prompt)
    while not validation_func(user_input):
        if not is_valid_input(user_input):
            print(f'{" " * 2}*** A Guess is Required.')
        elif not is_valid_int(user_input):
            print(f'{" " * 2}*** Invalid Input. Please Enter a Valid Integer.')
        elif not is_valid_int_in_range(user_input):
            print(
                f'{" " * 2}*** Invalid Guess. Please Enter a Number Between ({NUMBER_RANGE[0]}) and ({NUMBER_RANGE[1]}).'
            )
        user_input = input(prompt)
    return user_input


def generate_random_number() -> int:
    """
    Generate a random number within the specified range.

    This function generates a random number within the specified range defined by the NUMBER_RANGE constant.
    It uses the randint function from the random module to generate a random integer. The function takes no
    parameters and returns the random number.

    Returns:
        A random number within the specified range.
        :rtype: int
    """
    return randint(NUMBER_RANGE[0], NUMBER_RANGE[1])


def is_correct_guess(guess: int, target: int) -> bool:
    """
    Check if the player's guess is correct.

    This function compares the player's guess with the target number to determine if the guess is correct. It takes
    two parameters, guess, which is the player's guess, and target, which is the target number. It returns True if
    the guess is correct, otherwise, it returns False.

    Parameters:
        guess: The player's guess.
        :type guess: int

        target: The target (correct) number.
        :type target: int

    Returns:
        A boolean value indicating whether the player's guess is correct.
        :rtype: bool
    """
    return guess == target


def provide_feedback(guess: int, target: int) -> str:
    """
    Provide feedback to the player based on their guess.

    This function provides feedback to the player based on their guess. It compares the player's guess with the target
    number and returns a message indicating whether the guess is too high or too low. The function takes two parameters,
    guess, which is the player's guess, and target, which is the target number. It returns a message providing feedback
    to the player.

    Parameters:
        guess: The player's guess.
        :type guess: int

        target: The target (correct) number.
        :type target: int

    Returns:
        A message providing feedback to the player.
        :rtype: str
    """
    if guess < target:
        return "Too Low!"
    elif guess > target:
        return "Too High!"
    else:
        return "Congratulations! You guessed the correct number!"


def track_number_of_guesses(guesses: int) -> int:
    """
    Track the number of guesses made by the player.

    This function is used to track the number of guesses made by the player. It takes the current number of guesses
    as input and increments it by one each time the player makes a guess. The function returns the updated number
    of guesses.

    Parameters:
        guesses: The current number of guesses made by the player.
        :type guesses: int

    Returns:
        The updated number of guesses.
        :rtype: int
    """
    return guesses + 1


def is_game_over(guesses: int) -> bool:
    """
    Check if the game is over.

    This function checks if the game is over based on the number of guesses made by the player. It compares the number
    of guesses to the maximum number of guesses allowed. If the player has reached the maximum number of guesses, the
    game is over, and the function returns True. Otherwise, it returns False. The function takes a single parameter,
    guesses, which is the number of guesses made by the player.

    Parameters:
        guesses: The number of guesses made by the player.
        :type guesses: int
    """
    return guesses >= MAX_GUESSES


def play_again() -> bool:
    """
    Ask the player if they want to play again.

    This function prompts the player to enter whether they want to play the game again. It takes no parameters and
    returns a boolean value indicating whether the player wants to play again. If the player enters 'Y' or 'y', the
    function returns True, indicating that the player wants to play again. If the player enters 'N' or 'n', the
    function returns False, indicating that the player does not want to play again. The function will continue to
    prompt the player until a valid input is entered (either 'Y' or 'N'). Their input is converted to lowercase to
    make it case-insensitive.

    Returns:
        A boolean value indicating whether the player wants to play again.
        :rtype: bool
    """
    prompt = "Would You Like to Play Again? (Y/N): "
    user_input = validate_user_input(prompt, is_valid_input).lower()
    while user_input not in ["y", "n"]:
        print(
            f'{" " * 2}*** Invalid Input. Please Enter "Y" to Play Again or "N" to Quit.'
        )
        user_input = validate_user_input(prompt, is_valid_input).lower()
    return user_input == "y"


def play_game():
    """
    Play the number guessing game.

    This function contains the main game logic for the number guessing game. It generates a random number within the
    specified range, and then prompts the player to guess the number. The player has a maximum number of guesses to
    guess the correct number. The game provides feedback to the player based on their guess and informs them if the
    guess is too high or too low. If the player guesses the correct number, the game ends and the player is
    congratulated. If the player is unable to guess the correct number within the maximum number of guesses, the game
    ends and the player is informed that they lost the game. The correct number is displayed to the user and they
    are provided with the number of guesses it took to guess the correct number.

    Returns:
        None
    """
    target = generate_random_number()
    guesses = 0

    while not is_game_over(guesses):
        prompt = f"Enter Your Guess: "
        guess = validate_user_input(prompt, is_valid_input)
        if not is_valid_input(guess):
            print(f'{" " * 2}*** Invalid Input. Please Enter a Valid Integer.')
            continue
        elif not is_valid_int(guess):
            print(f'{" " * 2}*** Invalid Input. Please Enter a Valid Integer.')
            continue
        elif not is_valid_int_in_range(guess):
            print(
                f'{" " * 2}*** Invalid Guess. Please Enter a Number Between ({NUMBER_RANGE[0]}) and ({NUMBER_RANGE[1]}).'
            )
            continue

        guess = int(guess)
        guesses = track_number_of_guesses(guesses)

        if is_correct_guess(guess, target):
            print(f'{" " * 2}*** {provide_feedback(guess, target)}')
            print(
                f'{" " * 2}*** You Guessed the Correct Number in ({guesses}) Guesses!'
            )
            break

        print(f'{" " * 2}*** {provide_feedback(guess, target)}')

        if is_game_over(guesses):
            print(
                f'{" " * 2}*** Game Over! You Have Reached the Maximum Number of Guesses.'
            )
            print(f'{" " * 2}*** The Correct Number Was ({target}).')
            break

        print(f'{" " * 2}*** Number of Guesses Remaining: ({MAX_GUESSES - guesses})\n')

    if play_again():
        play_game()
    else:
        print("Thanks for Playing! Goodbye!")


if __name__ == "__main__":
    print(display_welcome())
    play_game()
