from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pets = []
owners = []

@app.route('/')
def home():
    return render_template('home.html', pets=pets, owners=owners)

@app.route('/add_pet')
def add_pet():
    name = request.args.get('name', 'Unknown')
    species = request.args.get('species', 'Unknown')
    age = request.args.get('age', 0)
    pets.append({"name": name, "species": species, "age": age})
    return redirect(url_for('home'))

@app.route('/add_owner')
def add_owner():
    name = request.args.get('name', 'Unknown')
    phone = request.args.get('phone', 'Unknown')
    owners.append({"name": name, "phone": phone})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)