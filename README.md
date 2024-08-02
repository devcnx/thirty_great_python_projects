<small style="text-align: justify;">

# 30 Great Python Projects To Help You Master It In 2024

This repository contains projects from the Udemy course "30 Great Python Projects to Help You Master It In 2024". Each project is designed to help you master different aspects of Python programming. 

## Table of Contents

1. [Project 1: Mad Libs Game](#project-1-mad-libs-game)
2. [Project 2: Number Guessing Game](#project-2-number-guessing-game)
3. [Project 3: Dice Simulator](#project-3-dice-simulator)
4. [Project 4: Hangman Game](#project-4-hangman-game)
5. [Project 5: Rock, Paper, Scissors Game](#project-5-rock-paper-scissors-game)
6. [Project 6: Password Generator](#project-6-password-generator)
7. [Project 7: QR Code Generator](#project-7-qr-code-generator)
8. [Project 8: Website Checker](#project-8-website-checker)
9. [Project 9: Password Checker](#project-9-password-checker)
10. [Project 10: Brute Force](#project-10-brute-force)
11. [Project 11: Image Downloader](#project-11-image-downloader)
12. [Project 12: TBD](#project-12-tbd)
13. [Project 13: TBD](#project-13-tbd)
14. [Project 14: TBD](#project-14-tbd)
15. [Project 15: TBD](#project-15-tbd)
16. [Project 16: TBD](#project-16-tbd)
17. [Project 17: TBD](#project-17-tbd)
18. [Project 18: TBD](#project-18-tbd)
19. [Project 19: TBD](#project-19-tbd)
20. [Project 20: TBD](#project-20-tbd)
21. [Project 21: TBD](#project-21-tbd)
22. [Project 22: TBD](#project-22-tbd)
23. [Project 23: TBD](#project-23-tbd)
24. [Project 24: TBD](#project-24-tbd)
25. [Project 25: TBD](#project-25-tbd)
26. [Project 26: TBD](#project-26-tbd)
27. [Project 27: TBD](#project-27-tbd)
28. [Project 28: TBD](#project-28-tbd)
29. [Project 29: TBD](#project-29-tbd)
30. [Project 30: TBD](#project-30-tbd)


## Project 1: Mad Libs Game
[Back to Top](#table-of-contents)

### Description

The Mad Libs game is an interactive game that challenges players to provide various types of words
(nouns, verbs, adjectives, etc.) to complete a story template. The game uses these words to generate
a humorous and nonsensical story.

The game begins by displaying a series of prompts to the user, asking for specific types of words. 
After collecting all the necessary words, the game substitutes them into a pre-defined story 
template, creating a unique and (sometimes) funny story based on the user's input.


**Key Learning Points**
- Handling user inputs dynamically. 
- Using string formatting techniques to insert user inputs into a template. 
- Basic game flow and logic. 

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/mad_libs
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter various types of words (nouns, verbs, adjectives, etc.). 
The game will display a story using the words you provided. 

**Completed on**: Sunday, July 14th, 2024  

## Project 2: Number Guessing Game
[Back to Top](#table-of-contents)

### Description

The Number Guessing Game is a simple game where the player tries to guess a randomly generated number
between a specified range (1 to 100). The player is given feedback on whether their guess is too high, 
too low, or correct. The game continues until the player guesses the correct number or exhausts the
maximum number of guesses. 

The game also includes features to handle invalid inputs and provides and option for the player to 
play again after each game session. 

**Key Learning Points**
- Implementing input validation. 
- Using random number generation.
- Handling game flow and logic for a guessing game.

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/number_guess
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter your guesses. The game will provide feedback after each guess
and indicate whether the guess was too high, too low, or correct. 

**Completed on**: Sunday, July 14th, 2024  

## Project 3: Dice Simulator
[Back to Top](#table-of-contents)

### Description

The Dice Simulator allows the user to roll a specified number of dice and get random results for each roll. For each roll,
the total (sum) of the dice are displayed to the user. This simulation mimics the rolls of physical dice, providing
practice working with random numbers and user input.

**Key Learning Points**
- Generating random numbers.
- Handling user inputs and validation.
- Creating a loop for continuous user interaction.

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/dice_simulator
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter the number of dice to roll. The game will display the results of the dice
rolls, and the total (sum) of the rolls. Type 'exit' to quit the game.

**Completed on**: Monday, July 15th, 2024 

## Project 4: Hangman Game
[Back to Top](#table-of-contents)

### Description

The Hangman game is a classic word-guessing game where the player tries to guess the letters of a randomly selected
word. The player has a limited number of attempts to guess the word correctly. The game displays the word with
underscores representing the letters that have not been guessed yet. The player wins if they guess all the letters
in the word before running out of attempts and loses if they run out of attempts before guessing the word. 

The game provides feedback after each guess, indicating whether the guessed letter is correct or incorrect. Correct
guesses reveal the position of the letter in the word, while incorrect guesses reduce the number of attempts 
remaining. The game ends when the player wins or loses, and the final result is displayed. The player can choose
to play again or exit the game.

**Key Learning Points**
- Implementing word-guessing game logic. 
- Handling user inputs and validation. 
- Managing game state and user feedback.

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/hangman
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to guess the letters of the word. The game will provide feedback after
each guess, indicating whether the letter is correct or incorrect. The player can choose to play again
after each game session.

**Completed on**: Monday, July 15th, 2024

## Project 5: Rock, Paper, Scissors Game
[Back to Top](#table-of-contents)

### Description

The Rock, Paper, Scissors game is a classic hand game played between two people. The player competes against the computer by choosing one of the three options: Rock, Paper, or Scissors. The computer also randomly selects one of the three choices. The winner is determined based on the following rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

The game provides feedback on the outcome of each round and allows the player to play multiple rounds.

**Key Learning Points**
- Implementing game logic for Rock, Paper, Scissors.
- Handling user inputs and validation.
- Generating random choices for the computer.

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/password_generator
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter the number of passwords you want to generate. The application will
display the generated passwords after ensuring they are valid. The user can choose to generate more passwords
or exit the application. 

**Completed on**: Wednesday, July 17th, 2024 

## Project 6: Password Generator
[Back to Top](#table-of-contents)

### Description

The Password Generator module generates random passwords for the user. It allows the user to generate between (1) and (5)
passwords at a time, with each password being between (8) and (15) characters. The module ensures that the generated passwords
contain a mix of uppercase letters, lowercase letters, numbers, and special characters. 

**Key Learning Points**
- Generating random passwords with a mix of character types.
- Validating user input for the number of passwords and their length. 
- Ensuring validated passwords meet common security requirements. 

### Technologies
- Python

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/rock_paper_scissors
    ```
2. Install required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter your choice of Rock, Paper, or Scissors. The game will display the computer's choice and the result of each round. The player can choose to play again after each round.

**Completed on**: Wednesday, July 17th, 2024 

## Project 7: QR Code Generator
[Back to Top](#table-of-contents)

### Description

The QR Code Generator application allows users to generate QR codes for any input text or URL.
The generated QR codes can be saved as image files (PNG) for later use. This project demonstrates
how to work with external libraries in Python to create and manipulate images.

**Key Learning Points**
- Generating QR codes using Python libraries. 
- Handling user inputs and validations. 
- Saving generated QR codes as image files. 

### Technologies
- Python
- qrcode (Python library)
- Pillow (Python Imaging Library)

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/qr_code_generator
    ```
2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
Follow the on-screen instructions to enter the text or URL you want to generate a QR code for. 
The application will displayed the generated QR code and save it as an image file. 

**Completed on**: Sunday, July 21st, 2024

## Project 8: Website Checker
[Back to Top](#table-of-contents)

### Description

The Website Checker application allows users to check the status of websites. The user can enter a
list of websites in a CSV file, and the website checker will check the status of each website and
print the results to the console. This project demonstrates how to work with external libraries
in Python to: create and manipulate files, read and write CSV files, and send HTTP requests. 

**Key Learning Points**
- Checking website status using Python libraries. 
- Reading from CSV files. 
- Sending HTTP requests. 

### Technologies
- Python
- csv (Python Library)
- os (Python Library)
- requests (Python Library)
- fake_useragent (Python Library)
- http (Python Library)

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/website_checker
    ```
2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
(If applicable) Enter the list of websites in a CSV file. The website checker will check the status
of each website and print the results to the console. 

**Completed on**: Sunday, July 21st, 2024

## Project 9: Password Checker
[Back to Top](#table-of-contents)

### Description

The Password Checker application allows users to check if their password is considered a common
password. The user can enter a password and the application will tell the user if the password is
considered common based on if it's located in a list of common passwords. This project demonstrates
working with reading files (.txt) in Python and working with user inputs and validations. 

**Key Learning Points**
- Checking if a password is common against a list of common passwords. 
- Handling user inputs and validations.
- Reading from files.

### Technologies
- Python
- os (Python Library)


### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/password_checker
    ```
2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
The user is prompted to enter their password. The application will tell the user if the password is
considered common based on if it's located in a list of common passwords. The user has the ability
to continue checking passwords until they want to exit the application.

**Completed on**: Monday, July 22nd, 2024

## Project 10: Brute Force
[Back to Top](#table-of-contents)

### Description

The Brute Force application is used to crack passwords. This application is for educational purposes only. The project demonstrates working with reading files (.txt), working with the itertools library, and threads to run the application in parallel. 

**Key Learning Points**
- Generating all possible combinations of characters using the itertools library. 
- Scrambling characters to generate random words. 
- Checking for common matches in a list of words. 
- Implementing brute force login to crack passwords. 
- Using threading to run multiple brute force attempts in parallel. 
- Calculating potential number of combinations for tracking progress. 

### Technologies
- Python
- itertools (Python Library)
- threading (Python Library)

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/brute_force
    ```
2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
The application selects a random word from a list of words. It scrambles the word and then checks for
common matches. It performs brute force attacks until it finds the correct password. There is no
user input for the console application. 

**Completed on**: Sunday, July 28th, 2024

## Project 11: Image Downloader
[Back to Top](#table-of-contents)

### Description

The Image Downloader application is used to download images. The project demonstrates how to
work with the requests library and validate user inputs (image URLs). 

**Key Learning Points**
- Making HTTP GET requests. 
- Handling user inputs and validations. 
- Saving downloaded images to a directory.

### Technologies
- Python
- requests (Python Library)

### Installation 
1. Clone the repository
    ```sh
    git clone https://github.com/devcnx/thirty_great_python_projects.git
    cd thirty_great_python_projects/image_downloader
    ```
2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the project:
    ```sh
    python3 main.py
    ```

### Usage
The user is prompted to enter a URL for an image. The application checks if the URL is valid by
making sure it starts with 'http://' or 'https://', and that it contains a valid image file type
('.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'). If the URL is valid, the application
downloads it and saves it to a specified directory. 

TODO: Update application to validate that the directory exists. 

**Completed on**: Friday, August 2nd, 2024

More projects from "30 Great Python Projects to Help You Master It In 2024" (Udemy) will be added as they are completed. 

</small>
