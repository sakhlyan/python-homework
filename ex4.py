# A number guessing game where the program generates a random number between 1 and 10,  
# and the user has to guess what the number is. After each guess, the program provides  
# hints like "Too high" or "Too low" to help the user. The game continues until the  
# user correctly guesses the number. Once guessed, it displays the number of attempts  
# taken. The program also includes error handling to ensure that only valid integers  
# are entered.  

import random
from helpers import get_valid_integer

def get_valid_guess():
    while True:
        try:
            guess = get_valid_integer()
            if 1 <= guess <= 10:
                return guess
            print("Out of range! Enter a number between 1 and 10.") 
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def game():
    num, attempts = random.randint(1, 10), 0
    print("Guess the number I'm thinking of! (between 1 and 10)")

    while (guess := get_valid_guess()) != num:
        print("Too high" if guess > num else "Too low")
        attempts += 1  

    print(f"You guessed it! It's {num} in {attempts + 1} tries!") 

if __name__ == "__main__":
    game()

