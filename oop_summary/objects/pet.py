class Pet:
    """
    Represents a pet in the pet management system.
    """

    def __init__(self, name, species, age, owner=None):

        self._name = name
        self._species = species
        self._age = age
        self._owner = owner
        self._vaccinated = False

    # Getters
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def get_owner(self):
        return self._owner

    # Setters
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_owner(self, owner):
        self._owner = owner

    def is_vaccinated(self):
        return self._vaccinated

    def vaccinate(self):

        self._vaccinated = True

    def __str__(self):
        return f"{self._name} the {self._species}, {self._age} years old"