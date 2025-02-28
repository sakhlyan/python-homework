# Exercise:
# This program asks the user to input a number and determines if the number is even or odd.
# If the user inputs 0, the program exits the loop. It uses the modulus operator (%) to check
# if the number is divisible by 2, which defines whether the number is even or odd.
# The program also includes error handling to ensure that only valid integers are processed.

from helpers import get_valid_integer

def check_even_odd():
    while True:
        num = get_valid_integer()
        if num == 0:
            print("Exiting...")
            break
        elif num % 2 == 0:
            print(f"{num} is even.\n")
        else:
            print(f"{num} is odd.\n")


if __name__ == "__main__":
    print("Type 0 to exit, or any number to check if it's odd.")
    check_even_odd()
