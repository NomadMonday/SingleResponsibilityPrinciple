from person import Person

def main():
    print("Welcome to my application!")

    # Ask for user information
    user = Person()
    user.first_name = input("What is your first name: ")
    user.last_name = input("What is your last name: ")

    # Checks to be sure the first and last names are valid
    if not user.first_name.strip():
        input("You did not give us a valid first name!")
        return

    if not user.last_name.strip():
        input("You did not give us a valid last name!")
        return

    # Create a username for the person
    input(f"Your username is {user.first_name[0]}{user.last_name}")

if __name__ == "__main__":
    main()
