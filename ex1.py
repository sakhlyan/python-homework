# Exercise:
# Write a program that repeatedly prompts the user to choose between two options:
# 1. If the user selects 1, they should be able to input a number, and the program will continue prompting for another choice.
# 2. If the user selects 2, the program will stop the loop and display the sum of all previously inputted numbers.

from helpers import get_user_choice

MAX_LIMIT = 1e10

def format_number(n):
    return int(n) if n == int(n) else n

def get_valid_number():
    while True:
        try:
            num = float(input("Number: "))
            if abs(num) > MAX_LIMIT:
                print(f"Too large! Enter a number smaller than {MAX_LIMIT}.")
                continue
            print(f"Number: {format_number(num)}")
            return num
        except ValueError:
            print("Bad input. Enter a valid number.")

def sum_inputs():
    total = 0
    while True:
        print("Select an option:\n1 - Add Number\n2 - Finish")
        option = get_user_choice({1,2})
        if option == 1:
            num = get_valid_number()
            total += num
            print(f"Added: {format_number(num)}, Sum: {format_number(total)}\n")
        else:
            print("Finalizing...\n")
            return total


def display_result(final_sum):
    print(f"Total sum: {format_number(final_sum)}")


if __name__ == "__main__":
    display_result(sum_inputs())
