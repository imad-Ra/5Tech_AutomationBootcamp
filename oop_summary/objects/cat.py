from oop_summary.objects.pet import Pet

class Cat(Pet):
    """
    Represents a cat, which is a specific type of pet.
    """

    def __init__(self, name, age, indoor, owner=None):
        """
        Initialize a new Cat instance.
        """
        super().__init__(name, "Cat", age, owner)
        self._indoor = indoor

    def is_indoor(self):
        """Check if the cat is an indoor cat."""
        return self._indoor

    def set_indoor(self, indoor):
        """Set whether the cat is an indoor cat."""
        self._indoor = indoor

    def __str__(self):
        """Return a string representation of the cat."""
        indoor_status = "indoor" if self._indoor else "outdoor"
        return f"{self._name} the {indoor_status} Cat, {self._age} years old"