from standard_messages import *
from person_data_capture import *

def main():
    welcome_message()

    user = capture_person_data()

    # Checks to be sure the first and last names are valid
    if not user.first_name.strip():
        print("You did not give us a valid first name!")
        end_application()
        return

    if not user.last_name.strip():
        print("You did not give us a valid last name!")
        end_application()
        return

    # Create a username for the person
    print(f"Your username is {user.first_name[0]}{user.last_name}")
    end_application()

if __name__ == "__main__":
    main()
