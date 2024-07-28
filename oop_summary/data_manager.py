import json
from objects.pet import Pet
from objects.owner import Owner
from objects.dog import Dog
from objects.cat import Cat


def save_data(owners, pets):
    """
    Save owners and pets data to a JSON file.
    """
    data = {
        "owners": [
            {
                "name": owner.name,
                "phone_number": owner.phone_number,
                "pets": [pet.name for pet in owner.pets]
            } for owner in owners
        ],
        "pets": [
            {
                "name": pet.name,
                "species": pet.species,
                "age": pet.age,
                "owner": pet.owner.name if pet.owner else None,
                "vaccinated": pet.is_vaccinated(),
                "breed": pet.breed if isinstance(pet, Dog) else None,
                "indoor": pet.indoor if isinstance(pet, Cat) else None
            } for pet in pets
        ]
    }

    with open("pet_data.json", "w") as file:
        json.dump(data, file, indent=2)


def load_data():
    """
    Load owners and pets data from a JSON file.
    If the file doesn't exist, return empty lists.
    """
    try:
        with open("pet_data.json", "r") as file:
            data = json.load(file)

        owners = [Owner(o["name"], o["phone_number"]) for o in data["owners"]]

        pets = []
        for p in data["pets"]:
            owner = next((o for o in owners if o.name == p["owner"]), None)
            if p["species"] == "Dog":
                pet = Dog(p["name"], p["age"], owner, p["breed"])
            elif p["species"] == "Cat":
                pet = Cat(p["name"], p["age"], owner, p["indoor"])
            else:
                pet = Pet(p["name"], p["species"], p["age"], owner)
            pet.set_vaccinated(p["vaccinated"])
            pets.append(pet)
            if owner:
                owner.add_pet(pet)

        return owners, pets

    except FileNotFoundError:
        print("No existing data file found. Starting with empty lists.")
        return [], []