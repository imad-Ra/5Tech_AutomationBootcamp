from oop_summary.objects.pet import Pet

class Dog(Pet):
    """
    Represents a dog in the pet management system.
    """

    def __init__(self, name, age, owner, breed):
        """
        Initialize a new Dog instance.
        """
        super().__init__(name, "Dog", age, owner)
        self.breed = breed

    def __str__(self):
        """Return a string representation of the dog, including its breed."""
        return f"{self.name} the {self.breed} Dog"