# cli.py
# This file handles the command-line interface for our library manager

import argparse
from tabulate import tabulate

class CLI:
    # Parse command-line arguments
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Personal Library Manager")
        parser.add_argument('action', choices=['add', 'list', 'edit', 'delete'], help="Action to perform")
        parser.add_argument('--title', help="Book title")
        parser.add_argument('--author', help="Book author")
        parser.add_argument('--year', type=int, help="Publication year")
        parser.add_argument('--genre', help="Book genre")
        parser.add_argument('--filter', choices=['author', 'genre'], help="Filter for listing books")
        return parser.parse_args()

    # Display books in a nice table format
    @staticmethod
    def display_books(books):
        if not books:
            print("No books found.")
        else:
            headers = ["Title", "Author", "Year", "Genre"]
            table_data = [[book.title, book.author, book.year, book.genre] for book in books]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Get book details from user input
    @staticmethod
    def get_book_details():
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter publication year: "))
        genre = input("Enter book genre: ")
        return title, author, year, genre

    # Get a book to edit from user input
    @staticmethod
    def get_book_to_edit(books):
        CLI.display_books(books)
        while True:
            title = input("Enter the title of the book to edit: ")
            book = next((b for b in books if b.title.lower() == title.lower()), None)
            if book:
                return book
            print("Book not found. Please try again.")

    # Get a book to delete from user input
    @staticmethod
    def get_book_to_delete(books):
        CLI.display_books(books)
        while True:
            title = input("Enter the title of the book to delete: ")
            book = next((b for b in books if b.title.lower() == title.lower()), None)
            if book:
                return book
            print("Book not found. Please try again.")