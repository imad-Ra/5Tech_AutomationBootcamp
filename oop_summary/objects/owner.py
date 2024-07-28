class Owner:
    """
    Represents an owner in the pet management system.
    """

    def __init__(self, name, phone_number):
        """
        Initialize a new Owner instance.
        """
        self.name = name
        self.phone_number = phone_number
        self.pets = []

    def add_pet(self, pet):
        """
        Add a pet to the owner's list of pets.

        :param pet: The Pet object to add
        """
        self.pets.append(pet)

    def remove_pet(self, pet):
        """
        Remove a pet from the owner's list of pets.

        :param pet: The Pet object to remove
        """
        if pet in self.pets:
            self.pets.remove(pet)

    def __str__(self):
        """Return a string representation of the owner, including their pets."""
        pet_names = ", ".join([pet.name for pet in self.pets])
        return f"{self.name} (Phone: {self.phone_number}) - Pets: {pet_names}"