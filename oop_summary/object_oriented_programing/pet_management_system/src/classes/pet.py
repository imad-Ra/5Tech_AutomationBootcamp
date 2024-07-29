import logging

from oop_summary.object_oriented_programing.pet_management_system.src.classes.owner import Owner
from oop_summary.object_oriented_programing.pet_management_system.src.utilities.config_provider import ConfigProvider


class Pet:

    def __init__(self, name, species, age, owner: Owner, vaccinated):
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self._vaccinated = vaccinated
        self._config_path = r"C:\Users\nraba\PycharmProjects\Tzahi Lessons\5Tech_AutomationBootcamp\oop_summary\object_oriented_programing\pet_management_system\pet_store.json"
        self._config = ConfigProvider().load_from_file(self._config_path)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, value):
        self._vaccinated = value

    def __str__(self):
        try:
            logging.info("listing pet details")
            return f'Pet: {self.name}, {self.species}, {self.age}, {self.owner}, {self._vaccinated}'
        except Exception as e:
            logging.error(f"Error listing pet details: {e}")

    def __eq__(self, other):
        try:
            logging.info("Checking if pets ar equal.")
            if self.name == other.name and self.species == other.species:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f'Error checking if pets are equal: {e}')

    def total_pets_count(self):
        try:
            logging.info("Counting total pets")
            total_pets = len(self._config['pets'])
            return total_pets
        except Exception as e:
            logging.error(f"Error counting total pets: {e}")

    def check_pet_is_vaccinated(self):
        try:
            logging.info("Checking pet is vaccinated")
            if self._vaccinated:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"Error checking pet is vaccinated: {e}")

    def set_pet_vaccinated(self):
        try:
            logging.info("Setting pet as vaccinated")
            self._vaccinated = True
        except Exception as e:
            logging.error(f"Error setting pet as vaccinated: {e}")

    def age_retrieve(self):
        try:
            logging.info("Retrieving pet age")
            return self.age * 7
        except Exception as e:
            logging.error(f"Error retrieving pet age: {e}")

    def pet_to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "owner": self.owner,
            "vaccinated": self.vaccinated
        }


pet_1 = Pet('saun', 'dog', 5, 'Luis', True)
pet_2 = Pet('rex', 'dog', 9, 'Amos', False)
pet_3 = Pet('meow', 'cat', 10, 'James', True)

print(pet_1 == pet_2)
print(pet_3 == pet_1)

pet_2.set_pet_vaccinated()
print(pet_2)

print(pet_1.check_pet_is_vaccinated())
print(pet_2.check_pet_is_vaccinated())
print(pet_3.check_pet_is_vaccinated())

print(pet_1.age_retrieve())
print(pet_2.age_retrieve())
print(pet_3.age_retrieve())
