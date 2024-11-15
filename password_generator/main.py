"""
Password Generator

This module generates random passwords for the user. It allows the user to generate between (1)
and (5) passwords at a time, with each password being between (8) and (15) characters long (inclusive).
The module ensures that the generated passwords contain a mix of uppercase letters, lowercase letters, 
numbers, and special characters, meeting common password requirements.

The module imports the MIN_PASSWORD_LENGTH and MAX_PASSWORD_LENGTH constants from the constants module,
and uses the following standard libraries:
    - random: For generating random characters for the password. 
    - string: For getting the list of printable characters to use in the password. 
    - secrets: For generating cyptographically secure random passwords.
    - sys: For exiting the application. 
    
The main functionality of the module includes:
    - Generating a random password between a specified length range.
    - Validating the user's input for the number of passwords to generate. 
    - Allowing the user to generate another set of passwords or exit the application. 
    - Ensuring that the generated passwords meet common password requirements.
    - Printing the generated passwords to the user. 
    - Handling exceptions and errors gracefully.
    
The module is designed to be run from the command line, and provides a simple interface for the user to
generate passwords.
"""
import random
import secrets
import string
import sys
from constants import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH, MIN_NUMBER_OF_PASSWORDS, MAX_NUMBER_OF_PASSWORDS


def display_welcome() -> str:
    """
    Display a welcome message to the user. 

    This function displays a welcome message to the user along with brief instructions for how to use the
    application. It does not take any parameters or return any values. 

    Returns:
        None
    """
    return f'''
    Welcome to the Password Generator!

    This application allows you to generate random passwords that meet common password requirements.
    You can generate between (1) and (5) passwords at a time, with each password being between (8) and
    (15) characters long. The passwords will contain a mix of uppercase and lowercase letters, numbers,
    and special characters.

    Follow the prompts to generate your passwords.
    '''


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
    Determine if the user's input is valid. 

    This function is used to validate the user's input by checking if it's equal to an empty string. 
    If it is, the input is considered invalid. It takes a single parameter, user_input, which is the 
    user's input as a string. It returns a boolean value indicating whether the input is valid or not.

    Parameters:
        user_input: The user's input to validate. 
        :type user_input: str

    Returns:
        A boolean value indicating whether the input is valid or not. 
        :rtype: bool
    """
    return user_input != '' and user_input != None


def is_valid_int(user_input: str) -> bool:
    """
    Determine if the user's input is a valid integer. 

    This function checks to see if the user's input is a valid integer by trying to convert the
    input to an integer. If the conversion is successful, the input is considered valid. It takes
    a single parameter, user_input, which is the user's input as a string. It returns a boolean
    value indicating whether the input is a valid integer or not. 

    Parameters:
        user_input: The user's input to validate. 
        :type user_input: str

    Returns:
        A boolean value indicating whether or not the user's input is valid. 
        :rtype: bool
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid_int_within_range(user_input: str, min_value: int = MIN_PASSWORD_LENGTH, max_value: int = MAX_PASSWORD_LENGTH) -> bool:
    """
    Determine if the user's input is a valid integer within a specified range. 

    This function checks to see if the user's input is a valid integer, and if it falls within the specified
    range. It takes three parameters: user_input, which is the user's input as a string, min_value, which is
    the minimum value the input can be, and max_value, which is the maximum value the input can be. It returns
    a boolean value indicating whether the input is a valid integer within the specified range. 

    Parameters:
        user_input: The user's input to validate.
        :type user_input: str

        min_value: The minimum value the input can be. 
        :type min_value: int

        max_value: The maximum value the input can be.
        :type max_value: int

    Returns:
        A boolean value indicating whether the user's input is a valid integer within the specified range.
        :rtype: bool
    """
    return is_valid_int(user_input) and min_value <= int(user_input) <= max_value


def generate_password() -> str:
    """
    Generate a random password. 

    This function generates a random password with a specified length. It uses the constant values
    MIN_PASSWORD_LENGTH and MAX_PASSWORD_LENGTH to determine the length of the password, with the
    random length being between these two values. It returns the generated password as a string. 

    Returns:
        A random password as a string.
        :rtype: str
    """
    length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password_characters) for _ in range(length))


def contains_uppercase(password: str) -> bool:
    """
    Check that the password contains an uppercase letter. 

    This function checks if the password contains at least one uppercase letter. It takes a single parameter, 
    password, which is the password to check. It returns a boolean value of True if the password contains an
    uppercase letter, and False otherwise. 

    Parameters:
        password: The password to check. 
        :type password: str

    Returns:
        A boolean value indicating whether the password contains an uppercase letter. 
        :rtype: bool
    """
    return any(character.isupper() for character in password)


