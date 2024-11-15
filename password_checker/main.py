"""
Password Checker. 

This application allows a user to check how common a password is. The user can input a password and the application
will tell the user how common the password is. The application works with a list of common passwords stored in the
password_checker/files/common_passwords.txt file (COMMON_PASSWORDS_FILE_PATH). 
"""

from constants import COMMON_PASSWORDS_FILE_PATH


def get_user_input(prompt: str) -> str:
    """
    Get the user's input.

    This function is used to get the user's input. It takes a single parameter, which is the prompt to
    display to the user. The function prompts the user with the prompt and waits for the user to enter
    input. The input is then returned as a string. The function does not validate the input.

    Parameters:
        prompt: The prompt to display to the user.
        :type prompt: str

    Returns:
        The user's input.
        :rtype: str
    """
    return input(prompt)


def is_valid_input(user_input: str) -> bool:
    """
    Check if the user's input is valid.

    This function is used to validate the user's input. Valid input is input that is not an empty string.
    The function takes a single parameter, which is the user's input. The function returns True if the input
    is not an empty string, otherwise, it returns False.

    Parameters:
        user_input: The user's input.
         :type user_input: str

    Returns:
        True if the user's input is not an empty string, otherwise, it returns False.
        :rtype: bool
    """
    return user_input != ""


def get_file_data(file_path: str) -> list:
    """
    Get the data from a file.

    This function is used to get the data from a file. The function takes a single parameter, which is the
    path to the file. The function returns a list of strings. There is no validation handled in this function.

    Parameters:
        file_path: The path to the file.
        :type file_path: str

    Returns:
        A list of strings.
        :rtype: list
    """
    with open(file_path, "r") as file:
        return file.read().splitlines()


def get_common_passwords() -> list:
    """
    Get the common passwords.

    This function is used to get the common passwords from the file. The function returns a list of strings
    containing the common passwords. There is no validation handled in this function.

    Returns:
        A list of strings containing the common passwords.
        :rtype: list
    """
    return get_file_data(COMMON_PASSWORDS_FILE_PATH)


def is_common_password(password: str, common_passwords: list) -> bool:
    """
    Check if the password is common.

    This function is used to check if the password is common. It takes two parameters, password and common_passwords,
    which are the password to check and the list of common passwords. The function iterates over the common passwords
    and returns True if the password is in the list of common passwords, and False otherwise. There is no validationi
    handled in this function.

    Parameters:
        password: The password to check.
        :type password: str

        common_passwords: A list of common passwords.
        :type common_passwords: list

    Returns:
        A boolean value indicating whether the password is common or not.
        :rtype: bool
    """
    return password in common_passwords


def check_again() -> bool:
    """
    Check if the user wants to check another password.

    This function is used to check if the user wants to check another password. It returns True if the user
    enters 'Y' or 'y', and False if the user enters 'N' or 'n'. There is no validation handled in this function.
    It takes no parameters and returns a boolean.

    Returns:
        A boolean value indicating whether the user wants to check another password.
        :rtype: bool
    """
    user_input = get_user_input("Would you like to check another password? (Y/N): ")
    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        return False
    else:
        print(f'{" " * 2}*** Invalid Input. Please Try Again.\n')
        return check_again()


if __name__ == "__main__":
    common_passwords = get_common_passwords()

    while True:
        password = get_user_input("Enter a Password: ")
        if not is_valid_input(password):
            print(f'{" " * 2}*** A Password is Required. Please Try Again.\n')
            continue

        if is_common_password(password, common_passwords):
            print(f"\n❌ {password} is a Common Password.\n")
        else:
            print(f"\n✅ {password} is a Unique Password.\n")

        if not check_again():
            print(f"\nThanks for Using the Password Checker. Goodbye!\n")
            break
        else:
            continue
