#helper functions

def get_valid_integer():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_choice(valid_choices):
    while True:
        try:
            choice = int(input("Select an option: "))
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Please enter one of {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

