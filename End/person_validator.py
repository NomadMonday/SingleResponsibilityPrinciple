def validate_person(person):
    """Checks to be sure the first and last names are valid."""

    if not person.first_name.strip():
        print("You did not give us a valid first name!")
        return False

    if not person.last_name.strip():
        print("You did not give us a valid last name!")
        return False
    
    return True
