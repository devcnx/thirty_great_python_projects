import os

MESSAGES = {
    'welcome': f'''

    Welcome to Brute Force.

    You'll enter a word or password when prompted.
    This application attempts to find a specified word or password using brute force techniques.
    It will check a list of common words for a match.
    If not found, it will go through every possible combination of characters to find the correct word.

    This application is for educational purposes only.

    Let's get started!

    ''',
    'exit': f'''\nThanks for Using Brute Force! Goodbye!'''
}
WORDS_FILE_PATH = os.path.join(os.path.dirname(__file__), 'files/words.txt')
MAX_ATTEMPTS = 10 ** 8
TIMER_SLEEP = 5
PAUSE_INTERVAL = 10
PAUSE_DURATION = 3
