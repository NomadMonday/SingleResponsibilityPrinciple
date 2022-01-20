from person import Person

def capture_person_data():
    """Asks for user information and returns a Person object."""

    user = Person()
    user.first_name = input("What is your first name: ")
    user.last_name = input("What is your last name: ")

    return user