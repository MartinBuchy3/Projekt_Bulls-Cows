"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Buchal
email: buchalM@seznam.cz
discord: Martin_Buchy
"""

import random
import time

separator = 40 * "-"

def generate_secret_number():
    """
    Generates a four-digit secret number with unique digits that doesn't start with 0.
    """
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        for i in range(1, 10):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(map(str, digits[:4]))

def get_bulls_and_cows(guess, secret):
    """
    Calculates the number of 'bulls' and 'cows' for the player's guess.
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1 
        elif guess[i] in secret:
            cows += 1

    return bulls, cows

def valid_guess(guess):
    """
    Checks if the guess is a valid four-digit number with unique digits and no leading zero.
    """
    if not guess.isdigit():
        print("Invalid input! Please enter a four-digit number.")
        return False
    if len(guess) != 4:
        print("Invalid input! Please enter a four-digit number.")
        return False
    if len(set(guess)) != 4:
        print("Invalid input! Please enter a number with unique digits.")
        return False
    if guess[0] == '0':
        print("Invalid input! The number should not start with 0.")
        return False
    return True

def evaluate_performance(attempts):
    """
    Evaluates the player's performance based on the number of attempts.
    """
    if attempts <= 5:
        return "Great job!"
    elif attempts <= 10:
        return "That's a decent try!"
    else:
        return "Well, you can surely do better.."
    
def bulls_and_cows_game():
    """
    Main game loop for Bulls and Cows.
    """
    print(  f"{separator}\nHi there!\n{separator}\n"
            f"I've generated a random 4 digit number for you.\nLet's play a bulls and cows game."
            f"\n{separator}"
            f"\nRULES:\n -'bulls' indicates the number of correct digits in the correct position"
            f"\n -'cows' indicates the number of correct digits in the wrong position"
            f"\n - To quit the game, type 'quit'."
            f"\n{separator}"
        )

    # Timer
    start_time = time.time()
    secret_number = generate_secret_number()
    attempts = 0
    
    while True:
        guess = input(f"\nEnter your guess (or type 'quit' to exit):\n").strip()
        print(separator)

        # Quit option for player
        if guess.lower() == 'quit':
            print("\nGame has been quit. Thanks for playing!")
            return
        
        # Check for validity of player's guess
        if not valid_guess(guess):
            continue
        
        attempts += 1
        bulls, cows = get_bulls_and_cows(guess, secret_number)

        # Singular or plural for bull and cow
        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"

        # Display of player's guess
        print(f">>> {guess}")
        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        print(separator)

        # Check if the player has guessed the secret number
        if bulls == 4:
            # End time and calculates player's time
            end_time = time.time()
            time_spent = end_time - start_time
            minutes, seconds = divmod(time_spent, 60)

            print(f"\nCongratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            print(f"You completed the game in {int(minutes)} minutes and {int(seconds)} seconds.")

            # Player's performance
            performance = evaluate_performance(attempts)
            print(performance)
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    bulls_and_cows_game()