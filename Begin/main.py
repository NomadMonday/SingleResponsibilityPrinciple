from person import Person

def main():
    print("Welcome to my application!")

    # Ask for user information
    user = Person()
    user.first_name = input("What is your first name: ")
    user.last_name = input("What is your last name: ")

    # Checks to be sure the first and last names are valid
    if not user.first_name.strip():
        print("You did not give us a valid first name!")
        input()
        return

    if not user.last_name.strip():
        print("You did not give us a valid last name!")
        input()
        return

    # Create a username for the person
    print(f"Your username is {user.first_name[0]}{user.last_name}")
    input()

if __name__ == "__main__":
    main()