def contains_lowercase(password: str) -> bool:
    """
    Check that the password contains a lowercase letter. 

    This function checks if the password contains at least one lowercase letter. It takes a single parameter, 
    password, which is the password to check. It returns a boolean value of the True if the password contains a
    lowercase letter, and False otherwise. 

    Parameters:
        password: The password to check. 
        :type password: str

    Returns:
        A boolean value indicating whether the password contains a lowercase letter. 
        :rtype: bool
    """
    return any(character.islower() for character in password)


def contains_digit(password: str) -> bool:
    """
    Check that the password contains a number. 

    This function checks if the password contains at least one number. It takes a single parameter, password, 
    which is the password to check. It returns a boolean value of True if the password contains a number, and
    False otherwise. 

    Parameters:
        password: The password to check. 
        :type password: str

    Returns:
        A boolean value indicating whether the password contains a number. 
        :rtype: bool
    """
    return any(character.isdigit() for character in password)


def contains_special_character(password: str) -> bool:
    """
    Check that the password contains a special character. 

    This function checks if the password contains at least one special character. It takes a single parameter,
    password, which is the password to check. It returns a boolean value of True if the password contains a
    special character, and False otherwise.

    Parameters:
        password: The password to check. 
        :type password: str

    Returns:
        A boolean value indicating whether the password contains a special character. 
        :rtype: bool
    """
    return any(not character.isalnum() for character in password)


def is_valid_password(password: str) -> bool:
    """
    Determine if the password is valid. 

    This function checks if the password meets common password requirements, including containing an uppercase
    letter, a lowercase letter, a number, and a special character. Using the helper functions contains_uppercase,
    contains_lowercase, contains_digit, and contains_special_character, it checks if the password meets these
    requirements. It takes a single parameter, password, which is the password to validate. It returns a boolean
    value indicating whether the password is valid or not. 

    Parameters
        password: The password to validate.
        :type password: str

    Returns:
        A boolean value indicating whether the password is valid or not. 
        :rtype: bool
    """
    return contains_uppercase(password) and contains_lowercase(password) and contains_digit(password) and contains_special_character(password)


def print_passwords(passwords: list) -> None:
    """
    Print the passwords to the user. 

    This function is used to print the passwords to the user. It takes a single parameter, passwords, which is 
    a list of passwords to print. It does not return any values. 

    Parameters:
        passwords: The list of passwords to print. 
        :type passwords: list

    Returns:
        None
    """
    f'''
    Generated Passwords:
    '''
    for index, password in enumerate(passwords, start=1):
        print(f'{index} {password}')
    print()


def exit_application() -> None:
    """
    Exit the application. 

    This function is used to exit the application. It does not take any parameters or return any values. 
    It uses the sys.exit() function to exit the application. 

    Returns:
        None
    """
    print('\nThank You for Using the Password Generator. Goodbye!\n')
    sys.exit()


def generate_again() -> bool:
    """
    Prompt the user to generate more passwords. 

    This function prompts the user to generate more passwords or exit the application. It takes no parameters
    and returns a boolean value indicating whether the user wants to generate more passwords. 

    Returns:
        A boolean value indicating whether the user wants to generate more passwords.
        :rtype: bool
    """
    while True:
        get_user_input = input(
            'Would You Like to Generate More Passwords? (Y/N): ').lower()
        if not is_valid_input(get_user_input):
            print(f'{" " * 2}*** Invalid. An Entry is Required.\n')
            continue
        if get_user_input not in ['y', 'n']:
            print(f'{" " * 2}*** Invalid Input. Please Enter "Y" or "N".\n')
            continue
        return get_user_input == 'y'


if __name__ == '__main__':
    print(display_welcome())
    while True:
        number_of_passwords = get_user_input(
            'How Many Passwords Would You Like to Generate? ')
        if not is_valid_input(number_of_passwords):
            print(f'{" " * 2}*** Invalid. An Entry is Required.\n')
            continue
        if not is_valid_int_within_range(number_of_passwords, MIN_NUMBER_OF_PASSWORDS, MAX_NUMBER_OF_PASSWORDS):
            print(f'{" " * 2}*** Invalid Input. The Number of Passwords Must Be Between({
                  MIN_NUMBER_OF_PASSWORDS}) and ({MAX_NUMBER_OF_PASSWORDS}).\n')
            continue
        number_of_passwords = int(number_of_passwords)

        passwords = []
        while len(passwords) < number_of_passwords:
            password = generate_password()
            if is_valid_password(password):
                passwords.append(password)
        print_passwords(passwords)

        if not generate_again():
            exit_application()
