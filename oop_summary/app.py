# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for

# Import our custom classes
from pet import Pet
from owner import Owner
from dog import Dog
from cat import Cat

# Import data management functions
from data_manager import load_data, save_data

# Initialize Flask application
app = Flask(__name__)

# Load initial data
owners, pets = load_data()


# Route for home page
@app.route('/')
def home():
    # Render home.html template, passing owners and pets data
    return render_template('home.html', owners=owners, pets=pets)


# Route for adding a new owner
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        # If form is submitted, create new owner
        name = request.form['name']
        phone = request.form['phone']
        new_owner = Owner(name, phone)
        owners.append(new_owner)
        # Save updated data
        save_data(owners, pets)
        # Redirect to home page
        return redirect(url_for('home'))
    # If GET request, just render the add_owner form
    return render_template('add_owner.html')


# Route for adding a new pet
@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        # If form is submitted, create new pet
        name = request.form['name']
        species = request.form['species']
        age = int(request.form['age'])
        owner_name = request.form['owner']
        # Find the owner object
        owner = next((o for o in owners if o.name == owner_name), None)

        # Create appropriate pet object based on species
        if species == 'Dog':
            breed = request.form['breed']
            new_pet = Dog(name, age, owner, breed)
        elif species == 'Cat':
            indoor = 'indoor' in request.form
            new_pet = Cat(name, age, owner, indoor)
        else:
            new_pet = Pet(name, species, age, owner)

        # Add new pet to list and to owner
        pets.append(new_pet)
        if owner:
            owner.add_pet(new_pet)
        # Save updated data
        save_data(owners, pets)
        # Redirect to home page
        return redirect(url_for('home'))
    # If GET request, render the add_pet form
    return render_template('add_pet.html', owners=owners)


# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)