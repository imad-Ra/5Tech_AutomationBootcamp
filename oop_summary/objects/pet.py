class Pet:
    """
    Represents a generic pet in the pet management system.
    """

    total_pets = 0

    def __init__(self, name, species, age, owner):
        """
        Initialize a new Pet instance.
        """
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self.__vaccinated = False
        Pet.total_pets += 1

    def __str__(self):
        """Return a string representation of the pet."""
        return f"{self.name} the {self.species}"

    def is_vaccinated(self):
        """Check if the pet is vaccinated."""
        return self.__vaccinated

    def set_vaccinated(self, status):
        """
        Set the vaccination status of the pet.

        :param status: Boolean indicating vaccination status
        """
        self.__vaccinated = status

    def age_in_human_years(self):
        """Convert pet age to human years."""
        return self.age * 7

    def __eq__(self, other):
        """
        Compare two pets based on name and species.

        :param other: Another Pet object to compare with
        :return: True if pets are equal, False otherwise
        """
        if isinstance(other, Pet):
            return self.name == other.name and self.species == other.species
        return False

    @classmethod
    def get_total_pets(cls):
        """Get the total number of pets created."""
        return cls.total_pets