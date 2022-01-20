from standard_messages import *
from person_data_capture import *
from person_validator import *

def main():
    welcome_message()

    user = capture_person_data()

    if not validate_person(user):
        end_application()
        return

    # Create a username for the person
    print(f"Your username is {user.first_name[0]}{user.last_name}")
    end_application()

if __name__ == "__main__":
    main()
