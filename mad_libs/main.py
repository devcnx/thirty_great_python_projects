
"""
Mad Libs Game. 

This module contains the main game logic for the Mad Libs game. It prompts the user to enter words based on the word
types required for a randomly selected story template. The user's words are used to fill in the story template, and the
filled story is displayed to the user. The user can choose to play again after each story. 

The module imports the random module to select a random story template from the constants module. The module also 
imports the STORIES constant from the constants module, which contains the story templates and word types for the game. 

The module contains the following functions:
    - is_valid_input(user_input: str) -> bool: Returns True if the user input is not an empty string. Otherwise, False. 
    - get_user_input(prompt: str) -> str: Prompts the user to enter input based on the given prompt. 
    - format_word_type(word_type: str) -> str: Formats the word type for display in the prompt. 
    - fill_story_template(template: str, word_types: list) -> str: Fills in the story template with the user's words. 
    - get_random_story() -> dict: Returns a random story template from the STORIES constant. 
    - display_story(story: dict) -> None: Displays the story with the user's words filled in. 
    - display_instructions() -> None: Displays the instructions for the game. 
"""
import random
from constants import STORIES


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
    return user_input != ''


def get_user_input(prompt: str) -> str:
    """
    Get user input based on the given prompt. 

    This function prompts the user to enter input based on the given prompt. It validates the user's input using the
    is_valid_input function of the module. If the input is not valid, the user is prompted to enter the input again. 
    It takes a single parameter, prompt, which is the message displayed to the user. 

    Parameters:
        prompt: The message displayed to the user. 
        :type prompt: str

    Returns:
        The user's input.
        :rtype: str
    """
    user_input = input(prompt).strip()
    while not is_valid_input(user_input):
        user_input = input(f'{" " * 2}*** Invalid Input. Please Try Again...\n\n{prompt}').strip()
    return user_input


def format_word_type(word_type: str) -> str:
    """
    Format the word type for display in the prompt. 

    This function formats the word type for display in the prompt. It capitalizes the word type and adds additional
    information for verbs (past tense). It takes a single parameter, word_type, which is the type of word to be
    formatted. The word type is expected to be in the format 'base_type_suffix', where the suffix is a unique
    identifier for the word type in the story template. The function uses the rsplit method to extract the base word
    type and capitalize it.

    Parameters:
        word_type: The type of word to be formatted.
        :type word_type: str

    Returns:
        The formatted word type.
        :rtype: str
    """
    base_word_type = word_type.rsplit('_', 1)[0]
    formatted_word_type = base_word_type.replace('_', ' ').capitalize()

    if 'verb' in word_type.lower():
        formatted_word_type += f'(s) (Past Tense)'
    return formatted_word_type


def fill_story_template(template: str, word_types: list) -> str:
    """
    Fill in the story template with the user's words. 

    This function fills in the story template with the user's words based on the word types required for the story. 
    It prompts the user to enter the words based on the word types and replaces the placeholders in the template with
    the user's words. It takes two parameters, template and word_types, where template is the story template with
    placeholders for the words, and word_types is a list of word types required for the story. The function uses a
    dictionary to store the user's words based on the base word type. The number of words required for each base word
    type is determined by counting the occurrences of the base word type in the word_types list. The function then
    prompts the user to enter the required number of words for each base word type, separated by commas. If the user
    enters the wrong number of words, they are prompted to enter the words again. 

    Parameters:
        template: The story template with placeholders for the words. 
        :type template: str

        word_types: A list of word types required for the story. 
        :type word_types: list

    Returns:
        The story template with the user's words filled in. 
        :rtype: str
    """
    word_count = {}
    for word_type in word_types:
        base_word_type = word_type.rsplit('_', 1)[0]
        word_count[base_word_type] = word_count.get(base_word_type, 0) + 1

    user_words = {}
    for base_word_type, count in word_count.items():
        formatted_word_type = format_word_type(base_word_type)
        while True:
            words = get_user_input(f'Enter ({count}) {formatted_word_type}{
                                   "s" if count > 1 else ""}: ')
            word_list = [word.strip() for word in words.split(',')]
            if len(word_list) == count:
                user_words[base_word_type] = word_list
                break
            else:
                print(f'{" " * 2}*** Invalid Input. Please Enter ({count}) {formatted_word_type}{"s" if count >
                      1 else ""} Separated by Commas...\n')

    for word_type in word_types:
        base_word_type = word_type.rsplit('_', 1)[0]
        template = template.replace(f'{{{word_type}}}', user_words[base_word_type].pop(0), 1)

    return template


def get_random_story() -> dict:
    """
    Get a random story template. 

    This function returns a random story template from the STORIES constant. It uses the random.choice method to select
    a random story id, which is the key in the STORIES dictionary. The function returns the story template associated
    with the selected story id. The function takes no parameters and returns a dictionary containing the story template
    and word types for the selected story. 

    Returns:
        A dictionary containing the story template and word types for the selected story. 
        :rtype: dict
    """
    story_id = random.choice(list(STORIES.keys()))
    return STORIES[story_id]


def display_story(story: dict) -> None:
    """
    Display the story with the user's words filled in. 

    This function displays the story with the user's words filled in based on the word types required for the story. 
    It uses the fill_story_template function to fill in the story template with the user's words. The function then
    displays the title of the story, followed by the filled story. The function takes a single parameter, story, which
    is a dictionary containing the story template and word types for the story. 

    Parameters:
        story: A dictionary containing the story template and word types for the story. 
        :type story: dict

    Returns:
        None
    """
    print(f'\n{story["title"]}\n')
    print(f'{"-" * len(story["title"])}\n')
    filled_story = fill_story_template(story['template'], story['word_types'])
    print(f'\n{filled_story}\n')


def display_instructions() -> None:
    """
    Display the instructions for the game. 

    This function displays the instructions for the Mad Libs game. It provides information on how to play the game,
    including entering words, displaying the story, and playing again. It takes no parameters and returns None. 

    Returns:
        None
    """
    print(f'Instructions:')
    print(f'1. Enter the requested words when prompted, separated by commas.')
    print(f'2. The story will be displayed with your words filled in.')
    print(f'3. Decide if you want to play again after each story.')
    print(f'4. Have fun!\n')


if __name__ == '__main__':
    print(f'\nWelcome to Mad Libs!\n')
    display_instructions()
    while True:
        story = get_random_story()
        display_story(story)
        play_again = input('Would you like to play again? (Y/N): ').strip().lower()
        if play_again != 'y':
            break
        print(f'\nThanks for playing! Goodbye!\n')
