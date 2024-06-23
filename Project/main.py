from book import Book
from library import Library
import datetime

def display_menu():
    print("\n--- Personal Library Manager ---")
    print("1. Add a book")
    print("2. List all books")
    print("3. Search books by author")
    print("4. Search books by genre")
    print("5. Edit a book")
    print("6. Delete a book")
    print("7. Exit")

def get_valid_string_input(prompt, allow_digits=False):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
        elif not allow_digits and any(char.isdigit() for char in value):
            print("Input cannot contain digits. Please try again.")
        elif not all(char.isalnum() or char.isspace() for char in value):
            print("Input can only contain letters, numbers, and spaces. Please try again.")
        else:
            return value

def get_valid_year():
    current_year = datetime.datetime.now().year
    while True:
        try:
            year = int(input("Enter publication year: "))
            if year < 1000 or year > current_year:
                print(f"Please enter a valid year between 1000 and {current_year}.")
            else:
                return year
        except ValueError:
            print("Please enter a valid year (e.g., 2023)")

def get_book_details():
    title = get_valid_string_input("Enter book title: ", allow_digits=True)
    author = get_valid_string_input("Enter book author: ")
    year = get_valid_year()
    genre = get_valid_string_input("Enter book genre: ")
    return Book(title, author, year, genre)

def display_books(books):
    if not books:
        print("No books found.")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")

def get_valid_index(books):
    while True:
        try:
            index = int(input("Enter the number of the book: ")) - 1
            if 0 <= index < len(books):
                return index
            else:
                print(f"Please enter a number between 1 and {len(books)}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    try:
        library = Library.load_from_file("library.json")
    except Exception as e:
        print(f"Error loading library: {e}")
        print("Starting with an empty library.")
        library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        try:
            if choice == '1':
                book = get_book_details()
                library.add_book(book)
                print("Book added successfully.")

            elif choice == '2':
                print("\nAll Books:")
                display_books(library.get_all_books())

            elif choice == '3':
                author = get_valid_string_input("Enter author name: ")
                books = library.get_books_by_author(author)
                print(f"\nBooks by {author}:")
                display_books(books)

            elif choice == '4':
                genre = get_valid_string_input("Enter genre: ")
                books = library.get_books_by_genre(genre)
                print(f"\nBooks in {genre} genre:")
                display_books(books)

            elif choice == '5':
                books = library.get_all_books()
                if not books:
                    print("No books to edit.")
                    continue
                display_books(books)
                index = get_valid_index(books)
                new_book = get_book_details()
                books[index] = new_book
                print("Book edited successfully.")

            elif choice == '6':
                books = library.get_all_books()
                if not books:
                    print("No books to delete.")
                    continue
                display_books(books)
                index = get_valid_index(books)
                removed_book = books.pop(index)
                print(f"Deleted: {removed_book}")

            elif choice == '7':
                try:
                    library.save_to_file("library.json")
                    print("Library saved. Goodbye!")
                except Exception as e:
                    print(f"Error saving library: {e}")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()