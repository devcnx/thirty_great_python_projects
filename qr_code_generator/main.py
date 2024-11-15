"""
QR Code Generator. 

This application allows you to generate QR codes for any input (at least 3 characters long) - text or URL. The
user is prompted to enter the text or URL, their size choice, and their color choice. The application generates
the QR code and saves it as an image file (PNG) in the QR_CODE_IMAGES_DIRS directory. The user is then prompted
to generate another QR code or exit the application. 

This module imports the qrcode, os, and constants modules to aid in the application. The qrcode module is used
to generate the QR code. The os module is used to create and manage directories. The constants module contains
the QR_CODE_IMAGES_DIRS, QR_CODE_SIZES, and COLOR_CODES lists. The QR_CODE_IMAGES_DIRS list contains the
directory path where the QR code images will be saved. The QR_CODE_SIZES list contains the possible size choices
for the QR code. The COLOR_CODES list contains the possible color choices for the QR code.
"""

import qrcode
import os
from constants import QR_CODE_IMAGES_DIRS, QR_CODE_SIZES, COLOR_CODES


def display_welcome() -> None:
    """
    Display the welcome message to the user.

    This function is used to display the welcome message to the user. It takes no parameters and returns
    nothing. The welcome message is displayed to the user when the application is started.

    Returns:
        None
    """
    print(
        """
    Welcome to the QR Code Generator!

    This application allows you to generate QR codes for any input text or URL.
    The generated QR codes can be saved as image files (PNG) for later use.

    Follow the on-screen instructions to enter your choice of text or URL.
    """
    )


def display_list(message: str, list_to_display: list) -> None:
    """
    Display a list of options to the user.

    This function is used to display a list of options to the user. It takes two parameters, message
    and list_to_display. The message is displayed as a message before the list of options and the list_to_display
    is a list of options to be displayed. The function prints the message to the console and
    then iterates over the list_to_display and prints each item in the list to the console.
    The function does not return any values.

    Parameters:
        message: The message to be displayed before the list of options.
        :type message: str

        list_to_display: A list of options to be displayed.
        :type list_to_display: list

    Returns:
        None
    """
    print(message)
    for index, item in enumerate(list_to_display, start=1):
        print(f"  {index}. {item}")
    print()


def get_user_input(prompt: str) -> str:
    """
    Get the user's input.

    This function is used to get the user's input with the specified prompt. It takes a single parameter,
    prompt, which is the prompt message displayed to the user. It returns the user's input as a string.
    There's no validation handled in this function.

    Parameters:
        prompt: The prompt displayed to the user.
        :type prompt: str

    Returns:
        The user's input as a string.
        :rtype: str
    """
    return input(prompt)


def is_valid_input(user_input: str) -> bool:
    """
    Check if the user's input is valid.

    This function is used to validate the user's input. It returns True if the input is at least (3) characters
    long after stripping whitespace, otherwise, it returns False. It takes a single parameter, user_input, which
    is the input entered by the user.

    Parameters:
        user_input: The input entered by the user.
        :type user_input: str

    Returns:
        True if the input is at least (3) characters long after stripping whitespace, otherwise, it returns False.
        :rtype: bool
    """
    return len(user_input.strip()) >= 3


