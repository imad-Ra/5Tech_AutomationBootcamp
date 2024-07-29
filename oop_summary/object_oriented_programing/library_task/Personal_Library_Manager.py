import json
#
# This class manages the collection of books in your library.
class MyLibrary:
    def __init__(self, name):
        self.price = None
        self.book_name = None
        self.name = name
        self.books = []

    # Setting the name of the library
    def create_library(self, name):
        self.name = name

    # Printing details of all books in the library
    def show_library(self):
        for book in self.books:
            print(book.show_book())

    #Adding a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Findign a book in the library by it's name
    def find_book(self, book_name):
        for book in self.books:
            if book_name.lower() == book.name.lower():
                return book
        return None

    # Removing a book from the library
    def remove_book(self, book_name):
        for book in self.books:
            if book_name.lower() == book.name.lower():
                self.books.remove(book)
                print(f'{book_name} was removed from the libray.')
                return
            else:
                print(f'{book_name} is not found in the library.')

    # Editing a book detailscand allowing the user to make changes
    def edit_book(self, name):
        book = self.find_book(name)
        if book:
            new_name = input("Insert the new name of the book: ")
            new_price = float(input("Insert the new price of the book: "))
            new_author = input("Inset the name of the new author of the book: ")
            new_genre = input("Insert the type of the new genre of the book: ")
            new_year = input("Insert the new year of the book: ")
            new_link = input("Insert the new link of the book: ")
            book.name = new_name
            book.price = new_price
            book.author = new_author
            book.genre = new_genre
            book.year = new_year
            book.link = new_link
            print("The book's -Name-Price-Author-Genre-Year-link were changed. ")
        else:
            print("The book was not found in the library.")

    # Returnign a string representation of a library with included books.
    def to_string(self):
        result = (f'Name of library: {self.name}\n'
                  f'Books in the library:\n')

        for book in self.books:
            result = result + book.show_book() + '\n'

        return result

    # Saving the library to JSON file

    def save_library(self, library_file_path):
        with open(library_file_path, 'w') as file:
            json.dump({'name': self.name, 'books': [book.__dict__ for book in self.books]}, file, indent=1)

    # Loading the library from a JSON file
    @classmethod
    def load_library(cls, library_file_path):
        try:
            with open(library_file_path, 'r') as file:
                data = json.load(file)
                library = cls(name=data['name'])
                library.books = [Book(**book_data) for book_data in data['books']]
                return library
        except FileNotFoundError:
            return cls(name="My Personal Library")
        except Exception as e:
            print(f"Error loading library: {e}")
            return cls(name="My Personal Library")


# This class represeents a book with it's details
class Book:
    # @property
    def __init__(self, name, price, author, genre, year, link):
        self.name = name
        self.price = price
        self.author = author
        self.genre = genre
        self.year = year
        self.link = link

    # returning a string representation of the book's details
    # @property
    def show_book(self):
        return (f'Name: {self.name}\nPrice: {self.price}\nAuthor: {self.author}\n'
                f'Genre: {self.genre}\nYear: {self.year}\nLink: {self.link}\n----------------')
