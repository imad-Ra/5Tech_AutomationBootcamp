import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book 1", "Author 1", 2020, "Genre 1")
        self.book2 = Book("Book 2", "Author 2", 2021, "Genre 2")
        self.book3 = Book("Book 3", "Author 1", 2022, "Genre 3")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertEqual(self.library.books, [self.book1])

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.remove_book(self.book1)
        self.assertEqual(self.library.books, [self.book2])

    def test_get_all_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        result = self.library.get_all_books()
        self.assertEqual(result, [self.book1, self.book2])

    def test_get_books_by_author(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        result = self.library.get_books_by_author("Author 1")

    def test_author_is_string(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        result = self.library.get_books_by_author("Author 1")
        self.assertEqual(result, [self.book1, self.book3])

    def test_get_books_by_genre(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        result = self.library.get_books_by_genre("Genre 1")
        self.assertEqual(result, [self.book1])


if __name__ == '__main__':
    unittest.main()