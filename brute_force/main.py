"""
Brute Force. 

This program is designed to crack common passwords. The program contains several functions that are used to 
crack common passwords. It's designed to be run from the command line. It imports the itertools library, which
contains a function that generates all possible combinations of characters. The random library is used to generate
random passwords which are scrambled words from a list of words. The string library is used to get the list of
printable characters to use in the password. The time library is used to pause the program for a specified amount
of time. The threading library is used to create threads for the program to run in parallel. From the constants
module, it imports the MESSAGES, WORDS_FILE_PATH, TIMER_SLEEP, PAUSE_INTERVAL, and PAUSE DURATION variables. 
From the threading library, it imports the Thread, Event, and Lock classes. 

Key Features:
    - Generates a random password using words from a list of words. 
    - Scramble the characters in the password. 
    - Check if the password is common.
    - Check if the password contains digits, symbols, or both. 
    - Get the length of the password. 
    - Update the number of attempts. 
    - Check if the password matches a common password.
    - Pause the program for a specified amount of time.
    - Create threads for the program to run in parallel.
    
NOTE:
    The print statements are used to print the results for debugging purposes.
"""
import itertools
import random
import string
import time
from constants import MESSAGES, WORDS_FILE_PATH, TIMER_SLEEP, PAUSE_INTERVAL, PAUSE_DURATION
from threading import Thread, Event, Lock


def get_words() -> list:
    """
    Get the words from the file. 

    This function is used to get the words from the file. The function returns a list of strings from the file. 
    There is no validation handled in this function. It uses the open() function to read the file, and the
    read() function to read the contents of the file. The splitlines() function is used to split the file
    into lines and store them in a list. The function returns the list of words back to the user. 

    Returns:
        The list of words. 
        :rtype: list
    """
    with open(WORDS_FILE_PATH, 'r') as file:
        return file.read().splitlines()


def scramble_chars(word: str) -> str:
    """ 
    Scramble the characters in the word. 

    This function is used to scramble the characters in a given word. It takes a single parameter, word,
    which is the word to scramble. Using random.sample, it scrambles the characters in the word and returns
    the scrambled word.

    Parameters:
        word: The word to scramble. 
        :type word: str

    Returns:
        The scrambled word. 
        :rtype: str
    """
    return ''.join(random.sample(word, len(word)))


def get_random_word(words: list) -> str:
    """
    Get a random word from the list. 

    This function is used to get a random word from the list of words. It takes a single parameter, words,
    which is the list of words to choose from. It uses the random.choice function to select the random word
    and returns it to the user. 

    Parameters:
        words: The list of words to choose from. 
        :type words: list

    Returns:
        The random word. 
        :rtype: str
    """
    return random.choice(words)


