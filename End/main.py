from standard_messages import *
from person_data_capture import *
from person_validator import *
from account_generator import *

def main():
    welcome_message()

    user = capture_person_data()

    if not validate_person(user):
        end_application()
        return

    create_account(user)
    
    end_application()

if __name__ == "__main__":
    main()
