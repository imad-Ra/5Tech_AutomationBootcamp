import logging

from oop_summary.object_oriented_programing.pet_management_system.src.classes.pet import Pet


class Dog(Pet):
    def __init__(self, breed):
        super().__init__(self.name, self.species, self.age, self.owner, self._vaccinated)
        self.breed = breed

    @property
    def breed(self):
        return self.breed

    @breed.setter
    def breed(self, value):
        self.breed = value

    def __str__(self):
        try:
            logging.info("Listing dog details")
            return f'Dog: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}, {self.breed}'
        except Exception as e:
            logging.error(f"Error listing dog details: {e}")