def find_match(word: str, word_list: list) -> str | None:
    """
    Find a match. 

    This function is used to find a match in a list of words. It takes two parameters, word and word_list, 
    which are the word to search for and the list of words to search in. It uses the enumerate function
    to get the index of the word in the list. If the word is found in the list, it returns the common
    match along with the index as a string. If the word is not found, it returns None. 

    Parameters:
        word: The word to search for. 
        :type word: str

        word_list: The list of words to search in.
        :type word_list: list

    Returns:
        The common match along with the index as a string or None if the word is not found. 
        :rtype: str | None
    """
    for index, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common Match: {match} (#{index:,})'
    return None


def get_word_length(word: str) -> int:
    """
    Get the length of the word. 

    This function is used to get the length of the word using the len() function. It takes a single parameter,
    word, which is the word to get the length of. It returns the length of the word as an integer. 

    Parameters:
        word: The word to get the length of.
        :type word: str

    Returns:
        The length of the word as an integer. 
        :rtype: int
    """
    return len(word)


def update_attempts(attempts: int) -> int:
    """
    Update the number of attempts. 

    This function takes a single parameter, attempts, which is the current number of attempts. It increments 
    the number of attempts by 1 and returns the updated number of attempts. 

    Parameters:
        attempts: The current number of attempts. 
        :type attempts: int

    Returns:
        The updated number of attempts. 
        :rtype: int
    """
    return attempts + 1


def has_digits(word: str) -> bool:
    """
    Check if the word has digits. 

    This function checks if the given word, which is the single parameter, contains digits. Digits are considered
    numeric characters in Python. It returns True if the word contains digits, and False otherwise. 

    Parameters:
        word: The word to check. 
        :type word: str

    Returns:
        True if the word contains digits, and False otherwise. 
        :rtype: bool
    """
    return any(char.isdigit() for char in word)


def has_symbols(word: str) -> bool:
    """
    Check if the word has symbols. 

    This function is used to check if the word has symbols. It takes a single parameter, word, which is the word
    to check. Symbols are considered punctuation characters in Python. It returns True if the word contains symbols,
    and False otherwise. 

    Parameters:
        word: The word to check. 
        :type word: str

    Returns:
        True if the word contains symbols, and False otherwise. 
        :rtype: bool
    """
    return any(char in string.punctuation for char in word)


def get_chars(word: str) -> str:
    """
    Get the characters. 

    This function is used to get the characters in the word. It takes a single parameter, word, which is the word
    to get the characters from. It returns the characters as a string after checking if the word has digits and/or
    symbols. 

    Parameters:
        word: The word to get the characters from. 
        :type word: str

    Returns:
        The characters as a string after checking if the word has digits and/or symbols. 
        :rtype: str
    """
    chars = string.ascii_lowercase
    if has_digits(word):
        chars += string.digits
    if has_symbols(word):
        chars += string.punctuation
    return chars


def check_guess(word: str, guess: str, attempts: int) -> str | None:
    """
    Check the guess. 

    This function is used to check if the guess is correct. It takes three parameters: word, guess, and attempts. 
    Word is the word to guess, guess is the guess to check, and attempts is the number of attempts. It returns a string
    if the guess is correct, and None if the guess is incorrect. 

    Parameters:
        word: The word to guess.
        :type word: str

        guess: The guess to check.
        :type guess: str

        attempts: The number of attempts.
        :type attempts: int

    Returns:
        A string if the guess is correct, and None if the guess is incorrect. 
        :rtype: str | None
    """
    if guess == word:
        return f'\n\n"{word}" Cracked in {attempts:,} Attempts!'
    return None


def brute_force(word: str, length: int, attempts: list[int], stop_event: Event, print_lock: Lock, thread_id: int, start_from_end: bool = False, start_from_middle: bool = False, reverse_direction: bool = False) -> str | None:
    """
    Perform the brute force attack. 

    This function is used to perform the brute force attack. It takes several parameters, including the word to guess,
    the length of the word, the list of attempts, the stop event, the print lock, the thread ID, the start from end,
    the start from middle, and the reverse direction. If the start from end parameter is True, the word will be
    scrambled from the end. If the start from middle parameter is True, the word will be scrambled from the middle.
    If the reverse direction parameter is True, the word will be scrambled in reverse direction. The function uses
    itertools.product to generate all possible combinations of characters in the word. 

    The function checks if the stop event is set. If it is, it breaks out of the loop. If the time elapsed since the
    start of the function is greater than the pause interval, it prints a message and pauses for the pause duration.
    If the time elapsed since the start of the function is less than or equal to the pause interval, it prints a
    message without pausing. 

    Parameters:
        word: The word to guess. 
        :type word: str

        length: The length of the word.
        :type length: int

        attempts: The list of attempts. 
        :type attempts: list[int]

        stop_event: The stop event. 
        :type stop_event: Event

        print_lock: The print lock. 
        :type print_lock: Lock

        thread_id: The thread ID. 
        :type thread_id: int

        start_from_end: Determine if the word should be scrambled from the end. 
        :type start_from_end: bool

        start_from_middle: Determine if the word should be scrambled from the middle. 
        :type start_from_middle: bool

        reverse_direction: Determine if the word should be scrambled in reverse direction. 
        :type reverse_direction: bool

    Returns:
        A string if the guess is correct, and None if the guess is incorrect. 
        :rtype: str | None
    """
    chars = get_chars(word)
    if start_from_end:
        chars = chars[::-1]

    if start_from_middle:
        half_length = len(chars) // 2
        if reverse_direction:
            chars = chars[half_length:] + chars[:half_length][::-1]
        else:
            chars = chars[half_length:] + chars[:half_length]

    start_time = time.perf_counter()
    for guess in itertools.product(chars, repeat=length):
        if stop_event.is_set():
            break
        attempts[0] = update_attempts(attempts[0])
        guess_str = ''.join(guess)
        result = check_guess(word, guess_str, attempts[0])
        if result:
            stop_event.set()
            with print_lock:
                print(result)
            return result
        if time.perf_counter() - start_time >= PAUSE_INTERVAL:
            with print_lock:
                print(f'Thread {thread_id}: Trying "{guess_str}", {attempts[0]:,} Attempts')
            time.sleep(PAUSE_DURATION)
            start_time = time.perf_counter()
    return None


def track_time(start_time: float) -> float:
    """
    Calculate the time elapsed. 

    This function is used to calculate the time elapsed. It takes a single parameter, start_time, which is the time
    starting time used to calculate. It returns the elapsed time in seconds using the time.perf_counter() function.

    Parameters:
        start_time: The starting time. 
        :type start_time: float

    Returns:
        The elapsed time in seconds. 
        :rtype: float
    """
    return time.perf_counter() - start_time


def calculate_combinations(chars: str, length: int) -> int:
    """
    Calculate the potential number of combinations. 

    This function calculates the potential number of combinations given the characters and length of the word. It
    uses the formula for permutations with repetition (number of chars ** length).

    Parameters:
        chars: The characters to use.
        :type chars: str

        length: The length of the word.
        :type length: int

    Returns:
        The potential number of combinations.
        :rtype: int
    """
    return len(chars) ** length


def run_brute_force(word: str, length: int, stop_event: Event) -> None:
    """
    Run the brute force attack. 

    This function is used to run the brute force attack. It takes three parameters, word, length, and stop_event. It
    uses the other functions in the module to aid in the brute force attack by generating all possible combinations off
    the characters in the word, calculating the potential number of combinations, triggering multiple threads to
    concurrently run the brute force attack, and checking if the stop event is set. 

    Parameters:
        word: The word to guess. 
        :type word: str

        length: The length of the word. 
        :type length: int

        stop_event: The stop event. 
        :type stop_event: Event

    Returns:
        None
    """
    attempts = [0]
    print_lock = Lock()
    chars = get_chars(word)
    combinations = calculate_combinations(chars, length)
    print(f"Potential Combinations to Try: {combinations:,}")

    threads = [
        Thread(target=brute_force, args=(word, length, attempts, stop_event, print_lock, 1, False, False, False)),
        Thread(target=brute_force, args=(word, length, attempts, stop_event, print_lock, 2, True, False, False)),
        Thread(target=brute_force, args=(word, length, attempts, stop_event, print_lock, 3, False, True, False)),
        Thread(target=brute_force, args=(word, length, attempts, stop_event, print_lock, 4, False, True, True))
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    if not stop_event.is_set():
        with print_lock:
            print(f'Failed to Crack "{word}" in {attempts[0]:,} Attempts')


if __name__ == '__main__':
    print(MESSAGES['welcome'])

    words = get_words()
    scrambled_random_word = scramble_chars(get_random_word(words))
    print(f'Starting Search for: {scrambled_random_word}\nStandby...')
    time.sleep(TIMER_SLEEP)

    start_time = time.perf_counter()
    if common_match := find_match(scrambled_random_word, words):
        print(common_match)
    else:
        stop_event = Event()
        length = get_word_length(scrambled_random_word)
        run_brute_force(scrambled_random_word, length, stop_event)
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time:.2f} Seconds')
