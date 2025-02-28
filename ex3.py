#Exercise: 3
#A simple calculator program that performs basic arithmetic operations:
#addition, subtraction, multiplication, and division. 
#The user selects an operation from a menu, inputs two numbers, and 
#the program outputs the result of the chosen operation. 
#If the user selects 5, the program exits. It includes error handling 
#to manage invalid inputs and prevents division by zero.

from helpers import get_valid_integer, get_user_choice

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b


def calculator():
    operations = {
        1: ("Addition", add),
        2: ("Subtraction", subtract),
        3: ("Multiplication", multiply),
        4: ("Division", divide),
    }

    while True:
        print("\nCalculator Menu:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = get_user_choice(set(operations.keys()) | {5})

        if choice == 5:
            print("Exiting calculator.")
            break

        print("Enter two numbers:")
        num1 = get_valid_integer()
        num2 = get_valid_integer()

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)

        if result is not None:
            print(f"{operation_name} Result: {result}")


if __name__ == "__main__":
    calculator()
