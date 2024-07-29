from oop_summary.objects.pet import Pet

class Dog(Pet):
    """
    Represents a dog, which is a specific type of pet.
    """

    def __init__(self, name, age, breed, owner=None):
        """
        Initialize a new Dog instance.
        """
        super().__init__(name, "Dog", age, owner)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def __str__(self):
        """Return a string representation of the dog."""
        return f"{self._name} the {self._breed} Dog, {self._age} years old"