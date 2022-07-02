from person import Person

def create_account(person: Person) -> None:
    """Creates a username for the person."""

    print(f"Your username is {person.first_name[0]}{person.last_name}")
