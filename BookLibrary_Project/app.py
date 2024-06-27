from flask import Flask, render_template, request, redirect, url_for
from book import Book
from BookLibrary_Project.library import Library

app = Flask(__name__)
library = Library.load_from_file("library.json")

@app.route('/')
def index():
    return render_template('index.html', books=library.get_all_books())

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = int(request.form['year'])
        genre = request.form['genre']
        new_book = Book(title, author, year, genre)
        library.add_book(new_book)
        library.save_to_file("library.json")
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = library.get_all_books()[book_id]
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = int(request.form['year'])
        book.genre = request.form['genre']
        library.save_to_file("library.json")
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book, book_id=book_id)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = library.get_all_books()[book_id]
    library.remove_book(book)
    library.save_to_file("library.json")
    return redirect(url_for('index'))

@app.route('/filter', methods=['POST'])
def filter_books():
    filter_type = request.form['filter_type']
    filter_value = request.form['filter_value']
    if filter_type == 'author':
        books = library.get_books_by_author(filter_value)
    elif filter_type == 'genre':
        books = library.get_books_by_genre(filter_value)
    else:
        books = library.get_all_books()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)