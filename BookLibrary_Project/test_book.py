import unittest
from BookLibrary_Project.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Book 1", "Author 1", 2020, "Genre 1")

    def test_title(self):
        self.assertEqual(self.book.title, "Book 1")

    def test_author(self):
        self.assertEqual(self.book.author, "Author 1")

    def test_year(self):
        self.assertEqual(self.book.year, 2020)

    def test_genre(self):
        self.assertEqual(self.book.genre, "Genre 1")

    def test_set_title(self):
        self.book.title = "New Title"
        self.assertEqual(self.book.title, "New Title")

    def test_set_author(self):
        self.book.author = "New Author"
        self.assertEqual(self.book.author, "New Author")

    def test_set_year(self):
        self.book.year = 2021
        self.assertEqual(self.book.year, 2021)

    def test_set_genre(self):
        self.book.genre = "New Genre"
        self.assertEqual(self.book.genre, "New Genre")

    def test_year_type(self):
        self.assertIsInstance(self.book.year, int)

    def test_genre_type(self):
        self.assertIsInstance(self.book.genre, str)


if __name__ == '__main__':
    unittest.main()
