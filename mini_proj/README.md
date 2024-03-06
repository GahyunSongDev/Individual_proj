# Individual mini Projects

## Before you start !

1. Ensure you have Python installed on your system.

2. Clone the repository:
   ```bash
   git clone https://github.com/GahyunSongDev/Individual_proj.git


## [1] MBTI Personality Test

Welcome to the MBTI (Myers-Briggs Type Indicator) Personality Test! 
This simple Python script helps you discover your personality type based on four key dimensions: Extraversion/Introversion, Sensing/Intuition, Feeling/Thinking, and Perceiving/Judging.

### Getting Started

- Move to the directory
    ```bash
    cd mini_proj

- Run the script
  ```bash
  python3 mbti_test.py

#### Credits
This MBTI Personality Test is a simple Python implementation inspired by the Myers-Briggs Type Indicator. It was created by Gahyun Song.
Have fun discovering your MBTI!


## [2] UP&DOWN Game

Experience the thrill of the UP&DOWN Number Game! This Python script challenges you to guess the correct number within a specified range.

### Getting Started

- Move to the directory
    ```bash
    cd mini_proj

- Run the script
   ```bash
   python3 updown_num_game.py

#### credits
The UP&DOWN Number Game is a simple Python implementation created by Gahyun Song.

Have fun playing the UP&DOWN Number Game!



## [3] Rock Scissors Paper Game

Get ready for some fun with the Rock Scissors Paper Game! This Python script lets you play the classic game against the computer.

### Getting Started

- Move to the directory
    ```bash
    cd mini_proj

- Run the script
    ```bash
    python3 rock_paper_scissors.py

#### credits
The Rock Scissors Paper Game is a simple Python implementation created by Gahyun Song. 

Enjoy the game and may the best hand win!


## [4] Gold Mining Adventure Game

Embark on an exciting Gold Mining Adventure and navigate through a series of challenges to discover the hidden gold! Follow the correct sequence of directions and make critical decisions to overcome obstacles.

### Getting Started

#### Instructions
1. Enter your name to begin the adventure.

2. Respond to the prompt to decide whether you want to go on the gold mining adventure (YES/NO).

3. Type the direction you want to move in (Right / Left / Up / Down) and follow the path carefully.

4. Make strategic choices when faced with challenges such as rivers and mountains.

5. Reach the final destination with the correct sequence to find the gold.

6. Enjoy the game and see how much gold you can collect!

#### Features
- Engaging storyline with interactive decision-making.
- Dynamic challenges and obstacles to test your strategy.
- Keep track of the gold you've collected along the way.
- Enjoy the thrill of the adventure and the satisfaction of finding gold!

#### How to Run
- Move to the directory
    ```bash
    cd mini_proj

- Run the script
    ```bash
    python3 gold_mining_adventure.py

#### credits
Enjoy the Gold Mining Adventure, and may you strike it rich with gold!

## [5] User Authentication System with Encryption

This is a simple user authentication system implemented in Python, utilizing the cryptography library for password encryption.

### Requirements

- Python 3 
- cryptography library (`pip3 install cryptography`)

### Usage

1. Key Generation : Before running the script, you need to generate a key for encryption/decryption. Uncomment and run the `writeKey()` function in the script to generate the key and save it as `key.key`.
    ```python
    # Uncomment and run this function to generate the key
    # def writeKey():
    #     key = Fernet.generate_key()
    #     with open("key.key", "wb") as key_file:
    #         key_file.write(key)
    # writeKey()

2.  Sign Up : Run the script and choose the "sign up" option. Enter your name, password, and date of birth when prompted. Your information will be encrypted and saved in the `members.txt` file.

3.  Sign In : Choose the "sign in" option, enter your name, password, and date of birth. The script will decrypt the stored password and verify your credentials.

4.  Forget Username/Password : If you forget your username or password, choose the "forget" option. Enter your date of birth to find your username or enter your username and date of birth (comma-separated) to find your password.

### Script Structure

