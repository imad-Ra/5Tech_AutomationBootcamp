from Personal_Library_Manager import MyLibrary, Book


def bye():
    print("Good bye! You can visit us anytime you want!")



def add_book(library):
    book_add = input("Insert the name of your book: ")
    while True:
        try:
            price_add = int(input("Insert the price of the book: "))
            if price_add <= 0:
                print("Please insert a correct value of price: ")
            else:
                break
        except ValueError:
            print("Please insert a correct value of price: ")
    author_add = input("Insert the name of the author: ")
    genre_add = input("Insert the genre of the book: ")
    while True:
        try:
            year_add = int(input("Insert the year of the book: "))
            if year_add <= 0:
                print("Please insert a correct value of year: ")
            else:
                break
        except ValueError:
            print("Please insert a correct value of year: ")
    link_add = input("Insert the link of the online reading page (from: www.manybooks.net): ")
    new_book = Book(name=book_add, price=price_add, author=author_add, genre=genre_add, year=year_add, link=link_add)
    library.add_book(new_book)
    print("Book added successfully!")


def main():
    ask_adding_library = input("Hey dear! Welcome to our online library! would you like to add a new personal library? (yes/no): ")
    if ask_adding_library == 'yes':
        library_name = input("Enter the name of your library: ")
        library = MyLibrary(name=library_name)

        while True:
            add_suggest = input("Would you like to add a new book to the library? (yes/no): ")
            if add_suggest.lower() != "yes":
                # bye()
                break
            else:
                add_book(library)

            while True:
                print("Please choose an option:")
                print("1. Add a new book\n2. Show the library\n3. Choose a book\n4. Edit a book"
                      "\n5. Remove a book\n6. Exit the program")
                choice = input("Choose an option: ")
                if choice == '1':
                    add_book(library)
                elif choice == '2':
                    if library.books:
                        print("Your library:\n")
                        print(library.to_string())
                    else:
                        print("The library is empty.")
                elif choice == '3':
                    book_name = input("Insert the name of the book you want to show: ")
                    book = library.find_book(book_name)
                    if book is not None:
                        print("Book details:\n\n", book.show_book())
                    else:
                        print("Book is not found in the library.")
                elif choice == '4':
                    book_to_edit = input("Insert the name of the book you want to edit: ")
                    library.edit_book(book_to_edit)
                elif choice == '5':
                    book_to_remove = input("Insert the name of the book you want to remove: ")
                    library.remove_book(book_to_remove)
                elif choice == '6':
                    bye()
                    return
                    break
                else:
                    print("Invalid option, please choose again.")

                # After performing an action, print the menu again
                print()

    bye()



if __name__ == '__main__':
    main()
