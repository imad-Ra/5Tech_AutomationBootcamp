import json
from book import Book

class Library:
    def __init__(self):
        self._books = []

    # Add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Remove a book from the library
    def remove_book(self, book):
        self._books.remove(book)

    # Get all books in the library
    def get_all_books(self):
        return self._books

    # Get books by author
    def get_books_by_author(self, author):
        return [book for book in self._books if book.author.lower() == author.lower()]

    # Get books by genre
    def get_books_by_genre(self, genre):
        return [book for book in self._books if book.genre.lower() == genre.lower()]

    # Save library to a JSON file
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.to_dict() for book in self._books], f)

    # Load library from a JSON file
    @classmethod
    def load_from_file(cls, filename):
        library = cls()
        try:
            with open(filename, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    library.add_book(Book.from_dict(book_data))
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")
        return library