- `writeKey()`: Generates a key for encryption/decryption and saves it as `key.key`.
- `loadKey()`: Loads the key from the `key.key` file.
- `encrypt_info(info)`: Encrypts the provided information using the loaded key.
- `decrypt_info(cipher_info)`: Decrypts the provided encrypted information using the loaded key.
- `signUp()`: Registers a new user by taking their name, password, and date of birth.
- `signIn()`: Authenticates a user by verifying their name, password, and date of birth.
- `forgetName(a)`: Finds and displays the username based on the provided date of birth.
- `forgetPwd(b)`: Finds and displays the decrypted password based on the provided username and date of birth.

### Notes

- Ensure you have the cryptography library installed before running the script (`pip3 install cryptography`).
- It is crucial to keep the `key.key` file secure, as it is used for encryption and decryption.

## [6] Dice Rolling Game

### Introduction

This Python script implements a simple dice rolling game where players take turns rolling a six-sided die to accumulate scores. The goal is to reach a randomly determined winning score before the other players.

### Getting Started

#### Usage
- Run the script 
  ```bash
  python3 dice_rolling_game.py

#### Game Rules
-   The number of players is determined at the beginning of the game (2 to 4 players).
-   Each player takes turns rolling a six-sided die.
-   Rolling a 1 resets the player's score to 0.
-   The game continues until one player reaches a randomly determined winning score.

#### Main Game Loop
1. Input validation for the number of players.
2. Set a random winning score for the round.
3. Initialize scores for each player.
4. Main game loop iterating through each player's turn.
5. Display the current scores and check for a winner.

## [7] Mad Libs Generator

### Introduction
This Python script allows you to create a Mad Libs story by replacing placeholders in a given story template. The user is prompted to input words to fill in the placeholders, resulting in a customized and often humorous narrative.

### Getting Started

#### Usage
- Run the script 
  ```bash
  python3 madlibs_generator.py

### How to use
-   Story Template: Prepare a text file (before_story.txt) with placeholders enclosed in square brackets, such as [Adjective], [Noun], or [Verb].

-   Run the Script: Execute the Python script (madlibs_generator.py). The script reads the story template and identifies the placeholders.- 

-   User Input: Enter words to replace each placeholder when prompted. The script uses an OrderedDict to maintain the order of placeholders and removes duplicates.

-   Generated Story: The script generates a new story by replacing the placeholders with the user-input words. The updated story is displayed, and it's saved to a file (story_replaced.txt).




## [8] Math Challenge Game

### Introduction

A simple Python console-based math challenge game that tests your arithmetic skills. The game randomly generates math problems with addition, subtraction, and multiplication operations.

#### How to Play

1. Run the script in a Python environment.
2. Choose to start the math challenge by entering 'y' when prompted.
3. Solve the math problems presented to you.
4. For each problem, input your answer.
5. The game will provide feedback on whether your answer is correct or not.
6. Complete all the problems to finish the challenge.
7. The total time taken, number of incorrect answers, and your score will be displayed at the end.

#### Features

- Randomly generated math problems.
- Adjustable difficulty by changing the range of numbers.
- Timer to track the total time taken to complete the challenge

## [9] Slot Machine Game

### Introduction

This is a simple text-based slot machine game implemented in Python.

#### Overview

The Slot Machine game consists of the following components:

- **Slotmachine Class**: Defines the slot machine with methods for spinning the reels and calculating payouts.

- **Main Program (main())**: Implements the main game loop, allowing the player to deposit money, place bets, spin the slot machine, and see the results.

#### How to Play

1. Run the `slot_machine.py` script using a Python interpreter.

2. Upon starting, you will be prompted to deposit money. Type the amount you want to deposit (type 'q' to quit).

3. Choose the amount you want to bet for the current game: $5, $50, or $100.
    -> If you bet $100 and win, you earn x3 to the winning money.
    -> If you bet $50 and win, you earn x2 times to the winning money.
    -> If you bet $5 and win, you earn x1 times to the winning money.

4. The slot machine will spin, and the result will be displayed.

5. If you win, your balance will be updated accordingly.

6. Continue playing or quit as desired.

#### Game Rules

- **Jackpot**: If all three reels show the same item, you win $100 times the bet amount.

- **Two of a Kind**: If two reels show the same item, you win $20 times the bet amount.

- **No Win**: If there is no match, no money is won.