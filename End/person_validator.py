from standard_messages import display_validation_error

def validate_person(person):
    """Checks to be sure the first and last names are valid."""

    if not person.first_name.strip():
        display_validation_error("first name")
        return False

    if not person.last_name.strip():
        display_validation_error("last name")
        return False
    
    return True
