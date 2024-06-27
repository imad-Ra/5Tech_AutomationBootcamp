import json
from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_all_books(self):
        return self.books

    def get_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def get_books_by_genre(self, genre):
        return [book for book in self.books if book.genre.lower() == genre.lower()]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f)

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
