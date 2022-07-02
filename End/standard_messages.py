def welcome_message() -> None:
    print("Welcome to my application!")

def end_application() -> None:
    input("Press enter to close...")

def display_validation_error(field_name: str) -> None:
    print(f"You did not give us a valid {field_name}!")
