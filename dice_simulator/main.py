"""
Dice Simulator.

This is a simple dice simulator that allows the user to roll a dice and get a random number between (1) and (6).
The user can roll the dice as many times as they want. Once the user is done rolling the dice, they can exit the
application by typing 'exit'. This module contains functions that prompt the user for input, validate the input,
generate a random number between (1) and (6), and display the result to the user. This module imports the random
module to generate the random number.
"""

import random
from constants import DICE_RANGE, DEFAULT_ROLLS


def display_welcome() -> str:
    """
    Display the welcome message to the user.

    This function displays the welcome message to the user. The welcome message is displayed when the user starts the
    application and is the first message the user sees. It takes no parameters and returns a string, which is the
    welcome message and instructions for the user.

    Returns:
        The welcome message and instructions for the user.
        :rtype: str
    """
    return f"""
    Welcome to the Dice Simulator!

    This is a dice simulator that allows you to roll a specified number of dice and get random numbers between
    (1) and (6). You can roll the dice as many times as you want. Once you are done rolling the dice, you can
    exit the application by typing 'exit'.

    Let's get started!
    """


def get_user_input(prompt: str) -> str:
    """
    Get the user's input.

    This function is used to get the user's input. It takes a single parameter, which is the prompt message that is
    displayed to the user. The function prompts the user with the message and waits for the user to enter input.
    The input is then returned as a string. The function does not validate the input.

    Parameters:
        prompt: The message displayed to the user as a prompt.
        :type prompt: str

    Returns:
        The user's input.
        :rtype: str
    """
    return input(prompt)


def is_valid_input(user_input: str) -> bool:
    """
    Check if the user's input is valid.

    This function checks if the user's input is valid. It takes a single parameter, which is the user's input as a
    string. The function checks if the input is not an empty string and returns a boolean value based on the
    validation results. If the input is valid, the function returns True. Otherwise, it returns False.

    Parameters:
        user_input: The user's input to be validated.
        :type user_input: str

    Returns:
        A boolean value indicating if the input is valid. True if the input is not empty, False otherwise.
    """
    return user_input != ""


def is_valid_int(user_input: str) -> bool:
    """
    Check if the user's input is a valid integer.

    This function checks if the user's input is a valid integer. It takes a single parameter, which is the user's input
    as a string. The function tries to convert the input to an integer and returns a boolean value based on the
    conversion results. If the input can be converted to an integer, the function returns True. Otherwise, it returns
    False.

    Parameters:
        user_input: The user's input to be validated.
        :type user_input: str

    Returns:
        A boolean value of True if the input can be converted to an integer, False otherwise.
        :rtype: bool
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid_int_greater_than_zero(user_input: str) -> bool:
    """
    Check if the user's input is a valid integer greater than zero.

    This function checks if the user's input is a valid integer greater than zero. It takes a single parameter, which is
    the user's input as a string. Using the is_valid_input() and is_valid_int() functions, it checks if the input is
    valid and can be converted to an integer. If the input is valid and greater than zero, the function returns True.
    Otherwise, it returns False.

    Parameters:
        user_input: The user's input to be validated.
        :type user_input: str

    Returns:
        A boolean value of True if the input is a valid integer greater than zero, False otherwise.
        :rtype: bool
    """
    return (
        is_valid_input(user_input) and is_valid_int(user_input) and int(user_input) > 0
    )


def generate_random_number() -> int:
    """
    Generate a random number between (1) and (6).

    This function generates a random number between (1) and (6) using the random module. The range is stored in a
    constant variable, DICE_RANGE, which is used to generate the random number. The function returns the random number
    as an integer.

    Returns:
        A random number between (1) and (6).
        :rtype: int
    """
    return random.randint(*DICE_RANGE)


def roll_dice(amount: int = DEFAULT_ROLLS) -> list[int]:
    """
    Roll the dice a specified number of times.

    This function rolls the dice a specified number of times and returns a list of the random numbers generated.
    It takes a single parameter, amount, which specifies the number of times the dice should be rolled. The default
    value is stored in a constant variable, DEFAULT_ROLLS. The function generates random numbers using the
    random module and the generate_random_number() function. The random numbers are stored in a list, which is
    returned by the function.

    Parameters:
        amount: The number of times the dice should be rolled.
        :type amount: int

    Returns:
        A list of random numbers generated by rolling the dice.
        :rtype: list[int]
    """
    return [generate_random_number() for _ in range(amount)]


def display_result(rolls: list[int]) -> str:
    """
    Display the result of rolling the dice.

    This function displays the result of rolling the dice to the user. It takes a single parameter, rolls, which is a
    list of random numbers generated by rolling the dice. The function formats the result message and the random
    numbers in a readable format and returns the message as a string.

    Parameters:
        rolls: A list of random numbers generated by rolling the dice.
        :type rolls: list[int]

    Returns:
        The result message and random numbers in a readable format.
        :rtype: str
    """
    return f'You Rolled: {", ".join(map(str, rolls))}'


def total_rolls(rolls: list[int]) -> str:
    """
    Display the total of the rolls.

    This function displays the total of the rolls to the user. It takes a single parameter, rolls, which is a list of
    random numbers generated by rolling the dice. The function calculates the total of the rolls and returns the total
    as a string.

    Parameters:
        rolls: A list of random numbers generated by rolling the dice.
        :type rolls: list[int]

    Returns:
        The total of the rolls as a string.
        :rtype: str
    """
    return f"Total: {sum(rolls)}"


def display_exit_message() -> str:
    """
    Display the exit message to the user.

    This function displays the exit message to the user. The exit message is displayed when the user exits the
    application. The function returns the exit message as a string.

    Returns:
        The exit message.
        :rtype: str
    """
    return f"""
    Thank You for Using the Dice Simulator!
    Exiting the Application...
    """


def play_dice_simulator() -> None:
    """
    Play the dice simulator.

    This function is the main function that runs the dice simulator. It contains the main logic of the application,
    including prompting the user for input, validating the input, generating random numbers by rolling the dice, and
    displaying the result to the user. The function uses the helper functions defined in this module to perform these
    tasks. The function runs in a loop until the user exits the application by typing 'exit'. The function takes no
    parameters and does not return any values.

    Returns:
        None
    """
    print(display_welcome())
    while True:
        user_input = get_user_input("Enter the Number of Dice to Roll: ")
        if user_input.lower() == "exit":
            print(display_exit_message())
            break
        if not is_valid_int_greater_than_zero(user_input):
            print(
                f'{" " * 2}*** Invalid Input! Please Enter a Valid Integer Greater Than Zero.'
            )
            continue
        rolls = roll_dice(int(user_input))
        print(display_result(rolls))
        print(total_rolls(rolls))


if __name__ == "__main__":
    play_dice_simulator()
