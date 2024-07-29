import json
import logging

from oop_summary.object_oriented_programing.pet_management_system.src.classes.owner import Owner
from oop_summary.object_oriented_programing.pet_management_system.src.classes.pet import Pet


class Main:
    def __init__(self):
        pass

    @staticmethod
    def pet_to_dict(pet: Pet):
        return {
            "name": pet.name,
            "species": pet.species,
            "age": pet.age,
            "owner": pet.owner,
            "vaccinated": pet.vaccinated
        }

    @staticmethod
    def owner_to_dict(owner: Owner):
        # owner = Owner(owner.name, owner.phone, owner.pets)
        return {
            "name": owner.name,
            "phone": owner.phone,
            "pets": [pet.pet_to_dict() for pet in owner.pets]
        }

    @staticmethod
    def add_owner(self):
        try:
            logging.info("Adding new owner")
            self._config["owners"].append(self.owner_to_dict(self))
            with open(self._config_path, 'w') as file:
                json.dump(self._config, file, indent=1)
                logging.info(f"Owner was added and data saved to json")
        except Exception as e:
            logging.error(f"Error adding and saving owner: {e}")


if __name__ == "__main__":
    pet_1 = Pet('rex', 'dog', 5, 'john', True)
    pet_2 = Pet('boby', 'dog', 9, 'john', False)
    pet_3 = Pet('meow', 'cat', 10, 'mark', True)
    owner_1 = Owner('john', '0523362356', (pet_1, pet_2))
    owner_2 = Owner('mark', '0542253236', (pet_3, pet_2))
    owner_2.add_owner()
    owner_1.add_owner()
    print(owner_1)
    print(owner_2)

