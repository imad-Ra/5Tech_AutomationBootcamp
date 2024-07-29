import logging

from oop_summary.object_oriented_programing.pet_management_system.src.classes.pet import Pet


class Cat(Pet):

    def __init__(self, indoor):
        super().__init__(self.name, self.species, self.age, self.owner, self._vaccinated)
        self.indoor = indoor

    @property
    def indoor(self):
        return self.indoor

    @indoor.setter
    def indoor(self, value):
        self.indoor = value

    def __str__(self):
        try:
            logging.info("Listing all pets in the store.")
            return f'Cat: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}, {self.indoor}'
        except Exception as e:
            logging.error(f"Error listing pets: {e}")


