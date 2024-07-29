class Owner:
    """
    Represents an owner in the pet management system.
    """

    def __init__(self, name, phone):
        """
        Initialize a new Owner instance.

        """
        self._name = name
        self._phone = phone
        self._pets = []

    # Getters
    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_pets(self):
        return self._pets

    # Setters
    def set_name(self, name):
        self._name = name

    def set_phone(self, phone):
        self._phone = phone

    def add_pet(self, pet):
        """
        Add a pet to the owner's list of pets.
        """
        self._pets.append(pet)
        pet.set_owner(self)

    def __str__(self):
        """Return a string representation of the owner."""
        return f"{self._name} (Phone: {self._phone})"