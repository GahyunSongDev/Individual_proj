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

Run the main script to start the dice rolling game.
    ```bash
    cd rolling_dice_gmae.py

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