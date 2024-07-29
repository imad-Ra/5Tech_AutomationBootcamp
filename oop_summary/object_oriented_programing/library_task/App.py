import argparse
import logging  # Error handling and recording adding/editing/removing a book.
from flask import Flask, render_template, request, redirect, url_for
from Personal_Library_Manager import MyLibrary, Book
#
# Configure logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
library_file_path = 'library.json'
library = MyLibrary.load_library(library_file_path)


# Validation functions for argument parsing to ensure prices are positive floats
# and years are positive integers.
def check_positive_float(value):
    try:
        float_value = float(value)
        if float_value < 0:
            raise argparse.ArgumentTypeError("Price must be a positive number")
        return float_value
    except ValueError:
        raise argparse.ArgumentTypeError("Price must be a number")


def check_positive_int(value):
    try:
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError("Year must be a positive integer")
        return int_value
    except ValueError:
        raise argparse.ArgumentTypeError("Year must be an integer")


@app.route('/')  # Home page
def home():
    return render_template('home.html')


@app.route('/library')  # Libary page
def show_library():
    return render_template('library.html', library=library)


@app.route('/add', methods=['GET', 'POST'])  # Addig a book, handling get and post requests.
def add_book():
    if request.method == 'POST':
        try:
            name = request.form['name']
            price = float(request.form['price'])
            if price < 0:
                check_positive_float()
            author = request.form['author']
            genre = request.form['genre']
            year = int(request.form['year'])
            if year <= 0:
                check_positive_int()
            link = request.form['link']
            book = Book(name=name, price=price, author=author, genre=genre, year=year, link=link)
            library.add_book(book)
            library.save_library(library_file_path)
            logging.info(f"Book added: {book.show_book()}")
            return redirect(url_for('show_library'))
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            return render_template('add_book.html', error=str(e))
    return render_template('add_book.html')


@app.route('/edit/<string:book_name>', methods=['GET', 'POST'])  # Editing a book's details
def edit_book(book_name):
    book = library.find_book(book_name)
    if not book:
        return redirect(url_for('show_library'))
    if request.method == 'POST':
        try:
            book.name = request.form['name']
            book.price = float(request.form['price'])
            if book.price < 0:
                check_positive_float()
            book.author = request.form['author']
            book.genre = request.form['genre']
            book.year = int(request.form['year'])
            if book.year <= 0:
                check_positive_int()
            book.link = request.form['link']
            library.save_library(library_file_path)
            logging.info(f"Book edited: {book.show_book()}")
            return redirect(url_for('show_library'))
        except Exception as e:
            logging.error(f"Error editing book: {e}")
            return render_template('edit_book.html', book=book, error=str(e))
    return render_template('edit_book.html', book=book)


@app.route('/delete/<string:book_name>', methods=['POST'])  # Deleting a book from the library
def delete_book(book_name):
    try:
        library.remove_book(book_name)
        library.save_library(library_file_path)
        logging.info(f"Book removed: {book_name}")
        return redirect(url_for('show_library'))
    except Exception as e:
        logging.error(f"Error deleting book: {e}")
        return redirect(url_for('show_library'))


@app.route('/contact')  # contact and get help page
def contact():
    return render_template('contact.html')


@app.route('/about')  # About us page
def about():
    return render_template('about.html')



# if __name__ == '__main__':
#     app.run(debug=True)
