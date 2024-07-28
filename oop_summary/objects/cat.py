from oop_summary.objects.pet import Pet

class Cat(Pet):
    """
    Represents a cat in the pet management system.
    """

    def __init__(self, name, age, owner, indoor):
        """
        Initialize a new Cat instance.
        """
        super().__init__(name, "Cat", age, owner)
        self.indoor = indoor

    def __str__(self):
        """Return a string representation of the cat, including whether it's indoor or outdoor."""
        indoor_status = "indoor" if self.indoor else "outdoor"
        return f"{self.name} the {indoor_status} Cat"