def is_valid_int(user_input: str) -> bool:
    """
    Determine if the user's input is a valid integer.

    This function is used to check if the user's input is a valid integer. It tries to convert the user's input into
    an integer and returns True if the conversion is successful, otherwise, it returns False. It takes a single
    parameter, user_input, which is the user's input as a string to be validated.

    Parameter:
        user_input: The user's input as a string to be validated.
        :type user_input: str

    Returns:
        True if the user's input is a valid integer, otherwise, it returns False.
        :rtype: bool
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid_option(user_input: str, options: list) -> bool:
    """
    Determine if the user's input is a valid option.

    This function is used to check if the user's input is a valid option. A valid option is considered one that is
    in the list of options. It takes two parameters, user_input and options. The user_input is the user's input
    as a string (and must be able to be converted into an integer). The options is a list of options to be
    considered valid.

    Parameters:
        user_input: The user's input as a string to be validated.
        :type user_input: str

        options: A list of options to be considered valid.
        :type options: list

    Returns:
        True if the user's input is a valid option, otherwise, it returns False.
        :rtype: bool
    """
    return is_valid_int(user_input) and 1 <= int(user_input) <= len(options)


def get_valid_user_input(prompt: str, validation_function) -> str:
    """
    Get a valid user input.

    This function is used to get a valid user input. It takes two parameters, prompt and validation_function.
    The prompt is the message displayed to the user. The validation_function is a function that takes a single
    parameter, user_input, and returns True if the user_input is valid, otherwise, it returns False.
    The function returns the user_input if it is valid.

    Parameters:
        user_input: The user's input as a string to be validated.
        :type user_input: str

        validation_function: A function that takes a single parameter, user_input, and returns True if the
        user_input is valid, otherwise, it returns False.
        :type validation_function: function

    Returns:
        The user_input if it is valid.
        :rtype: str
    """
    while True:
        user_input = get_user_input(prompt)
        if validation_function(user_input):
            return user_input
        print("  *** Invalid Input. Please Try Again...\n")


def get_user_choice(options: list) -> str:
    """
    Get the user's choice.

    This function is used to get the user's choice from a list of options. it takes a single parameter,
    options, which is a list of options to choose from. The function returns the user's choice as a string.

    Parameters:
        options: A list of options to choose from.
        :type options: list

    Returns:
        The user's choice as a string.
        :rtype: str
    """
    return get_valid_user_input(
        "Enter Your Choice: ", lambda user_input: is_valid_option(user_input, options)
    )


def display_user_choice(choice: str, options: list) -> str:
    """
    Display the user's choice.

    This function is used to display the user's choice from a list of options. It takes two parameters, choice and
    options. The choice is the user's choice as a string (and must be able to be converted into an integer). The
    options is a list of options to choose from. The function returns the user's choice as a string.

    Parameters:
        choice: The user's choice as a string.
        :type choice: str

        options: A list of options to choose from.
        :type options: list

    Returns:
        The user's choice as a string.
        :rtype: str
    """
    user_choice = int(choice) - 1
    if user_choice >= 0:
        selected_option = options[user_choice]
        print(f"  Your Choice: {selected_option}")
        return selected_option
    else:
        print("  *** Invalid Choice. Please Try Again...\n")
        return None


def get_number_of_saved_qr_codes() -> int:
    """
    Get the number of saved QR codes.

    This function is used to get the number of saved QR codes. It takes no parameters and returns the number of saved
    QR codes as an integer. This is done to keep track of the number of saved QR codes, which is used to name the
    file names of the saved QR codes in the QR_CODE_IMAGES_DIRS directory.

    Returns:
        The number of saved QR codes as an integer.
        :rtype: int
    """
    return (
        len(os.listdir(QR_CODE_IMAGES_DIRS))
        if os.path.exists(QR_CODE_IMAGES_DIRS)
        else 0
    )


def generate_qr_code(text: str, size: int, color: str) -> None:
    """
    Generate a QR code.

    This function is used to generate a QR code. It takes three parameters, text, size, and color. The text is the
    text to be encoded in the QR code. The size is the size of the QR code image. The color is the color of the
    QR code image. The function generates the QR code and saves it as an image file (PNG) in the QR_CODE_IMAGES_DIRS
    directory.

    Parameters:
        text: The text to be encoded in the QR code.
        :type text: str

        size: The size of the QR code image.
        :type size: int

        color: The color of the QR code image.
        :type color: str

    Returns:
        None
    """
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    file_name = f"qr_code_{get_number_of_saved_qr_codes() + 1}".lower()
    qr_code.add_data(text)
    qr_code.make(fit=True)
    qr_code_image = qr_code.make_image(fill_color=color, back_color="white")
    os.makedirs(QR_CODE_IMAGES_DIRS, exist_ok=True)
    qr_code_image.save(f"{QR_CODE_IMAGES_DIRS}{file_name}.png")
    print(
        f"\n  QR Code Generated Successfully.\n  The Image Has Been Saved As {file_name}.png\n"
    )


def generate_again() -> bool:
    """
    Prompt the user to generate another QR code.

    This function is used to prompt the user to generate another QR code. It takes no parameters and returns the
    user's choice as a boolean. The user is prompted to enter Y or N to generate another QR code. Their response
    is converted to lowercase and compared to y or n. If the user enters Y or y, the function returns True. If the
    user enters N or n, the function returns False.

    Returns:
        True if the user wants to generate another QR code, and False if the user does not want to generate another
        QR code.
        :rtype: bool
    """
    return (
        get_valid_user_input(
            "Would You Like to Generate Another QR Code? (Y/N): ",
            lambda user_input: user_input.lower() in ["y", "n"],
        ).lower()
        == "y"
    )


def display_exit_message() -> str:
    """
    Display the exit message.

    This function is used to display the exit message. It takes no parameters and returns the exit message as a
    string. The exit message is displayed when the user exits the application.

    Returns:
        The exit message.
        :rtype: str
    """
    return f"\nThanks for using the QR Code Generator. Goodbye!\n"


if __name__ == "__main__":
    display_welcome()
    while True:
        qr_code_text_or_url = get_user_input("Enter Text or URL: ")
        if not is_valid_input(qr_code_text_or_url):
            print("  *** Invalid Input. Please Try Again...\n")
            continue

        display_list("\nPick Your QR Code Size:", QR_CODE_SIZES)
        qr_code_size_choice = get_user_choice(QR_CODE_SIZES)
        qr_code_size = display_user_choice(qr_code_size_choice, QR_CODE_SIZES)
        if qr_code_size is None:
            continue

        display_list("\nPick Your QR Code Color:", COLOR_CODES)
        qr_code_color_choice = get_user_choice(COLOR_CODES)
        qr_code_color = display_user_choice(qr_code_color_choice, COLOR_CODES)
        if qr_code_color is None:
            continue

        qr_code_color = qr_code_color.split(" (")[0]  # Extract color code

        generate_qr_code(qr_code_text_or_url, int(qr_code_size), qr_code_color)

        if not generate_again():
            print(display_exit_message())
            break
        print()
