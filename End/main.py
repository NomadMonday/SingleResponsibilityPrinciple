from standard_messages import welcome_message, end_application
from person_data_capture import capture_person_data
from person_validator import validate_person
from account_generator import create_account

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
