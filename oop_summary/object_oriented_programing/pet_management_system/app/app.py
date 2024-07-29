from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owners')
def owners():
    return render_template('owners.html')

@app.route('/pets')
def pets():
    return render_template('pets.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        # Process the form data
        pass
    return render_template('add_owner.html')

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        # Process the form data
        pass
    return render_template('add_pet.html')

if __name__ == '__main__':
    app.run(debug=True)