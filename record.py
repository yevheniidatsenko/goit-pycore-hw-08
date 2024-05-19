from phone import Phone
from name import Name
from birthday import Birthday


class Record:
    """Represents a contact record containing a name and a list of phone numbers."""

    def __init__(self, name: str):
        """Initialize the Record with a name and an empty list of phones."""
        self.name = Name(name)
        self.phones = []

    def __str__(self) -> str:
        """Return a string representation of the Record."""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, number: str):
        """Add a phone number to the record."""
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        """Remove a phone number from the record."""
        self.phones = [phone for phone in self.phones if phone.value != number]

    def edit_phone(self, old_number: str, new_number: str):
        """Edit a phone number in the record."""
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                break

    def find_phone(self, number: str) -> Phone:
        """Find a phone number in the record."""
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None
    
    def add_birthday(self, date):
        self.birthday = Birthday(date)